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

## Alternate Solution
Since we need to manipulate the data and send it back to the server in the same session (the output we get when we connect to the server is different each time), a good method is to use Python sockets. Below is an annotated version of the script I used. You can also find it [here](NM01.py)

```python
import socket

HOST = "cfta-nm01.allyourbases.co"
PORT = 8017

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # AF_INET signifies an INET (IPv4) socket and SOCK_STREAM is for TCP port
	s.connect((HOST, PORT)) # connect to the given host and port
	hex = s.recv(1024) # retrieve the \x delimited hex data that should look something like this: b'\\x48\\x51\\x57\\x54\\x53\\x45\\x41\n'
	ascii = hex.decode("unicode-escape") # decode the data into ASCII: HQWTSEA
	s.send(ascii.encode()) # we must send back the ASCII input as encoded bytes, not a string
	s.send("\n".encode())
	flag = s.recv(1024)
	print(flag.decode()) # yay!
```


## Flag
Flag: `o[hex]=>i[ascii]=:)`
