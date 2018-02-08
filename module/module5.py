#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import subprocess, sys, os

sys.path.append("/data/data/com.termux/files/usr/share/txtool/core")
from fungsi import txtool_dir, warna, empty, finish_dorking, IP, info_page
import sub_menu2 as back

def menu_utama():
    print(warna.hijau + "\n\t[*]" + warna.tutup + warna.abuabu + "  Page 1 - Page 15 " + warna.tutup)
    print(warna.hijau + "\t[*]" + warna.tutup + warna.abuabu + "  Press 0 to back\n" + warna.tutup)
    print(warna.kuning + "\n[!] " + warna.tutup + " Googles collection of web sites sharing sensitive directories. The files contained in here will vary from sensitive to über-secret! \n")
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
            filewrite.write("""\n"lv_poweredBy" -twitter -lang -ghdb -google -cloud -forum -pastebin -site:www.tankeast.ru -site:http://artcool.org\nintext:"/wp-content/uploads/wpsc/"\nintitle:index.of .bashrc\nintext:"index of /userfiles/file/"\ninurl:/wp-content/plugins/seo-pressor/classes/\ninurl:"nfs://www." "index of /"\nintext:/wp-content/plugins/woocommerce/templates/emails/plain/\ninurl:/sym/root/ intitle:index.of\nintext:"Index of /database"\nintext:"Index of /.git"\nintitle:index.of intext:viewvc\n"m.zippyshare.com/"\nindex of /htdocs\n""")
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
            filewrite.write("""\nintitle:"Index of /" "joomla_update.php"\n-inurl:htm -inurl:html intitle:"index of" NIKON\n-inurl:htm -inurl:html intitle:"index of" 100CANON\ninurl:"/drive/folders/" site:drive.google.com\ninurl:"folderview?id=" site:drive.google.com\n"Index of" inurl:"/$Recycle.Bin/"\n"Powered by AutoIndex PHP Script" ext:php\n""")
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
            filewrite.write("""\npowered by h5ai\nsite:onedrive.live.com shared by\ninurl:admin inurl:uploads\ninurl:".esy.es/default.php"\ninurl:/fckeditor/editor/plugins/ajaxfilemanager/ajaxfilemanager.php\nHostinger © 2016. All rights reserved inurl:default.php\nindex:"html/js/editor/fckeditor/editor/filemanager/connectors"\n""")
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
            filewrite.write("""\n(intext:"index of /.git") ("parent directory")\ninurl:/FCKeditor/editor/filemanager/upload/\ninurl:pictures intitle:index.of\ninurl:trash intitle:index.of\ninurl:.ssh intitle:index.of authorized_keys\ninurl:/sites/default/files/webform/\nintitle:Index of /__MACOSX ...\ninurl:safm.asp ext:asp\nintitle: Index of /awstats/data\n""")
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
            filewrite.write("""\ninurl:/server/webapps\nintitle:index.of.mail\ninurl:pipermail intitle:index.of parent\ninurl:"wp-content/uploads/private"\nintitle:index.of inurl:grades site:edu\nintitle:index.of parent inurl:repos\n"Desktop" parent intitle:index.of\ninurl:/aspnet_client/system_web/\n"sql" "parent" intitle:index.of -injection\n"My Documents" "parent" intitle:index.of\n""")
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
            filewrite.write("""\ninurl:.DS_Store intitle:index.of\ninurl:.listing intitle:index.of\ninurl:users intitle:index.of\nprivate parent intitle:index.of\nmail spool intitle:index.of\ninurl:"/cms/app/webroot"\nintitle:"Index.of" "attachments"\n""")
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
            filewrite.write("""\nintitle:"index of" inurl:"no-ip.com"\nintitle:"Index Of" intext:"iCloud Photos" OR intext:"My Photo Stream" OR intext:"Camera Roll"\nintitle:"index of" "onetoc2" "one"\ninurl:private_files\ninurl:wp-admin/ intext:css/\nintitle:"Index of ftp"\nintitle:index.of.dropbox\n""")
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
            filewrite.write("""\nintitle:"index of" intext:".ds_store"\nintitle:"index of" myshare\ninurl:8080 intitle:"Dashboard [Jenkins]"\nintitle:index.of intext:.bash_history\n"index of" inurl:sym\nintext:xampp-dav-unsecure:$apr1$6O9scpDQ$JGw2Tjz0jkrqfKh5hhiqD1\ninurl:ckfinder intext:"ckfinder.html" intitle:"Index of /ckfinder"\n""")
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
            filewrite.write("""\nintitle:"Index of" "WhatsApp Databases"\ninurl:"default.php" intext:"website" "has been successfully installed on the server!"\nintitle:"Index of" "WhatsApp Images"\nintitle:"Index of" "DCIM"\nintext:index of sym\nintitle:index.of.pubs\nintitle:"Index of" "wwwroot"\n""")
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
            filewrite.write("""\nintitle:index.of.accounts\nintitle:index.of +"Indexed by Apache::Gallery"\ninurl:/wp-content/wpbackitup_backups\n"Config" intitle:"Index of" intext:vpn\n"jos_users" intitle:"Index of"\ninurl:/cgi-bin/.cgi\nallinurl:/hide_my_wp=\n""")
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
            filewrite.write("""\n"index of" inurl:root intitle:symlink\ninurl:/xampp\nallintext:"WebServerX Server at"\nintitle:index.of ios -site:cisco.com\nintitle:index.of cisco asa -site:cisco.com\nintitle:index.of.config\nallintitle:"FirstClass Login"\n""")
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
            filewrite.write("""\ninurl:install.pl intext:"Reading path paramaters" -edu\n"Warning: Installation directory exists at" "Powered by Zen Cart" -demo\n"Welcome to the directory listing of" "NetworkActiv-Web-Server"\nlog inurl:linklint filetype:txt -"checking"\n"Directory Listing for" "Hosted by Xerver"\nintitle:"Folder Listing" "Folder Listing" Name Size Date/Time File Folder\nintitle:"Backup-Management (phpMyBackup v.0.4 beta * )" -johnny.ihackstuff\nintitle:"pictures thumbnails" site:pictures.sprintpcs.com\n""")
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
            filewrite.write("""\nintitle:index.of WEB-INF\nintitle:index.of /maildir/new/\nfiletype:ini Desktop.ini intext:mydocs.dll\nfiletype:torrent torrent\n"Index of" rar r01 nfo Modified 2004\n"Web File Browser" "Use regular expression"\nintitle:"HFS /" +"HttpFileServer"\nintitle:upload inurl:upload intext:upload -forum -shop -support -w3c\n""")
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
            filewrite.write("""\nintitle:index.of abyss.conf\nintitle:"Index of /CFIDE/" administrator\nallinurl:"/*/_vti_pvt/" | allinurl:"/*/_vti_cnf/"\nintitle:"index of" inurl:ftp (pub | incoming)\n"Powered by Invision Power File Manager" (inurl:login.php) | (intitle:"Browsing directory /" )\nintitle:"index of" "parent directory" "desktop.ini" site:dyndns.org\nintext:"Powered By: TotalIndex" intitle:"TotalIndex"\n"intitle:Index.Of /" stats merchant cgi-* etc\n""")
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
            filewrite.write("""\nintitle:"index of" intext:"content.ie5"\nintitle:"index of" -inurl:htm -inurl:html mp3\nindex.of.dcim\nintitle:"Directory Listing For" intext:Tomcat -int\nintitle:"webadmin - /*" filetype:php directory filename permission\nintitle:index.of (inurl:fileadmin | intitle:fileadmin)\nintitle:"Index of *" inurl:"my shared folder" size modified\nintitle:index.of /AlbumArt_\n""")
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
