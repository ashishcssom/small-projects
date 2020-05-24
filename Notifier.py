# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:12:18 2020

@author: imash
"""

import time         
from plyer import notification
from datetime import datetime
def Notifier():
    while True:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        notification.notify(
            title="Please Drink water now!",
            message="The National Academic of Science, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cupps (2.7 liters) of fluids a day for woman.",
            app_icon="./DrinkingWater.ico",
            timeout=5
        )
        print(f"Notification timing {now}")
        time.sleep(60*60)    
if __name__=="__main__":
    Notifier()

