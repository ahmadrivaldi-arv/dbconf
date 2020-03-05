import os, sys, time
def clear():
	os.system("clear")
def sleep():
	time.sleep(3)

def voip():
	clear()
	notlp=input("Buat nomor telepon contoh: 0221191 : ")
	context=input("Context contoh: XITKJ: ")
	username=input("Username untuk VOIP: ")
	secret=input("Secret (password): ")

	asterisk="""
	\n[general]\nport = 5060\nbindaddr = 0.0.0.0\ncontext = others\n[{}]\ntype = friend\ncontext = {}\nusername = {}\nsecret = {}\nhost = dynamic
	""".format(notlp,context,username,secret)
	fileVoip=open(" /etc/asterisk/sip.conf","a")
	fileVoip.write(asterisk)
	fileVoip.close()
	clear()
	print("\nBuat User Yang Kedua\n")
	
	notlp2=input("nomor telepon contoh: 0221191 : ")
	username=input("username untuk VOIP: ")
	secret=input("secret (password): ")

	asterisk="""
	\n[{}]\ntype = friend\ncontext = {}\nusername = {}\nsecret = {}\nhost = dynamic
	""".format(notlp2,context,username,secret)
	fileVoip=open(" /etc/asterisk/sip.conf","a")
	fileVoip.write(asterisk)
	fileVoip.close()

	eks="""
	\n[others]\n[{}]\nexten => {},1,Dial(SIP/{})\nexten => {},1,Dial(SIP/{})
	""".format(context,notlp,notlp,notlp2,notlp2)
	fileEks=open(" /etc/asterisk/extensions.conf","a")
	fileEks.write(eks)
	fileEks.close()

	from modul.style import style
	style()
	sleep()
	clear()
	from modul.style import restart
	restart()
	sleep()
	os.system("service asterisk restart")
	clear()
	from modul.style import success
	success()
	print("\nCek hasil configurasi di aplikasi zoiper menggunaan username yang dibut contoh dbconf@192.168.1.99 ")




