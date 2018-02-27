#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import subprocess, sys, os

sys.path.append("/data/data/com.termux/files/usr/share/txtool/core")
import menu as back
from fungsi import empty, warna, IP, txtool_dir, finish_dorking

def dorking():
    IP()
    print(warna.kuning + "\n[!]" + warna.tutup + " Example :  inurl:.php?id= ")
    dork = raw_input(warna.biru + "[+]" + warna.tutup + " Enter your dork keyword :  ")
    exploit = """ --exploit-get "'?%270x27" """
    inurl = '/data/data/com.termux/files/usr/share/txtool/core'
    if dork == '':
        empty()
        back.menu['menu_utama']()

    print(warna.kuning + "\n[!]" + warna.tutup + " if you dont want to use proxy, so just let it blank")
    print(warna.kuning + "[!]" + warna.tutup + " Example proxy :  socks5://127.0.0.1:9050 ")
    proxy = raw_input(warna.biru + "[+]" + warna.tutup + " Enter your proxy :  ")
    print(warna.kuning + "\n[!]" + warna.tutup + " Example :  output.txt")
    output = raw_input(warna.biru + "[+]" + warna.tutup + " Input the output file you want :  ")
    if output == '':
        empty()
        back.menu['menu_utama']()

    filewrite = open(txtool_dir + "/dork.txt", "w")
    filewrite.write("""\n%s\n""" % (dork))
    filewrite.close()
    if proxy == '':
        subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6,24 -t 1 %s -s %s " %
            (inurl, txtool_dir, exploit, output), shell=True).wait()
        finish_dorking()
        print(warna.hijau + "[*]" + warna.tutup + " Dork result has been saved to /data/data/com.termux/files/home/.txtool/output/%s " %
            (output))
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
        back.menu['menu_utama']()

    else :
        subprocess.Popen("cd %s && ./inurlbr --no-banner --proxy %s --dork-file %s/dork.txt -q 1,6,24 -t 1 %s -s %s " %
            (inurl, proxy, txtool_dir, exploit, output), shell=True).wait()
        finish_dorking()
        print(warna.hijau + "[*]" + warna.tutup + " Dork result has been saved to /data/data/com.termux/files/home/.txtool/output/%s " %
            (output))
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        back.menu['menu_utama']()
