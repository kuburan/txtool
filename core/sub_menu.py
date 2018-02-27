#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, os, time
import menu as back
from fungsi import check_metasploit, warna

def menu_utama():
    print("\n\t[" + warna.hijau + "1" + warna.tutup + "]" + warna.abuabu + "  Multi Handler" + warna.tutup)
    print("\t[" + warna.hijau + "2" + warna.tutup + "]" + warna.abuabu + "  Gmail App < 7.11.5.176568039 - Directory Traversal" + warna.tutup)
    print("\t[" + warna.hijau + "0" + warna.tutup + "]" + warna.abuabu + "  Back To Main Menu\n" + warna.tutup)
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def eksekusi_menu(pilih):
    masukan = pilih.lower()
    if masukan == '':
        menu['menu_utama']()
    else:
        try:
            menu[masukan]()
        except KeyError:
            print("\n Wrong command  ~~>>  " + warna.merah + str(masukan) + warna.tutup)
            menu['menu_utama']()

    return

def menu1():
    check_metasploit()
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module7
    module7.menu1()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu2():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module7
    module7.menu2()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return

def Kembali():
    back.menu['menu_utama']()

def kembali():
    menu['menu_utama']()

menu = {
    'menu_utama': menu_utama,
    '1': menu1,
    '2': menu2,
    '0': Kembali,
}
