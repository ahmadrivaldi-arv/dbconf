import os
import sys, time

def style():
	print("_________________________\n")
	print("\r 	Membuat File")
	print("_________________________")
def success():
	print("_________________________\n")
	print("\r 	Success")
	print("_________________________")
def restartnet():
	print("_________________________\n")
	print("\r 	Restarting ")
	print("_________________________")

def ip_replace():
	#baris untuk input user
	interface=input("interface [contoh: eth0, eth1]:  ")
	get_ip=input("Masukan Ip Adress: ")
	get_netmask=input("Netmask: ")
	get_gateway=input("Gateway: ")
	os.system("cls")
	style()
	time.sleep(2)
	os.system("cls")
	success()
	#cetak hasil input 
	hasil="""
	\nsource /etc/network/interfaces.d/*

	\n# The loopback network interface
	\nauto lo
	\niface lo inet loopback

	\n# The primary network interface
	\nauto {}\niface {} inet static
		address  {}
		netmask  {}
		gateway  {}
	""".format(interface,interface,get_ip,get_netmask,get_gateway)

	file_ip=open("/etc/network/interfaces","w")
	file_ip.write(hasil)
	file_ip.close()

	restartnet()
	time.sleep(2)
	os.system("service networking restart")

def ip_new():
	interface=input("interface [contoh: eth0, eth1]:  ")
	get_ip=input("Masukan Ip Adress: ")
	get_netmask=input("Netmask: ")
	get_gateway=input("Gateway : ")

	os.system("clear")
	style()
	time.sleep(2)
	
	os.system("clear")
	success()
	

	hasil="""
	\nauto {}\niface {} inet static
		address  {}
		netmask  {}
		gateway  {}\n
	""".format(interface,interface,get_ip,get_netmask,get_gateway)

	file_ip=open("/etc/network/interfaces","a")
	file_ip.write(hasil)
	file_ip.close()
	os.system("clear")
	restartnet()
	time.sleep(2)
	os.system("service networking restart")
	os.system("service networking restart")
	os.system("service networking restart")
	os.system("clear")
	success()

def menuip():
	print("1. Konfigurasi Ip Address baru")
	print("2. Tambah Ip Address ")
	print("3. Exit")
	pilih=input("Pilih: ")
	if pilih=='1':
		os.system("clear")
		ip_replace()
	elif pilih=='2':
		os.system("clear")
		ip_new()
	elif pilih=='3':
		sys.exit(0)
	else:
		print("Mohon Pilih Dengan Benar")
		input()
		os.system("clear")
		menuip()