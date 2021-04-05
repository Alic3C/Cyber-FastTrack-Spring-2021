# NM01
> 250pts

## Briefing
> Retrieve output from network endpoint at `cfta-nm01.allyourbases.co` port `8017` and figure out how to get the flag.

## Solution
When you try to connect to the server, we get the following output:

```console
CDSkids@kali:~$ nc cfta-ne01.allyourbases.co 8017
\x53\x42\x5A\x4F\x58\x4A
```

This is Hex with the delimiter `\x`, with the server expecting an input of the hex translated to ASCII. However, the hex changes each time you connect:

```console
CDSkids@kali:~$ nc cfta-ne01.allyourbases.co 8017
\x4B\x43\x59\x43\x55\x53
```

Although not the intended solution, we noticed one of the correct inputs it would take is `AAAAAAA`. With the command `yes 'echo "AAAAAAA" | nc cfta-ne01.allyourbases.co 8017' | bash` and a bit of waiting for a few seconds, the output `Correct! - Flag: o[hex]=>i[ascii]=:)\x51\x4C\x50\x59\x54\x56` was spat out when the hex was `\x41\x41\x41\x41\x41\x41\x41`.

The correct solution is to create a script to take the hex input and spit it back out at the server - however none of our attempts worked! 

## Flag
Flag: `o[hex]=>i[ascii]=:)`
