# BM01
> 250pts

## Briefing
> Download the file and find a way to get the flag.

## Solution
The provided file can be found [here](bm01.zip).   

When running the program, we get asked for the password.    
```
$ ./program
Какой пароль？<-- what's the password?
> password
неверный <-- wrong
```   

To find the password, run the program through GDB using `gdb ./program`.   
From `info func`, we can see there is a main function so set a breakpoint by doing `b main`.   

Stepping through main, we see that our input is being compared to a string here:   
```
0x55555555482f <main+101>    call   strcmp@plt <strcmp@plt>
        s1: 0x5555555549c8 ◂— 0xbed0bbd0bed0bcd0
        s2: 0x7fffffffe010 ◂— 0xa61616161 /* 'aaaa\n' */
```   

Where 'aaaa' is my current input. 
Now, all we need to do is view the string at memory address `0x5555555549c8`:   
```
pwndbg> x/s 0x5555555549c8
0x5555555549c8: "молоток123\n
```

And there we go, we have the password!

```
$ ./program
Какой пароль？
> молоток123
верный!

флаг: wh1te%BluE$R3d
```   


## Flag
Flag: `wh1te%BluE$R3d`
