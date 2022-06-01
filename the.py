#usr/bin/python3
# mr root
"power for vip"
#---------------------
import sys,uuid,random,string
from time import sleep
from os import system
#---------------------
try:
    import requests
except:
    system("pip Install requests")
try:
    import datetime
except:
    try:
        system('pip install datetime')
    except:
        system('pip3 install datetime')
try:
    import flags
except:
    system("pip install flags")
#--------------------
try:
    from colorama import Fore
except:
    system("pip install colorama")
try:
    import colored
except:
    system("pip install colored")
#----
from colored import fg, bg, attr #background
import flags,requests
from colorama import Fore
import requests
#try:
    #system('pkg install sox -y')
#except:
    #None
    
#import MySql
#---------------------
# the   # color----
class color:
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    blue = "\033[36m"
    PINK = "\033[35m"
    DARKBLUE = "\033[34m"
    WHITE = "\033[00m"
#---------
tim = (datetime.datetime.today())
# random ---
a = ["f","¥","€","$","£","¢","&"]
b = ["f","¥","€","$","£","¢","&"]
c = ["f","¥","€","$","£","¢","&"]
d = ["f","¥","€","$","£","¢","&","ß","ę","€","$","£","¢","&","₹","₱","†"]
lol = ["ß","ę","€","$","£","¢","&","₹","₱","†"]
lo1 = (random.choice(a))
lo2 = (random.choice(b))
lo3 = (random.choice(c))
lo4 = (random.choice(d))
lo5 = (random.choice(lol))
lo6 = (random.choice(a))
lo7 = (random.choice(b))
lo8 = (random.choice(c))
name = F"{color.DARKBLUE}VIP"
target = input(f"\n{color.GREEN}[{tim}]<~> {color.blue}enter your target {color.WHITE}>> {color.PINK}\n")
print()
sleep(1)
#--------
try:
    system('clear')
except:
    system('cls')
#--------

sleep(0.5)
try:
    system('clear')
except:
    system('cls')
tim = (datetime.datetime.today())
te = requests.get("https://api.codebazan.ir/time-date/?td=all").text
sleep(1)
banner = (f'''\n{color.YELLOW}
         {color.GREEN} -[{name}]-{color.YELLOW}


.o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO                                                         OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO                                                   OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .



{color.BLUE}[{te}]



'''+f"""{color.RED}
_____________________________\n"""+Fore.BLUE+'''
[to enter the directory]'''+f"""

{color.YELLOW}[{color.GREEN}tyep{color.YELLOW}] {color.BLUE}="""+Fore.WHITE+''' /account/code/'''+f"""

{color.YELLOW}[{color.GREEN}type{color.YELLOW}] {color.BLUE}="""+ Fore.WHITE+''' /channel/code/'''+f""" 
{color.GREEN}

[type] {color.BLUE}="""+ Fore.WHITE+''' /group/code/'''+f"""\n\n{color.YELLOW}[{color.GREEN}type{color.YELLOW}] {color.BLUE}=""" + Fore.WHITE+"""/test/"""+f"""\n\n{color.YELLOW}[{color.GREEN}type{color.YELLOW}] {color.BLUE}=""" + Fore.WHITE+' /source-site/'+f"""{color.RED}

—————————————————————————————\n

{color.GREEN}[{tim}] {color.YELLOW}> {color.RED}root@terminal~:/code/# {color.BLUE}─╼ ❯❯❯"""+Fore.WHITE +''' ''')

for bnr in banner:
    sys.stdout.write(bnr)
    sys.stdout.flush()
    sleep(0.01)
code = input()
sleep(2) 
# Method 1 test" ----
system("clear")
if code == '/source-site/'.lower():
    sleep(1)
    source = input(f"\n{color.GREEN}[{tim}] | {color.YELLOW}enter web site for source html {color.WHITE}⟩⟩{color.PINK} ")
    rq = requests.get(source).text
    print(F"{color.YELLOW}source:\n\n")
    sleep(1)
    print(F'{color.RED}__________________________')
    print(Fore.WHITE+'')
    print(rq)
    print(f'\n{color.RED}____________________________\n')

if code == '/test/'.lower():
    sleep(1)
    usr = input(f"\n{color.GREEN}[{tim}] | {color.blue}enter username (channel) don't {color.RED}'@' {color.WHITE}>> {color.PINK}")
    req = requests.get(f"https://rubika.ir/{usr}")
    print()
    if req.status_code == 200:
        sleep(1)
        print (F"{color.PINK}found user: {color.DARKBLUE}[{usr}]")
        print ()
    elif req.status_code == 404:
        print (f"{color.RED}not found user: {color.DARKBLUE}[{usr}]")
        print ()
    elif req.status_code == 302:
        print ()
        print (f"{color.RED}not found user: {color.DARKBLUE}[{usr}]")
        print ()
    else:
        pass
