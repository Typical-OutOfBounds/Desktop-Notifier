from plyer import notification as notif
import time
import threading

app_name = 'Notifier'

water_title = 'Water Reminder'
water_message = 'Take a sip of water!'

stretch_title = 'Stretch Reminder'
stretch_message = 'Stand up and stretch for a bit!'

break_title = 'Break Reminder'
break_message = 'Walk away for a few minutes!'

def water():
    while True:
        time.sleep(5)
        notif.notify(water_title, water_message, app_name)


def stretch():
    while True:
        time.sleep(10)
        notif.notify(stretch_title, stretch_message, app_name)

def take_break():
    while True:
        time.sleep(60*120)
        notif.notify(break_title, break_message, app_name)

threads = []

reminders = [water, stretch, take_break]
for x in reminders:
    temp = threading.Thread(target=x)
    temp.start()
    threads.append(temp)

for thread in threads:
    thread.join()
