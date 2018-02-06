#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import menu as back
from fungsi import info, warna, empty, scan_finish

def menu_utama():
    print("\n\t[" + warna.hijau + "1" + warna.tutup + "]" + warna.abuabu + "   Sensitive Directories " + warna.tutup)
    print("\t[" + warna.hijau + "2" + warna.tutup + "]" + warna.abuabu + "   Vulnerable Files " + warna.tutup)
    print("\t[" + warna.hijau + "3" + warna.tutup + "]" + warna.abuabu + "   Vulnerable Servers " + warna.tutup)
    print("\t[" + warna.hijau + "4" + warna.tutup + "]" + warna.abuabu + "   Error Messages " + warna.tutup)
    print("\t[" + warna.hijau + "5" + warna.tutup + "]" + warna.abuabu + "   Network or Vulnerability Data " + warna.tutup)
    print("\t[" + warna.hijau + "6" + warna.tutup + "]" + warna.abuabu + "   Various Online Devices " + warna.tutup)
    print("\t[" + warna.hijau + "7" + warna.tutup + "]" + warna.abuabu + "   Web Server Detection " + warna.tutup)
    print("\t[" + warna.hijau + "8" + warna.tutup + "]" + warna.abuabu + "   Files Containing Passwords " + warna.tutup)
    print("\t[" + warna.hijau + "9" + warna.tutup + "]" + warna.abuabu + "   Files Containing Usernames " + warna.tutup)
    print("\t[" + warna.hijau + "10" + warna.tutup + "]" + warna.abuabu + "  Files Containing Juicy Info " + warna.tutup)
    print("\t[" + warna.hijau + "11" + warna.tutup + "]" + warna.abuabu + "  Pages Containing Login Portals " + warna.tutup)
    print("\t[" + warna.hijau + "0" + warna.tutup + "]" + warna.abuabu + "   Back\n" + warna.tutup)
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
    import module5
    module5.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  ~~>>  " + warna.tutup)
    eksekusi_menu(pilih)
    return


def menu2():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module8
    module8.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return


def menu3():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module9
    module9.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return


def menu4():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module10
    module10.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return


def menu5():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module11
    module11.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return


def menu6():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module12
    module12.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return


def menu7():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module13
    module13.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return


def menu8():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module14
    module14.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return


def menu9():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module15
    module15.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return


def menu10():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module16
    module16.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return


def menu11():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module17
    module17.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return


def Kembali():
    back.menu['menu_utama']()


menu = {
    'menu_utama': menu_utama,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '6': menu6,
    '7': menu7,
    '8': menu8,
    '9': menu9,
    '10': menu10,
    '11': menu11,
    '0': Kembali,
}
