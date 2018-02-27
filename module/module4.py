#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, urllib2
from urllib2 import Request, urlopen, URLError, HTTPError

sys.path.append('/data/data/com.termux/files/usr/share/txtool/core')
from fungsi import warna, IP, txtool_dir
import menu as back

def empty():
    try:
        print(warna.kuning + "\n[!] " + warna.tutup + "Warning. your input is empty, txtool will be assume searching is canceled")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")

    except KeyError:
        pass

def cari_admin_panel():
    IP()
    admin_panel_folder = '/data/data/com.termux/files/usr/share/txtool/core'
    file = open("%s/daftar_admin_panel.txt" %
                     (admin_panel_folder), "r");
    print(warna.kuning + "\n[!]" + warna.tutup + " Example : example.com or www.example.com")
    link = raw_input(warna.biru + "[+]" + warna.tutup + " Enter your website " + warna.kuning + "  >>  " + warna.tutup)
    if link == '':
        empty()
        back.menu['menu_utama']()

    if "." not in link:
        print(warna.merah + "\n[x]" + warna.tutup + " warning ! website address is not valid, txtool will be assume searching is canceled.")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        back.menu['menu_utama']()

    print(warna.hijau + "\n[*]" + warna.tutup + " searching admin login pages, please wait a moment...\n")
    while True:
        sub_link = file.readline()
        if not sub_link:
            break
        request_link = "http://"+link+"/"+sub_link
        requests = Request(request_link)
        try:
            response = urlopen(requests)

        except HTTPError:
            continue

        except URLError:
            continue

        else:
            print warna.hijau + "[*]" + warna.tutup + " Found  ~~>>" ,request_link

