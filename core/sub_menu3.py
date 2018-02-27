#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, os
import menu as KEMBALI
from fungsi import warna, check_metasploit

def menu_utama():
    print("\n\t[" + warna.hijau + "1" + warna.tutup + "]" + warna.abuabu + "  Siemens S7-1200 Remote Code Execution" + warna.tutup)
    print("\t[" + warna.hijau + "2" + warna.tutup + "]" + warna.abuabu + "  Phoenix Control PLC ILC-150" + warna.tutup)
    print("\t[" + warna.hijau + "3" + warna.tutup + "]" + warna.abuabu + "  Modbus Client Utility" + warna.tutup)
    print("\t[" + warna.hijau + "4" + warna.tutup + "]" + warna.abuabu + "  Schneider Modicon Remote Command Execution" + warna.tutup)
    print("\t[" + warna.hijau + "5" + warna.tutup + "]" + warna.abuabu + "  Schneider Modicon Quantum Password Recovery" + warna.tutup)
    print("\t[" + warna.hijau + "6" + warna.tutup + "]" + warna.abuabu + "  Moxa Device Credential Retrieval" + warna.tutup)
    print("\t[" + warna.hijau + "7" + warna.tutup + "]" + warna.abuabu + "  Allen-Bradley/Rockwell Automation EtherNet/IP CIP RCE" + warna.tutup)
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
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module7
    module7.menu10()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu2():
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module7
    module7.menu9()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu3():
    check_metasploit()
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module7
    module7.menu11()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu4():
    check_metasploit()
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module7
    module7.menu8()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu5():
    check_metasploit()
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module7
    module7.menu7()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>>  " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu6():
    check_metasploit()
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module7
    module7.menu6()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return

def menu7():
    check_metasploit()
    sys.path.append("/data/data/com.termux/files/usr/share/txtool/module")
    import module7
    module7.menu5()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " ~~>> " + warna.tutup)
    eksekusi_menu(pilih)
    return

def back():
    KEMBALI.menu['menu_utama']()

menu = {
    'menu_utama': menu_utama,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '6': menu6,
    '7': menu7,
    '0': back,
}
