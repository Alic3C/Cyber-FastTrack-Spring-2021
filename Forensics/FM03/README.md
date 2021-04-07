# FM03
> 250pts

## Briefing
> Download the file and find a way to get the flag.

## FM03 Hint
During the competition, the following hint was emailed out:

> **Hint:** It's a Veracrypt encrypted volume 🤔

## Solution
The provided file can be found [here](fm03.zip).

This disk is a VeraCrypt encrypted volume, protected with a password. Bruteforce the password using Hashcat and the rockyou word list, to get the phrase "redwings". Download the VeraCrypt encryption software and open the disk volume using the password. The flag folder will be located within the root directory. Open the text file within the folder to get the flag.

## Flag
Flag: `Us3_5tr0ng_P@55w0Rds!`
