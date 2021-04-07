# WM02
> 250pts

## Briefing
> View the page at https://cfta-wm02.allyourbases.co and try to get the flag.

## Solution
Notice that the page is constantly checking the values in HTML of your username, userid and userref - because when you change them, the content of the page changes. There is JavaScript being run - which defines a custom hashing function and uses it to check that your userref matches your username and userid. The check that it does is:
```js
if (get("user").dataset['userRef'] ===
    hash(get("user").dataset['userName'] + "_" + get("user").dataset['userId']).split("").reverse().join("")) {
```
Let's try to become the admin. We can guess that the username would be `admin`, and the userid probably `0`. Substituting that into the above, we can calculate that our userref must be:
```js
hash("admin" + "_" + "0").split("").reverse().join("");
```
Running this in the console returns a hash `31f7934415f3d31c64359bd51d378177` that will match the in-built check for admin, 0, if we set our userref to that hash. Thus, going into the HTML and changing:
```html
<h1 id="user" data-user-name="henrywhite" data-user-id="152874"
    data-user-ref="c897cd08c105c0eff5ca296f56eaa4ab">Hello henrywhite!</h1>
```
to
```html
<h1 id="user" data-user-name="admin" data-user-id="0"
    data-user-ref="31f7934415f3d31c64359bd51d378177">Hello henrywhite!</h1>
```
Gives us the flag.

## Flag
Flag: `epoch_wizard`
