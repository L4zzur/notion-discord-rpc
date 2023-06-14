# notion-discord-rpc
Discord Rich Presence Client (RPC) for Notion

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

![image](https://github.com/L4zzur/notion-discord-rpc/assets/66362624/669799e8-7cb0-4497-974f-c8ffa744d57d)

#### Big thanks to [nandiniproothi](https://github.com/nandiniproothi/notion-discord-rpc) and [Lockna](https://stackoverflow.com/a/70659506)
This is my variation of this script, but written under Windows OS.

### Warning!
The use of this script is possible only on Windows OS, since the Win32 API is involved here.

# Requirements
- Windows
- Python 3.*
- Notion Desktop App

# Installation
0. Install `pipenv` or check that it is installed:
```bash
pip install pipenv
```
1. Clone the repository:
```bash
git clone https://github.com/L4zzur/notion-discord-rpc.git
```
2. Go to projects folder:
```bash
cd notion-discord-rpc
```
3. Create virtual environment using `pipenv`:
```bash
pipenv shell
```
or using virtualenv/venv and activate it:
```bash
virtualenv venv
```
```bash
python -m venv venv
```
4. Install all dependencies:
Using `pipenv`:
```bash
pipenv install
```
or the old-fashioned way using `requirements.txt`:
```bash
pip3 install -r requirements.txt
```
5. Run the python script:
```bash
python main.py
```

# Further updates
- I would like to wrap this script using the pystray library and assemble it into an exe file, as well as create a GUI and installer.
