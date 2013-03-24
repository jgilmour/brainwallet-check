#!/usr/bin/python

# Brainwallet Check
# Takes in string as an argument, generates private key and address, then checks blockchain.info to see if it is in use
# Most code taken from https://bitcointalk.org/index.php?topic=84238.0 - thank you JeromeS! 
# You need libpcre3-dev for the GET request to work to blockchain.info (apt get libpcre3-dev)
# - Josh Gilmour

import os
import sys, getopt
import ecdsa
import urllib2
import binascii, hashlib

secp256k1curve=ecdsa.ellipticcurve.CurveFp(115792089237316195423570985008687907853269984665640564039457584007908834671663,0,7)
secp256k1point=ecdsa.ellipticcurve.Point(secp256k1curve,0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)
secp256k1=ecdsa.curves.Curve('secp256k1',secp256k1curve,secp256k1point,(1,3,132,0,10))

def addy(pk):
 pko=ecdsa.SigningKey.from_secret_exponent(pk,secp256k1)
 pubkey=binascii.hexlify(pko.get_verifying_key().to_string())
 pubkey2=hashlib.sha256(binascii.unhexlify('04'+pubkey)).hexdigest()
 pubkey3=hashlib.new('ripemd160',binascii.unhexlify(pubkey2)).hexdigest()
 pubkey4=hashlib.sha256(binascii.unhexlify('00'+pubkey3)).hexdigest()
 pubkey5=hashlib.sha256(binascii.unhexlify(pubkey4)).hexdigest()
 pubkey6=pubkey3+pubkey5[:8]
 pubnum=int(pubkey6,16)
 pubnumlist=[]
 while pubnum!=0: pubnumlist.append(pubnum%58); pubnum/=58
 address=''
 for l in ['123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'[x] for x in pubnumlist]:
  address=l+address
 return '1'+address

if __name__ == "__main__":
  if len(sys.argv) != 2:
    sys.exit("ERROR: Provide brainwallet string as parameter\n./brainwallet-check.py 'Satoshi Nakamoto'")
  privatekey = (int(hashlib.sha256(sys.argv[1]).hexdigest(),16))
  privatekeysha = (hashlib.sha256(sys.argv[1])).hexdigest()
  bcaddy = addy(privatekey)
  word = str(sys.argv[1])
  firstseen = os.popen("GET http://blockchain.info/q/addressfirstseen/" + str(bcaddy)).read()
  amount = os.popen("GET http://blockchain.info/q/addressbalance/" + str(bcaddy)).read()
  print "-----------------------------------------------------"
  print "brainwallet string: " + word
  print "private key: " + str(privatekeysha)
  print "bitcoin address: " + str(bcaddy)
  if str(firstseen) == "null":
    print "[ADDRESS ISN'T IN USE ACCORDING TO BLOCKCHAIN.INFO]"
  else:
    print "First seen according to blockchain.info: " + firstseen
    print "Wallet amount: " + amount
  print "-----------------------------------------------------"
