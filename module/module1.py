#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import subprocess, sys, os
import module2
import module3

sys.path.append("/data/data/com.termux/files/usr/share/txtool/core")
from fungsi import empty, scan_finish, check_vulscan, check_redpoint
from fungsi import IP, check_proxychains, info, warna, check_vulners, check_ndiff
import menu as back

def menu_utama():
    print("\n\t[" + warna.hijau + "1" + warna.tutup + "]" + warna.abuabu + "  Vulscan" + warna.tutup)
    print("\t[" + warna.hijau + "2" + warna.tutup + "]" + warna.abuabu + "  Scan With Bogus TCP + Decoy" + warna.tutup)
    print("\t[" + warna.hijau + "3" + warna.tutup + "]" + warna.abuabu + "  Scan Through Proxychains" + warna.tutup)
    print("\t[" + warna.hijau + "4" + warna.tutup + "]" + warna.abuabu + "  SCADA, ICS, PLC Scanning" + warna.tutup)
    print("\t[" + warna.hijau + "5" + warna.tutup + "]" + warna.abuabu + "  Checking Eternalblue Doublepulsar Vulnerability" + warna.tutup)
    print("\t[" + warna.hijau + "6" + warna.tutup + "]" + warna.abuabu + "  Vulners" + warna.tutup)
    print("\t[" + warna.hijau + "7" + warna.tutup + "]" + warna.abuabu + "  Compare Nmap output files with Ndiff" + warna.tutup)
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
    IP()
    check_vulscan()
    module2.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _>  " + warna.tutup)
    eksekusi_menu(pilih)

    return

def menu2():
    IP()
    decoy = "-D 100.10.2.190,180.250.11.21,22.90.67.125,10.2.111.191,120.122.225.50,88.36.66.190,33.28.190.111,120.180.10.2,90.90.37.189,225.80.96.10 --badsum"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    info()
    port = raw_input(warna.biru + "[+] " + warna.tutup + "Enter the port number" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to use nse script, so just let it blank.")
    script = raw_input(warna.biru + "[+] " + warna.tutup + "Enter nse script" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if port == '' and script == '' and output_file == '':
        subprocess.Popen("nmap -sV %s %s " %
                        (pilih, decoy), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if port == '' and script == '':
        subprocess.Popen("nmap -sV %s %s -oN /data/data/com.termux/files/home/.txtool/%s" %
                        (pilih, decoy, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
             (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()

    if port == '' and output_file == '':
        subprocess.Popen("nmap -sV %s --script %s %s " %
                        (pilih, script, decoy), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if script == '' and output_file == '':
        subprocess.Popen("nmap -sV %s -p%s %s" %
                        (pilih, port, decoy), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif port == '':
        subprocess.Popen("nmap -sV %s --script %s %s -oN /data/data/com.termux/files/home/.txtool/%s" %
                       (pilih, script, decoy, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
                (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()

    elif script == '':
        subprocess.Popen("nmap -sV %s -p%s %s -oN /data/data/com.termux/files/home/.txtool/%s" %
                       (pilih, port, decoy, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
                (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()

    elif output_file == '':
        subprocess.Popen("nmap -sV %s -p%s --script %s %s" %
                          (pilih, port, script, decoy), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -sV -p%s %s --script %s %s -oN /data/data/com.termux/files/home/.txtool/%s" %
                         (port, pilih, script, decoy, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
                   (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()
        a = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _>  " + warna.tutup)
        eksekusi_menu(a)

    return

def menu3():
    IP()
    check_proxychains()
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    info()
    port = raw_input(warna.biru + "[+] " + warna.tutup + "Enter the port number" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to use nse script, so just let it blank.")
    script = raw_input(warna.biru + "[+] " + warna.tutup + "Enter nse script" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if port == '' and script == '' and output_file == '':
        subprocess.Popen("proxychains4 nmap -sV %s " %
                          (pilih), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if port == '' and script == '':
        subprocess.Popen("proxychains4 nmap -sV %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                            (pilih, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
                (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()

    if port == '' and output_file == '':
        subprocess.Popen("proxychains4 nmap -sV %s --script %s" %
                          (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if script == '' and output_file == '':
        subprocess.Popen("proxychains4 nmap -sV -p%s %s" %
                       (port, pilih), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif port == '':
        subprocess.Popen("proxychains4 nmap -sV %s --script %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                            (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
                (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()

    elif script == '':
        subprocess.Popen("proxychains4 nmap -sV %s -p%s -oN /data/data/com.termux/files/home/.txtool/%s " %
                            (pilih, port, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
                (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()

    elif output_file == '':
        subprocess.Popen("proxychains4 nmap -sV -p%s %s --script %s" %
                       (port, pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("proxychains4 nmap -sV -p%s %s --script %s -oN /data/data/com.termux/files/home/.txtool/%s" %
                            (port, pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
                (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()
        a = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _>  " + warna.tutup)
        eksekusi_menu(a)

    return

def menu4():
    IP()
    check_redpoint()
    module3.menu_utama()
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _>  " + warna.tutup)
    eksekusi_menu(pilih)

    return

def menu5():
    IP()
    script = "--script smb-vuln-ms17-010,smb-double-pulsar-backdoor,stuxnet-detect"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p443,445 %s %s " %
                          (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p443,445 %s %s -oN /data/data/com.termux/files/home/.txtool/%s" %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
                (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " _>  " + warna.tutup)
        eksekusi_menu(pilih)

    return


def menu6():
    IP()
    check_vulners()
    script = "--script vulners"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    info()
    port = raw_input(warna.biru + "[+] " + warna.tutup + "Enter the port number" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if port == '' and output_file == '':
        subprocess.Popen("nmap -sV %s %s " %
                          (script, pilih), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif output_file == '':
        subprocess.Popen("nmap -sV -p%s %s  %s" %
                       (port, script, pilih), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif port == '':
        subprocess.Popen("nmap -sV %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                            (script, pilih, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
                (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -sV -p%s %s %s -oN /data/data/com.termux/files/home/.txtool/%s" %
                         (port, script, pilih, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
                   (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()

def menu7():
    check_ndiff()
    print(warna.hijau + "\n[*]" + warna.tutup + " Compare two Nmap XML files and display a list of their differences. Differences include host state changes, port state changes, and changes to service and OS detection.")
    file_1 = raw_input(warna.biru + "\n[+] " + warna.tutup + "first output file" + warna.kuning + "  >>  " + warna.tutup)
    if file_1 == '':
        empty()
        menu['menu_utama']()

    if not ".xml" in file_1:
        print(warna.merah + "\n[x] Error : " + warna.tutup + "the output file should be in .xml format")
        menu['menu_utama']()

    file_2 = raw_input(warna.biru + "\n[+] " + warna.tutup + "second output file to compare" + warna.kuning + "  >>  " + warna.tutup)
    if file_2 == '':
        empty()
        menu['menu_utama']()

    if not ".xml" in file_2:
        print(warna.merah + "\n[x] Error : " + warna.tutup + "the output file should be in .xml format")
        menu['menu_utama']()

    print(warna.hijau + '\n[*] ' + warna.tutup + 'if you want to read in xml format, choose "yes". else return text format')
    q = raw_input(warna.biru + "[+]" + warna.tutup + " Do you want to read in xml format ?" + warna.kuning + "  >>  " + warna.tutup)
    if q == "yes" or q == "YES" or q == "y" or q == "Y" or q == "ya":
        subprocess.Popen("ndiff --xml %s %s " %
                         (file_1, file_2), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("ndiff %s %s " %
                         (file_1, file_2), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

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
    '0': Kembali,
}
