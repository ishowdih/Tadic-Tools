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
        total_minutes = int(input("Geri sayım süresini dakika olarak girin: "))
    except ValueError:
        print("Lütfen geçerli bir tam sayı girin.")
        return

    total_seconds = total_minutes * 60
    
    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        
        time_format = f"{minutes:02d}:{seconds:02d}"
        
        print(f"\rKalan Süre: {time_format}", end="", flush=True)
        
        time.sleep(1)
        
        total_seconds -= 1

    print("\nSüre doldu!")


 def ai_menu(self):
  print('-- Yapay Zeka Menüsü --')
  print('[1. ChatGPT]')
  print('[2. Gemini]')
  print('[3. Grok]')
  print('[4. Claude]')
  print('[5. Çıkış]')
  print(' ')
  ai_select = input('Yaypay Zeka Seçin: ')
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
     print('Bir seçim yapmalısınız. ')
     input('Geri dönmek için Enter\'a basın')

 def get_file_path(self):
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(
        title="HTML Dosyası Seçin",
        filetypes=[("HTML Dosyaları", "*.html"), ("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")]
    )
    return file_path


log_clock = datetime.datetime.now().strftime('%H: %M: %S')
beatiful_clck = pyfiglet.figlet_format(log_clock)


tembel_instance = tembel()

