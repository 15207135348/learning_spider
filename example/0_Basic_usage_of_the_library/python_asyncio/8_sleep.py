#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8_sleep.py
@Time    :   2020-11-09
@Author  :   EvilRecluse
@Contact :   https://github.com/RecluseXU
@Desc    :   

    coroutine asyncio.sleep(delay, result=None, *, loop=None)
        阻塞 delay 指定的秒数。
        如果指定了 result，则当协程完成时将其返回给调用者。
        sleep() 总是会挂起当前任务，以允许其他任务运行。
'''

# here put the import lib
import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())
