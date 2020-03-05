

import os,sys,time

def zone():
	Kuning='\033[93m'
	ungu='\033[95m '
	nila='\033[94m '
	merah='\033[91m'
	hijau='\033[92m'


	domain=input(hijau+"masukan nama domain: ")
	os.system("clear")
	print(Kuning+"Masukan Ip Address dengan cara dibalik contoh:"+merah+"192.168.20.1"+Kuning+" menjadi "+merah+"20.168.192")
	ip=input(merah+"masukan ip address: ")

	kurawal="{"
	kurawalt="}"

	hasil="""

	zone "{}" {}
		type master;
		file "/etc/bind/db.domain";
	{};

	zone "{}.in-addr.arpa"{}
		type master;
		file "/etc/bind/db.192";
	{};
	""".format(domain,kurawal,kurawalt,ip,kurawal,kurawalt)
	file=open("/etc/bind/named.conf.local","a")
	file.write(hasil)
	file.close()
	bind9()

def style():
	print("___________________________\n")
	print("\r 	Membuat File")
	print("___________________________")
def resolv():
	print("_________________________\n")
	print("\r 	Membuat File Resolv")
	print("_________________________")
def success():
	print("_________________________\n")
	print("\r 	Success")
	print("_________________________")
def restartnet():
	print("____________________________\n")
	print("\r 	Restarting Bind9")
	print("____________________________")

def bind9():
	nama_domain=input("\nMasukan nama domain kembali: ")
	ip_address=input("\nMasukan Ip server tanpa dibalik: ")
	oktet=input("\nMasukan host IP contoh: 192.168.1.99 hosnya adalah: 99: ")

	hasil=""" 
	\n;\n; BIND data file for local loopback interface\n;\n$TTL	604800\n@	IN	SOA	{}. root.{}. (
				      2		; Serial
				 604800		; Refresh
				  86400		; Retry
				2419200		; Expire
				 604800 )	; Negative Cache TTL\n;\n@	IN	NS	{}.\n@	IN	A	{}\nwww	IN	A	{}
	""".format(nama_domain,nama_domain,nama_domain, ip_address, ip_address)
	os.system("clear")
	style()
	time.sleep(3)

	file_dns=open("/etc/bind/db.domain","a")
	file_dns.write(hasil)

	hasil192="""

	\n;\n; BIND reverse data file for local loopback interface\n;\n$TTL    604800\n@       IN      SOA     {}. root.{}. (
	                              1         ; Serial
	                         604800         ; Refresh
	                          86400         ; Retry
	                        2419200         ; Expire
	                         604800 )       ; Negative Cache TTL\n;\n@       IN      NS      {}.\n{}      IN      PTR     {}.
	""".format(nama_domain,nama_domain,nama_domain,oktet,nama_domain)
	os.system("clear")
	style()
	time.sleep(3)
	db192=open("/etc/bind/db.192","a")
	db192.write(hasil192)
	db192.close()


	os.system("clear")
	style()
	time.sleep(3)

	hasil_resolv="""
	domain {}
	search {}
	nameserver {}
	""".format(nama_domain,nama_domain,ip_address)
	file_resolv=open("/etc/resolv.conf","w") # menyimpan file ke resolv
	file_resolv.write(hasil_resolv)
	file_dns.close()

	os.system("clear")
	restartnet()
	time.sleep(2)
	os.system("service bind9 restart")
	os.system("clear")
	success()
