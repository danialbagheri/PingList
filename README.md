# PingList.py

## 2020 Updates

[x] - Support for python3
[x] - Support for notification on Mac & Linux

### Author

Brantley Richbourg <brichbourg AT gmail.com>
Danial Bagheri (Python3)
#Installation and Usage

1.) Clone repo:

    git clone https://github.com/danialbagheri/PingList.git for python3
    Original git repository https://github.com/brichbourg/PingList.git Python2 using socket library

2.) Edit ips.txt to populate with your list of random IP addresses you want to test.

    10.10.1.10
    10.10.1.20
    10.20.30.40
    ...
    10.254.254.1

3.) Run script

    sudo python3 pinglist.py ips.txt

## Notes

This script uses a variation of the Python Ping script (http://www.g-loaded.eu/2009/10/30/python-ping/). This code is included in this repo and is imported by PingList.py. The use of this script requires running PingList.py as root, hence the reason to run with sudo.

## Python3

Python 3 is much more simplified and all pureping.py file is removed as the project no longer requires socket. I have tested it on UNIX/MAC and it should also work fine on Linux systems.

## Notification

Simply create a cronjob like the example below:

```python
0 */3 * * * /usr/bin/python3 <FULL PATH>/PingList/pinglist.py ips.txt
* * * * * /usr/bin/python3 <FULL PATH>/PingList/pinglist.py "<FULL PATH>/PingList/ips.txt" > /tmp/out.txt >> /tmp/out.txt
```

above will run every 3 hours to check the available systems and if there is any issue you will get a notification on your notification baar.
Also among the IPS you can enter websites.
make sure your python file executable by using `chmod a+x pinglist.py`
in case if there is any issue, you can check your logs by typing `mail` in OSX terminal.
