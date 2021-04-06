# BE01
> 100pt

## Briefing
> Download the file and find a way to get the flag.

## Solution
The provided file can be found [here](be01.zip).

Using Binwalk, extract any embedded files and/or executable code from `chicken.pdf` using `binwalk -e chicken.pdf`:

```console
binwalk -e chicken.pdf

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PDF document, version: "1.4"
72            0x48            Zip archive data, at least v1.0 to extract, compressed size: 550522, uncompressed size: 550522, name: egg.zip
550609        0x866D1         End of Zip archive, footer length: 22
551319        0x86997         Zlib compressed data, default compression
6478358       0x62DA16        Zlib compressed data, default compression
6478601       0x62DB09        End of Zip archive, footer length: 22
```

From this you get the output `_chicken.pdf.extracted`, containing a zip file called `chicken.zip`. Opening this we are greeted with `egg.zip` then `chicken.zip` then `egg.zip`, etc. 

Just keep extracting from the zip files a few times and you'll be greeted with `egg.pdf` containing the flag.

## Flag
Flag: `wh1ch_came_f1rst?`
