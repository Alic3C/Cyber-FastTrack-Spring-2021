# WH02
> 500pts

## Briefing
> Access the site at https://cfta-wh02.allyourbases.co and find a way to get the flag.

## Solution
1. Use DIRB to find the Git directory - `dirb https://cfta-wh02.allyourbases.co`
   * This shows  `https://cfta-wh02.allyourbases.co/.git/HEAD`
2. `https://cfta-wh02.allyourbases.co/.git/` is indexable
3. Use `wget -r https://cfta-wh02.allyourbases.co/.git/` to download the whole Git directory
4. Open the directory in a Git client
5. Look at `setup.sh` that was commited on `7/3/2021`:

```sh
#!/bin/bash

FLAG="giTisAGreat_ResoURCe8337"

cd build
cp ../sitedata.zip sitedata.zip
unzip sitedata.zip
```

## Flag
Flag: `giTisAGreat_ResoURCe8337`
