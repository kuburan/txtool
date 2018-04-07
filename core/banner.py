#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

from fungsi import warna

def banner():
    version = open("/data/data/com.termux/files/usr/share/txtool/core/version.txt", "r").read().rstrip()
    print(warna.hijau + """
   ______     __  ____  ____  __
  /_  __/  __/ /_/ __ \/ __ \/ /
   / / | |/_/ __/ / / / / / / / """ + warna.kuning + """
  / / _>  </ /_/ /_/ / /_/ / /___
 /_/ /_/|_|\__/\____/\____/_____/
"""+ warna.tutup + """
  Author     : """ + warna.abuabu + """ Kuburan A.K.A Gembur Ae """+ warna.tutup + """
  Version    : """ + warna.abuabu +version+ warna.tutup + """
  Codename   : """ + warna.abuabu + """ Tali Pocong """+ warna.tutup + """
""" + warna.merah + """ =======================================
 =======================================""" + warna.tutup + """
""")
