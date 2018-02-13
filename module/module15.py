#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import subprocess, sys, os

sys.path.append("/data/data/com.termux/files/usr/share/txtool/core")
from fungsi import txtool_dir, warna, empty, finish_dorking, IP, info_page
import sub_menu2 as back


def menu_utama():
    print(warna.hijau + "\n\t[*]" + warna.tutup + warna.abuabu + "  Page 1 - Page 8 " + warna.tutup)
    print(warna.hijau + "\t[*]" + warna.tutup + warna.abuabu + "  Press 0 to back\n" + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + " These files contain usernames, but no passwords... Still, Google finding usernames on a web site. \n")
    info_page()
    pilih = raw_input(warna.biru + "[+] " + warna.tutup + " Which page do you want to crawl ?" + warna.kuning + "  >>  " + warna.tutup)
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
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + "  >>  " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""\ninurl:/_layouts/mobile/view.aspx?List=\ninurl:/profile.php?lookup=1 -git -stackoverflow\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6,24 --sall %s" %
                (inurl, txtool_dir, output), shell=True).wait()
            finish_dorking()
            print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s " %
                (output))
            raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
            back.menu['menu_utama']()

    except(KeyboardInterrupt):
        print(warna.merah + "\n[x] " + warna.tutup + "{0}CTRL+C{1} Detected, force program to stop !\n".format(warna.merah, warna.tutup))
        os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
        print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s \n" %
                (output))
        sys.exit()


def menu2():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""\n"authentication failure; logname=" ext:log -git\ninurl:"/root/etc/passwd" intext:"home/*:" -git -ibutterfly -questions -CodeWeblog.com -site:"https://nomads.in" -intext:"Forbidden"  -intitle:"Free convertor"\nsite:extremetracking.com inurl:"login=" -intitle:"/ Lost my Code / My Account"\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6,24 --sall %s" %
                (inurl, txtool_dir, output), shell=True).wait()
            finish_dorking()
            print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s " %
                (output))
            raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
            back.menu['menu_utama']()

    except(KeyboardInterrupt):
        print(warna.merah + "\n[x] " + warna.tutup + "{0}CTRL+C{1} Detected, force program to stop !\n".format(warna.merah, warna.tutup))
        os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
        print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s \n" %
                (output))
        sys.exit()


def menu3():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""\nfiletype:conf inurl:proftpd.conf -Fossies -Examples -Blog -sample -git -Searchcode -gitlab -Projects -Debian\nfiletype:reg reg HKEY_CURRENT_USER username\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6,24 --sall %s" %
                (inurl, txtool_dir, output), shell=True).wait()
            finish_dorking()
            print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s " %
                (output))
            raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
            back.menu['menu_utama']()

    except(KeyboardInterrupt):
        print(warna.merah + "\n[x] " + warna.tutup + "{0}CTRL+C{1} Detected, force program to stop !\n".format(warna.merah, warna.tutup))
        os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
        print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s \n" %
                (output))
        sys.exit()


def menu4():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""\nfiletype:log username putty -git\nfiletype:reg "reg" intext:"internet account manager"\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6,24 --sall %s" %
                (inurl, txtool_dir, output), shell=True).wait()
            finish_dorking()
            print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s " %
                (output))
            raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
            back.menu['menu_utama']()

    except(KeyboardInterrupt):
        print(warna.merah + "\n[x] " + warna.tutup + "{0}CTRL+C{1} Detected, force program to stop !\n".format(warna.merah, warna.tutup))
        os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
        print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s \n" %
                (output))
        sys.exit()


def menu5():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""\nGoogle for: +intext:"webalizer" +intext:"Total Usernames" +intext:"Usage Statistics for"\ninurl:php inurl:hlstats intext:"Server Username"\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6,24 --sall %s" %
                (inurl, txtool_dir, output), shell=True).wait()
            finish_dorking()
            print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s " %
                (output))
            raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
            back.menu['menu_utama']()

    except(KeyboardInterrupt):
        print(warna.merah + "\n[x] " + warna.tutup + "{0}CTRL+C{1} Detected, force program to stop !\n".format(warna.merah, warna.tutup))
        os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
        print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s \n" %
                (output))
        sys.exit()


def menu6():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""\n"index of" / lck -Google -Github -gitlab -git -forums -ghdb -books\ninurl:admin filetype:asp inurl:userlist\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6,24 --sall %s" %
                (inurl, txtool_dir, output), shell=True).wait()
            finish_dorking()
            print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s " %
                (output))
            raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
            back.menu['menu_utama']()

    except(KeyboardInterrupt):
        print(warna.merah + "\n[x] " + warna.tutup + "{0}CTRL+C{1} Detected, force program to stop !\n".format(warna.merah, warna.tutup))
        os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
        print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s \n" %
                (output))
        sys.exit()


def menu7():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""\nintitle:"Index of" .sh_history -git -Github -gitlab -Google -stackoverflow -site:"https://myechooff.wordpress.com"\nintitle:index.of .bash_history -git -Google -github -questions -stackoverflow\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6,24 --sall %s" %
                (inurl, txtool_dir, output), shell=True).wait()
            finish_dorking()
            print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s " %
                (output))
            raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
            back.menu['menu_utama']()

    except(KeyboardInterrupt):
        print(warna.merah + "\n[x] " + warna.tutup + "{0}CTRL+C{1} Detected, force program to stop !\n".format(warna.merah, warna.tutup))
        os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
        print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s \n" %
                (output))
        sys.exit()


def menu8():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""\nintitle:"index of /" intext:"perform.ini" -Google -Github -git -books\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6,24 --sall %s" %
                (inurl, txtool_dir, output), shell=True).wait()
            finish_dorking()
            print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s " %
                (output))
            raw_input("\n press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
            back.menu['menu_utama']()

    except(KeyboardInterrupt):
        print(warna.merah + "\n[x] " + warna.tutup + "{0}CTRL+C{1} Detected, force program to stop !\n".format(warna.merah, warna.tutup))
        os.system("cd %s && rm -fr dork.txt" % (txtool_dir))
        print(warna.hijau + "[*] " + warna.tutup + " Crawl result has been saved to /data/data/com.termux/files/home/.txtool/output/%s \n" %
                (output))
        sys.exit()


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
