from plyer import notification
import time

title = "Ding! Ding! Ding!"
message = "It's time to have a glass of water!"

while(True):

    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 10,
        toast=False
    )
    time.sleep(3600)

