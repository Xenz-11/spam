#===========================================================================================================================#



#===================================================#
# OPEN SOURCE DIPELAJARI JAN GANTI BANNER DOANG :v  #
#===================================================#

#============[ INFO AUTHOR ]============#
'''
NAMA      : XENZ
GITHUB    : https://github.com/Xenz-11
WHATSAPP  : https://wa.me/6283138613993
INSTAGRAM : https://instagram/xenz_why
'''
#==============[ MODULE ]==============#
import os,sys,random,time,requests,json
from time import sleep
from time import strftime
#==============[ WARNA ]===============#

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
BM = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # CLEAR
O = '\033[38;2;255;127;0;1m' # ORANGE

#===============[ BANNER ]==============#
banner = (f'''
{M}┌───────────────────────────────────────────────────────────┐
{M}│    ███████╗██████╗  █████╗ ███╗   ███╗███████╗██████╗     │
{M}│    ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██╔══██╗    │
{M}│    ███████╗██████╔╝███████║██╔████╔██║█████╗  ██████╔╝    │
{P}│    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗    │
{P}│    ███████║██║     ██║  ██║██║ ╚═╝ ██║███████╗██║  ██║    │
{P}│    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    │
{P}└───────────────────────────────────────────────────────────┘
''')

class mulai:
	#=============[ JAN DI UBAH TAMBAHIN AJA HARGAI PEMBUATNYA :( ]==============#
	def follow(self):
		try:
			os.system('clear')
			print ('[•] FOLLOW FACEBOOK GW DULU BIAR KEREN >_<')
			sleep(1)
			os.system('xdg-open https://facebook.com/inu.pembangkang.7')

			sleep(7)
			os.system('clear')
			print ('[•] FOLLOW INSTAGRAM GW JUGA >_<')
			sleep(2)
			os.system('xdg-open https://instagram.com/xenz_why')
			sleep(3)
			self.spam()
		except ConnectionError:
			print ('[!] PERIKSA KONESI ANDA')
	#=============[ UBAH AJA SESUKA LU SAMPE RUSAK ]==============#
	def spam(self):
		os.system('clear')
		print (banner)
		print ('\tGUNAKAN AWALAN 8XXX\n')
		no = input (' [•] MASUKAN NOMOR TARGET : ')
		if no in ['83138613993','083138613993','6283138613993']:
			print (' [!] JANGAN NYEPAM AUTHOR HARGAI DIKIT ASU');sleep(2)
			self.spam()
		jum = int(input(' [•] MASUKAN JUMLAH SPAM  : '))
		print (f'\n     #=================[ SPAM DIMULAI ]==============#\n')
		for i in range(jum):
			x = i+1
			war = (M,K,U,B,O)
			ran = random.choice(war)
			xnxx = random.choice(['●','○','■','□','•'])
			req = requests.get('https://xenzi-wa.herokuapp.com/api/wa',params={'phone':no}).text
			js = json.loads(req)["result"]["Message"]
			jam = strftime('%H:%M:%S')
			if "Berhasil Spam Whatsapp | Xenzi Gan'z" in req:
				print (f'\r      {H}[{ran}{xnxx}{H}] SPAM TERKIRIM ► {x}\t\t{P}{jam}',end='',flush=True)
			else:
				print (f'      {P}[{M}×{P}] {M}SPAM GAGAL')
		print (f'\n\n     #=================[ SPAM SELESAI ]==============#\n')
		while True:
			try:
				nanya = input (' [?] MAU LAGI? Y/t : ')
				if nanya in ['y','Y']:
					self.spam()
				if nanya in ['t','T']:
					sys.exit()
				if not os.path.isfile(nanya):
					print (' [!] PILIH YANG BENER')
				else:
					break
			except KeyboardInterrupt:
				sys.exit()
if __name__ == "__main__":
	os.system('git pull')
	mulai().follow()
#===========================================================================================================================#
