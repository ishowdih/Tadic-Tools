print("Loading TadicTools...")
import os
import datetime
import time
import webbrowser
import json
import subprocess
import secrets
import string
import shutil
import pyfiglet
import qrcode
import sys
import uuid
import base64
from socket import gethostname, create_connection
from getpass import getuser 



script_dir = os.path.dirname(os.path.abspath(__file__))
robot_dir = os.path.join(script_dir, 'robot.mp4')
data_home = os.environ.get('XDG_DATA_HOME', os.path.join(os.path.expanduser('~'), '.local', 'share'))
generated_dir = os.path.join(data_home, 'tadictools')
qr_folder_dir = os.path.join(generated_dir, 'QR Codes')
os.makedirs(generated_dir, exist_ok=True)
os.makedirs(qr_folder_dir, exist_ok=True)

paths_file = os.path.abspath(os.path.join(generated_dir, 'paths.json'))
uuid_file = os.path.abspath(os.path.join(generated_dir, 'uuid.txt'))
todolist_file = os.path.abspath(os.path.join(generated_dir, 'to-do-list.txt'))

user = getuser()
pcname = gethostname()
ihavednsig = ['1.1.1.1', '2']
ihavedns = ['8.8.8.8', '1']
Tadic_text = pyfiglet.figlet_format("TadicTools")
CYAN = "\033[36m"
YELLOW = "\033[33m"
ORANGE = '\033[38;5;214m'
RED = '\033[31m'
RESET = "\033[0m"

def autoclear():
    os.system("clear")

def input_bold(prompt):
    return input(f"\033[1m{prompt}\033[0m")

def print_bold(value):
    print(f"\033[1m{value}\033[0m")

def copy_to_clipboard(value):
    for command in (("wl-copy",), ("xclip", "-selection", "clipboard"), ("xsel", "--clipboard", "--input")):
        if shutil.which(command[0]):
            try:
                subprocess.run(command, input=value, text=True, check=True)
                print("Password copied to clipboard.")
                return
            except (OSError, subprocess.CalledProcessError):
                pass
    print("Clipboard tool unavailable. Copy the password from the terminal above.")


tadictext = CYAN+r"""sdSS_SSSSSSbs   .S_SSSs     .S_sSSs     .S    sSSs  sdSS_SSSSSSbs    sSSs_sSSs      sSSs_sSSs    S.        sSSs  
YSSS~S%SSSSSP  .SS~SSSSS   .SS~YS%%b   .SS   d%%SP  YSSS~S%SSSSSP   d%%SP~YS%%b    d%%SP~YS%%b   SS.      d%%SP  
     S%S       S%S   SSSS  S%S   `S%b  S%S  d%S'         S%S       d%S'     `S%b  d%S'     `S%b  S%S     d%S'    
     S%S       S%S    S%S  S%S    S%S  S%S  S%S          S%S       S%S       S%S  S%S       S%S  S%S     S%|     
     S&S       S%S SSSS%S  S%S    S&S  S&S  S&S          S&S       S&S       S&S  S&S       S&S  S&S     S&S     
     S&S       S&S  SSS%S  S&S    S&S  S&S  S&S          S&S       S&S       S&S  S&S       S&S  S&S     Y&Ss    
     S&S       S&S    S&S  S&S    S&S  S&S  S&S          S&S       S&S       S&S  S&S       S&S  S&S     `S&&S   
     S&S       S&S    S&S  S&S    S&S  S&S  S&S          S&S       S&S       S&S  S&S       S&S  S&S       `S*S  
     S*S       S*S    S&S  S*S    d*S  S*S  S*b          S*S       S*b       d*S  S*b       d*S  S*b        l*S  
     S*S       S*S    S*S  S*S   .S*S  S*S  S*S.         S*S       S*S.     .S*S  S*S.     .S*S  S*S.      .S*P  
     S*S       S*S    S*S  S*S_sdSSS   S*S   SSSbs       S*S        SSSbs_sdSSS    SSSbs_sdSSS    SSSbs  sSS*S   
     S*S       SSS    S*S  SSS~YSSY    S*S    YSSP       S*S         YSSP~YSSY      YSSP~YSSY      YSSP  YSS'    
     SP               SP               SP                SP                                                      
     Y                Y                Y                 Y                                                       
                                                                                                                 """+RESET


