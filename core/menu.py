#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, os, time
from banner import banner
from fungsi import check_php, check_nmap, warna

def menu_utama():
    banner()
    time.sleep(2)
    print("\t[" + warna.hijau + "1" + warna.tutup + "]" + warna.abuabu + "  Advanced Nmap Scanning" + warna.tutup)
    print("\t[" + warna.hijau + "2" + warna.tutup + "]" + warna.abuabu + "  Search Admin login Page" + warna.tutup)
    print("\t[" + warna.hijau + "3" + warna.tutup + "]" + warna.abuabu + "  Google Hacking Database (GHDB)" + warna.tutup)
    print("\t[" + warna.hijau + "4" + warna.tutup + "]" + warna.abuabu + "  Dorking For SQL Injection Vulnerability" + warna.tutup)
    print("\t[" + warna.hijau + "5" + warna.tutup + "]" + warna.abuabu + "  Exploiting Android" + warna.tutup)
    print("\t[" + warna.hijau + "6" + warna.tutup + "]" + warna.abuabu + "  Exploiting SCADA System" + warna.tutup)
    print("\t[" + warna.hijau + "7" + warna.tutup + "]" + warna.abuabu + "  Hardware Exploitation" + warna.tutup)
    print("\t[" + warna.hijau + "q" + warna.tutup + "]" + warna.abuabu + "  Exit\n" + warna.tutup)
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _>  " + warna.tutup)
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
    check_nmap()
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module1
    module1.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu2():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module4
    module4.cari_admin_panel()
    print(warna.hijau + "\n[*] " + warna.tutup + "Finish searching !!!")
    pilih = raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
    eksekusi_menu(pilih)
    return

def menu3():
    check_php()
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import sub_menu2
    sub_menu2.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu4():
    check_php()
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module6
    module6.dorking()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu5():
    import sub_menu
    sub_menu.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu6():
    import sub_menu3
    sub_menu3.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _> " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu7():
    import sub_menu4
    sub_menu4.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _> " + warna.tutup)
    eksekusi_menu(pilih)
    return

def Keluar():
    print(warna.kuning + "\n[!]  Thank You For Using tXtool. have a great day !\n" + warna.tutup)
    sys.exit()

menu = {
    'menu_utama': menu_utama,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '6': menu6,
    '7': menu7,
    'keluar': Keluar,
    'exit': Keluar,
    'quit': Keluar,
    'q': Keluar,
    'Q': Keluar,
}
