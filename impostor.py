# !/data/data/com.termux/files/home/spamSMS/impostor.py
# -*- coding : utf-8 -*-
import xncode
import sys
import base64
import time
import os

user_token=[
    {'service_plan_id' : 'ffd5a3bece11476fa839f2d3a2a13dd6',
     'token' : '15711ec874be479b9dd5aec3fbdb2829'
    }]

failcount=0
try:
    with open('.failsend', 'rb') as o:
        count=o.readlines()
    failcount+=len(count)
except IOError:
    pass

def user():
    io=["linux", 'linux2']
    if sys.platform not in io:
        print 'Maaf Tols Hanya Dapat Digunakan Pada Platform Linux Saja :('
        exit()

def fail(msg, number):
    with open('.failsend', 'ab') as o:
        o.write("Succes %s {'number': '%s',  'msg' : '%s' }\n"%(failcount+1, number, msg))


def xcode_banner():
    BOLD='\033[1;37m'
    time.sleep(1)
    x=base64.b64decode("4paI")
    a=base64.b64decode("4pWU")
    l=base64.b64decode("4pWa")
    j=base64.b64decode("4pWX")
    i=base64.b64decode("4pWR")
    n=base64.b64decode("4pWQ")
    c=base64.b64decode("4pWd")
    me="                  \033[1m\033[41m              ..::zollamXcode::..               \033[0m%s\n"%(BOLD)
    R="\033[31m"
    W="\033[37m"
    #os.system("clear")
#    print "\033[1mTryng... Kartu Keluraga : %s    Data Warga : %s\n"%(O,V)
    print "%s                  {}%s    {}%s{}   {}%s    {}%s  {}%s  {}%s   {}%s{}%s".format(a,a,W,a,a,a,a,a,a)%(R,x*3,x*3,x*2,x*2,x*2,x*6,x*2,x*2)
    print "%s                  {}{}%s  {}%s{}    {}{}{}    {}{}{}  {}{}{}  {}{}{}   {}{}{}{}{}{}".format(l,j,a,W,l,n,c,l,n,c,l,n,c,l,n*5,c,l,n,c,l,n,c)%(R,x*3,x*3)
    print "%s                   {}{}%s{}%s{}    {}%s  {}%s  {}%s   {}%s".format(l,j,a,W,a,a,a,a)%(R,x*3,x*3,x*5,x*7,x*6,x*5)
    print "%s                    {}{}%s{}     {}%s{}{}  {}%s{}{}%s  {}%s{}{}%s  {}%s{}{}".format(l,j,W,i,n*2,c,i,n*2,j,i,n*2,j,i,n*2,c)%(R,x*5,x*2,x*2,x*2,x*2,x*2,x*2)
    print "%s                    {}%s{}%s{}    {}%s     {}%s  {}%s  {}%s  {}%s  {}%s".format(a,j,W,i,i,i,i,i,i)%(R,x*3,x*3,x*2,x*2,x*2,x*2,x*2,x*5)
    print "%s                   {}%s {}{}%s{}   {}%s     {}%s  {}%s  {}%s  {}%s  {}%s{}{}".format(a,l,j,W,i,i,i,i,i,i,n*2,c)%(R,x*3,x*3,x*2,x*2,x*2,x*2,x*2,x*2)
    print "%s                  {}%s   {}{}%s{}  {}%s  {}%s  {}%s   {}%s".format(a,l,j,W,i,i,i,i)%(R,x*3,x*3,x*5,x*7,x*6,x*5)
    print "%s                  {}{}{}    {}{}{}{}  {}{}{}  {}{}{}  {}{}{}   {}{}{}".format(l,n*2,c,l,n*2,c,W,l,n*4,c,l,n*6,c,l,n*5,c,l,n*4,c)%(R)
    print me

def importerror():
    r=raw_input("    Maaf ada module yang dibutuhkan dan belum di install !\n    Gunakan : $ pip install clx-sdk-xms\n    dan kembali lagi :)\n    Apakah Anda Ingin Menginstall Secara Otomatis [Y] | [N] : ")
    if r.lower() == 'y':
        os.system('pip install clx-sdk-xms')
        print 'Oke, Back To Script Lagi Boss..'; exit()
    else:
        print 'Oke, Good Luck :)'; time.sleep(1); exit()



#---------------> Jika Anda Membutuhkan Token
class sadpeople:
    service_plan_id='a5a442d99c504ef3bd31b7d738d5c09a'
    token='3aea4aeda912486084dbe0c974057e35'
    # Ini Token Baru Dan Isi Nya 27 Pesan Lagi



if __name__ == '__main__':
    site=os.environ['_']+'.7/'
    try:
        from shutil import copy as cp
        cp('xncode.pyc', site)
    except IOError:
        pass
