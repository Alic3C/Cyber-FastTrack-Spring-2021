# CH01
> 500pts

## Briefing
> Download the files and find a way to retrieve the encrypted data.

## Solution
The provided file can be found [here](ch01.zip).

We're given public keys (`.pub` files), so we know [asymmetric encryption](https://en.wikipedia.org/wiki/Public-key_cryptography) is used. RSA is the most common algorithm used, so it's probably that, but we can verify this by decoding the given certificates with [this website](https://8gwifi.org/PemParserFunctions.jsp). If we select `PUBLIC KEY` from the dropdown, copy & paste the whole text of the `1.pub` file into the textbox, and click `Submit`, we get the following output:

```
Algo RSA
Format X.509
 ASN1 Dump
RSA Public Key [f2:bf:0e:41:15:3e:dd:40:bd:ba:66:e6:6e:f3:27:f3:16:51:a6:14]
            modulus: b0aeafaa2ab2be760ddc6cd1bb173117bf084a82c2a10b1a41806f1844129d2d52a86d2f8cb4c9a870213d4a0f359cc29dda6dc7e524c72feeed79c992650c00860ede40ec45ad510d0fc3783d384637f7fc6f9dd7da45fcf38ac02d04a420c5ecaf13c3b15ba94ee11bf7391fd3610430e4565fb3e01710d94128a549249151bdf9e3ac837c5db27186c504779d04728b5b7fac14e61c084cc4de3872a8073fec3b739486f5b2970cc40e3c717e4d8a6f49f78667249795284749c4d62275d23381fab252a6c316bf2c160e05637ae98b3ccdc60794359d4e48f3ea3d4a61e460e52632ddee5c6ce858873d57815477d3664af0d5ac4eb6dfc9778628b8fc39
    public exponent: 1f
```

Even though our output is in hexadecimal (base 16), we can easily convert `n` and `e` to decimal (base 10):
```python
e_hex = "1f"
e_dec = int(e_hex, 16) # e_dec = 31
# do the same for n
```

If we do the same for `2.pub`, we get the following:
```
Algo RSA
Format X.509
 ASN1 Dump
RSA Public Key [48:19:4c:30:74:2e:ff:71:03:2f:b3:66:22:ac:c7:b8:90:fe:0c:95]
            modulus: b0aeafaa2ab2be760ddc6cd1bb173117bf084a82c2a10b1a41806f1844129d2d52a86d2f8cb4c9a870213d4a0f359cc29dda6dc7e524c72feeed79c992650c00860ede40ec45ad510d0fc3783d384637f7fc6f9dd7da45fcf38ac02d04a420c5ecaf13c3b15ba94ee11bf7391fd3610430e4565fb3e01710d94128a549249151bdf9e3ac837c5db27186c504779d04728b5b7fac14e61c084cc4de3872a8073fec3b739486f5b2970cc40e3c717e4d8a6f49f78667249795284749c4d62275d23381fab252a6c316bf2c160e05637ae98b3ccdc60794359d4e48f3ea3d4a61e460e52632ddee5c6ce858873d57815477d3664af0d5ac4eb6dfc9778628b8fc39
    public exponent: 7f
```

Notice anything? The two modulus values are the same for both public keys! That means this encrypted message is vulnerable to a [Common Modulus Attack](https://thescipub.com/pdf/jcssp.2006.665.671.pdf). To use this, we need the common modulus `n`, an `e1` value for the first ciphertext, the cipher `c1`, `e2`, and the second cipher `c2`. These all must be in decimal.

So, we need to convert the ciphertexts (`.enc` files) into decimal form (currently encoded in base 64 - the `=` at the end is a pretty clear giveaway). We can run the following command in the terminal:
```sh
┌─[blueberries@parrot]─[~/NCS/ch01]
└──╼ $cat m1.enc | tr -d '\n' | base64 -d | xxd -p | tr -d '\n' | python -c "for line in __import__('sys').stdin: print(int(line, 16))"
21309803042637511615406342604933393537655925140785513083274322583558182079041118765482939986628901169787272691086561237113288586368420325065436357775257935802831043663673837252070041351749169522998611163218888265038945207598427746990103441950180533601623498698545622327439440344796439341725541470559089916313370842110684712058343303527166791927762271018509679749352510508159522961683738897850333323303362813548703908301525247827743141771601986863380717353344825838293763129970208393090005209923927877453665029197529883591618222619423895467206313580495805992208572894659166150171412562825445087384520240206729335170516
```
Let's break this up:
* `cat m1.enc` > displays the contents of `m1.enc`
* `tr -d '\n'` > removes all the newline characters
* `base64 -d` > decodes from base 64
* `xxd -p` > creates a hexdump, but only the actual hex bytes; ignores the ASCII representation
* `tr -d '\n'` > removes all the newlines again
* `python -c "for line in __import__('sys').stdin: print(int(line, 16))"` > converts the hex input into decimal

The output is our ciphertext `c1`. We can repeat this for `m2.enc` to get the second ciphertext.

Now, we can plug these variables into any attack script we find online, such as [this one](https://blog.0daylabs.com/2015/01/17/rsa-common-modulus-attack-extended-euclidean-algorithm/).

We can convert the plaintext output in decimal to ASCII like so:
```python
import binascii
dec = 8890125754887937411828077954731805906286490380137883135984143260551703819734842400222717478646646077726129754152536477411210370477872730243768640237139024274761857845969320109130732059872358070976283518327690405764700575068395929876003269646407806676159415224498086016969007643394525867668303737918845568202735259258227280892282760950054976219763159884043733610551287602341292147384860085214837257222191875036612558464281771937205223471518801238849738303991791717613596567715589016505529736013585710651567970584890437169998475070192492375054693957775149134444634185125814262316852761032851538733940990589701231950368
hex = format(dec, 'x')
ascii = binascii.unhexlify(hex).decode()
print(ascii)
```

## Flag
Flag: `shaRinGisCaRinG-010`

## Resources
* Another way to dump the public exponent (`e`) and the modulus (`n`) from a `.pub` file
    * [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) - download from GitHub, extract, add to `$PATH` environment variable, and then run `RsaCtfTool.py --dumpkey --key 1.pub`; very useful, as it gives us the output immediately in decimal form
```
n: 22304082644975852743114008695808899287719118009359226182581213403566595839656670815053963599656774184858473201312054532505026757535932368367552515866751304952688361192721984673475384139991343339703058297718180178240939008100002482955267423978148956507166370605992035813498744307130036017491275494370518089644388850785284413492552358793080613280275110944701686910132732081781239770715042010219435107141330923208438588892661274158371830390690056633934039171627447439108435026509588471553930678536862126583867207063222702315747676742797697684348464221215761305755347211413921942012391134432498185676674403999995213184057
e: 31
```

* Alternative way to convert base 10 > ASCII
```python
from libnum import *
ascii = n2s(dec).decode()
print(ascii)
```


* Read more about the Common Modulus Attack
    * [rsa - how to use common modulus attack? - Cryptography Stack Exchange](https://crypto.stackexchange.com/questions/16283/how-to-use-common-modulus-attack)
    * [RSA Attacks: Common Modulus. RSA, named after Rivest–Shamir–Adleman… | by Andreas Pogiatzis | InfoSec Write-ups](https://infosecwriteups.com/rsa-attacks-common-modulus-7bdb34f331a5)
    * [CodeBlue CTF 2017 - Common Modulus 1,2,3](https://pequalsnp-team.github.io/writeups/common_modulus)


* RSA tools
    * [attackrsa](https://github.com/rk700/attackrsa)
    * [cryptools](https://github.com/sonickun/cryptools)
    * [CTF-Crypto](https://github.com/ValarDragon/CTF-Crypto)
    * [goRsaTool](https://github.com/sourcekris/goRsaTool)
    * [RSA-Common-Modulus-Attack](https://github.com/HexPandaa/RSA-Common-Modulus-Attack)
    * [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)
    * [rsatool](https://github.com/ius/rsatool)
    * [RSHack](https://github.com/zweisamkeit/RSHack)
    * [X-RSA](https://github.com/X-Vector/X-RSA)
