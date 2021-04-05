# FE02
> 100pt

## Briefing
> We're sure there's a flag at `cfta-fe02.allyourbases.co` - can you find it?

## Solution
Using a website such as [CentralOps](https://centralops.net/co/), you can check the TXT DNS records:

| Name | Class | Type | Data | Time To Live |
|--------------|------|--------|------|---------|
| cfta-fe02.allyourbases.co	| IN | TXT | flag=unlimited_free_texts | 300s	(00:05:00) |

## Flag
Flag: `unlimited_free_texts`
