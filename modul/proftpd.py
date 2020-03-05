import sys,os,time

def clear():
	os.system("clear")
def sleep():
	time.sleep(3)
def ftp():
	clear()
	path=input("Masukan lokasi folder contoh: /home/user/ftp: ")
	user=input("Insert user [ user debian ]: ")
	ftp="""
	\n<Anonymous {}>\nuser {}\n</Anonymous> 
	""".format(path,user)

	fileFtp=open("/etc/proftpd/proftpd.conf","a")
	fileFtp.write(ftp)
	fileFtp.close()

	from modul.style import style
	style()
	sleep()
	clear()
	from modul.style import restart
	restart()
	os.system("service proftpd restart")
	clear()
	from modul.style import success
	success()

	print("\nSilahkan cek konfigurasi di browser anda dengan mengetikan alamat ftp://ip_address_Debian_anda\n")