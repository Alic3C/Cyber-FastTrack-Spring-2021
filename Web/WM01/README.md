# WM01
> 250pts

## Briefing
> View the page at https://cfta-wm01.allyourbases.co and try to get the flag.

## Solution
Ok so starting off, we notice this comment in the `/assets/js/site.js` file:   
`// Image slideshow. Moved in from /new-images when each is finalised`   

Going to `https://cfta-wm01.allyourbases.co/new-images/`, and examining the images, we use super guessing skills to hone in on this one:    
<img src="5.jpg" width="350" >   

hmmm, how strange- perhaps there is a mii-home directory?    
https://cfta-wm01.allyourbases.co/mii-home/ Gosh! there is!

Now, an email and password. 

Firstly, the email: It can be seen on the first webpage at the bottom, where Rupert asks for enquiries. 
```
Need some freelance photography? Contact me at:
rupert@get-vizual.med.ia 
```

Now for the password. After trying various arbitrary strings, we get a password hint! 
`Hint: My fav city`

Now, going back to the main webpage, if we inspect element at the images, we see this:    
`<img src="assets/images/IMG_20201211_1642.jpg" alt="My office, guess my fav city!" id="img_4" style="opacity: 0;">`   

Well well, looking at the image, Rupert has a New York pillowcase.   

After some trial and error, we are able to log in with `rupert@get-vizual.med.ia` and password `newyork`.   

Now, Rupert's [home security feed](https://cfta-wm01.allyourbases.co/mii-home/security-camera/feed/), how exciting.

Navigating to `office`, we see the wifi password left in plain view. And alas, that is our flag. 

## Flag
Flag: `XGHEV7HGEV`