startuptext = CYAN+"""░██████████   ░███    ░███████   ░██████  ░██████  ░██████████  ░██████     ░██████   ░██           ░██████   
    ░██      ░██░██   ░██   ░██    ░██   ░██   ░██     ░██     ░██   ░██   ░██   ░██  ░██          ░██   ░██  
    ░██     ░██  ░██  ░██    ░██   ░██  ░██            ░██    ░██     ░██ ░██     ░██ ░██         ░██         
    ░██    ░█████████ ░██    ░██   ░██  ░██            ░██    ░██     ░██ ░██     ░██ ░██          ░████████  
    ░██    ░██    ░██ ░██    ░██   ░██  ░██            ░██    ░██     ░██ ░██     ░██ ░██                 ░██ 
    ░██    ░██    ░██ ░██   ░██    ░██   ░██   ░██     ░██     ░██   ░██   ░██   ░██  ░██          ░██   ░██  
    ░██    ░██    ░██ ░███████   ░██████  ░██████      ░██      ░██████     ░██████   ░██████████   ░██████   
                                                                                                              
                                                                                                              
                                                                                                              """+RESET


ascii_raw = pyfiglet.figlet_format('TadicTools', font='standard')
RealTDC_text = CYAN + ascii_raw + RESET

def internet_available():
    try:
        connection = create_connection(("8.8.8.8", 53), timeout=3)
        connection.close()
        return True
    except OSError:
        return False
def download_fastfetch():
    subprocess.run(["sudo", "pacman", "-S", "fastfetch"], check=False)
