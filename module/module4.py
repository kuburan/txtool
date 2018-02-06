#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, urllib2
from urllib2 import Request, urlopen, URLError, HTTPError

sys.path.append('/data/data/com.termux/files/usr/share/txtool/core')
from fungsi import warna, IP, txtool_dir


# search admin login page
def cari_admin_panel():
    IP()
    admin_panel_folder = '/data/data/com.termux/files/usr/share/txtool/core'
    file = open("%s/daftar_admin_panel.txt" %
                     (admin_panel_folder), "r");
    print(warna.kuning + "\n[!]" + warna.tutup + "  Example : example.com or www.example.com")
    link = raw_input(warna.biru + "[+]" + warna.tutup + " Enter your website " + warna.kuning + "  >>  " + warna.tutup)
    print(warna.hijau + "\n[*] " + warna.tutup + " tXtool still searching admin login pages, please wait a moment...\n")
    while True:
        sub_link = file.readline()
        if not sub_link:
            break
        request_link = "http://"+link+"/"+sub_link
        requests = Request(request_link)
        try:
            response = urlopen(requests)

        except HTTPError as e:
            continue

        except URLError as e:
            continue

        else:
            print warna.hijau + "[*] " + warna.tutup + " Found  ~~>>" ,request_link

