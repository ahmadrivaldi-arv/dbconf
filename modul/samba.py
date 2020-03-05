import time,os,sys

def smb():
	tanya=input("Buat user terlebih dahulu ketik yes, jika sudah memiliki user ketik no: ")
	
	if tanya=='yes' or tanya=='y':
		mkusr=input("Buat User Untuk SAMBA: ")
		os.system("adduser {}".format(mkusr))

	user=input("Masukan User Yang Telah Dibuat : ")
	path=input("Masukan Lokasi Folder Contoh: [ /home/user/samba]: ")
	browsable=input("Aktifkan Browsable Ketik yes / no: ")
	writeable=input("Aktifkan Writeable Ketik yes / no: ")


	rslt="""

	\n[{}]\npath = {}\nvalid user = {}\nbrowseable = {}\nwriteable = {}
	""".format(user,path,user,browsable,writeable)
	os.system("clear")
	from modul.style import style
	style()
	time.sleep(2)
	fileSamba=open("/etc/samba/smb.conf","a")
	fileSamba.write(rslt)
	fileSamba.close()
	os.system("clear")
	from modul.style import success
	success()
	input("\nEnter untuk melanjutkan")
	os.system("clear")
	print("\nBuat password untuk SAMBA")
	os.system('smbpasswd -a {}'.format(user))
	os.system('chmod -R 777 {}'.format(path))
	os.system("clear")
	from modul.style import restart
	restart()
	time.sleep(3)
	os.system("/etc/init.d/samba restart")
	os.system("clear")
	print("\nKonfigurasi berhasil silahkan cek di client\n")
	
