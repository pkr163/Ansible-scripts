#!/usr/bin/env python

import requests
import sys

app_host = "{{ app_host }}"
app_port = "{{ app_port }}"
app_healthcheck_url = "{{ app_healthcheck_url }}"

web_host = "{{ web_host }}"
web_port = "{{ web_port }}"
web_healthcheck_url = "{{ web_healthcheck_url }}"

def check_app_status():
    try:
        response = requests.get("http://{}:{}/{}".format(app_host, app_port, app_healthcheck_url))
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def check_web_status():
    try:
        response = requests.get("http://{}:{}/{}".format(web_host, web_port, web_healthcheck_url))
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

if check_app_status() and check_web_status():
    sys.exit(0)
else:
    sys.exit(1)
