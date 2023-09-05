import argparse
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def show_banner():
	print('''
 ____  _      ____                      _     
|  _ \\(_)_ __/ ___|  ___  __ _ _ __ ___| |__  
| | | | | '__\___ \ / _ \/ _` | '__/ __| '_ \\ 
| |_| | | |   ___) |  __/ (_| | | | (__| | | |
|____/|_|_|  |____/ \___|\\__,_|_|  \\___|_| |_|
                                              
	--[ Coded by : King D a.k.a N3utr0n
	--[ Team : FHC (FR13NDs Hackers Club)
	''')

def readFile(filename):
	try:
		filename = open(filename, 'r').read().split('\n')
		return filename
	except:
		print('[-] Erro ao abrir o arquivo.')
		return False

def make_url(url, uri):
	if url.endswith('/'):
		return url + uri
	else:
		return url + '/' + uri

def return_code(url):
	try:
		return requests.get(url, verify=False, allow_redirects=False).status_code
	except:
		pass

def DirSearch(url, filename, sn):
	print('[+] Target URL :', url)
	print('[!] File :', filename)
	print('[*] Searching directories and files...\n')

	filename = readFile(filename)
	if filename:
		for uri in filename:
			target_url = make_url(url, uri)
			code = return_code(target_url)
			if code == 200:
				print('\033[1;32m[+]\033[m Code : 200 OK | Found :', target_url,'\033[m')
			elif code == 302 or code == 303:
				print('\033[1;35m[!]\033[m Code :', code, ' | Moved :', target_url,'\033[m')
			if sn:
				print('\033[1;31m[-]\033[m Code : 404 | Not Found :\033[31m', target_url,'\033[m')
		print('\n[!] Done...')
	else:
		return False

show_banner()
parser = argparse.ArgumentParser(description='This tool search for directories and files.')
parser.add_argument('-u', '--url', help='Target URL.', required=True)
parser.add_argument('-f', '--filename', help='Filename that contains the URI.')
parser.add_argument('-sn', '--show-notfound', help='Show result not found', action='store_true')
parser.add_argument('-r', '--run', help='Running tool.', action='store_true')
args = parser.parse_args()

if args.run:
	if args.filename == None:
		args.filename = 'common.txt'

	DirSearch(args.url, args.filename, args.show_notfound)
