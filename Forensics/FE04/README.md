# FE04
> 100pt

## Briefing
> Download the file and filter down to the username according to criteria below.

> The username you are looking for has `x` as the 3rd character, followed immediately by a number from `2` to `6`, it has a `Z` character in it and the last character is `S`.

> When you have the username, submit it as the flag.

## Solution
The provided file can be found [here](fe04.zip).

Grep on steriods, let's break it down step by step.

We have the criteria of:
- has x as the 3rd character
- a number from 2-6 immediately after
- contains the character `Z`
- finishes off with `S`

You can do this in many ways, but the easiest would likely be grep + regex to filter:

`grep -P '^..x[2-6].*Z.*S$' 50k-users.txt`

## Flag
Flag: `YXx52hsi3ZQ5b9rS`
