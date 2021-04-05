# WE02
> 100pt

## Briefing
> View the page at https://cfta-we02.allyourbases.co and try to get the flag.

## Solution
A simple visit to [/robots.txt](https://cfta-we02.allyourbases.co/robots.txt) gives us the following output:

```
User-agent: *

Allow: /
Disallow: /4ext6b6.html
```

If we visit [/4ext6b6.html](https://cfta-we02.allyourbases.co/4ext6b6.html), we get the following output:

![Flag: Shhh_robot_you_said_too_much!](4ext6b6.PNG)

## Flag
Flag: `Shhh_robot_you_said_too_much!`
