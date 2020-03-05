import os, sys, time


def author():
	print ("\n\tAUTHOR\n\t===================================\n\tCREATED BY : ahmadrivaldi_arv\n\tCODED BY   : rivaldi\n\tGITHUB     : https://github.com/ahmadrivaldi-arv\n\t\t     \n\tREPORT BUG ON FACEBOOK OR INSTAGRAM\n\t===================================\n\tfb : ahmad rivaldi\n\tig : ahmadrivaldi_arv\n\t===================================\n\t")

def clear():
	os.system("clear")

os.system("clear")

author()

def menu():
	print("1. Konfigurasi IP")
	print("2. Konfigurasi DNS")
	print("3. Konfigurasi SAMBA")
	print("4. Konfigurasi VOIP")
	print("5. Konfigurasi FTP")
	print("6. Quit\n")
	

	chs=input("Pilih: ")
	if (chs=='1'):
		from modul.ip import menuip
		os.system("clear")
		menuip()
	elif chs=='2':
		clear()
		os.system("apt-get install bind9 -y")
		input("\nTekan ENTER untuk melanjutkan ")
		os.system("clear")
		from modul.named import zone
		zone()
	elif chs=='3':
		clear()
		os.system("apt-get install samba -y")
		input("\nTekan ENTER untuk melanjutkan " )
		os.system("clear")
		from modul.samba import smb
		smb()
	elif chs=='4':
		clear()
		print("\nMasukan Debian 8 DVD 2\n")
		os.system("apt-cdrom add ")
		os.system("apt-get install asterisk -y")
		clear()
		from modul.voip import voip
		voip()
	elif chs=='5':
		clear()
		os.system("apt-get install proftpd -y")
		clear()
		from modul.proftpd import ftp
		ftp()
	elif chs=='6':
		sys.exit()
	else:
		
		print("\nMohon Pilih Dengan Benar\n")
		menu()

menu()



#____________________________
#|							|
#|			Author 			|
#|		 Ahmad rivaldi		|
#|__________________________|