class tembel:
    def clr_shit(self):
        os.system("clear")

    def timer(self):
        try:
            self.clr_shit()
            total_minutes = int(input("Enter the countdown time in minutes: "))
        except ValueError:
            print("Please enter a valid whole number.")
            input('press enter to go back')
            return

        total_seconds = total_minutes * 60
        
        while total_seconds > 0:
            minutes, seconds = divmod(total_seconds, 60)
            time_format = f"{minutes:02d}:{seconds:02d}"
            print(f"\rTime Remaining: {time_format}", end="", flush=True)
            time.sleep(1)
            total_seconds -= 1

        print("\nTime's up!")
        input('press enter to go back')
        self.clr_shit()

    def ai_menu(self):
        print('--Ai Menu--')
        print('[1. ChatGPT]')
        print('[2. Gemini]')
        print('[3. Grok]')
        print('[4. Claude]')
        print('[5. Exit]')
        print(' ')
        ai_select = input('Select Ai: ')
        if ai_select == '1':
            webbrowser.open('https://Chatgpt.com')
        elif ai_select == '2':
            webbrowser.open('https://gemini.google.com/app')
        elif ai_select == '3':
            webbrowser.open('https://grok.com')
        elif ai_select == '4':
            webbrowser.open('https://claude.ai/new')
        elif ai_select == '5':
            self.clr_shit()
        else:
            self.clr_shit()
            print('you should select one. ')
            input('press enter to go back')

    def get_file_path(self):
        path = input("Enter the full path of the file to scan: ").strip().strip('"')
        return os.path.expanduser(path) if path else ""

    def ascii_clock(self):
        self.clr_shit()
        if shutil.which("tty-clock") is None:
            print("TTY-Clock is not installed.")
            install_choice = input("Install it now with sudo pacman -S tty-clock? (Y/N): ").strip().lower()
            if install_choice.startswith("y"):
                if shutil.which("pacman") is None:
                    print("Pacman was not found. This installer command is for Arch Linux.")
                    input("press enter to go back")
                    self.clr_shit()
                    return
                subprocess.run(["sudo", "pacman", "-S", "tty-clock"], check=False)
            else:
                print("TTY-Clock was not installed.")
                input("press enter to go back")
                self.clr_shit()
                return

        if shutil.which("tty-clock") is not None:
            subprocess.run(["tty-clock"], check=False)
            input("press enter to go back")
        else:
            print("TTY-Clock is still unavailable. Check the installation and try again.")
            input("press enter to go back")
        self.clr_shit()

    def open_a_game(self):
        self.clr_shit()
        print('-Game Menu-')
        print('[1. Save a path to a Linux executable or game launcher]')
        print('[2. Saved Paths]')
        print('[3. Delete Saved Paths]')
        print('[4. Open Valorant]')
        print('[5. Open Roblox]')
        print('')
        seçenek = input('Select one (Or 0 to go back to main menu): ')
        if seçenek == '0':
            self.clr_shit()
        elif seçenek == '1':
            self.clr_shit()
            path = input('Enter the full path to a Linux executable or launcher: ')
            if os.path.exists(path):
                try:
                    if os.path.exists(paths_file):
                        with open(paths_file, "r") as f:
                            try:
                                data = json.load(f)
                                if not isinstance(data, list):
                                    data = [data]
                            except json.JSONDecodeError:
                                data = []
                    else:
                        data = []
                    
                    path_exists = any(entry["path"] == path for entry in data)
                    if path_exists:
                        self.clr_shit()
                        print("Warning: This path is already saved!")
                        input('press enter to go back')
                        self.clr_shit()
                    else:
                        subprocess.Popen([path])
                        print("Game started.")
                        input('press enter to go back')
                        self.clr_shit()

                        log_entry = {
                            "path": path,
                            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        }
                        data.append(log_entry)

                    with open(paths_file, "w") as f:
                        json.dump(data, f, indent=4)

                except Exception as e:
                    print(RED + f"An error occurred while launching: {e}" + RESET)
                    input('press enter to go back')
                    self.clr_shit()
            else:
                print(RED + "Error: The path specified does not exist. Please check it." + RESET)
                input('press enter to go back')
                self.clr_shit()

        elif seçenek == '4':
            try:
                webbrowser.open('riotclient://launch-app/bhang/live/na')
            except FileNotFoundError:
                print('VALORANT not found.')
                input('press enter to go back')
                self.clr_shit()
        elif seçenek == '5':
            try:
                webbrowser.open("roblox-player:")
            except FileNotFoundError:
                print('RobloxPlayer not found.')
                input('press enter to go back')
                self.clr_shit()

        elif seçenek == '2':
            self.clr_shit()
            if os.path.exists(paths_file):
                with open(paths_file, "r") as f:
                    try:
                        data = json.load(f)
                        if not isinstance(data, list):
                            data = [data]
                    except json.JSONDecodeError:
                        data = []
            else:
                data = []

            if not data:
                print("No saved paths found.")
                input('press enter to go back')
                self.clr_shit()
            else:
                print("--Saved Paths--")
                for i, entry in enumerate(data, 1):
                    print(f"[{i}. {entry['path']} ({entry['timestamp']})]")
                print(' ')
                path_choice = input("Select a path to run (or 0 to go back): ")
                if path_choice == '0':
                    self.clr_shit()
                else:
                    try:
                        path_index = int(path_choice) - 1
                        if 0 <= path_index < len(data):
                            selected_path = data[path_index]["path"]
                            if os.path.exists(selected_path):
                                subprocess.Popen([selected_path])
                                print("Game started.")
                                input('press enter to go back')
                                self.clr_shit()
                            else:
                                print(RED+"Error: The selected path no longer exists."+RESET)
                                input('press enter to go back')
                                self.clr_shit()
                        else:
                            print("Invalid selection.")
                            input('press enter to go back')
                            self.clr_shit()
                    except ValueError:
                        print("Invalid input.")
                        input('press enter to go back')
                        self.clr_shit()
        
        elif seçenek == '3':
            self.clr_shit()
            if os.path.exists(paths_file):
                with open(paths_file, "r") as f:
                    try:
                        data = json.load(f)
                        if not isinstance(data, list):
                            data = [data]
                    except json.JSONDecodeError:
                        data = []
            else:
                data = []

            if not data:
                print("No saved paths found.")
                input('press enter to go back')
                self.clr_shit()
            else:
                print("--Delete Saved Paths--")
                for i, entry in enumerate(data, 1):
                    print(f"[{i}. {entry['path']} ({entry['timestamp']})]")
                print('[0. Go back]')
                print(' ')
                delete_choice = input("Select a path to delete (or 0 to go back): ")
                if delete_choice == '0':
                    self.clr_shit()
                else:
                    try:
                        delete_index = int(delete_choice) - 1
                        if 0 <= delete_index < len(data):
                            deleted_path = data.pop(delete_index)
                            with open(paths_file, "w") as f:
                                json.dump(data, f, indent=4)
                            self.clr_shit()
                            print(f"Path deleted: {deleted_path['path']}")
                            input('press enter to go back')
                            self.clr_shit()
                        else:
                            print("Invalid selection.")
                            input('press enter to go back')
                            self.clr_shit()
                    except ValueError:
                        print("Invalid input.")
                        input('press enter to go back')
                        self.clr_shit()
              
    def web_shortcuts(self):
        self.clr_shit()
        print('--Web Menu--')
        print('[1. Open your itch.io dashboard]')
        print('[2. Open your Youtube profile]')
        print('[3. Select an Ai site to open]')
        print(' ')
        msgofthechc = input('Select one (Or 0 to go back to main menu): ')
        if msgofthechc == '1':
            webbrowser.open('https://itch.io/dashboard')
        elif msgofthechc == '2':
            webbrowser.open('https://youtube.com/profile')
        elif msgofthechc == '3':
            self.clr_shit()
            self.ai_menu()
        elif msgofthechc == '0':
            self.clr_shit()

    def qr_code_generator(self):
      try:
        self.clr_shit()
        veri = input("Enter text or URL> ")
        nameqr = input("Enter name for the png file> ")
        qr_file = os.path.abspath(os.path.join(qr_folder_dir, f'{nameqr}.png'))
        img = qrcode.make(veri)
        img.save(qr_file)
        print(f"QR code saved as {nameqr}.png")
        print("Saved to:", os.path.abspath(qr_file))
        input('press enter to go back')
        self.clr_shit()
      except Exception as e:
        print(RED+f"\nError: {e}"+RESET)
        input("press enter to go back")

    def password_generator(self):
        self.clr_shit()
        karakterler = string.ascii_letters + string.digits + "!@#$%&*"
        customsifre = input('Select length (Max 30) (only type numbers): ')
        try:
            customsifre_int = int(customsifre)
            if customsifre_int > 30 or customsifre_int <= 0:
                print('Invalid Length!')
                print(' ')
                input('press enter to go back')
                self.clr_shit()
            else:
                sifre = "".join(secrets.choice(karakterler) for _ in range(customsifre_int))
                print('Generating password...')
                print(' ')
                print(sifre)
                print(' ')
                input('Press ENTER to copy password and go back...')
                copy_to_clipboard(sifre)
                input("press enter to go back")
                self.clr_shit()
        except ValueError:
            print('Please enter a valid number!')
            input('press enter to go back')
            self.clr_shit()
         
    def ping_test(self):
        self.clr_shit()
        print('Which address do you want to test your ping on?')
        msgonthehc = input('8.8.8.8 or 1.1.1.1 (you can say 1 or 2)> ')

        if msgonthehc in ihavedns:
            os.system('ping -c 4 8.8.8.8')
            print(' ')
            input('press enter to go back')
            self.clr_shit()
        elif msgonthehc in ihavednsig:
            os.system('ping -c 4 1.1.1.1')
            print(' ')
            input('press enter to go back')
            self.clr_shit()
        else:
            print('Invalid Option!')
            print(' ')
            input('press enter to go back')
            self.clr_shit()

    def delete_temp(self):
        self.clr_shit()
        temp_path = os.environ.get("TMPDIR", "/tmp")
        print(f"This will remove files older than 24 hours in {temp_path} that belong to your user.")
        if input("Continue? (y/N): ").strip().lower() != "y":
            input("press enter to go back")
            self.clr_shit()
            return

        cutoff = time.time() - 24 * 60 * 60
        deleted_count = 0
        deleted_bytes = 0
        current_uid = os.getuid() if hasattr(os, "getuid") else None
        try:
            for entry in os.scandir(temp_path):
                try:
                    info = entry.stat(follow_symlinks=False)
                    if current_uid is not None and info.st_uid != current_uid:
                        continue
                    if info.st_mtime > cutoff:
                        continue
                    if entry.is_symlink():
                        os.unlink(entry.path)
                    elif entry.is_dir(follow_symlinks=False):
                        shutil.rmtree(entry.path)
                    else:
                        os.remove(entry.path)
                    deleted_count += 1
                    deleted_bytes += info.st_size
                except (PermissionError, FileNotFoundError, OSError) as error:
                    print(f"Skipped {entry.name}: {error}")
        except OSError as error:
            print(f"Could not access the temporary directory: {error}")

        print(f"Removed {deleted_count} old item(s), about {deleted_bytes / (1024 * 1024):.2f} MB of file data.")
        input("press enter to go back")
        self.clr_shit()

    def lock_unlock_file(self):
        self.clr_shit()
        print('-- Encrypted File Hider --')
        print('WARNING: To restore an encrypted file, you MUST use the EXACT SAME file path and the EXACT SAME password.')
        print(' ')
        print('[1. Encrypt / Decrypt a File]')
        print('[0. Go Back]')
        print(' ')
        secim8 = input('Select one: ')

        if secim8 == '1':
            self.clr_shit()
            dosya_yolu = input('Enter the full path of the file: ')
            sifre = input('Enter a password (or enter the existing password to decrypt): ')

            if os.path.exists(dosya_yolu) and sifre:
                try:
                    with open(dosya_yolu, 'rb') as f:
                        veri = bytearray(f.read())

                    sifre_byte = bytearray(sifre.encode('utf-8'))

                    for i in range(len(veri)):
                        veri[i] ^= sifre_byte[i % len(sifre_byte)]

                    with open(dosya_yolu, 'wb') as f:
                        f.write(veri)

                    self.clr_shit()
                    print('Success! The file has been encrypted (or decrypted).')
                    input('press enter to go back')
                    self.clr_shit()

                except PermissionError:
                    self.clr_shit()
                    print('Error: You do not have permission to access this file, or it is currently being used by another program.')
                    input('press enter to go back')
                    self.clr_shit()
                except Exception as e:
                    self.clr_shit()
                    print(f'An error occurred: {e}')
                    input('press enter to go back')
                    self.clr_shit()
            else:
                self.clr_shit()
                print('Error: File not found or password was left blank!')
                input('press enter to go back')
                self.clr_shit()
                 
        elif secim8 == '0':
            self.clr_shit()
        else:
            self.clr_shit()
             
    def webhook_scanner(self):
        import re
        self.clr_shit()
        print("\n[Opening file browser... Please select your readable file.]")
        selected_file = self.get_file_path()

        if selected_file:
            try:
                with open(selected_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                 
                webhook_patterns = [
                    r'https://(?:discord|discordapp|canary\.discord|ptb\.discord)\.com/api/webhooks/\d+/[A-Za-z0-9_-]+',
                    r'https://discord\.com/api/webhooks/[A-Za-z0-9_-]+/[A-Za-z0-9_-]+',
                ]
                found_webhooks = []
                for webhook_pattern in webhook_patterns:
                    found_webhooks.extend(re.findall(webhook_pattern, html_content))

                base64_pattern = r'(?<![A-Za-z0-9+/])(?:[A-Za-z0-9+/]{4}){3,}={0,2}(?![A-Za-z0-9+/])'
                found_base64 = []
                for value in re.findall(base64_pattern, html_content):
                    try:
                        base64.b64decode(value, validate=True)
                        found_base64.append(value)
                    except (ValueError, base64.binascii.Error):
                        pass
             
                if found_webhooks or found_base64:
                    if found_webhooks:
                        print(f'\n[RESULT] Yes, there is a webhook in this file.')
                        print("Found Webhook URL(s):")
                        for webhook in set(found_webhooks):
                            print(f" -> {webhook}")
                    else:
                        print('\n[RESULT] No webhook found in this file.')
                    if found_base64:
                        print("\nPossible Base64 value(s):")
                        for value in set(found_base64):
                            print(f" -> {value}")
                    print(' ')
                    input('press enter to go back')
                    self.clr_shit()
                else:
                    print('\n[RESULT] No webhook or Base64 value found in this file.')
                    print(' ')
                    input('press enter to go back')
                    self.clr_shit()
                 
            except Exception as e:
                print(RED + f"Error reading file: {e}" + RESET) 
                print(' ')
                input('press enter to go back')
                self.clr_shit()

    def uuid_generator(self):
        self.clr_shit()
        generated_uuid = str(uuid.uuid4()) 
        print('Your UUID:')
        print(generated_uuid) 
        print(' ')
         
        try:
            with open(uuid_file, "a", encoding="utf-8") as f:
                f.write(f"Generated UUID ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}):\n")
                f.write(generated_uuid + "\n" + " \n")
             
            print("Saved to: ", os.path.abspath(uuid_file))
        except Exception as e:
            print(RED + f"Error saving file: {e}" + RESET)
             
        print(' ')
        input('press enter to go back')
        self.clr_shit()

    def reverse_text(self):
        self.clr_shit()
        text = input("Text: ")
        print(text[::-1])
        print(' ')
        input('press enter to go back')
        self.clr_shit()

    def character_counter(self):
        self.clr_shit()
        text = input('Text (if it doesn\'t fit in 1 line, type "00805" to select a file): ')
        if text == '00805':
            selected_file = self.get_file_path()
            if selected_file:
                try:
                    with open(selected_file, 'r', encoding='utf-8') as f:
                        text = f.read()
                except Exception as e:
                    self.clr_shit()
                    print(RED + f'Error reading file: {e}' + RESET)
                    input('press enter to go back')
                    self.clr_shit()

        total_characters = len(text)
        total_characters_no_spaces = len(text.replace(' ', ''))  

        print(f"Total characters (with spaces): {total_characters}")
        print(f"Total characters (without spaces): {total_characters_no_spaces}")
        print(' ')
        input('press enter to go back')
        self.clr_shit()

    def banner_generator(self):
      try:
        self.clr_shit()
        ascii_text = input("Text: ")
        print(pyfiglet.figlet_format(ascii_text, font='banner'))
        print(' ')
        input('press enter to go back')
        self.clr_shit()
      except Exception as e:
          print(RED+f'Error: {e}'+RESET)

    def fastfetch(self):
        self.clr_shit()
        if shutil.which("fastfetch") is None:
            print("Fastfetch is not installed.")
            install_choice = input("Install it now with sudo pacman -S fastfetch? (Y/N): ").strip().lower()
            if install_choice.startswith("y"):
                if shutil.which("pacman") is None:
                    print("Pacman was not found. This installer command is for Arch Linux.")
                    input("press enter to go back")
                    self.clr_shit()
                    return
                download_fastfetch()
            else:
                print("Fastfetch was not installed.")
                input("press enter to go back")
                self.clr_shit()
                return

        if shutil.which("fastfetch") is not None:
            print(tadictext)
            subprocess.run(["fastfetch"], check=False)
            input("press enter to go back")
        else:
            print("Fastfetch is still unavailable. Check the installation and try again.")
            input("press enter to go back")
        self.clr_shit()

    def to_do_list(self):
        self.clr_shit()

        print("To-Do-List")
        print("1. Show To-Do-List")
        print("2. Add to/Create To-Do List")
        print("3. Go back")

        choice = input("Choice> ").strip()

        if choice == "1":
            try:
                with open(todolist_file, 'r', encoding='utf-8') as file:
                    tasks = [line.rstrip('\n') for line in file if line.strip()]
                if tasks:
                    print('\n'.join(f'{number}. {task}' for number, task in enumerate(tasks, 1)))
                else:
                    print('Your To-Do-List is empty.')
            except FileNotFoundError:
                print('Your To-Do-List is empty.')
            except OSError as e:
                print(f'Could not read the To-Do-List: {e}')

        elif choice == "2":
            task = input('Enter a task (leave blank to cancel): ').strip()
            if task:
                try:
                    os.makedirs(os.path.dirname(todolist_file), exist_ok=True)
                    with open(todolist_file, 'a', encoding='utf-8') as file:
                        file.write(task + '\n')
                    print('Task added.')
                except OSError as e:
                    print(f'Could not save the task: {e}')
            else:
                print('No task added.')

        elif choice != "3":
            print('Invalid choice.')

        input('press enter to go back')
        self.clr_shit()

    def exit(self):
        print(f"goodbye")
        time.sleep(0.5)
        sys.exit()

    def restart(self):
        print("Restarting TadicTools...")
        time.sleep(0.5)
        os.execv(sys.executable, [sys.executable] + sys.argv)
        
    def about_us(self):
        self.clr_shit()
        print('''Tadic-Tools REIMAGINED
Simple tools. No ads. No nonsense.

Features:
-QR Code Generator    -Password Generator
-Webhook Scanner      -ASCII Clock
-Game Launcher        -Timer
-UUID Generator       -Text Reverser
-Character Counter    -ASCII Banner Generator
-Sys Info             -and more...

Website: https://tadicservicesofficial.netlify.app 
Itch.io: https://eymorty.itch.io''')
        print(' ')
        input('press enter to go back')
        self.clr_shit() 


tembel_instance = tembel()
tembel_instance.clr_shit()
tools = {
    '1' : tembel_instance.ascii_clock,
    '2' : tembel_instance.open_a_game,
    '3' : tembel_instance.web_shortcuts,
    '4' : tembel_instance.qr_code_generator,
    '5' : tembel_instance.password_generator,
    '6' : tembel_instance.ping_test,
    '7' : tembel_instance.delete_temp,
    '8' : tembel_instance.lock_unlock_file,
    '9' : tembel_instance.timer,
    '10': tembel_instance.webhook_scanner,
    '11': tembel_instance.uuid_generator,
    '12': tembel_instance.reverse_text,
    '13': tembel_instance.character_counter,
    '14': tembel_instance.banner_generator,
    '15': tembel_instance.fastfetch,
    '16': tembel_instance.to_do_list,
    '17': tembel_instance.exit,
    '18': tembel_instance.restart,
    '99': tembel_instance.about_us
}

if not internet_available():
    print("TadicTools Reimagined needs an internet connection to start. Connect and try again.")
    input("press enter to exit")
    sys.exit()

autoclear()
robot = input_bold(RED+"Are you a robot? (Y/N) "+RESET).strip()
if robot.lower() == "y":
    if os.path.isfile(robot_dir) and shutil.which("xdg-open"):
        subprocess.Popen(["xdg-open", robot_dir])
        time.sleep(1)
    else:
        print("The optional robot video is not available in this build.")
        input("press enter to continue")
else:
  while True: 
     time.sleep(0.1)
     autoclear()
     print_bold(startuptext)
     print(YELLOW + 'Hello! This is TadicTools by Eymorty. Simple tools. No ads. No nonsense. Select an option below:' + RESET)
     print(' ')
     print(YELLOW + '-' * 85 + RESET)
     print(ORANGE + '|    [1. ASCII Clock.]                     [2. Open a game.]                        |' + RESET)                                                  
     print(ORANGE + '|    [3. Web Shortcuts.]                   [4. QR Code Generator.]                  |' + RESET)
     print(ORANGE + '|    [5. Password Generator.]              [6. See Your Ping.]                      |' + RESET)
     print(ORANGE + '|    [7. Delete Temp Folders (trash).]     [8. Lock Files/Open Locked Files.]       |' + RESET)
     print(ORANGE + '|    [9. Set Timer.]                       [10. Webhook Detector.]                  |' + RESET)
     print(ORANGE + '|    [11. UUID Generator.]                 [12. Text Reverser.]                     |' + RESET)
     print(ORANGE + '|    [13. Character Counter.]              [14. ASCII Banner Generator.]            |' + RESET)
     print(ORANGE + '|    [15. System Info.]                    [16. To-Do-List.]                        |' + RESET)
     print(ORANGE + '|    [17. EXIT]                            [18. RESTART TADICTOOLS]                 |' + RESET)
     print(YELLOW + '-' * 85 + RESET)
     print(' ')
     print_bold(YELLOW + '--Made by Eymorty--' + RESET)
     print(YELLOW + ' Itch.io: https://eymorty.itch.io' + RESET)
     print(YELLOW + ' Github:  https://github.com/ishowdih/Tadic-Tools' + RESET)
     print(' ')

     choice = input_bold(CYAN + f'Choice> ' + RESET).strip()
     if choice in tools:
        tools[choice]()

     elif choice == "cmd":
      autoclear()
      while True:
         print(ORANGE+"Tadic-Tools Reimagined Terminal\nType in your command freely."+RESET)
         cmd_command=input_bold(CYAN+f"{user}@{pcname}>"+RESET).strip()
         if cmd_command == "back_to_tools":
             break
         else:
          os.system(cmd_command)
          print(' ')

     else:
         autoclear()
         print('Well, either you typed it wrong or just didn\'t select something. Please enter a valid number (1-18 or 99).')
         input('press enter to go back')
