# NE01
> 100pts

## Briefing
> There is a TCP network service running on `cfta-ne01.allyourbases.co`. Find it to get the flag after you connect.

> Note: The target has many open ports - only one is the correct one. The correct port will identify itself with `ID: ne01` after you connect.

## Solution
As we need to find a port, a quick [Nmap](https://nmap.org/) search takes care of this:

```console
nmap -sV -sC -Pn cfta-ne01.allyourbases.co
Starting Nmap 7.80 ( https://nmap.org ) at 2021-04-05 12:51 EDT
Nmap scan report for cfta-ne01.allyourbases.co (34.251.231.207)
Host is up (0.046s latency).
Other addresses for cfta-ne01.allyourbases.co (not scanned): 52.210.101.44
rDNS record for 34.251.231.207: ec2-34-251-231-207.eu-west-1.compute.amazonaws.com
Not shown: 999 filtered ports
PORT     STATE SERVICE    VERSION
1061/tcp open  tcpwrapped
```

Using [Netcat](https://nc110.sourceforge.io/), we can quickly connect to the service using `nc cfta-ne01.allyourbases.co 1061`:

```console
nc cfta-ne01.allyourbases.co 1061
ID: ne01
Flag: Nmap_0f_the_W0rld!
```

## Flag
Flag: `Nmap_0f_the_W0rld!`
