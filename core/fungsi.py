#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import re, subprocess, sys, os, time, socket, select, termios, tty

class warna():
    abuabu = '\033[96m'
    biru = '\033[94m'
    kuning = '\033[93m'
    hijau = '\033[92m'
    merah = '\033[91m'
    tutup = '\033[0m'

def txtool_dir():
    return os.path.join(os.path.expanduser('~'), '.txtool')
txtool_dir = txtool_dir()


def IP():
    try:
        local_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        local_ip.connect(('google.com', 0))
        local_ip.settimeout(2)
        alamat_ip = local_ip.getsockname()[0]

    except:
        print(warna.merah + "\n[x] " + warna.tutup + "{0}fatal error{1} no internet connection\n".format(warna.merah, warna.tutup))
        sys.exit()

    return local_ip

def check_ndiff():
    ndiff_path = '/data/data/com.termux/files/usr/bin'
    if not os.path.isfile("%s/ndiff" % (ndiff_path)):
        print(warna.merah + "\n[x] Fatal error" + warna.tutup + " ndiff not found !")
        print(warna.kuning + "[!] " + warna.tutup + "you can download ndiff binary at my Brach.")
        print(warna.hijau + " https://github.com/kuburan/kuburan.github.io/tree/master/files/dists/termux/external/binary-all" + warna.tutup)
        sys.exit()

    else :
        return True


def check_proxychains():
    proxychains_path = '/data/data/com.termux/files/usr/bin'
    proxychains_conf = '/data/data/com.termux/files/usr/etc'
    if not os.path.isfile("%s/proxychains4" % (proxychains_path)):
        if not os.path.isfile("%s/proxychains.conf" % (proxychains_conf)):
            print(warna.merah + "\n[x] Fatal error" + warna.tutup + " proxychains not found !")
            print(warna.kuning + "[!] " + warna.tutup + "you can download proxychains binary at its-pointless Brach.")
            print(warna.hijau + " https://github.com/its-pointless/its-pointless.github.io/tree/master/files/dists/termux/extras\n" + warna.tutup)
            sys.exit()

    else :
        return True


def check_php():
    php_path = '/data/data/com.termux/files/usr/bin'
    php_lib = '/data/data/com.termux/files/usr/lib'
    if not os.path.isfile("%s/php" % (php_path)):
        if not os.path.isdir("%s/php" % (php_lib)):
            print(warna.merah + "\n[x] Fatal error" + warna.tutup + " it seems php not installed in your device")
            print(warna.kuning + "[!]" + warna.tutup + " please, install php and try again.\n")
            sys.exit()
    else:
        return True


def check_nmap():
    nmap_path = '/data/data/com.termux/files/usr/bin'
    nmap_lib = '/data/data/com.termux/files/usr/share'
    if not os.path.isfile("%s/nmap" % (nmap_path)):
        if not os.path.isdir("%s/nmap" % (nmap_lib)):
            print(warna.merah + "\n[x] Fatal error" + warna.tutup + " it seems nmap not installed in your device")
            print(warna.kuning + "[!]" + warna.tutup + " please, install nmap and try again.\n")
            sys.exit()
    else:
        return True


def empty():
    try:
        print(warna.kuning + "\n[!] " + warna.tutup + "Warning. your input is empty, txtool will be assume scanning is canceled")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")

    except KeyError:
        pass


def scan_finish():
    try:
        print(warna.hijau + "\n[*] " + warna.tutup + "Finish scanning !!!")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")

    except KeyError:
        pass


def finish_dorking():
    try:
        print(warna.hijau + "\n[*] " + warna.tutup + " Finish dorking !!!")

    except KeyError:
        pass


def finish_exploit():
    try:
        print(warna.hijau + "\n[*]" + warna.tutup + " Exploitation finished !!!")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")

    except KeyError:
        pass


def info_page():
    print(warna.kuning + "\n[!] " + warna.tutup + " Example: press 1 for crawling page 1, press 2 for crawling page 2. and so on.")


def info():
    print(warna.kuning + "\n[!] " + warna.tutup + "if you are not spesified the port number, txtool will scan all port for you.")


def check_vulners():
    try:
        if os.path.isfile("/data/data/com.termux/files/usr/share/nmap/scripts/vulners.nse"):
            return True

        if not os.path.isfile("/data/data/com.termux/files/usr/share/nmap/scripts/vulners.nse"):
            print(warna.hijau + "\n[*]" + warna.tutup + " checking vulners script, please wait a moment.")
            time.sleep(5)
            print(warna.kuning + "\n[!]" + warna.tutup + " it seems vulners not installed in your device")
            time.sleep(2)
            print(warna.kuning + "\n[!]" + warna.tutup + " alright, txtool will prepare it for you.")
            print(warna.hijau + "\n[*]" + warna.tutup + " please wait a moment.... ")
            time.sleep(5)
            vulners_dir = '/data/data/com.termux/files/usr/share/nmap/scripts'
            os.system("apt-get install -y wget")
            os.system("cd %s && wget https://raw.githubusercontent.com/vulnersCom/nmap-vulners/master/vulners.nse" %
                      (vulners_dir))
            print(warna.hijau + "\n[*]" + warna.tutup + " updating script. please wait a moment....")
            time.sleep(3)
            subprocess.Popen("nmap --script-updatedb",
                             stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True).wait()
            print(warna.hijau + "\n[*]" + warna.tutup + " ok, everything is fine.")
            raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")

    except KeyError:
        pass

