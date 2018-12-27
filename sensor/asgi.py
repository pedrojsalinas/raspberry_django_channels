import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sensor.settings")
channel_layer = chennals.asgi.get_channel_layer()
