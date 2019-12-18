# ExchangeRate-USD--Python

This project aims to see one specific element of exchange rates(USD) based EUR and It will send an email according to currency to user.

Add those libraries:
```
import requests
import json
import smtplib
import time
```

request = allows you to send HTTP request.

json = is text, written with JavaScript object notation and a syntax for storing and exchanging data.

smtplib = defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener            daemon.

Here is the url for exchange rates:

```
url = "https://api.exchangeratesapi.io/latest"
```

