#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import menu as back
from fungsi import warna

def menu_utama():
    print("\n\t[" + warna.hijau + "1" + warna.tutup + "]" + warna.abuabu + "  D-Link DIR605L (Denial of Service)" + warna.tutup)
    print("\t[" + warna.hijau + "2" + warna.tutup + "]" + warna.abuabu + "  Telesquare SKT LTE Router SDT-CS3B1" + warna.tutup)
    print("\t[" + warna.hijau + "3" + warna.tutup + "]" + warna.abuabu + "  Contec SmartHome Unauthorized Users Added" + warna.tutup)
    print("\t[" + warna.hijau + "4" + warna.tutup + "]" + warna.abuabu + "  VideoFlow DVP 10 Root ssh Backdoor Access" + warna.tutup)
    print("\t[" + warna.hijau + "5" + warna.tutup + "]" + warna.abuabu + "  Master IP CAM 01 Multiple Vulnerabilities" + warna.tutup)
    print("\t[" + warna.hijau + "0" + warna.tutup + "]" + warna.abuabu + "  Back To Main Menu\n" + warna.tutup)
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  ~~>>  " + warna.tutup)
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
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module18
    module18.exploit1()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu2():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module18
    module18.exploit2()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)

def menu3():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module18
    module18.exploit3()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)

def menu4():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module18
    module18.exploit4()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)

def menu5():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module18
    module18.exploit5()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)

def Kembali():
    back.menu['menu_utama']()

menu = {
    'menu_utama': menu_utama,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '0': Kembali,
}
