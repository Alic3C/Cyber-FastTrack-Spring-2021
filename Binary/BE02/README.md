# BE02
> 100pt

## Briefing
> Download the file and find a way to get the flag.

## BE02 Hint
During the competition, the following hint was emailed out:

![](BE02Hint.png)

## Solution
The provided file can be found [here](be02.zip).

This challenge is a simple buffer overflow, just spam your keyboard and enter your input:

```console
CDSkids@kali:~/Desktop$ ./rot13
===================================
ROT IN sHELL :: ROT13's your input!
===================================
> aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

Segmentation fault.
*** stack smashing detected ***: <unknown> terminated
Aborted (core dumped)

Flag: luckyNumber13
```
## Flag
Flag: `luckyNumber13`
