# Brainwallet Check

## Overview
Brainwallet is a concept of memorizing a passphrase to generate a bitcoin address. If not used properly (**ie. not using a secure passphrase that is easily guessable**), the wallet can be generated with malicious intent to steal the bitcoins in it. 

More information about what a brainwallet is can be found here: [https://en.bitcoin.it/wiki/Brainwallet](https://en.bitcoin.it/wiki/Brainwallet)

**Brainwallet Check** is a python script that allows you to specify a passphrase as an argument and will generate the private key and bitcoin address based off the passphrase. In addition, it will check blockchain.info to see if the wallet has been used before, and if it has, it will return the amount stored in the wallet. 

The script could easily be modified to read from a file, which could contain multiple lines of passphrases, however blockchain.info will temp-ban you if API requests are more than one every 10 seconds. 

## Requirements
* **Python**
* **Python Modules**: os, sys, getopt, ecdsa, urllib2, binascii, hashlib
* **libpcre3-dev** (for the GET system command)

## Usage

Usage of **Brainwallet Check** is pretty simple, just call the python script and pass it along the passphrase:

	python brainwallet-check.py 'passphrase to use' 

## Examples
Basic run with no parameters:

    root@techsmog:~/brainwallet-check# ./brainwallet-check.py
    ERROR: Provide brainwallet string as parameter
    ./brainwallet-check.py 'Satoshi Nakamoto'
    
Basic run with a valid address, but nothing in the wallet:    
    
    root@techsmog:~/brainwallet-check# ./brainwallet-check.py  'Satoshi Nakamoto'
	-----------------------------------------------------
	brainwallet string: Satoshi Nakamoto
	private key: 72759466100064397073952777052424474334519735946222029294952053344302920927294
	bitcoin address: 1JryTePceSiWVpoNBU8SbwiT7J4ghzijzW
	First seen according to blockchain.info: 1322885134
	Wallet amount: 0
	-----------------------------------------------------

Basic run with an address that hasn't been used yet:

	root@techsmog:~/brainwallet-check# ./brainwallet-check.py 'gimme da loot'
	-----------------------------------------------------
	brainwallet string: gimme da loot
	private key: 112095600548568711100952985931940355672316008458252242110023944239157495839427
	bitcoin address: 1AYmvzSbZrdhV5S39S2Ce1u3xBqAhJUYaG
	[ADDRESS ISN'T IN USE ACCORDING TO BLOCKCHAIN.INFO]
	-----------------------------------------------------

## Credit

A vast amount of this code is from **JeromeS** on bitcointalk.org forums. Specifically this thread: [https://bitcointalk.org/index.php?topic=84238.0](https://bitcointalk.org/index.php?topic=84238.0)

## Questions/Comments/etc ?

* **Email** [jgilmour@techsmog.com](mailto:jgilmour@techsmog.com)
* **Site**: [http://www.techsmog.com](http://www.techsmog.com)
* **GitHub**: [http://www.github.com/jgilmour](http://www.github.com/jgilmour)

Feel free to fork! 

March 23, 2013 11:16 PM
