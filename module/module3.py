#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import subprocess, sys, os
import module1 as back

sys.path.append("/data/data/com.termux/files/usr/share/txtool/core")
from fungsi import warna, empty, scan_finish, txtool_dir

def menu_utama():
    print("\n\t[" + warna.hijau + "1" + warna.tutup + "]" + warna.abuabu + "   iec-61850-8-1 (mms identify) " + warna.tutup)
    print("\t[" + warna.hijau + "2" + warna.tutup + "]" + warna.abuabu + "   atg info" + warna.tutup)
    print("\t[" + warna.hijau + "3" + warna.tutup + "]" + warna.abuabu + "   melsecq discover " + warna.tutup)
    print("\t[" + warna.hijau + "4" + warna.tutup + "]" + warna.abuabu + "   cspv4 info " + warna.tutup)
    print("\t[" + warna.hijau + "5" + warna.tutup + "]" + warna.abuabu + "   dnp3 info " + warna.tutup)
    print("\t[" + warna.hijau + "6" + warna.tutup + "]" + warna.abuabu + "   enip enumerate " + warna.tutup)
    print("\t[" + warna.hijau + "7" + warna.tutup + "]" + warna.abuabu + "   fox info " + warna.tutup)
    print("\t[" + warna.hijau + "8" + warna.tutup + "]" + warna.abuabu + "   modicon info " + warna.tutup)
    print("\t[" + warna.hijau + "9" + warna.tutup + "]" + warna.abuabu + "   omrontcp info" + warna.tutup)
    print("\t[" + warna.hijau + "10" + warna.tutup + "]" + warna.abuabu + "  pcworx info" + warna.tutup)
    print("\t[" + warna.hijau + "11" + warna.tutup + "]" + warna.abuabu + "  proconos info" + warna.tutup)
    print("\t[" + warna.hijau + "12" + warna.tutup + "]" + warna.abuabu + "  s7 enumerate" + warna.tutup)
    print("\t[" + warna.hijau + "13" + warna.tutup + "]" + warna.abuabu + "  iec identify " + warna.tutup)
    print("\t[" + warna.hijau + "14" + warna.tutup + "]" + warna.abuabu + "  modbus discover" + warna.tutup)
    print("\t[" + warna.hijau + "0" + warna.tutup + "]" + warna.abuabu + "   back\n" + warna.tutup)
    pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
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
    mms_file = '/data/data/com.termux/files/usr/share/nmap/scripts/Redpoint'
    if not os.path.isfile("%s/mms-identify.nse" % (mms_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " mms-identify.nse file not found !!\n")
        sys.exit()

    script = "--script Redpoint/mms-identify.nse"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
            subprocess.Popen("nmap -Pn -n -p102 %s %s " %
                          (pilih, script), shell=True).wait()
            scan_finish()
            menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p102 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu2():
    atg_file = '/data/data/com.termux/files/usr/share/nmap/scripts/Redpoint'
    if not os.path.isfile("%s/atg-info.nse" % (atg_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " atg-info.nse file not found !!\n")
        sys.exit()

    script = "--script Redpoint/atg-info.nse"
    script_args = "--script-args command=I20200"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p10001 %s %s " %
                          (pilih, script), shell=True).wait()

        print(warna.hijau + "\n[*] " + warna.tutup + "Scanning second info")
        subprocess.Popen("nmap -Pn -n -p10001 %s %s %s" %
                          (pilih, script, script_args), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p10001 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        os.system("cd %s && mv %s %s.bak1" % (txtool_dir, output_file, output_file))

        print(warna.hijau + "\n[*] " + warna.tutup + "Scanning second info")
        subprocess.Popen("nmap -Pn -n -p10001 %s %s %s -oN /data/data/com.termux/files/home/.txtool/%s" %
                          (pilih, script, script_args, output_file), shell=True).wait()
        os.system("cd %s && mv %s %s.bak2" % (txtool_dir, output_file, output_file))
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        os.system("cd %s && cat %s.bak1 %s.bak2 >> %s" % (txtool_dir, output_file, output_file, output_file))
        os.system("cd %s && rm *.bak1 *.bak2" % (txtool_dir))
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu3():
    melsecq_file = '/data/data/com.termux/files/usr/share/nmap/scripts/Redpoint'
    if not os.path.isfile("%s/melsecq-discover.nse" % (melsecq_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " melsecq-discover.nse file not found !!")
        sys.exit()

    script = "--script Redpoint/melsecq-discover.nse"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.abuabu + "\n Input the output file you want :  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -sT -p5007 %s %s " %
                          (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -sT -p5007 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                            (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return


def menu4():
    cspv4_file = '/data/data/com.termux/files/usr/share/nmap/scripts/Redpoint'
    if not os.path.isfile("%s/cspv4-info.nse" % (cspv4_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " cspv4-info.nse file not found !!")
        sys.exit()

    script = "--script Redpoint/cspv4-info.nse"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p2222 %s %s " %
                          (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p2222 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu5():
    dnp3_file = '/data/data/com.termux/files/usr/share/nmap/scripts/Redpoint'
    if not os.path.isfile("%s/dnp3-info.nse" % (dnp3_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " dnp3-info.nse file not found !!")
        sys.exit()

    script = "--script Redpoint/dnp3-info.nse"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p20000 %s %s " %
                          (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p20000 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu6():
    enip_file = '/data/data/com.termux/files/usr/share/nmap/scripts'
    if not os.path.isfile("%s/enip-info.nse" % (enip_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " enip-info.nse file not found !!")
        sys.exit()

    script = "--script enip-info"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p44818 %s %s " %
                          (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p44818 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu7():
    fox_file = '/data/data/com.termux/files/usr/share/nmap/scripts'
    if not os.path.isfile("%s/fox-info.nse" % (fox_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " fox-info.nse file not found !!")
        sys.exit()

    script = "--script fox-info"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p1911 %s %s " %
                          (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p1911 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu8():
    modicon_file = '/data/data/com.termux/files/usr/share/nmap/scripts/Redpoint'
    if not os.path.isfile("%s/modicon-info.nse" % (modicon_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " modicon-info.nse file not found !!")
        sys.exit()

    script = "--script Redpoint/modicon-info.nse"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p502 %s %s " %
                          (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p502 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return


def menu9():
    omrontcp_file = '/data/data/com.termux/files/usr/share/nmap/scripts'
    if not os.path.isfile("%s/omron-info.nse" % (omrontcp_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " omron-info.nse file not found !!")
        sys.exit()

    script = "--script omron-info"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p9600 %s %s " %
                          (pilih, script), shell=True).wait()

        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p9600 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return


def menu10():
    pcworx_file = '/data/data/com.termux/files/usr/share/nmap/scripts'
    if not os.path.isfile("%s/pcworx-info.nse" % (pcworx_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " pcworx-info.nse file not found !!")
        sys.exit()

    script = "--script pcworx-info"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p1962 %s %s " %
                          (pilih, script), shell=True).wait()

        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p1962 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return


def menu11():
    proconos_file = '/data/data/com.termux/files/usr/share/nmap/scripts/Redpoint'
    if not os.path.isfile("%s/proconos-info.nse" % (proconos_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " proconos-info.nse file not found !!")
        sys.exit()

    script = "--script Redpoint/proconos-info.nse"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p20547 %s %s " %
                          (pilih, script), shell=True).wait()

        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p20547 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu12():
    s7_file = '/data/data/com.termux/files/usr/share/nmap/scripts'
    if not os.path.isfile("%s/s7-info.nse" % (s7_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " s7-info.nse file not found !!")
        sys.exit()

    script = "--script s7-info"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p102 %s %s " %
                          (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p102 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu13():
    iec_file = '/data/data/com.termux/files/usr/share/nmap/scripts'
    if not os.path.isfile("%s/iec-identify.nse" % (iec_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " iec-identify.nse file not found !!")
        sys.exit()

    script = "--script iec-identify"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + " >> " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + " >> " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p2404 %s %s " %
                          (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p2404 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " >> " + warna.tutup)
        eksekusi_menu(pilih)

    return


def menu14():
    modbus_file = '/data/data/com.termux/files/usr/share/nmap/scripts'
    if not os.path.isfile("%s/modbus-discover.nse" % (modbus_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " modbus-discover.nse file not found !!")
        sys.exit()

    script = "--script modbus-discover"
    pilih = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Target IP or Host" + warna.kuning + " >> " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + " >> " + warna.tutup)
    if output_file == '':
        subprocess.Popen("nmap -Pn -n -p502 %s %s  " %
                          (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -Pn -n -p502 %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "\n[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + " >> " + warna.tutup)
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
    '12': menu12,
    '13': menu13,
    '14': menu14,
    '0': Kembali,
}