# ----- method 1.1 ----+
if code == '/account/code/':
    print(f'{color.RED}\nreporter: ({name})\n\n')
    sleep(0.7)
    print(f'{color.GREEN}----------------------\n')
    cood = f"’/%/#/{lo1}/{lo2}{lo3}/{lo4}.{lo6}/{lo7}/{lo8}/#/%/’"
    #
    sleep(0.6)
    print(F'''{color.YELLOW}'''+cood)
    sleep(0.5)
    print(f'\n{color.GREEN}--------------------')
    print(F'\n{color.WHITE}send to {color.RED}[{target}]')
    print(f'\n[{color.PINK}{tim}]')
    # method 2 -----
elif code == "/channel/code/".lower():
    print(f'{color.RED}\nreporter: ({name})\n\n')
    sleep(0.7)
    print(f'{color.GREEN}----------------------\n')
    cd = ('["')
    dc = ('"]')
    uu = str(uuid.uuid1())
    cood = (cd+uu+dc)
    sleep(0.6)
    print(F'''{color.YELLOW}'''+cood)
    sleep(0.5)
    print(f'\n{color.GREEN}--------------------')
    print(F'\n{color.WHITE}send to {color.RED}[{target}]')
    print(f'\n[{color.PINK}{tim}]')
    # --- method 3 ----
elif code == "/group/code/".lower():
    print(f'{color.RED}\nreporter: ({name})\n\n')
    sleep(0.7)
    print(f'{color.GREEN}----------------------\n')
    #----- numbers ----
    number = (random.randint(1, 9))
    number1 = (random.randint(1, 9))
    number2 = (random.randint(1, 9))
    number3 = (random.randint(1, 9))
    number4 = (random.randint(1, 9))
    number5 = (random.randint(1, 9))
    number6 = (random.randint(1, 9))
    number7 = (random.randint(1, 9))
    number8 = (random.randint(1, 9))
    number9 = (random.randint(1, 9))
    number10 = (random.randint(1, 9))
    number11 = (random.randint(1, 9))
    number12 = (random.randint(1, 9))
    number13 = (random.randint(1, 9))
    number14 = (random.randint(1, 9))
    number15 = (random.randint(1, 9))
    number16 = (random.randint(1, 9))
    number17 = (random.randint(1, 9))
    number18 = (random.randint(1, 9))
    number19 = (random.randint(1, 9))
    number20 = (random.randint(1, 9))
    number21 = (random.randint(1, 9))
    number22 = (random.randint(1, 9))
    number23 = (random.randint(1, 9))
    number24 = (random.randint(1, 9))
    number25 = (random.randint(1, 9))
    
    num = str(number1)
    num1 = str(number2)
    num2 = str(number3)
    num3 = str(number4)
    num4 = str(number5)
    num5 = str(number6)
    num6 = str(number7)
    num7 = str(number)
    num8 = str(number8)
    num9 = str(number10)
    num10 = str(number11)
    num11 = str(number12)
    num12 = str(number9)
    num13 = str(number13)
    num14 = str(number14)
    num15 = str(number15)
    num16 = str(number16)
    num17 = str(number17)
    num18 = str(number18)
    num19 = str(number19)
    num20 = str(number20)
    num21 = str(number21)
    num22 = str(number22)
    num23 = str(number23)
    num24 = str(number24)
    num25 = str(number25)
    # --------
    
    algorithm = ["/f/h.u","/f/h","/M/f/h/","/m/G/","/g/r/h","/€/£/ĥ"]
    
    h = ["/6XC0/","/M3/g","/r/f/g//","/f/h.3/"]

    am = (random.choice(algorithm))
    
    am1 = (random.choice(h))

    char = (f"(`/{num}.{num1}.{num2}.{num3}{am1}{num4}{num5}{num6}{num7}{num8}{num9}{num10}{num11}{num12}{num13}{num14}/`)")
    chr = (f"(’/{num}.{num1}.{num2}.{num3}{am}{num4}{num5}{num6}{num7}{num8}{num9}{num10}{num11}{num12}{num13}{num14}/’)")
    cr = (f"(`/{num20}.{num1}.{num2}.{num3}{am}{num4}{num5}{num6}{num7}{num8}{num23}{num10}{num11}{num12}{num13}{num14}{num15}{num16}{num17}{num18}{num19}{num25}/`)")
    coode = [char,chr,cr]
    cood = (random.choice(coode))
    sleep(0.6)
    print(F'{color.YELLOW}')
    print(cood)
    sleep(0.5)
    print(f'\n{color.GREEN}--------------------')
    print(F'\n{color.WHITE}send to {color.RED}[{target}]')
    print(f'\n[{color.PINK}{tim}]')
    #---
# ------- the end ------
print()
sleep(3)
input(Fore.WHITE+"[music] "+Fore.RED+"(enter) ⟩⟩")
# file music ↓
try:
    system("play music.mp3 &> /dev/null")
except:
    system("pkg install sox")
#----- finished ------
print(Fore.WHITE+"\npower off")
sys.exit()