# BH01
> 500pts

## Briefing
> Download the file and find a way to get the flag.

## Solution
The provided file can be found [here](bh01.zip).
Running the binary asks for a magic word, at which point we can provide some input. After we press enter, the binary prints garbage and then asks if we understood it.
I played about with different inputs, and eventually found:
```
➜ ~ $ ./program
What is the magic word?
hhhhhhhhhhhhh
Flag: aLittLeO*���E
Did you understand that?
➜ ~ $
```
This is odd, it looks like a partial amount of the flag can be retrieved. But running the same command again doesn't always produce this output - which leads me to believe they're using a random number seeded with time.

I loaded the binary into Ghidra and found the main function, which contained a loop that looked like it might be generating the flag. After some changing of types and renaming, I was able to get the decompilation into a fairly readable state.
```c
  char input_char;
  uint iter;
  int random;
  time_t curr_time;
  byte indexes [5];
  char input [40];
  char flag [8];

  curr_time = time();
  srand((uint)curr_time);
  memset(input, 0, sizeof input);
  indexes = [0x16, 0x12, 0x0a, 0x05, 0x18];
  puts("What is the magic word?");
  fflush(stdout);
  fgets(input,0x28,stdin);
  flag = 0x103f4f6c803a05b6;
  random = rand();
  input_char = input[(int)indexes[random % 5]];
  iter = 0;
  while (iter < (int)input_char - 0x5a) {
    [ OBFUSCATED FLAG GEN ]
    if ((int)((int)input_char - 0x5a) < 0) break;
    [ OBFUSCATED FLAG GEN ]
    iter = iter + 1;
  }
  puts(flag);
  puts("Did you understand that?");
```

The binary picks a random number between 0 and 4 inclusive, and then looks up that index in the `indexes` array. It then uses *that value* to index your input, subtracts hex `5a` (decimal 90), and will iterate through the while loop that many times.

At this point, I realised why I was getting different behaviour when I put 16 or so "h"s in. If the random index picked was less than 16, then the while loop would execute `ord("h") - 90` (14) times, and checking the output of the program it looked like I was getting 14 characters of human-readable flag out!

So. I need to make that while loop run as long as possible, and I need to provide enough bytes of input so that any random index it could pick would still hit the byte of input that I provided (and not \x00, if I had not provided that much input). The input buffer is 40 long, so I wrote a quick python oneliner to generate the payload for me.

```
➜ ~ $ python -c "print('h'*40)" | ./program
What is the magic word?
Flag: aLittLeO*���E
Did you understand that?
➜ ~ $
```
Sure enough, the result each time of running that is the same and no longer affected by the time-seeded-random aspect. As I tried `i`, then `j`, as expected I got one more character of flag output at a time. I kept working my way down the ASCII table, until eventually:

```
➜ ~ $ python -c "print('~'*40)" | ./program
What is the magic word?
Flag: aLittLeObfuScatIonalCharActEr
Did you understand that?
➜ ~ $
```
Looks like we have a flag!


## Flag
Flag: `aLittLeObfuScatIonalCharActEr`
