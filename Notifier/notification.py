from plyer import notification as notif
import time
import threading

app_name = 'Notifier'

water_title = 'Water Reminder'
water_message = 'Take a sip of water!'

stretch_title = 'Stretch Reminder'
stretch_message = 'Stand up and stretch for a bit!'

def water():
    while True:
        time.sleep(600)
        notif.notify(water_title, water_message, app_name)


def stretch():
    while True:
        time.sleep(1800)
        notif.notify(stretch_title, stretch_message, app_name)

threads = []

t = threading.Thread(target=water)
t.start()
threads.append(t)

t2 = threading.Thread(target=stretch)
t2.start()
threads.append(t2)

for thread in threads:
    thread.join()