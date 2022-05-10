#!/usr/bin/python
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import socket
import json				   		
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
Cyan = '\033[36m'
white = '\033[37m'
black = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
  _____             _   _             _               
 |  __ \           | | (_)           | |              
 | |__) |___   ___ | |_ _ _ __   __ _| |__   _____  __
 |  _  // _ \ / _ \| __| | '_ \ / _` | '_ \ / _ \ \/ /
 | | \ \ (_) | (_) | |_| | | | | (_| | |_) | (_) >  < 
 |_|  \_\___/ \___/ \__|_|_| |_|\__,_|_.__/ \___/_/\_\
                                                      
                                                             
 Websites Grabber V2.0    |   Priv8 method    | |  Coded by Rootinabox                             
                      
 [+] Telegram : @rootinabox
 [+] Channel  : https://t.me/Rootinabox_Channel

   \033[32m>----------------------------------<
   [-] 1. Grab list of IPs
   [-] 2. Reverse IPs
   \033[32m>---------------------------------<  
   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

choice = raw_input(':~# \033[34mChoose\033[32m Number : ')

def revsip1(url):
	try:
		grab = requests.get('https://www.threatcrowd.org/searchApi/v2/ip/report/?ip='+url, timeout=10,headers={'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}).text
		if 'response_code' in grab:
			res = re.findall('"domain":"(.*?)"',grab)
			for rr in res:
				resk = rr.replace('cpanel.','').replace('cpcalendars.','').replace('cpcontacts.','').replace('webmail.','').replace('webdisk.','').replace('hostmaster.','').replace('mail.','').replace('ns1.','').replace('ns2.','')
				print(yellow+'[+]' + str(resk) + green +' '+  '>' +'OK')
				open('Results.txt', 'a').write('http://'+resk+'\n')
			else:
				print(yellow+"[+]" + str(url) + red + " " + ">" +" error can't reslove domain")
				
	except:
		pass


def IpS():
	Shinn = raw_input('Start from page ~#: ')
	Codde = raw_input('Stop at page ~#: ')
	try:
		Head={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		for page in range(int(Shinn), int(Codde)):
			UrlWebs = 'http://bitverzo.com/recent_ip?p='+str(page)
			Shin = requests.get(UrlWebs, headers=Head, timeout=15).content
			if 'Recent IP reviews' in Shin:
				Shine = re.findall('<a href="http://bitverzo.com/ip/(.*?)">', Shin)
				for xxx in Shine:
					Repshin = xxx.replace('http://bitverzo.com/ip/', '')
					print('[+]' + Fore.GREEN + Repshin + Fore.WHITE)
					open('Rootinabox_IPs.txt', 'a').write(Repshin+'\n')
				else:
					print(Fore.RED + 'Coded By Rootinabox' + Fore.WHITE)
	except:
		pass

def Main():
	try:
		if choice =='1':
			IpS()
		if choice =='2':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev1 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(revsip1, rev1)

	except:
		pass		


if __name__ == '__main__':
	Main()