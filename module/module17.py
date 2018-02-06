#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import subprocess, sys, os

sys.path.append("/data/data/com.termux/files/usr/share/txtool/core")
from fungsi import txtool_dir, warna, empty, finish_dorking, IP, info_page
import sub_menu2 as back

def menu_utama():
    print(warna.hijau + "\n\t[*]" + warna.tutup + warna.abuabu + "  Page 1 - Page 13 " + warna.tutup)
    print(warna.hijau + "\t[*]" + warna.tutup + warna.abuabu + "  Press 0 to back\n" + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + " These are login pages for various services. Consider them the front door of a websites more sensitive functions. \n")
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
            filewrite.write("""\ninurl:/login/index.php intitle:CentOS -site:www.microfin360.com\ninurl:"/jde/E1Menu.maf" -site:.info -site:www.533028.com  -site:www.yungaixie.com -site:www.xmarks.com -site:www.codeweblog.com -site:https://www.jdelist.com\ninurl:"/libs/granite/core/content/login.html"\ninurl:"https://mylogin."\ninurl:"/moodle/login/index.php" -site:https://www.apt-browse.org -site:phpcrossref.com\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\ninurl:"xamppsecurity.php" -git -wiki -forum -gitlab -community -foro -site:www.keywordsfind.com\nintitle:"Django site admin" inurl:admin -site:archive.is -site:https://www.easycounter.com -mail -git -site:stackoverflow.com -site:sur.ly -site:website.informer.com\ninurl:":8006" and intext:"Proxmox VE Login" -site:www.consulting-sale.com -site:www.architecture-coslovo.info  -site:www.medicine-tec.biz -site:www.consulting-sale.net  -site:www.medicine-tec.com -site:www.architecture-coslovo.net\ninurl:login/?next=/admin/ -git -blog -https -stackoverflow.com -site:http://cheng.logdown.com\nintitle:"Welcome to QNAP Turbo NAS" -git -gitlab -forum -wiki\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\ninurl:front/central.php -git -gitlab -site:http://phpcrossref.com -site:https://www.apt-browse.org\ninurl:"Admin/Index.aspx?A=LogOut"\ninurl:/remote/login?lang=en\nintitle:"Plesk Onyx" intext:"Interface language"\ninurl:"Login;jsessionid=" -git -wiki -forum\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\nintitle:"Dell SonicWALL - Authentication"\ninurl:"http://webmail."\ninurl:"/siteadmin/index.php"\ninurl:/helpdesk/staff/index.php? intext:Powered by Kayako\n"Log in" "Magento is a trademark of Magento Inc."\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\ninurl:"member.php?action=login"\ninurl:"/fmi/webd"\ninurl:/j_security_check;jsessionid= -site:www.codegist.net  -git -gitlab\ninurl:"/SecureAuth1"\ninurl:"/admin.php?cont="\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\n"Joomla! Administration Login" inurl:"/index.php" -git -forum -community -gitlab -wiki -site:https://www.granitewebdesign.com -site:https://my.hostking.co.za -site:https://www.aryanict.com\ninurl:".Admin;-aspx }" "~Login"\ninurl:".reset;-.pwd }" "~ User" -site:https://premium.wpmudev.org -git -gitlab\ninurl:"/ctl/SendPassword?returnurl=" "08"\nintitle:"Login - OpenStack Dashboard" inurl:"dashboard" -site:https://www.linuxtechi.com  -forum -community -ask\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\ninurl:forgot.do;jsessionid=\nintitle:Login "Login to pfSense" "Password" "LLC" -git -site:https://www.automaticleasing.com\nintitle:"Vigor Login Page" -site:www.accessify.com\nintitle:"Integrated Dell Remote Access Controller 6 - Enterprise"\ninurl:"https://vdi." -git -community -forum\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\ninurl:/human.aspx?r=\ninurl:/human?=arg12\ninurl:"/sgdadmin/" Secure Global Desktop\nintitle:Sign In inurl:/adfs/ls/?wa=wsignin1.0\ninurl:"/login/login.html" intitle:"Greenbone Security Assistant" -site:https://fossies.org\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\nZixmail inurl:/s/login? inurl:web1.\ninurl:/remote/login/ intext:"please login"|intext:"FortiToken clock drift detected" -site:bidn.com -site:https://www.raccoonbot.com -site:computerchimp.com\ninurl:/WebInterface/login.html\ninurl:citrix inurl:login.asp -site:citrix.com -site:https://www.cvedetails.com -site:https://www.unix.com\ninurl:"/eyeos/index.php" -github -forum\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\ninurl:"/owncloud/index.php" intitle:ownCloud -site:https://questionfocus.com -site:https://www.ccrossan.com -site:https://gemfury.com -site:.site -github -stackoverflow -forum\nfiletype:pwd intitle:index\ninurl:dynamic.php?page=mailbox\ninurl:/dynamic/login-simple.html? -site:www.medicine-tec.com -site:www.architecture-coslovo.info\ninurl:/Remote/logon?ReturnUrl\ninurl:9443/vsphere-client\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\ninurl:index.php?app=main intitle:sms\ninurl:backoffice intitle:login\nintitle:"OneAccess WCF" Username -git -site:http://architecture-coslovo.info -site:http://consultng-sale.net\nfiletype:asp intitle:" Microsoft Outlook Web Access" -logoff -tshoot -site:https://lernfilme.com -site:www.outshare.com -site:https://www.pcmag.com -site:www.centralctlawnservice.com -intitle:"Log Off"\nintitle:vood act=index Gateway >Login inurl:/vood/cgi-bin/\nintitle:"Login Page" intext:"Phone Adapter Configuration Utility" -intitle:Coslovo -intitle:Consulting\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\ninurl:/sap/bc/webdynpro/sap/ | "sap-system-login-oninputprocessing"\nintitle:"Openbravo" (inurl:"openbravo/security/Login_FS.html" | inurl:"openbravo/security/Login_Welcome.html" | inurl:"openbravo/security/Login_F1.html" | inurl:"openbravo/security/Login_F0.html")\nintitle:"Honeywell XL Web Controller - Login" (inurl:"standard/default.php" | inurl:"standard/header/header.php" | inurl:"standard/mainframe.php" | inurl:"standard/footer/footer.php" | inurl:"standard/update.php")\nintitle:"RouterOS" intitle:"configuration page" intext:"You have connected to a router. Administrative access only."\nintext:"2008" intext:"OpenERP SA" intitle:"Login" -intitle:Coslovo -intitle:BP-Bank -sites\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
            filewrite.write("""\nintitle:"Login" intext:"Use Web Messaging Lite" -inurl:sur.ly\nintitle:"Logon - SAP Web Application Server" -git\ninurl:"sap/hrrcf_a_startpage_ext_cand" | inurl:"sap/hrrcf_a_pw_via_email_extern"\ninurl:"/,DanaInfo=" -community -pdf -forum -git -stackoverflow -blog -facebook -site:https://7bsp1018.wikispaces.com\ninurl:"login.php?action=recover" -intitle:"Coslovo" -intitle:"Consulting Sale"\nintitle:"DirectAdmin Login" "Please enter your Username and Password"\n""")
            filewrite.close()
            subprocess.Popen("cd %s && ./inurlbr --no-banner --dork-file %s/dork.txt -q 1,6 -t 1 --sall %s" %
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
    '0': Kembali,
}
