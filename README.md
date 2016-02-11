# Telegram LMGTFY_bot
### Let Me Google That For You Bot

Bot available at [telegram.me/lmgtfy_bot](http://telegram.me/lmgtfy_bot)

## Usage

Be sure to create the file `lmgtfy_bot.conf` and set it as follows:

```
[DEFAULTS]
bot_token = 1234567890EXAMPLE0987654321
google_client = 1234567890EXAMPLE0987654321
```

Then run:

```
$ pip install -r requirements.txt
$ python3 lmgfy_bot.py
```

## Need help

I tried to add inline queries to this bot. It worked, but the VM's load would eventually get really high. So I removed the functionality.

My last attempt is commented on the code. Pull requests are welcome!
