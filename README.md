# TadicTools & TadicTools Reimagined

> Simple tools. No ads. No nonsense.

TadicTools/TadicTools Reimagined is a terminal-based toolkit by Eymorty. The repository includes the original Windows version and a Linux port, bringing everyday utilities into one interactive menu.

<img width="883" height="603" alt="image" src="https://github.com/user-attachments/assets/c13bdf79-5b52-47f3-b0ea-7edf0623aed2" />


## Features

- ASCII clock (TTY-Clock on Linux) and countdown timer
- Game launcher and saved game paths
- Web shortcuts
- QR code and password generators
- Ping checks
- Temporary-file cleanup
- File lock/unlock utility
- Discord webhook and possible Base64 scanner
- UUID generator, text reverser, and character counter
- ASCII banner generator and system information through Fastfetch
- To-do list and optional command prompt mode


## Downloads

- Published builds are available from the GitHub repo.
- The website is https://tadictools.pages.dev .
- [`TadicTools-Reimagined.py`](https://github.com/ishowdih/Tadic-Tools/blob/main/reimagined_and_linux/TadicTools-Reimagined.py) is the Windows source.
- [`Linux_version.py`](https://github.com/ishowdih/Tadic-Tools/blob/main/reimagined_and_linux/Linux_version.py) is the Linux source.
- Follow [`BUILD_APPIMAGE.md`](https://github.com/ishowdih/Tadic-Tools/blob/main/reimagined_and_linux/BUILD_APPIMAGE.md) to package the Linux port as `tadictools.AppImage`. An AppImage binary is not included yet.

## Run on Windows


The Windows source imports `pyfiglet`, `qrcode`, `pywin32`, and the `clearer` and `boldy` helper modules. Install the Python packages and make sure the helper modules are available on Python's import path, then run:

```CMD
pip install -r requirements.txt
python TadicTools-Reimagined.py
```

The prebuilt Windows installer is linked from the website.

## Run on Linux

`Linux_version.py` is designed for Linux terminals. For the optional install prompts for TTY-Clock and Fastfetch, use Arch Linux or another system with `pacman`; on other distributions, install those utilities with your distribution's package manager.

Install Python and pip, then install the Python dependencies and run the port:

```bash
python -m pip install -r requirements.txt
python Linux_version.py
```

The Linux version stores its generated files under `$XDG_DATA_HOME/tadictools`, or `~/.local/share/tadictools` when `XDG_DATA_HOME` is not set.


### Build the Linux AppImage

See [`BUILD_APPIMAGE.md`](https://github.com/ishowdih/Tadic-Tools/blob/main/reimagined_and_linux/BUILD_APPIMAGE.md) for the full PyInstaller and AppImageTool steps. The packaged executable bundles the Python runtime; TTY-Clock and Fastfetch remain optional system utilities.


## Another Way to Run On Linux (Easiest Way)
This guide is step-by-step and the easiest one, its literally only 3 commands, and you don't even need python. Just make sure your distro is either arch based or you use arch linux.
- Step 1.
  Download the package with the following commands:
  ```
  git clone https://github.com/ishowdih/Tadic-Tools
  cd Tadic-Tools/reimagined_and_linux/linux_aur_files
  makepgs -si
  ```
  with that commands, you will install TadicTools.
- Step 2.
  Run TadicTools:
  ```
  tadictools
  ```
  command `tadictools` runs TadicTools in your terminal, but don't forget that you need to be on Arch, not debian, not ubuntu, Arch.

  
## Important notes

- The file lock/unlock feature changes the selected file in place using a repeating XOR operation. This is **not secure encryption**. Keep a backup and do not use it to protect sensitive data.
- The temporary-file cleaner removes old items owned by the current user from the system temporary directory. Review anything important before confirming cleanup.
- The webhook scanner may display webhook URLs from a selected file. Treat any detected URL as a secret and do not publish or share it.

## Website and links

- [GitHub repository](https://github.com/ishowdih/Tadic-Tools)
- [Itch.io](https://eymorty.itch.io)
- [Tadic Tools Website](https://tadictools.pages.dev)

> QUICK NOTE FOR THE REPO (**READ THIS**): The requirements.txt, Linux_version.py and TadicTools-Reimagined.py is on the [folder reimagined_and_linux](https://github.com/ishowdih/Tadic-Tools/tree/main/reimagined_and_linux)


> Note 2: The project (TadicTools-Reimagined itself and other TadicTools versions) are made by a human. The website is made by Codex.
> The "NO AI WAS USED..." is for python scripts & other that are not in the website files.


**NO AI WAS USED ON THIS PROJECT. EVERY LINE IS WRITTEN BY A HUMAN.**
