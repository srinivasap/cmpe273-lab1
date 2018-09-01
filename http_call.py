#!/usr/bin/env python

import requests
import datetime

# Sat, 01 Sep 2018 08:20:36 GMT
for i in range(3):
    #print 'Call# ', i, ' request time ', datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S %z GMT')
    response = requests.get('https://webhook.site/6eff2626-7938-474a-905a-04a203e4c7e5')
    #print 'Call# ', i, ' completed in time ', r.headers['Date'], ' with X-Request-Id ', r.headers['X-Request-Id']
    print ('Call completion time ', response.headers['Date'], ' with X-Request-Id ', response.headers['X-Request-Id'])
