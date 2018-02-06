#!/data/data/com.termux/files/usr/bin/python2

import subprocess, sys, os
import module1 as back

sys.path.append("/data/data/com.termux/files/usr/share/txtool/core")
from fungsi import info, warna, empty, scan_finish

def menu_utama():
    print("\n\t[" + warna.hijau + "1" + warna.tutup + "]" + warna.abuabu + "  Cve" + warna.tutup)
    print("\t[" + warna.hijau + "2" + warna.tutup + "]" + warna.abuabu + "  Exploitdb" + warna.tutup)
    print("\t[" + warna.hijau + "3" + warna.tutup + "]" + warna.abuabu + "  Openvas" + warna.tutup)
    print("\t[" + warna.hijau + "4" + warna.tutup + "]" + warna.abuabu + "  Xforce" + warna.tutup)
    print("\t[" + warna.hijau + "5" + warna.tutup + "]" + warna.abuabu + "  Osvdb" + warna.tutup)
    print("\t[" + warna.hijau + "6" + warna.tutup + "]" + warna.abuabu + "  Scipvuldb" + warna.tutup)
    print("\t[" + warna.hijau + "7" + warna.tutup + "]" + warna.abuabu + "  Security Focus" + warna.tutup)
    print("\t[" + warna.hijau + "8" + warna.tutup + "]" + warna.abuabu + "  Security Tracker" + warna.tutup)
    print("\t[" + warna.hijau + "0" + warna.tutup + "]" + warna.abuabu + "  Back\n" + warna.tutup)
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
    cve_file = "/data/data/com.termux/files/usr/share/nmap/scripts/vulscan"
    if not os.path.isfile("%s/cve.csv" % (cve_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " cve database file not found !!")
        sys.exit()

    script = "--script=vulscan/vulscan.nse  --script-args vulscandb=cve.csv"
    pilih = raw_input(warna.biru + "\n[+] " + warna.tutup + "Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == "":
        empty()
        menu['menu_utama']()

    info()
    port = raw_input(warna.biru + "[+] " + warna.tutup + "Enter the port number" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == "" and port == "":
        subprocess.Popen("nmap -sV %s %s " %
                                 (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if output_file == "":
        subprocess.Popen("nmap -sV -p%s %s %s" %
                         (port, pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif port == "":
        subprocess.Popen("nmap -sV %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -sV -p%s %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (port, pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu2():
    exploitdb_file = '/data/data/com.termux/files/usr/share/nmap/scripts/vulscan'
    if not os.path.isfile("%s/exploitdb.csv" % (exploitdb_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " exploitdb database file not found !!")
        sys.exit()

    script = "--script=vulscan/vulscan.nse  --script-args vulscandb=exploitdb.csv"
    pilih = raw_input(warna.biru + "\n[+] " + warna.tutup + "Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    info()
    port = raw_input(warna.biru + "[+] " + warna.tutup + "Enter the port number" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '' and port == '':
        subprocess.Popen("nmap -sV %s %s " %
                         (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if output_file == '':
        subprocess.Popen("nmap -sV -p%s %s %s" %
                         (port, pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif port == '':
        subprocess.Popen("nmap -sV %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
                    (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -sV -p%s %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (port, pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu3():
    openvas_file = '/data/data/com.termux/files/usr/share/nmap/scripts/vulscan'
    if not os.path.isfile("%s/openvas.csv" % (openvas_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " openvas database file not found !!")
        sys.exit()

    script = "--script=vulscan/vulscan.nse  --script-args vulscandb=openvas.csv"
    pilih = raw_input(warna.biru + "\n[+] " + warna.tutup + "Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    info()
    port = raw_input(warna.biru + "[+] " + warna.tutup + "Enter the port number" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '' and port == '':
        subprocess.Popen("nmap -sV %s %s " %
                         (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if output_file == '':
        subprocess.Popen("nmap -sV -p%s %s %s" %
                         (port, pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif port == '':
        subprocess.Popen("nmap -sV %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                            (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -sV -p%s %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                            (port, pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu4():
    xforce_file = '/data/data/com.termux/files/usr/share/nmap/scripts/vulscan'
    if not os.path.isfile("%s/xforce.csv" % (xforce_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " xforce database file not found !!")
        sys.exit()

    script = "--script=vulscan/vulscan.nse --script-args vulscandb=xforce.csv"
    pilih = raw_input(warna.biru + "\n[+] " + warna.tutup + "Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    info()
    port = raw_input(warna.biru + "[+] " + warna.tutup + "Enter the port number" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '' and port == '':
        subprocess.Popen("nmap -sV %s %s " %
                         (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if output_file == '':
        subprocess.Popen("nmap -sV -p%s %s %s" %
                         (port, pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif port == '':
        subprocess.Popen("nmap -sV %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -sV -p%s %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (port, pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu5():
    osvdb_file = '/data/data/com.termux/files/usr/share/nmap/scripts/vulscan'
    if not os.path.isfile("%s/osvdb.csv" % (osvdb_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " osvdb database file not found !!")
        sys.exit()

    script = "--script=vulscan/vulscan.nse --script-args vulscandb=osvdb.csv"
    pilih = raw_input(warna.biru + "\n[+] " + warna.tutup + "Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    info()
    port = raw_input(warna.biru + "[+] " + warna.tutup + "Enter the port number" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '' and port == '':
        subprocess.Popen("nmap -sV %s %s " %
                         (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if output_file == '':
        subprocess.Popen("nmap -sV -p%s %s %s" %
                         (port, pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif port == '':
        subprocess.Popen("nmap -sV %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -sV -p%s %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (port, pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu6():
    scipvuldb_file = '/data/data/com.termux/files/usr/share/nmap/scripts/vulscan'
    if not os.path.isfile("%s/scipvuldb.csv" % (scipvuldb_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " scipvuldb database file not found !!")
        sys.exit()

    script = "--script=vulscan/vulscan.nse --script-args vulscandb=scipvuldb.csv"
    pilih = raw_input(warna.biru + "\n[+] " + warna.tutup + "Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    info()
    port = raw_input(warna.biru + "[+] " + warna.tutup + "Enter the port number" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '' and port == '':
        subprocess.Popen("nmap -sV %s %s " %
                         (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if output_file == '':
        subprocess.Popen("nmap -sV -p%s %s %s" %
                         (port, pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif port == '':
        subprocess.Popen("nmap -sV %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -sV -p%s %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (port, pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu7():
    securityfocus_file = '/data/data/com.termux/files/usr/share/nmap/scripts/vulscan'
    if not os.path.isfile("%s/securityfocus.csv" % (securityfocus_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " security focus database file not found !!")
        sys.exit()

    script = "--script=vulscan/vulscan.nse --script-args vulscandb=securityfocus.csv"
    pilih = raw_input(warna.biru + "\n[+] " + warna.tutup + "Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    info()
    port = raw_input(warna.biru + "[+] " + warna.tutup + "Enter the port number" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '' and port == '':
        subprocess.Popen("nmap -sV %s %s " %
                         (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if output_file == '':
        subprocess.Popen("nmap -sV -p%s %s %s" %
                         (port, pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif port == '':
        subprocess.Popen("nmap -sV %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -sV -p%s %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (port, pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
        eksekusi_menu(pilih)

    return

def menu8():
    securitytracker_file = '/data/data/com.termux/files/usr/share/nmap/scripts/vulscan'
    if not os.path.isfile("%s/securitytracker.csv" % (securitytracker_file)):
        print(warna.merah + "\n[-] Fatal error" + warna.tutup + " security tracker database file not found !!")
        sys.exit()

    script = "--script=vulscan/vulscan.nse --script-args vulscandb=securitytracker.csv"
    pilih = raw_input(warna.biru + "\n[+] " + warna.tutup + "Enter Target IP or Host" + warna.kuning + "  >>  " + warna.tutup)
    if pilih == '':
        empty()
        menu['menu_utama']()

    info()
    port = raw_input(warna.biru + "[+] " + warna.tutup + "Enter the port number" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + "if you don't want to save the output file, so just let it blank.")
    output_file = raw_input(warna.biru + "[+] " + warna.tutup + "Input the output file you want" + warna.kuning + "  >>  " + warna.tutup)
    if output_file == '' and port == '':
        subprocess.Popen("nmap -sV %s %s " %
                         (pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    if output_file == '':
        subprocess.Popen("nmap -sV -p%s %s %s" %
                         (port, pilih, script), shell=True).wait()
        scan_finish()
        menu['menu_utama']()

    elif port == '':
        subprocess.Popen("nmap -sV %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s " %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()

    else:
        subprocess.Popen("nmap -sV -p%s %s %s -oN /data/data/com.termux/files/home/.txtool/%s " %
                          (port, pilih, script, output_file), shell=True).wait()
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        print(warna.hijau + "[*]" + warna.tutup + " output file has been saved to : $HOME/.txtool/%s" %
               (output_file))
        raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        menu['menu_utama']()
        pilih = raw_input(warna.hijau + " tXtool " + warna.tutup + warna.kuning + "  >>  " + warna.tutup)
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
    '0': Kembali,
}
