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

## James Lyne's Spoiler Video
A day into the competition, a spoiler video was emailed out to all competitors:

> To help you make a start, watch Cyber FastTrack creator, James Lyne, [talk you through one of the first challenges - WE02](https://vimeo.com/533467285/d508b2bf61).

## Flag
Flag: `Shhh_robot_you_said_too_much!`
