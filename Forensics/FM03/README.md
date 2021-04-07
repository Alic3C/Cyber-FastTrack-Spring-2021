# FM03
> 250pts

## Briefing
> Download the file and find a way to get the flag.

## FM03 Hint
During the competition, the following hint was emailed out:

> **Hint:** It's a Veracrypt encrypted volume 🤔

## Solution
The provided file can be found [here](fm03.zip).

This disk is a VeraCrypt encrypted volume, protected with a password. Bruteforce the password using Hashcat and the rockyou word list, to get the phrase "redwings". 

`sudo hashcat jwt.txt -m 16500 -a 3 -w 2 /usr/share/wordlists/rockyou.txt --force`

And the output you get:

Dirvolume:redwings
Session..........: hashcat
Status...........: Cracked
Hash.Type........: VeraCrypt PBKDF2-HMAC-SHA512 + XTS 1024 bit
Hash.Target......: dirvolume
Time.Started.....: Tue Apr  6 14:49:28 2021 (14 mins, 46 secs)
Time.Estimated...: Tue Apr  6 15:04:14 2021 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:        6 H/s (10.87ms) @ Accel:128 Loops:64 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 5120/14344385 (0.04%)
Rejected.........: 0/5120 (0.00%)
Restore.Point....: 4608/14344385 (0.03%)`

Download the VeraCrypt encryption software and open the disk volume using the password. The flag folder will be located within the root directory. Open the text file within the folder to get the flag.


## Flag
Flag: `Us3_5tr0ng_P@55w0Rds!`
