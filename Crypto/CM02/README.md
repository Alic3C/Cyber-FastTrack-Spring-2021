# CM02
> 250pts

## Briefing
> Download the file and find a way to get the flag.

## Solution
The provided file can be found [here](cm02.zip).
Printing the file gives a lot of emoji, and some punctuation and number characters.

To determine the alphabet, I put each character on a new line and piped through `sort` and `uniq`. I also added line numbers.
```console
➜ ~ $ cat cm02.txt | sed -e "s/.\{1\}/&\n/g" | sort | uniq | awk '{print NR  "> " $s}'
1>
2>
3> "
4> (
.
.
.
18> 🍇
19> 🎩
20> 🏃
21> 🐍
.
.
.
42> 😽
43> 🙉
.
.
.
➜ ~ $
```

The emoji starts at 18, and ends at 43. That's 26 unique emoji letters - looks like this could be a substitution cipher.

To get a string of the alphabet on one line, I used `cat cm02.txt | sed -e "s/.\{1\}/&\n/g" | sort | uniq | tr -d \\n`.

I copy-pasted the emoji section, and used python to write a sed expression that replaces each emoji with a letter.

```py
emoji = "🍇🎩🏃🐍👀👅👉👐👥👨👯👶👷👼👽💛💨💩💪🔥😀😉😏😰😽🙉"
c = 65
print('sed -e "', end="")
for e in emoji:
    print(f"s/{e}/{chr(c)}/g; ", end="")
    c += 1
print('"')
```

Thus:

```console
➜ ~ $ cat cm02.txt | sed -e "s/🍇/A/g; s/🎩/B/g; s/🏃/C/g; s/🐍/D/g; s/👀/E/g; s/👅/F/g; s/👉/G/g; s/👐/H/g; s/👥/I/g; s/👨/J/g; s/👯/K/g; s/👶/L/g; s/👷/M/g; s/👼/N/g; s/👽/O/g; s/💛/P/g; s/💨/Q/g; s/💩/R/g; s/💪/S/g; s/🔥/T/g; s/😀/U/g; s/😉/V/g; s/😏/W/g; s/😰/X/g; s/😽/Y/g; s/🙉/Z/g; "
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
