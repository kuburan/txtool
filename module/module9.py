#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import subprocess, sys, os

sys.path.append("/data/data/com.termux/files/usr/share/txtool/core")
from fungsi import txtool_dir, warna, empty, finish_dorking, IP, info_page
import sub_menu2 as back


def menu_utama():
    print(warna.hijau + "\n\t[*]" + warna.tutup + warna.abuabu + "  Page 1 - Page 15 " + warna.tutup)
    print(warna.hijau + "\t[*]" + warna.tutup + warna.abuabu + "  Press 0 to back\n" + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + " These searches reveal servers with specific vulnerabilities. These are found in a different way than the searches found in the (Vulnerable Files) section. \n")
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
            filewrite.write("""
"dirLIST - PHP Directory Lister" "Banned files: php | php3 | php4 | php5 | htaccess | htpasswd | asp | aspx" "index of" ext:php -Hack -google
inurl:"/proc/self/cwd"
intext:"Smart PHP Poll. All Rights Reserved." -Google -exploit
inurl:"moadmin.php" intitle:"phpMoAdmin" -site:"https://fortiguard.com" -google -github
inurl:/elfinder/elfinder.html intitle:"elFinder 2.0"
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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
            filewrite.write("""
inurl:"/reports/rwservlet" intext:"Oracle"
inurl:.php? intext:CHARACTER_SETS,COLLATIONS, ?intitle:phpmyadmin -site:"https://searchcode.com" -site:"https://github.com"
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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
            filewrite.write("""
inurl:"/wp-content/w3tc/dbcache/"
filetype:php inurl:tiki-index.php  sirius  1.9.*
inurl:"/vb/install/install.php" intitle:"vBulletin"
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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
            filewrite.write("""
intitle:"[EasyPHP] - Administration" -ghdb -forums -Forum
inurl:php intitle:"Cpanel , FTP CraCkeR"
inurl:"/view.php?board1_sn="
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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
            filewrite.write("""
intitle:"ly0kha" intext:[ ly0kha Shell | VBF gr0up | ly0kha@yahoo.com | Sh3ll bypass safemode ]
intitle:"Black CyberSec Crew Shell" dragonddos
intitle:" - -=] fx0 [=- " intext:"-=] fx0 [=-" "hinnasto"
intitle:" - -=] fx0 [=- " intext:"-=] fx0 [=-" inurl:"/resimler/"
intitle:r57shell intext:[ phpinfo ]  [ php.ini ]  [ cpu ]  [ mem ]  [ users ]  [ tmp ]  [ delete ] -Google -blob  -codesearch -blog -tag -site:"www.keywordtown.com" -site:"https://pastebin.com" -site:"http://www.minikeyword.com"
intitle:":: b374k m1n1 1.01 ::"
filetype:php inanchor:c99 inurl:c99 intitle:c99shell -seeds -marijuana
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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
            filewrite.write("""
inurl:"/rpSys.html" intitle:"ZyXEL" -site:"https://www.zyxel.com"
intitle:"MvBlog powered"
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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
            filewrite.write("""
intitle:"Uploader - Uploader v6" -pixloads.com
intitle:" .::Welcome to the Web-Based Configuration::. "
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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
            filewrite.write("""
filetype:pl intitle:"Ultraboard Setup" intext:" Home | features | download | demos | support | links | credits | contact us "
intitle:"XOOPS Custom Installation" intext:"Welcome to the Install Wizard for XOOPS " -site:"https://www.softwarecube.org"
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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


def menu9():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""
inurl:"/pivot/" intitle:"Pivot" intext:"set up the administrator user" -blogging -Fossies
intitle:Guestbook intext:"Powered by BellaBook" intext:"Fill in your details in the form below"
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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


def menu10():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""
intitle:"Novell WebAccess" inurl:"servlet/webacc"
inurl:"/admin.php" intitle:"PHP-Nuke" intext:"There are no Administrators Accounts" -mysql_fetch_row
inurl:newsdesk.cgi? inurl:"t="
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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


def menu11():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""
natterchat inurl:home.asp -site:natterchat.co.uk
inurl:"index.php" "site=sglinks"
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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


def menu12():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""
inurl:"index.php?module=ew_filemanager"
filetype:cgi inurl:"/fileman.cgi"
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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


def menu13():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""
inurl:"/cgi-bin/web_store.cgi?page="
intitle:"ZyXEL Prestige Router" intext:"Welcome to the Prestige Web-Based Configurator"
filetype:php inurl:vAuthenticate -git
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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


def menu14():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""
intitle:"Samba Web Administration Tool" intext:"Help Workgroup"
intitle:"Gateway Configuration Menu" intext:"Gateway Global Settings "
inurl:"/install/install.php" intext:"Powered by PHPBoost"
inurl:"/install/install.php" intitle:"install Wizard"
inurl:"/intranet/" intitle:"Intranet login" -site:"https://github.com" -blog
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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


def menu15():
    try:
        IP()
        inurl = '/data/data/com.termux/files/usr/share/txtool/core'
        output = raw_input(warna.biru + "\n[+] " + warna.tutup + " Input the output file you want " + warna.kuning + " >> " + warna.tutup)
        if output == '':
            empty()
            back.menu['menu_utama']()

        else:
            filewrite = open(txtool_dir + "/dork.txt", "w")
            filewrite.write("""
"Select a database to view" intitle:"filemaker pro" intitle:"FileMaker Pro Web Companion" -KeyOptimize -cessna -forum -site:"http://archive.li" -site:"http://archive.is"
intitle:"Remote Desktop Web Connection" intext:"Send logon information for this connection"
intitle:osCommerce inurl:admin intext:"redistributable under the GNU" intext:"Online Catalog" -demo -site:oscommerce.com
intitle:"Gallery in Configuration mode" intext:"To configure gallery, Start the configuration wizard"
inurl:"/manyservers.htm" intitle:"Terminal Services Multiple Clients "
""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 --sall %s" %
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
    '9': menu9,
    '10': menu10,
    '11': menu11,
    '12': menu12,
    '13': menu13,
    '14': menu14,
    '15': menu15,
    '0': Kembali,
}
