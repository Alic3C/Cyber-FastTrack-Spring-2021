# CH02
> 500pts

## Briefing
> Below are 4 messages, 2 of them are insecure... find the flag!

> `2e310d15730618003c27392502592f1b016e1b1c364505191302`

> `27271e1d6f3935381618340a740404152d0063160106490a0a050d013d2`

> `313c0d45350d0c026f3d236b361120191e373c1c3a080e0c2b04`

> `1b060c2749020b354105271616532f27772f1c204811111745320b10021717`

## Solution
The insecure messages can be **broken with one-time-pad [crib dragging](https://samwho.dev/blog/toying-with-cryptography-crib-dragging/)**.

Basically, if you XOR the set of messages with the same length together, you **remove the key from the equation.**

Here, C1 and C2 are a pair of the encrypted messages with the same length.
```
C1 xor C2 = (M1 xor K) xor (M2 xor K)

C1 xor C2 = M1 xor K xor M2 xor K

C1 xor C2 = M1 xor M2 xor K xor K

C1 xor C2 = M1 xor M2
```

This means that:
```
K = CX xor M1
K = CX xor M2
C1 xor C2 = K
```

> [Reference](https://www.reddit.com/r/cryptography/comments/9ywfgm/xor_cipher/)

Now, we can start guessing the plaintext! (This would be the M1/M2). If we XOR our guess, or crib, with the XOR result of the encrypted messages (K), we can uncover the other value of the message.

`M1 (our guess) xor K = M2`

Using this [tool](https://github.com/SpiderLabs/cribdrag), we can guess away, **starting with the assumption that it contains "flag"**

> 

First, XOR the shorter pair of messages with the same length to produce K.
```bash
[agent@cyberstart cribdrag]$ python xorstrings.py 2e310d15730618003c27392502592f1b016e1b1c364505191302 313c0d45350d0c026f3d236b361120191e373c1c3a080e0c2b04

1f0d0050460b1402531a1a4e34480f021f5927000c4d0b153806
```
Start the procedure to crib drag. Note that by entering "flag" as the crib, we also get other clues such as `myYa` and ` gue`. [Reference](https://crypto.stackexchange.com/questions/33376/what-to-do-when-crib-dragging-does-not-work-in-otp-one-time-pad-ciphers)
```bash
[agent@cyberstart cribdrag]$ python cribdrag.py 1f0d0050460b1402531a1a4e34480f021f5927000c4d0b153806
Your message is currently:
0	__________________________
Your key is currently:
0	__________________________
Please enter your crib: flag
*** 0: "yaa7"
*** 1: "kl1!"
2: "f<'l"
3: "6*js"
*** 4: " gue"
*** 5: "mxc4"
6: "rn2}"
7: "d?{}"
8: "5v{)"
9: "|v/S"
10: "|"U/"
11: "(X)h"
12: "R$ne"
*** 13: ".ccx"
14: "in~>"
15: "ds8@"
*** 16: "y5Fg"
*** 17: "?Kak"
18: "Alm*"
19: "f`,l"
*** 20: "j!jr"
21: "+gt_"
*** 22: "myYa"
Enter the correct position, 'none' for no match, or 'end' to quit: 4
Is this crib part of the message or key? Please enter 'message' or 'key': key
Your message is currently:
0	____ gue__________________
Your key is currently:
0	____flag__________________
Please enter your crib: Keep guessing
*** 0: "The flag is S"
1: "Fe56+sw6ii'Z/"
2: "K5#{4e&i=]&h"
3: "d"4o=G!ae"
nqrs}o+G;flx"
5: "@qg#:};Q;|kq>"
6: "_g6j:)A-|qv7@"
7: "I6jnS=jql0Ig"
8: ">/zgl*Nnk"
9: "Q+Dhhwz*Tib*"
10: "Q+Q8/ej<Tse#l"
11: "Q-"x,Bs$er"
12: "-jr?>Re>b{_"
13: "jgoy@ui>x|Va"
Enter the correct position, 'none' for no match, or 'end' to quit: 0
Is this crib part of the message or key? Please enter 'message' or 'key': message
Your message is currently:
0	Keep guessing_____the flag
Your key is currently:
0	The flag is S_____ShimmyYa
Please enter your crib:  for
*** 0: "?ko""
1: "-f?4"
2: " 6)y"
*** 3: "p df"
4: "fm{p"
5: "+rm!"
6: "4d<h"
*** 7: ""5uh"
8: "s|u<"
9: ":|!F"
10: ":([:"
11: "nR'}"
12: ".`p"
*** 13: "himm"
14: "/dp+"
*** 15: ""y6U"
*** 16: "??Hr"
17: "yAo~"
18: "fc?"
*** 19: " j"y"
20: ",+dg"
*** 21: "mmzJ"
22: "+sWt"
Enter the correct position, 'none' for no match, or 'end' to quit: 13
Is this crib part of the message or key? Please enter 'message' or 'key': 0
Invalid response. Try again.
Is this crib part of the message or key? Please enter 'message' or 'key': message
Your message is currently:
0	Keep guessing for_the flag
Your key is currently:
0	The flag is Shimm_ShimmyYa
```

> Note: By the end, we can assume the message is "Keep guessing for the flag", which, XORed with K, produces `The flag is ShimmyShimmyYa`

### TL;DR: The solution [in CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'2e310d15730618003c27392502592f1b016e1b1c364505191302'%7D,'Standard',false)XOR(%7B'option':'UTF8','string':'The%20flag%20is%20ShimmyShimmyYa'%7D,'Standard',false)&input=MzEzYzBkNDUzNTBkMGMwMjZmM2QyMzZiMzYxMTIwMTkxZTM3M2MxYzNhMDgwZTBjMmIwNA)

## Flag
Flag: `ShimmyShimmyYa`