def check_vulscan():
    try:
        if os.path.isdir("/data/data/com.termux/files/usr/share/nmap/scripts/vulscan"):
            pass

        if not os.path.isdir("/data/data/com.termux/files/usr/share/nmap/scripts/vulscan"):
            print(warna.hijau + "\n[*]" + warna.tutup + " checking vulscan script, please wait a moment... ")
            time.sleep(5)
            vulscan_dir = '/data/data/com.termux/files/usr/share/nmap/scripts'
            print(warna.kuning + "\n[!]" + warna.tutup + " it seems vulscan not installed in your device")
            time.sleep(2)
            print(warna.kuning + "\n[!]" + warna.tutup + " alright, txtool will prepare it for you.")
            print(warna.hijau + "\n[*]" + warna.tutup + " please wait a moment.... ")
            time.sleep(5)
            os.system("apt-get install -y wget tar")
            os.system("cd %s && wget http://www.computec.ch/projekte/vulscan/download/nmap_nse_vulscan-2.0.tar.gz" %
                       (vulscan_dir))
            os.system("cd %s && tar -xf nmap_nse_vulscan-2.0.tar.gz " % (vulscan_dir))
            os.system("rm -fr %s/nmap_nse_vulscan-2.0.tar.gz " % (vulscan_dir))
            print(warna.hijau + "\n[*]" + warna.tutup + " updating script. please wait a moment.... ")
            time.sleep(3)
            subprocess.Popen("nmap --script-updatedb",
                             stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True).wait()
            print(warna.hijau + "\n[*]" + warna.tutup + " ok, everything is fine.")
            raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")

    except KeyError:
        pass

def check_redpoint():
    try:
        if os.path.isdir("/data/data/com.termux/files/usr/share/nmap/scripts/Redpoint"):
            pass

        if not os.path.isdir("/data/data/com.termux/files/usr/share/nmap/scripts/Redpoint"):
            print(warna.hijau + "\n[*]" + warna.tutup + " checking Redpoint scripts, please wait a moment. ")
            time.sleep(5)
            redpoint_tarball = '/data/data/com.termux/files/usr/share/txtool/other'
            redpoint_dir = '/data/data/com.termux/files/usr/share/nmap/scripts'
            print(warna.kuning + "\n[!]" + warna.tutup + " it seems Redpoint not installed in your device")
            time.sleep(2)
            print(warna.kuning + "\n[!]" + warna.tutup + " alright, txtool will prepare it for you.")
            print(warna.hijau + "\n[*]" + warna.tutup + " please wait a moment.... ")
            time.sleep(5)
            if os.path.isfile("%s/Redpoint.tar.xz" % (redpoint_tarball)):
                os.system("apt-get install -y tar")
                os.system("cp -f %s/Redpoint.tar.xz %s " %
                              (redpoint_tarball, redpoint_dir))
                os.system("cd %s && tar -xJf Redpoint.tar.xz " % (redpoint_dir))
                os.system("rm -fr %s/Redpoint.tar.xz " % (redpoint_dir))
                print(warna.hijau + "\n[*]" + warna.tutup + " updating script. please wait a moment.... ")
                time.sleep(3)
                subprocess.Popen("nmap --script-updatedb",
                             stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True).wait()
                print(warna.hijau + "\n[*]" + warna.tutup + " ok, everything is fine.")
                raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")

            elif not os.path.isfile("%s/Redpoint.tar.xz" % (redpoint_tarball)):
                print(warna.merah + "\n[x] Fatal error" + warna.tutup + " Redpoint file not found !!\n")
                sys.exit()

    except KeyError:
        pass


def check_metasploit():
    if os.path.isfile("/data/data/com.termux/files/usr/bin/msfvenom"):
        if os.path.isfile("/data/data/com.termux/files/usr/bin/msfconsole"):
            metasploit_path = "/data/data/com.termux/files/usr/bin"

    elif os.path.isdir("/data/data/com.termux/files/home/metasploit-framework"):
        metasploit_path = "/data/data/com.termux/files/home/metasploit-framework"

    else:
        print(warna.merah + "\n[x] Fatal error" + warna.tutup + " it seems metasploit not installed in your device")
        print(warna.kuning + "[!]" + warna.tutup + " please, install metasploit and try again.\n")
        sys.exit()


def IP2():
    try:
        local_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        local_ip.connect(('google.com', 0))
        local_ip.settimeout(2)
        alamat_ip = local_ip.getsockname()[0]
        local_ip = raw_input(warna.biru + "\n[+]" + warna.tutup + "  Enter IP for payload listener [" + alamat_ip + "]" + warna.kuning + "  >> " + warna.tutup)
        if local_ip == "":
            local_ip = alamat_ip

    except:
        print(warna.merah + "\n[x] " + warna.tutup + "{0}fatal error{1} no internet connection\n".format(warna.merah, warna.tutup))
        sys.exit()

    return local_ip


def ipv4(ip):
        match = re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip)
        if not match: return False
        quad = []
        for number in match.groups(): quad.append(int(number))
        if quad[0] < 1: return False
        for number in quad:
            if number > 255 or number < 0: return False
        return True

def ssh_shell(command):
    from paramiko.py3compat import u
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        command.settimeout(0.0)
        while True:
            r, w, e = select.select([command, sys.stdin], [], [])
            if command in r:
                try:
                    x = u(command.recv(1024))
                    if len(x) == 0:
                        sys.stdout.write('\r\n{0}[x]{1} shell closed'.format(warna.merah, warna.tutup))
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()

                except socket.timeout:
                    pass

            if sys.stdin in r:
                x = sys.stdin.read(1)
                if len(x) == 0:
                    break
                command.send(x)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
