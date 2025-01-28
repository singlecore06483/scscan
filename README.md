SCscan
-

this tool is a website and system scanner.

it can scan a website and shows you the informations about the site.

scans the IP for open and close ports.

scan with shodan, (but put your Shodan API in the code line 42!).

What OS this tool support ?
-

This tool supports linux,macOS and windows.

How to use this tool ?
-

This tool supports python3.

first you need to install libarys :

```
pip install -r requirements.txt
```

then type this to see help menu of tool :

```
python scscan.py
```

Example Commands :
-

```
python scscan.py -h
python scscan.py --help
python scscan.py -web-scan=https://example.com
python scscan.py -ip-scan=192.168.1.1
python scscan.py -shodan-scan=192.168.1.1
python scscan.py -find-info=192.168.1.1
python scscan.py -web-scan=https://example.com -wordlist-url=urllist.txt
python scscan.py -ip-scan=192.168.1.1 -p=22,80
```

This tool just for `Educational Purposes` only!

---------------------------------------------------------------------------

```
Malevolent code crawled through cybernetic veins,
consuming every digital defence mechanism In Darkness,
Alone.
No system is safe.
--single core--
```
