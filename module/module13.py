#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import subprocess, sys, os

sys.path.append("/data/data/com.termux/files/usr/share/txtool/core")
from fungsi import txtool_dir, warna, empty, finish_dorking, IP, info_page
import sub_menu2 as back

def menu_utama():
    print(warna.hijau + "\n\t[*]" + warna.tutup + warna.abuabu + "  Page 1 - Page 15 " + warna.tutup)
    print(warna.hijau + "\t[*]" + warna.tutup + warna.abuabu + "  Press 0 to back\n" + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + " These links demonstrate Googles awesome ability to profile web servers \n")
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
            filewrite.write("""\ninurl:readme.md intext:"Laravel"\ninurl:phpmyadmin/themes intext:"pmahomme"\nintext:"Welcome to CodeIgniter!"\ninurl:readme.rst intext:"CodeIgniter"\nintitle:"Index of" "Apache/2.4.7 (Ubuntu) Server"\n""")
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
            filewrite.write("""\ninurl:/pub/ inurl:_ri_\next:svc inurl:wsdl\ninurl:user_guide intext:"CodeIgniter User Guide"\n"PHP Credits" "Configuration" "PHP Core" ext:php inurl:info\ninurl:/php/info.php\nintitle:"HFS" "Server Uptime" "Server time"\n""")
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
            filewrite.write("""\ninurl:phpsysinfo/index.php?disp=dynamic\nintitle:"Apache Status" | intext:"Apache Server Status"\nintext:Apache/2.2.29 (Unix) mod_ssl/2.2.29 | intitle:"Index of /"\ninurl:"/web-console/" intitle:"Administration Console"\nfiletype:asmx inurl:(_vti_bin|api|webservice)\nintitle:"BadBlue: the file-sharing web server anyone can use"\n""")
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
            filewrite.write("""\nintext:"Target Multicast Group" "beacon"\nintitle:"Apache Status" "Apache Server Status for"\ninurl:wl.exe inurl:?SS1= intext:"Operating system:" -edu -gov -mil\ninurl:nnls_brand.html OR inurl:nnls_nav.html\n(intitle:"502 Proxy Error")|(intitle:"503 Proxy Error") "The proxy server could not handle the request" -topic -mail -4suite -list -site:geocrawler.co\nintitle:"Welcome to 602LAN SUITE *"\n""")
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
            filewrite.write("""\nintitle:"Document title goes here" intitle:"used by web search tools" " example of a simple Home Page"\nintitle:"Welcome To Your WebSTAR Home Page"\nintitle:"Welcome to the Advanced Extranet Server, ADVX!"\nintitle:"Welcome to Windows Small Business Server 2003"\nintitle:"IPC@CHIP Infopage"\nyaws.*.server.at\n""")
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
            filewrite.write("""\nintitle:"Test Page for the Apache HTTP Server on Fedora Core" intext:"Fedora Core Test Page"\nPowered.by.RaidenHTTPD intitle:index.of\n(inurl:81-cobalt | inurl:cgi-bin/.cobalt)\nintitle:"welcome to mono xsp"\n""")
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
            filewrite.write("""\nXAMPP "inurl:xampp/index"\ninurl:2506/jana-admin\nallintext:"Powered by LionMax Software" "WWW File Share"\nintitle:"Resin Default Home Page"\nintitle:"Welcome To Xitami" -site:xitami.com\n""")
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
            filewrite.write("""\n"Switch to table format" inurl:table|plain\nintitle:"Object not found!" intext:"Apache/2.0.* (Linux/SuSE)"\nintitle:"Open WebMail" "Open WebMail version (2.20|2.21|2.30) "\nintitle:"error 404" "From RFC 2068 "\nintitle:"Directory Listing, Index of /*/"\nintitle:"Lotus Domino Go Webserver:" "Tuning your webserver" -site:ibm.com\n""")
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
            filewrite.write("""\nintitle:"Object not found" netware "apache 1.."\nintitle:AnswerBook2 inurl:ab2/ (inurl:8888 | inurl:8889)\nintext:"404 Object Not Found" Microsoft-IIS/5.0\nintitle:"Shoutcast Administrator"\n"powered by" "shoutstats" hourly daily\n"Novell, Inc" WEBACCESS Username Password "Version *.*" Copyright -inurl:help -guides|guide\n""")
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
            filewrite.write("""\nfitweb-wwws * server at intitle:index.of\n"httpd+ssl/kttd" * server at intitle:index.of\nsEDWebserver * server +at intitle:index.of\n"Red Hat Secure/3.0 server at"\n"OpenSA/1.0.4" intitle:index.of\n"OmniHTTPd/2.10" intitle:index.of\n""")
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
            filewrite.write("""\n"Microsoft-IIS/6.0" intitle:index.of\n"Microsoft-IIS/5.0 server at"\n"Microsoft-IIS/* server at" intitle:index.of\n"MaXX/3.1" intitle:index.of\n"JRun Web Server" intitle:index.of\n""")
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
            filewrite.write("""\n"AnWeb/1.42h" intitle:index.of\nallinurl:".nsconfig" -sample -howto -tutorial\ninurl:domcfg.nsf\nintitle:"300 multiple choices"\nintitle:Snap.Server inurl:Func=\nintitle:"Test Page for Apache"\n""")
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
            filewrite.write("""\nallintitle:Netscape FastTrack Server Home Page\n"seeing this instead" intitle:"test page for apache"\nintitle:"Test Page for Apache" "It Worked!" "on this web"\n\n""")
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
            filewrite.write("""\nindex_i.shtml Ready\ninurl:tech-support inurl:show Cisco\nintitle:"Welcome to Windows 2000 Internet Services"\n"powered by openbsd" +"powered by apache"\n""")
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
            filewrite.write("""\nintitle:"Welcome to Your New Home Page!" "by the Debian release"\nintitle:"Page rev */*/*" inurl:"admin\nCERN httpd 3.0B (VAX VMS)"\ninurl:oraweb -site:oraweb.org\n"Netware * Home" inurl:nav.html\nintitle:"Index of /" "Proudly Served by Surftown at"\n""")
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
    '14': menu14,
    '15': menu15,
    '0': Kembali,
}
