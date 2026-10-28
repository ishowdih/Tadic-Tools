# Build the Linux AppImage

This repository does not contain a built `tadictools.AppImage` yet. The AppImage toolchain is Linux-only; Follow these steps on an x86_64 Linux machine (Arch Linux is recommended because the app's optional TTY-Clock and Fastfetch installers use `pacman`).

## 1. Install Python and pip

On Arch Linux:

```bash
sudo pacman -S --needed python python-pip
```

From the repository root, create a virtual environment and install the build and runtime packages:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pyinstaller pyfiglet "qrcode[pil]"
```

## 2. Build the standalone program

Run the requested PyInstaller command from the repository root:

```bash
pyinstaller --onefile --name tadictools LinuxTRE.py
```

This produces `dist/tadictools`, a standalone executable with the Python runtime and Python dependencies bundled. Try it before packaging:

```bash
./dist/tadictools
```

## 3. Create the AppDir

Create the layout and copy the executable and repository icon:

```bash
mkdir -p AppDir/usr/bin
cp dist/tadictools AppDir/usr/bin/tadictools
cp tadiclogo.png AppDir/tadiclogo.png
ln -sf tadiclogo.png AppDir/.DirIcon
```

Create the desktop entry at `AppDir/tadictools.desktop`:

```ini
[Desktop Entry]
Type=Application
Name=TadicTools Reimagined
Exec=tadictools
Icon=tadiclogo
Terminal=true
Categories=Utility;
```

Create `AppDir/AppRun`:

```sh
#!/bin/sh
HERE="$(dirname "$(readlink -f "$0")")"
exec "$HERE/usr/bin/tadictools" "$@"
```

Make the entry point and executable runnable:

```bash
chmod +x AppDir/AppRun AppDir/usr/bin/tadictools
```

## 4. Download and run appimagetool

Download the x86_64 AppImage from the official [appimagetool continuous releases](https://github.com/AppImage/appimagetool/releases/continuous):

```bash
wget -O appimagetool-x86_64.AppImage https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-x86_64.AppImage
chmod +x appimagetool-x86_64.AppImage
```

Build the final image:

```bash
ARCH=x86_64 ./appimagetool-x86_64.AppImage AppDir tadictools.AppImage
chmod +x tadictools.AppImage
```

You can launch it with:

```bash
./tadictools.AppImage
```

The `tty-clock` and `fastfetch` features remain optional system tools. On Arch Linux, LinuxTRE can offer to install them with `sudo pacman -S tty-clock` and `sudo pacman -S fastfetch` respectively.

> Note: LinuxTRE is the linux version of TadicTools-Reimagined.py (Linux_version.py on the repo)
