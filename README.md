# secheaders

![alt text](https://github.com/gotr00t0day/secheaders/blob/main/security-http-headers.png)

# INSTALLATION

```bash

git clone https://github.com/gotr00t0day/secheaders.git

cd secheaders

pip3 install -r requirements.txt

```

# USAGE 

```
usage: securityheaders.py [-h] [-hs headers [headers ...]] [-t domain.com]

optional arguments:
  -h, --help            show this help message and exit
  -hs headers [headers ...], --headers headers [headers ...]
                        add multiple headers
  -t domain.com, --target domain.com
                        scan for security headers                               
```

# EXAMPLE

Scan a target for missing security headers in a domain / site.
```
python3 secheaders.py -t https://www.yahoo.com --headers Content-Security-Policy
