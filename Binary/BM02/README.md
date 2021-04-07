# BM02
> 250pts

## Briefing
> Download the file and find a way to get the flag.

## Solution
The provided file can be found [here](bm02.zip).
Running the binary simply echoes the string `I'm not going to make it that easy for you.` and immediately exits. I tried lots of characters as an argument, and that didn't yield anything interesting either. It doesn't look like buffer overflow is the answer here.

After loading the binary into Ghidra, sure enough the main function is very bare.
```c
undefined8 main(void)

{
  puts("I\'m not going to make it that easy for you.");
  return 0;
}
```

However, the very function before that is one called `printFlag`!
```c
void printFlag(int param_1)

{
  byte bVar1;
  byte bVar2;
  long in_FS_OFFSET;
  uint local_2c;
  byte local_28 [24];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  if (param_1 == 0x539) {
    local_28[0] = 0x15;
    local_28[1] = 0x70;
    local_28[2] = 0xe5;
    local_28[3] = 100;
    .
    .
    .
```

Let's try running it by using the syntax `p function()` in gdb (after `b main` and `r`).
```console
(gdb) p printFlag()
'printFlag' has unknown return type; cast the call to its declared return type
(gdb)
```
Ok, looks like we need to cast it. Back in Ghidra, that function doesn't return anything, so I just cast to void.
```console
(gdb) p (void)printFlag()
$1 = void
(gdb)
```
Hmmm, it isn't printing anything. I then remembered that the function takes a parameter `param_1`, and then there's a check to see if it's exactly hex `539` (1337 in decimal, leet). Supplying that as the function argument yields the flag.
```console
(gdb) p (void)printFlag(0x539)
Flag: patchItFixIt
$3 = void
(gdb)
```

## Flag
Flag: `patchItFixIt`
