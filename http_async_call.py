#!/usr/bin/env python

import asyncio
import requests

async def invoke_webhook():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None, 
            requests.get, 
            'https://webhook.site/6eff2626-7938-474a-905a-04a203e4c7e5'
        )
        for i in range(3)
    ]
    for response in await asyncio.gather(*futures):
        print ('Call completion time ', response.headers['Date'], ' with X-Request-Id ', response.headers['X-Request-Id'])

loop = asyncio.get_event_loop()
loop.run_until_complete(invoke_webhook())