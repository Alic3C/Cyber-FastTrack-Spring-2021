# BX02
> 1,000pts

## Briefing
> Access the network service at url: `cfta-bx02.allyourbases.co` port: `8013` and find a way to get the flag.

## Notes (not a write up)

```console
➜ ~ $ nc cfta-bx02.allyourbases.co 8013
Come Fuzz Me Bro.
DEBUG: Waiting 100ms
d
DEBUG: Input length too large.
➜ ~ $ echo "" | nc cfta-bx02.allyourbases.co 8013
Come Fuzz Me Bro.
DEBUG: Waiting 100ms
DEBUG: Input length too large.
➜ ~ $
```

No clue what this service is doing.

## Solution

## Flag
Flag: ``