tembel_instance.clr_shit()
while True: 
 print(RealTDC_text)
 print(YELLOW + 'Merhaba! Bu TADİC SERVİCES tarafından yapılan TadicTools programıdır. Basit araçlar. Reklam yok. Saçmalık yok. Programın ne yaptığını görmek için menüden birini seçin:' + RESET)
 print(' ')
 print(ORANGE + '[1. ASCII Saat]' + RESET)
 print(ORANGE + '[2. Oyun Aç.]' + RESET)
 print(ORANGE + '[3. Web Kısayolları.]' + RESET)
 print(ORANGE + '[4. QR Kod Oluşturucu.]' + RESET)
 print(ORANGE + '[5. Şifre Oluşturucu.]' + RESET)
 print(ORANGE + '[6. Ping Durumunu Gör.]' + RESET)
 print(ORANGE + '[7. Geçici Klasörleri Temizle (Çöp).]' + RESET)
 print(ORANGE + '[8. Dosyaları Şifrele / Şifreyi Çöz.]' + RESET)
 print(ORANGE + '[9. Zamanlayıcı Kur.]' + RESET)
 print(ORANGE + '[10. Bir dosya seçip içinde Discord Webhook\'u olup olmadığını kontrol et.]' + RESET)
 print(ORANGE + '[11. UUID Oluşturucu (Her ihtimale karşı).]' + RESET)
 print(ORANGE + '[12. Metin Ters çevirici.]' + RESET)
 print(ORANGE + '[13. Karakter Sayıcı (Beta)]' + RESET)
 print(ORANGE + '[14. ASCII Banner Oluşturucu.]' + RESET)
 print(ORANGE + '[15. ÇIKIŞ]' + RESET)
 print(' ')
 print(YELLOW + '-- Eymorty Tarafından Yapılmıştır --' + RESET)
 print(YELLOW + ' itch.io: eymorty.itch.io' + RESET)
 print(YELLOW + ' Web Sitemiz: tadicofficial.netlify.app' + RESET)
 print(' ')

 choice = input('Seçim yapın: ').lower().strip()

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
             print('\033[2J\033[H', end='')  # Ekranı temizle
             print(beatiful_clck)
             print("Geri dönmek için Enter'a basın...")
             time.sleep(1)
         
         tembel_instance.clr_shit()
     except KeyboardInterrupt:
         tembel_instance.clr_shit()
         input()
         tembel_instance.clr_shit()
     

 elif choice == '2':
   tembel_instance.clr_shit()
   print('- Oyun Menüsü -')
   print(r'[1. Bir .exe Dosyasının Yolunu Girin. Örnek: D:\SteamLibrary\steamapps\common\People Playground\People Playground.exe]')
   print('[2. Kayıtlı Yollar]')
   print('[3. Kayıtlı Yolları Sil]')
   print('[4. Valorant\'ı Aç]')
   print('[5. Roblox\'u Aç]')
   print('')
   seçenek = input('Seçim yapın (Ana menüye dönmek için 0 yazın): ')
   if seçenek == '0':
      tembel_instance.clr_shit()
   elif seçenek == '1':
      tembel_instance.clr_shit()
      path = input('Dosya yolunu buraya yapıştırın (YALNIZCA DOSYA YOLU, EĞER YOL DIŞINDA BİR ŞEY YAZARSANIZ ÇALIŞMAZ): ')
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
                print("Uyarı: Bu dosya yolu zaten kayıtlı!")
                input('Geri dönmek için Enter\'a basın')
                tembel_instance.clr_shit()
            else:
                subprocess.Popen([path])
                print("Oyun başlatıldı.")
                input('Geri dönmek için Enter\'a basın')
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
            print(f"Başlatılırken bir hata oluştu: {e}")
            input('Geri dönmek için Enter\'a basın')
            tembel_instance.clr_shit()
      else:
        print("Hata: Belirtilen dosya yolu mevcut değil. Lütfen kontrol edin.")
        input('Geri dönmek için Enter\'a basın')
        tembel_instance.clr_shit()

   elif seçenek == '4':
      try:
         os.system('start riotclient://launch-app/bhang/live/na')
      except FileNotFoundError:
         print('VALORANT bulunamadı.')
         input('Geri dönmek için Enter\'a basın')
         tembel_instance.clr_shit()
   elif seçenek == '5':
      try:
         os.system("start roblox-player:")
      except FileNotFoundError:
         print('RobloxPlayer bulunamadı.')
         input('Geri dönmek için Enter\'a basın')
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
         print("Kayıtlı dosya yolu bulunamadı.")
         input('Geri dönmek için Enter\'a basın')
         tembel_instance.clr_shit()
      else:
         print("-- Kayıtlı Yollar --")
         for i, entry in enumerate(data, 1):
            print(f"[{i}. {entry['path']} ({entry['timestamp']})]")
         print(' ')
         path_choice = input("Çalıştırmak için bir yol seçin (veya geri dönmek için 0 yazın): ")
         if path_choice == '0':
            tembel_instance.clr_shit()
         else:
            try:
               path_index = int(path_choice) - 1
               if 0 <= path_index < len(data):
                  selected_path = data[path_index]["path"]
                  if os.path.exists(selected_path):
                     subprocess.Popen([selected_path])
                     print("Oyun başlatıldı.")
                     input('Geri dönmek için Enter\'a basın')
                     tembel_instance.clr_shit()
                  else:
                     print("Hata: Seçilen dosya yolu artık mevcut değil.")
                     input('Geri dönmek için Enter\'a basın')
                     tembel_instance.clr_shit()
               else:
                  print("Geçersiz seçim.")
                  input('Geri dönmek için Enter\'a basın')
                  tembel_instance.clr_shit()
            except ValueError:
               print("Geçersiz giriş.")
               input('Geri dönmek için Enter\'a basın')
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
         print("Kayıtlı dosya yolu bulunamadı.")
         input('Geri dönmek için Enter\'a basın')
         tembel_instance.clr_shit()
      else:
         print("-- Kayıtlı Yolları Sil --")
         for i, entry in enumerate(data, 1):
            print(f"[{i}. {entry['path']} ({entry['timestamp']})]")
         print('[0. Geri Dön]')
         print(' ')
         delete_choice = input("Silmek için bir yol seçin (veya geri dönmek için 0 yazın): ")
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
                  print(f"Yol silindi: {deleted_path['path']}")
                  input('Geri dönmek için Enter\'a basın')
                  tembel_instance.clr_shit()
               else:
                  print("Geçersiz seçim.")
                  input('Geri dönmek için Enter\'a basın')
                  tembel_instance.clr_shit()
            except ValueError:
               print("Geçersiz giriş.")
               input('Geri dönmek için Enter\'a basın')
               tembel_instance.clr_shit()
         
 elif choice == '3':
    tembel_instance.clr_shit()
    print('-- Web Menüsü --')
    print('[1. itch.io panelini aç]')
    print('[2. YouTube profilini aç]')
    print('[3. Açmak için bir Yapay Zeka sitesi seçin] (Bu seçenek, yapay zeka seçebileceğiniz yeni bir menü açar.)')
    print(' ')
    msgofthechc = input('Seçim yapın (Ana menüye dönmek için 0 yazın): ')
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
  veri = input("Metin veya URL girin: ")
  img = qrcode.make(veri)
  img.save("qr.png")
  print("QR kod qr.png olarak kaydedildi.")
  print("Kaydedilen konum:", os.path.abspath("qr.png"))
  input('Geri dönmek için Enter\'a basın')
  tembel_instance.clr_shit()

 elif choice == '5':
    tembel_instance.clr_shit()
    karakterler = string.ascii_letters + string.digits + "!@#$%&*"
    customsifre = input('Şifre uzunluğu seçin (Maks 30) (Sadece sayı girin): ')
    try:
       customsifre_int = int(customsifre)
       if customsifre_int > 30 or customsifre_int <= 0:
          print('Geçersiz Uzunluk!')
          print(' ')
          input('Geri dönmek için Enter\'a basın')
          tembel_instance.clr_shit()
       else:
          sifre = "".join(secrets.choice(karakterler) for _ in range(customsifre_int))
          print('Şifre oluşturuluyor...')
          print(' ')
          print(sifre)
          print(' ')
          input('Geri dönmek için Enter\'a basın')
          tembel_instance.clr_shit()
    except ValueError:
       print('Lütfen geçerli bir sayı girin!')
       input('Geri dönmek için Enter\'a basın')
       tembel_instance.clr_shit()
    
 elif choice == '6':
    tembel_instance.clr_shit()
    print('Hangi adreste ping testi yapmak istersiniz?')
    msgonthehc = input('8.8.8.8 veya 1.1.1.1 (1 veya 2 yazabilirsiniz): ')

    if msgonthehc in ihavedns:
     os.system('ping 8.8.8.8')
     print(' ')
     input('Geri dönmek için Enter\'a basın')
     tembel_instance.clr_shit()

    elif msgonthehc in ihavednsig:
     os.system('ping 1.1.1.1')
     print(' ')
     input('Geri dönmek için Enter\'a basın')
     tembel_instance.clr_shit()
    else:
       print('Geçersiz Seçenek!')
       print(' ')
       input('Geri dönmek için Enter\'a basın')
       tembel_instance.clr_shit()

 elif choice == '7':
     tembel_instance.clr_shit()
     print('Geçici dosyalar ve klasörler (çöp) siliniyor, lütfen bekleyin...')
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
     print('Temizlik Başarılı!')
     print(' ')
     print(f'Silinen dosya/klasör sayısı: {silinen_oge_sayisi}')
     print(f'Tahmini silinen çöp boyutu: {temizlenen_mb:.2f} MB')
     print(' ')
     input('Geri dönmek için Enter\'a basın')
     tembel_instance.clr_shit()

 elif choice == '8':
    tembel_instance.clr_shit()
    print('-- Gizli Dosya Şifreleyici --')
    print('UYARI: Şifrelenmiş bir dosyayı eski haline getirmek için KESİNLİKLE AYNI dosya yolunu ve AYNI şifreyi kullanmalısınız.')
    print(' ')
    print('[1. Bir Dosyayı Şifrele / Şifresini Çöz]')
    print('[0. Geri Dön]')
    print(' ')
    secim8 = input('Seçim yapın: ')

    if secim8 == '1':
        tembel_instance.clr_shit()
        dosya_yolu = input('Dosyanın tam yolunu girin (Örn: C:\\Gizli\\secret.txt): ')
        sifre = input('Bir şifre girin (veya şifreyi çözmek için mevcut şifreyi girin): ')

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
                print('Başarılı! Dosya şifrelendi (veya şifresi çözüldü).')
                input('Geri dönmek için Enter\'a basın')
                tembel_instance.clr_shit()

            except PermissionError:
                tembel_instance.clr_shit()
                print('Hata: Bu dosyaya erişim izniniz yok veya dosya başka bir program tarafından kullanılıyor.')
                input('Geri dönmek için Enter\'a basın')
                tembel_instance.clr_shit()
            except Exception as e:
                tembel_instance.clr_shit()
                print(f'Bir hata oluştu: {e}')
                input('Geri dönmek için Enter\'a basın')
                tembel_instance.clr_shit()
        else:
            tembel_instance.clr_shit()
            print('Hata: Dosya bulunamadı veya şifre boş bırakıldı!')
            input('Geri dönmek için Enter\'a basın')
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
    print("\n[Dosya tarayıcı açılıyor... Lütfen HTML veya .txt dosyanızı seçin.]")
    selected_file = tembel_instance.get_file_path()

    if selected_file:
       try:
        with open(selected_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        webhook_pattern = r'https://discord\.com/api/webhooks/\d+/[A-Za-z0-9_-]+'
        
        found_webhooks = re.findall(webhook_pattern, html_content)
        
        if found_webhooks:
            print(f'\n[SONUÇ] Evet, bu dosyada bir webhook bulundu.')
            print("Bulunan Webhook URL(leri):")
            for webhook in set(found_webhooks):
                print(f" -> {webhook}")
                print(' ')
                input('Geri dönmek için Enter\'a basın')
                tembel_instance.clr_shit()
        else:
            print('\n[SONUÇ] Bu dosyada webhook bulunamadı.')
            print(' ')
            input('Geri dönmek için Enter\'a basın')
            tembel_instance.clr_shit()
            
       except Exception as e:
        print(f"Dosya okunurken hata oluştu: {e}") 
        print(' ')
        input('Geri dönmek için Enter\'a basın')
        tembel_instance.clr_shit()

 elif choice == '11':
    import uuid
    tembel_instance.clr_shit()
    print('UUID\'niz:')
    print(uuid.uuid4()) 
    print(' ')
    input('Geri dönmek için Enter\'a basın')
    tembel_instance.clr_shit()

 elif choice == '12':
    tembel_instance.clr_shit()
    text = input("Metin: ")
    print(text[::-1])
    print(' ')
    input('Geri dönmek için Enter\'a basın')
    tembel_instance.clr_shit()

 elif choice == '13':
    tembel_instance.clr_shit()
    text = input('Metin (Eğer metin tek satıra sığmıyorsa, dosya seçiciden dosya seçmek için "00805" yazın): ')
    if text == '00805':
       selected_file = tembel_instance.get_file_path()
       if selected_file:
           try:
               with open(selected_file, 'r', encoding='utf-8') as f:
                   text = f.read()
           except Exception as e:
               tembel_instance.clr_shit()
               print(f'Dosya okunurken hata oluştu: {e}')
               input('Geri dönmek için Enter\'a basın')
               tembel_instance.clr_shit()


    total_characters = len(text)
    total_characters_no_spaces = len(text.replace(' ', ''))  

    print(f"Toplam karakter sayısı (boşluklar dahil): {total_characters}")
    print(f"Toplam karakter sayısı (boşluklar hariç): {total_characters_no_spaces}")
    print(' ')
    input('Geri dönmek için Enter\'a basın')
    tembel_instance.clr_shit()

 elif choice == '14':
    tembel_instance.clr_shit()
    ascıı_text = input("Metin: ")
    print(pyfiglet.figlet_format(ascıı_text, font= 'banner'))
    print(' ')
    input('Geri dönmek için Enter\'a basın')
    tembel_instance.clr_shit()

 elif choice == '15':
    sys.exit()

 else:
    tembel_instance.clr_shit()
    print('Görünüşe göre ya yanlış yazdınız ya da bir şey seçmediniz. Bunu kullanmak için YALNIZCA 1, 2, 3, 4, 5, 6, 7... yazmalısınız.')
    input('Geri dönmek için Enter\'a basın')
    tembel_instance.clr_shit()