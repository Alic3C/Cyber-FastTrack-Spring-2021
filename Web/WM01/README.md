# WM01
> 250pts

## Briefing
> View the page at https://cfta-wm01.allyourbases.co and try to get the flag.

## Solution
Head straight to the *source* (literally)! Go to [assets/js/site.js](https://cfta-wm01.allyourbases.co/assets/js/site.js) and we can find a comment at the top of the JS script.

`// Image slideshow. Moved in from /new-images when each is finalised`

Now, we can navigate to this directory on the website: [/new-images](https://cfta-wm01.allyourbases.co/new-images/)

### Now, there's something particularly fishy about the 5th image.
![image](https://user-images.githubusercontent.com/69332964/113920880-5a9b4f00-97b3-11eb-96e0-bdcb5a02a256.png)

> The `Date Modified` is `5/11/2020` instead of `4/11/2020` like the others. 

Browsing to the image gives us this:
![image](https://user-images.githubusercontent.com/69332964/113921128-a1894480-97b3-11eb-8d1f-c1cdaa0305d5.png)

> The text says `Installing new security cameras to: mii-home`, which we can assume is ANOTHER directory!

### Logging In
Let's go to [/mii-home](https://cfta-wm01.allyourbases.co/mii-home/), where we find a login portal to access security cameras...
As usual, we head to the source.

Below, we have `login.js`, which is lightly obfuscated.

```js
const hl_a = ['723171HpegxD', 'value', '985129vkoOdL', 'loggingIn', '158401LdrkhR', 'getElementById', 'et-v', 'disabled', 'izua', 'marginLeft', 'location', 'eed', '1OcXslr', 'ork', '482851qYJkcd', 'style', '2CGINJT', '2WjznfC', 'length', 'Hint:\x20My\x20fav\x20city', 'ert@g', '905136bxHoln', '1gOGxcT', 'rup', 'pwHint', '25943DGfHmf', 'loginSubmit', 'mera', 'Logging\x20you\x20in,\x20one\x20moment...', '4294452vlvLJt', 'l.med.ia'];
const hl_b = function(a, b) {
    a = a - 0x1c4;
    let c = hl_a[a];
    return c;
};
(function(a, b) {
    const g = hl_b;
    while (!![]) {
        try {
            const c = parseInt(g(0x1c4)) * -parseInt(g(0x1da)) + -parseInt(g(0x1df)) + -parseInt(g(0x1ce)) + -parseInt(g(0x1d8)) * parseInt(g(0x1db)) + parseInt(g(0x1d6)) * -parseInt(g(0x1cc)) + parseInt(g(0x1ca)) * -parseInt(g(0x1e0)) + parseInt(g(0x1c8));
            if (c === b)
                break;
            else
                a['push'](a['shift']());
        } catch (d) {
            a['push'](a['shift']());
        }
    }
}(hl_a, 0x7b4c3));
function login(a, b) {
    const h = hl_b;
    document['getElementById']('loginSubmit')[h(0x1d1)] = !![];
    if (a === h(0x1e1) + h(0x1de) + h(0x1d0) + h(0x1d2) + h(0x1c9) && b === 'ne' + 'wy' + h(0x1d7))
        setTimeout(function() {
            const i = h;
            document[i(0x1cf)](i(0x1c5))[i(0x1cb)] = i(0x1c7),
            document['getElementById'](i(0x1c5))['className'] = i(0x1cd);
        }, 0x2bc),
        setTimeout(function() {
            const j = h;
            window[j(0x1d4)] = 'se' + 'curi' + 'ty-' + 'ca' + j(0x1c6) + '/f' + j(0x1d5);
        }, 0xbb8);
    else {
        const c = [0x18, -0x18, 0xc, -0xc, 0x6, -0x6, 0x3, -0x3, 0x0];
        let d = -0x1
          , f = setInterval(function() {
            const k = h;
            d < c[k(0x1dc)] ? (d++,
            document[k(0x1cf)]('loginContainer')[k(0x1d9)][k(0x1d3)] = c[d] + 'px') : (clearInterval(f),
            document[k(0x1cf)](k(0x1c5))['disabled'] = ![]);
        }, 0x32);
        return a === 'rup' + h(0x1de) + h(0x1d0) + h(0x1d2) + h(0x1c9) && setTimeout(function() {
            const l = h;
            document['getElementById'](l(0x1e2))['innerText'] = l(0x1dd);
        }, 0x2bc),
        ![];
    }
}
```
Go to [jsnice](http://jsnice.org/) to make it slightly more readable, and you get:

```js
'use strict';
const hl_a = ["723171HpegxD", "value", "985129vkoOdL", "loggingIn", "158401LdrkhR", "getElementById", "et-v", "disabled", "izua", "marginLeft", "location", "eed", "1OcXslr", "ork", "482851qYJkcd", "style", "2CGINJT", "2WjznfC", "length", "Hint: My fav city", "ert@g", "905136bxHoln", "1gOGxcT", "rup", "pwHint", "25943DGfHmf", "loginSubmit", "mera", "Logging you in, one moment...", "4294452vlvLJt", "l.med.ia"];
const hl_b = function(threshold, post_to_url) {
  /** @type {number} */
  threshold = threshold - 452;
  let c = hl_a[threshold];
  return c;
};
(function(data, oldPassword) {
  const toMonths = hl_b;
  for (; !![];) {
    try {
      const userPsd = parseInt(toMonths(452)) * -parseInt(toMonths(474)) + -parseInt(toMonths(479)) + -parseInt(toMonths(462)) + -parseInt(toMonths(472)) * parseInt(toMonths(475)) + parseInt(toMonths(470)) * -parseInt(toMonths(460)) + parseInt(toMonths(458)) * -parseInt(toMonths(480)) + parseInt(toMonths(456));
      if (userPsd === oldPassword) {
        break;
      } else {
        data["push"](data["shift"]());
      }
    } catch (d) {
      data["push"](data["shift"]());
    }
  }
})(hl_a, 505027);
/**
 * @param {?} options
 * @param {?} callback
 * @return {?}
 */
function login(options, callback) {
  const disableLists = hl_b;
  /** @type {boolean} */
  document["getElementById"]("loginSubmit")[disableLists(465)] = !![];
  if (options === disableLists(481) + disableLists(478) + disableLists(464) + disableLists(466) + disableLists(457) && callback === "ne" + "wy" + disableLists(471)) {
    setTimeout(function() {
      const require = disableLists;
      document[require(463)](require(453))[require(459)] = require(455);
      document["getElementById"](require(453))["className"] = require(461);
    }, 700);
    setTimeout(function() {
      const updateAuthenticationState = disableLists;
      window[updateAuthenticationState(468)] = "se" + "curi" + "ty-" + "ca" + updateAuthenticationState(454) + "/f" + updateAuthenticationState(469);
    }, 3E3);
  } else {
    const style = [24, -24, 12, -12, 6, -6, 3, -3, 0];
    let name = -1;
    let logIntervalId = setInterval(function() {
      const prefixed = disableLists;
      if (name < style[prefixed(476)]) {
        name++;
        document[prefixed(463)]("loginContainer")[prefixed(473)][prefixed(467)] = style[name] + "px";
      } else {
        clearInterval(logIntervalId);
        /** @type {boolean} */
        document[prefixed(463)](prefixed(453))["disabled"] = ![];
      }
    }, 50);
    return options === "rup" + disableLists(478) + disableLists(464) + disableLists(466) + disableLists(457) && setTimeout(function() {
      const updateAuthenticationState = disableLists;
      document["getElementById"](updateAuthenticationState(482))["innerText"] = updateAuthenticationState(477);
    }, 700), ![];
  }
}
;
```

Go ahead and **dump the entire contents into the console**. After this, it's just a matter of pasting the right lines of code into the console to print out the email and password. [Here](https://drive.google.com/file/d/1gKGNsAN882_VuTEIMp3jjknOoHwQkmVl/view?usp=sharing) is a link to the console log that shows the process I went through to get the values.
> **Hint:** it's the expressions where there's an `&&` comparison.

**Email**: `rupert@get-vizual.med.ia`

**Password**: `newyork`

> **Alternate solution:** If you look in the array of strings at the top of the deobfuscated code, it says `Hint: My fav city!` and has parts of "newyork" in it. The email can also be found on the main page. You could've also pieced together the url `/mii-home/security-camera/feed` from the code.

Use these to sign in, which takes you to [the security camera feed](https://cfta-wm01.allyourbases.co/mii-home/security-camera/feed/)

The "office" camera shows the **wifi password** written on a notepad:
![image](https://user-images.githubusercontent.com/69332964/113934421-ba015b00-97c3-11eb-92d9-59314f1f1e3a.png)

## Flag
Flag: `XGHEV7HGEV`
