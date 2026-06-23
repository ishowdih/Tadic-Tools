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
import tkinter as tk
from tkinter import filedialog
import qrcode
import sys

ihavednsig = ['1.1.1.1', '2']
ihavedns = ['8.8.8.8', '1']
Tadic_text = pyfiglet.figlet_format("TadicTools")
CYAN = "\033[36m"
YELLOW = "\033[33m"
ORANGE = '\033[38;5;214m'
RESET = "\033[0m"

ascii_raw = pyfiglet.figlet_format('             TadicTools', font='slant')
RealTDC_text = CYAN + ascii_raw + RESET

class tembel:
 def clr_shit(self):
   os.system('cls' if os.name == 'nt' else 'clear')

 def timer(self):
    try:
        tembel_instance.clr_shit()
        total_minutes = int(input("Enter the countdown time in minutes: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    total_seconds = total_minutes * 60
    
    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        
        time_format = f"{minutes:02d}:{seconds:02d}"
        
        print(f"\rTime Remaining: {time_format}", end="", flush=True)
        
        time.sleep(1)
        
        total_seconds -= 1

    print("\nTime's up!")


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
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(
        title="Select HTML File",
        filetypes=[("HTML Files", "*.html"), ("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    return file_path


log_clock = datetime.datetime.now().strftime('%H: %M: %S')
beatiful_clck = pyfiglet.figlet_format(log_clock)


tembel_instance = tembel()

tembel_instance.clr_shit()
while True: 
 print(RealTDC_text)
 print(YELLOW + 'Hello! This is TadicTools by TADİC SERVİCES. Simple tools. No ads. No nonsense. To see what program does, select one from there:' + RESET)
 print(' ')
 print(ORANGE + '[1. ASCII Clock]' + RESET)
 print(ORANGE + '[2. Open a game.]' + RESET)
 print(ORANGE + '[3. Web Shortcuts.]' + RESET)
 print(ORANGE + '[4. QR Code Generator.]' + RESET)
 print(ORANGE + '[5. Password Generator.]' + RESET)
 print(ORANGE + '[6. See Your Ping.]' + RESET)
 print(ORANGE + '[7. Delete Temp Folders (trash).]' + RESET)
 print(ORANGE + '[8. Lock Files/Open Locked Files.]' + RESET)
 print(ORANGE + '[9. Set Timer.]' + RESET)
 print(ORANGE + '[10. Select a readable (can be readable when opened with notepad) file to see if it has discord webhook inside.]' + RESET)
 print(ORANGE + '[11. UUID Generator just in case.]' + RESET)
 print(ORANGE + '[12. Text Reverser.]' + RESET)
 print(ORANGE + '[13. Character Counter (beta)]' + RESET)
 print(ORANGE + '[14. ASCII Banner Generator.]' + RESET)
 print(ORANGE + '[15. EXIT]' + RESET)
 print(' ')
 print(YELLOW + '--Made by Eymorty--' + RESET)
 print(YELLOW + ' itch.io: eymorty.itch.io' + RESET)
 print(YELLOW + ' Our Website: tadicofficial.netlify.app' + RESET)
 print(' ')

 choice = input('Select one: ').lower().strip()

 if choice == '1':
     tembel_instance.clr_shit()
     import threading
     
     def wait_for_input():
         global stop_clock
         input()
         stop_clock = True
     
     stop_clock = False
     try:
         
         thread = threading.Thread(target=wait_for_input)
         thread.daemon = True
         thread.start()
         
         while not stop_clock:
             log_clock = datetime.datetime.now().strftime('%H: %M: %S')
             beatiful_clck = pyfiglet.figlet_format(log_clock)
             print('\033[2J\033[H', end='')  # Clear screen
             print(beatiful_clck)
             print("Press Enter to go back...")
             time.sleep(1)
         
         tembel_instance.clr_shit()
     except KeyboardInterrupt:
         tembel_instance.clr_shit()
         input()
         tembel_instance.clr_shit()
     

 elif choice == '2':
   tembel_instance.clr_shit()
   print('-Game Menu-')
   print(r'[1. Set Path To An .exe File. For example: D:\SteamLibrary\steamapps\common\People Playground\People Playground.exe]')
   print('[2. Saved Paths]')
   print('[3. Delete Saved Paths]')
   print('[4. Open Valorant]')
   print('[5. Open Roblox]')
   print('')
   seçenek = input('Select one (Or 0 to go back to main menu): ')
   if seçenek == '0':
      tembel_instance.clr_shit()
   elif seçenek == '1':
      tembel_instance.clr_shit()
      path = input('Put The Path here (ONLY THE PATH, İF YOU TYPE ANYTHİNG THATS NOT İN THE PATH İT WONT WORK.): ')
      if os.path.exists(path):
        try:
            if os.path.exists("paths.json"):
                with open("paths.json", "r") as f:
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
                tembel_instance.clr_shit()
                print("Warning: This path is already saved!")
                input('press enter to go back')
                tembel_instance.clr_shit()
            else:
                subprocess.Popen([path])
                print("Game started.")
                input('press enter to go back')
                tembel_instance.clr_shit()

                log_entry = {
                    "path": path,
                    "timestamp": datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                }

                data.append(log_entry)

            with open("paths.json", "w") as f:
                json.dump(data, f, indent=4)

        except Exception as e:
            print(f"An error occurred while launching: {e}")
            input('press enter to go back')
            tembel_instance.clr_shit()
      else:
        print("Error: The path specified does not exist. Please check it.")
        input('press enter to go back')
        tembel_instance.clr_shit()

   elif seçenek == '4':
      try:
         os.system('start riotclient://launch-app/bhang/live/na')
      except FileNotFoundError:
         print('VALORANT not found.')
         input('press enter to go back')
         tembel_instance.clr_shit()
   elif seçenek == '5':
      try:
         os.system("start roblox-player:")
      except FileNotFoundError:
         print('RobloxPlayer not found.')
         input('press enter to go back')
         tembel_instance.clr_shit()

   elif seçenek == '2':
      tembel_instance.clr_shit()
      if os.path.exists("paths.json"):
         with open("paths.json", "r") as f:
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
         tembel_instance.clr_shit()
      else:
         print("--Saved Paths--")
         for i, entry in enumerate(data, 1):
            print(f"[{i}. {entry['path']} ({entry['timestamp']})]")
         print(' ')
         path_choice = input("Select a path to run (or 0 to go back): ")
         if path_choice == '0':
            tembel_instance.clr_shit()
         else:
            try:
               path_index = int(path_choice) - 1
               if 0 <= path_index < len(data):
                  selected_path = data[path_index]["path"]
                  if os.path.exists(selected_path):
                     subprocess.Popen([selected_path])
                     print("Game started.")
                     input('press enter to go back')
                     tembel_instance.clr_shit()
                  else:
                     print("Error: The selected path no longer exists.")
                     input('press enter to go back')
                     tembel_instance.clr_shit()
               else:
                  print("Invalid selection.")
                  input('press enter to go back')
                  tembel_instance.clr_shit()
            except ValueError:
               print("Invalid input.")
               input('press enter to go back')
               tembel_instance.clr_shit()
   
   elif seçenek == '3':
      tembel_instance.clr_shit()
      if os.path.exists("paths.json"):
         with open("paths.json", "r") as f:
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
         tembel_instance.clr_shit()
      else:
         print("--Delete Saved Paths--")
         for i, entry in enumerate(data, 1):
            print(f"[{i}. {entry['path']} ({entry['timestamp']})]")
         print('[0. Go back]')
         print(' ')
         delete_choice = input("Select a path to delete (or 0 to go back): ")
         if delete_choice == '0':
            tembel_instance.clr_shit()
         else:
            try:
               delete_index = int(delete_choice) - 1
               if 0 <= delete_index < len(data):
                  deleted_path = data.pop(delete_index)
                  with open("paths.json", "w") as f:
                     json.dump(data, f, indent=4)
                  tembel_instance.clr_shit()
                  print(f"Path deleted: {deleted_path['path']}")
                  input('press enter to go back')
                  tembel_instance.clr_shit()
               else:
                  print("Invalid selection.")
                  input('press enter to go back')
                  tembel_instance.clr_shit()
            except ValueError:
               print("Invalid input.")
               input('press enter to go back')
               tembel_instance.clr_shit()
         
 elif choice == '3':
    tembel_instance.clr_shit()
    print('--Web Menu--')
    print('[1. Open your itch.io dashboard]')
    print('[2. Open your Youtube profile]')
    print('[3. Select an Ai site to open] (this opens a menu where you select an Ai and when you select the ai it opens the ai you selected.)')
    print(' ')
    msgofthechc = input('Select one (Or 0 to go back to main menu): ')
    if msgofthechc == '1':
       webbrowser.open('https://itch.io/dashboard')
    elif msgofthechc == '2':
       webbrowser.open('https://youtube.com/profile')
    elif msgofthechc == '3':
       tembel_instance.clr_shit()
       tembel_instance.ai_menu()
    elif msgofthechc == '0':
       tembel_instance.clr_shit()

 elif choice == '4':
  tembel_instance.clr_shit()
  veri = input("Enter text or URL: ")
  img = qrcode.make(veri)
  img.save("qr.png")
  print("QR code saved as qr.png")
  print("Saved to:", os.path.abspath("qr.png"))
  input('press enter to go back')
  tembel_instance.clr_shit()

 elif choice == '5':
    tembel_instance.clr_shit()
    karakterler = string.ascii_letters + string.digits + "!@#$%&*"
    customsifre = input('Select lenght (Max 30) (only type numbers): ')
    try:
       customsifre_int = int(customsifre)
       if customsifre_int > 30 or customsifre_int <= 0:
          print('İnvalid Lenght!')
          print(' ')
          input('press enter to go back')
          tembel_instance.clr_shit()
       else:
          sifre = "".join(secrets.choice(karakterler) for _ in range(customsifre_int))
          print('Generating password...')
          print(' ')
          print(sifre)
          print(' ')
          input('press enter to go back')
          tembel_instance.clr_shit()
    except ValueError:
       print('Please enter a valid number!')
       input('press enter to go back')
       tembel_instance.clr_shit()
    
 elif choice == '6':
    tembel_instance.clr_shit()
    print('Which adress do you want to test your ping on?')
    msgonthehc = input('8.8.8.8 or 1.1.1.1 (you can say 1 or 2): ')

    if msgonthehc in ihavedns:
     os.system('ping 8.8.8.8')
     print(' ')
     input('press enter to go back')
     tembel_instance.clr_shit()

    elif msgonthehc in ihavednsig:
     os.system('ping 1.1.1.1')
     print(' ')
     input('press enter to go back')
     tembel_instance.clr_shit()
    else:
       print('İnvalid Option!')
       print(' ')
       input('press enter to go back')
       tembel_instance.clr_shit()

 elif choice == '7':
     tembel_instance.clr_shit()
     print('Temp files and folders (trash) are getting deleted, please wait...')
     time.sleep(1)
    
     temp_path = os.environ.get('TEMP')
     silinen_oge_sayisi = 0
     temizlenen_boyut_bayt = 0

     if temp_path and os.path.exists(temp_path):
        for item in os.listdir(temp_path):
            item_path = os.path.join(temp_path, item)
            try:
                # Eğer bu bir dosyaysa
                if os.path.isfile(item_path):
                    boyut = os.path.getsize(item_path) 
                    os.remove(item_path) 
                    temizlenen_boyut_bayt += boyut
                    silinen_oge_sayisi += 1
                
                # Eğer bu bir klasörse
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path) 
                    silinen_oge_sayisi += 1
            except Exception:
                pass

     temizlenen_mb = temizlenen_boyut_bayt / (1024 * 1024)

     tembel_instance.clr_shit()
     print('Cleaning Succesful!')
     print(' ')
     print(f'Deleted file/folder number: {silinen_oge_sayisi}')
     print(f'Estimated deleted trash size: {temizlenen_mb:.2f} MB')
     print(' ')
     input('press enter to go back')
     tembel_instance.clr_shit()

 elif choice == '8':
    tembel_instance.clr_shit()
    print('-- Encrypted File Hider --')
    print('WARNING: To restore an encrypted file, you MUST use the EXACT SAME file path and the EXACT SAME password.')
    print(' ')
    print('[1. Encrypt / Decrypt a File]')
    print('[0. Go Back]')
    print(' ')
    secim8 = input('Select one: ')

    if secim8 == '1':
        tembel_instance.clr_shit()
        dosya_yolu = input('Enter the full path of the file (e.g. C:\\Hidden\\secret.txt): ')
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

                tembel_instance.clr_shit()
                print('Success! The file has been encrypted (or decrypted).')
                input('press enter to go back')
                tembel_instance.clr_shit()

            except PermissionError:
                tembel_instance.clr_shit()
                print('Error: You do not have permission to access this file, or it is currently being used by another program.')
                input('press enter to go back')
                tembel_instance.clr_shit()
            except Exception as e:
                tembel_instance.clr_shit()
                print(f'An error occurred: {e}')
                input('press enter to go back')
                tembel_instance.clr_shit()
        else:
            tembel_instance.clr_shit()
            print('Error: File not found or password was left blank!')
            input('press enter to go back')
            tembel_instance.clr_shit()
            
    elif secim8 == '0':
        tembel_instance.clr_shit()
    else:
        tembel_instance.clr_shit()
        
 elif choice == '9':
      tembel_instance.timer()

 elif choice == '10':
    import re
    tembel_instance.clr_shit()
    print("\n[Opening file browser... Please select your HTML or .txt file.]")
    selected_file = tembel_instance.get_file_path()

    if selected_file:
       try:
        with open(selected_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        webhook_pattern = r'https://discord\.com/api/webhooks/\d+/[A-Za-z0-9_-]+'
        
        found_webhooks = re.findall(webhook_pattern, html_content)
        
        if found_webhooks:
            print(f'\n[RESULT] Yes, there is a webhook in this file.')
            print("Found Webhook URL(s):")
            for webhook in set(found_webhooks):
                print(f" -> {webhook}")
                print(' ')
                input('press enter to go back')
                tembel_instance.clr_shit()
        else:
            print('\n[RESULT] No webhook found in this file.')
            print(' ')
            input('press enter to go back')
            tembel_instance.clr_shit()
            
       except Exception as e:
        print(f"Error reading file: {e}") 
        print(' ')
        input('press enter to go back')
        tembel_instance.clr_shit()

 elif choice == '11':
    import uuid
    tembel_instance.clr_shit()
    print('Your UUID:')
    print(uuid.uuid4()) 
    print(' ')
    input('press enter to go back')
    tembel_instance.clr_shit()

 elif choice == '12':
    tembel_instance.clr_shit()
    text = input("Text: ")
    print(text[::-1])
    print(' ')
    input('press enter to go back')
    tembel_instance.clr_shit()

 elif choice == '13':
    tembel_instance.clr_shit()
    text = input('Text (if it doesnt fit in 1 line (if u paste the text), say "00805" to open file explorer to select a file.): ')
    if text == '00805':
       selected_file = tembel_instance.get_file_path()
       if selected_file:
           try:
               with open(selected_file, 'r', encoding='utf-8') as f:
                   text = f.read()
           except Exception as e:
               tembel_instance.clr_shit()
               print(f'Error reading file: {e}')
               input('press enter to go back')
               tembel_instance.clr_shit()


    total_characters = len(text)
    total_characters_no_spaces = len(text.replace(' ', ''))  

    print(f"Total characters (with spaces): {total_characters}")
    print(f"Total characters (without spaces): {total_characters_no_spaces}")
    print(' ')
    input('press enter to go back')
    tembel_instance.clr_shit()

 elif choice == '14':
    tembel_instance.clr_shit()
    ascıı_text = input("Text: ")
    print(pyfiglet.figlet_format(ascıı_text, font= 'banner'))
    print(' ')
    input('press enter to go back')
    tembel_instance.clr_shit()

 elif choice == '15':
    sys.exit()

 else:
    tembel_instance.clr_shit()
    print('Well, either you typed it wrong or just didnt select something, To use this, you need to make sure to type ONLY 1, 2, 3, 4, 5, 6, 7...')
    input('press enter to go back')
    tembel_instance.clr_shit()