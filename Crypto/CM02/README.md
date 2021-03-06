# CM02
> 250pts

## Briefing
> Download the file and find a way to get the flag.

## Solution
The provided file can be found [here](cm02.zip).
Printing the file gives a lot of emoji, and some punctuation and number characters.

To determine the alphabet, I put each character on a new line and piped through `sort` and `uniq`. I also added line numbers.
```console
β ~ $ cat cm02.txt | sed -e "s/.\{1\}/&\n/g" | sort | uniq | awk '{print NR  "> " $s}'
1>
2>
3> "
4> (
.
.
.
18> π
19> π©
20> π
21> π
.
.
.
42> π½
43> π
.
.
.
β ~ $
```

The emoji starts at 18, and ends at 43. That's 26 unique emoji letters - looks like this could be a substitution cipher.

To get a string of the alphabet on one line, I used `cat cm02.txt | sed -e "s/.\{1\}/&\n/g" | sort | uniq | tr -d \\n`.

I copy-pasted the emoji section, and used python to write a sed expression that replaces each emoji with a letter.

```py
emoji = "ππ©πππππππ₯π¨π―πΆπ·πΌπ½ππ¨π©πͺπ₯ππππ°π½π"
c = 65
print('sed -e "', end="")
for e in emoji:
    print(f"s/{e}/{chr(c)}/g; ", end="")
    c += 1
print('"')
```

Thus:

```console
β ~ $ cat cm02.txt | sed -e "s/π/A/g; s/π©/B/g; s/π/C/g; s/π/D/g; s/π/E/g; s/π/F/g; s/π/G/g; s/π/H/g; s/π₯/I/g; s/π¨/J/g; s/π―/K/g; s/πΆ/L/g; s/π·/M/g; s/πΌ/N/g; s/π½/O/g; s/π/P/g; s/π¨/Q/g; s/π©/R/g; s/πͺ/S/g; s/π₯/T/g; s/π/U/g; s/π/V/g; s/π/W/g; s/π°/X/g; s/π½/Y/g; s/π/Z/g; "
LGAE SJ KTKCEFSCSEX?

PN EGK MTESOAEK DAEMFK PN KTKCEFSCSEX, AJ PN EGAE PN GKAE ADW TSYGE, LK
AFK AE ZFKJKDE SYDPFADE. HME SE GAJ HKKD CTKAFTX KJEAHTSJGKW EGAE ATT
EGFKK ZGKDPOKDA AFK HME OADSNKJEAESPDJ PN EGK KDKFYX ZKFIAWSDY EGK
MDSIKFJK. HX OKADJ PN JMSEAHTK AZZAFAEMJ PDK NPFO CAD HK CPDIKFEKW SDEP
...
```

I pasted the full message into https://www.boxentriq.com/code-breaking/cryptogram, and it was able to solve almost perfectly.

![boxentriq](boxentiq.jpg)

Copying the underscores back, and changing a few errors, we get the flag.

## Flag
Flag: `frequently_substitute_frowny_face_for_smiley_face`
