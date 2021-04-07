# BM03
> 250pts

## Briefing
> Download the file and find a way to get the flag.

## Solution
The provided file can be found [here](bm03.zip). Running the binary gives us this output:
```console
➜ ~ $ ./flag

 Flag:
       __       __                          _                      ____ __
  ____/ /___   / /_   __  __ ____ _ ____ _ (_)____   ____ _       / __// /_ _      __
 Error displaying rest of flag
➜ ~ $
```
Looks like the goal here is to make it print the entire flag, and not encounter that error.

Loading the binary into Ghidra shows that the main function simply calls an `output` function.
```c
int main(void)

{
  int rows;
  int cols;
  
  fflush(stdout);
  puts("\n\x1b[36m Flag:\x1b[0m");
  output(2,0x55);
  return 0;
}
```
This output function contains a condition, near the end, as follows:
```c
  if (rows < 6) {
    puts("\x1b[31m Error displaying rest of flag\x1b[0m");
  }
```
That figures. The main function is only telling it to print 2 rows, and it shows an error if that's less than 6. So, let's use gdb to call output manually with a higher number of rows.

```console
➜ ~ $ gdb ./flag
(gdb) b main
(gdb) r
(gdb) p output(6, 0x55)
       __       __                          _                      ____ __
  ____/ /___   / /_   __  __ ____ _ ____ _ (_)____   ____ _       / __// /_ _      __
 / __  // _ \ / __ \ / / / // __ `// __ `// // __ \ / __ `/      / /_ / __/| | /| / /
/ /_/ //  __// /_/ // /_/ // /_/ // /_/ // // / / // /_/ /      / __// /_  | |/ |/ /
\__,_/ \___//_.___/ \__,_/ \__, / \__, //_//_/ /_/ \__, /______/_/   \__/  |__/|__/
                          /____/ /____/           /____//_____/
$1 = void
(gdb)
```

And there's our flag.

## Flag
Flag: `debugging_ftw`
