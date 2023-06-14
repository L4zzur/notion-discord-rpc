import ctypes
import time

import psutil
import pypresence
import win32gui
import win32process

# Windows Functions
EnumWindows = ctypes.windll.user32.EnumWindows
GetWindowTextW = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible


def get_pids_by_procname(process_name: str) -> list[int]:
    """Getting all Process IDs by application name

    Args:
        process_name (str): application name

    Returns:
        list[int]: list of all PIDs
    """
    pids = []
    for process in psutil.process_iter():
        if process_name in process.name():
            pids.append(process.pid)
    return pids


def get_hwnds_for_pid(pid: int) -> list[int]:
    """Getting all HWNDs (handles to a appplication window) by Process ID

    Args:
        pid (int): Process ID of an application

    Returns:
        list[int]: list of all HWNDs
    """

    def callback(hwnd: int, hwnds: list[int]) -> bool:
        """A Python function to be used as the callback.

        Args:
            hwnd (int): HWND for application, which needs to be checked
            hwnds (list[int]): list of all HWNDs for application

        Returns:
            bool: returning True to continue enumerating windows
        """
        ctid, cpid = win32process.GetWindowThreadProcessId(hwnd)
        if cpid == pid:
            hwnds.append(hwnd)
        return True

    hwnds = []
    # Enumerates all top-level windows on the screen by passing
    # the handle to each window, in turn, to an application-defined
    # callback function.
    # EnumWindows continues until the last top-level window
    # is enumerated or the callback function returns FALSE
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


def get_process_hwnd(process_name: str) -> int:
    """Getting HWND for application by name

    Args:
        process_name (str): application name

    Returns:
        int: HWND for application
    """
    pids = get_pids_by_procname(process_name=process_name)
    for i in pids:
        hwnds = get_hwnds_for_pid(i)
        for hwnd in hwnds:
            if IsWindowVisible(hwnd):
                return hwnd
    else:
        raise Exception("HWND not found.")


def get_wintitle_by_hwnd(hwnd: int) -> str:
    """Getting window title for application by HWND

    Args:
        hwnd (int): HWND of application

    Returns:
        str: window title of application
    """
    length = GetWindowTextLength(hwnd)
    title = ctypes.create_unicode_buffer(length + 1)
    GetWindowTextW(hwnd, title, length + 1)
    return title.value


if __name__ == "__main__":
    client_id = "1118566458595737752"  # application ID
    RPC = pypresence.Presence(client_id=client_id)
    RPC.connect()

    process_name = "Notion.exe"
    process_hwnd = get_process_hwnd(process_name=process_name)
    process_wintitle = False

    while True:
        if process_wintitle != get_wintitle_by_hwnd(process_hwnd):
            process_wintitle = get_wintitle_by_hwnd(process_hwnd)
            RPC.update(
                pid=get_pids_by_procname(process_name=process_name)[0],
                large_image="notion_512",
                large_text="Notion",
                small_image="writing",
                small_text="Writing some magic...",
                start=int(time.time()),
                details=("Editing: " + process_wintitle),
            )
            print(f"Changing title. New title: {process_wintitle}")  # debug
        time.sleep(3)
