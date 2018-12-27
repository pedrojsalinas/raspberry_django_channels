from channels import Group
# from channels.consumer import AsyncConsumer
import asyncio

# class HabitacionesConsumer(AsyncConsumer):
#     async def websocket_connect(self,event):
#         print("conectado", event)
#         await self.send({
#             "type": "websocket.accept"
#         })

async def ws_connect(message):
    print("Someone connected.")
    path = message['path']
    print(path)

    if path == '/sensor/':
        print("Adding new user to sensor group")
        Group("sensor").add(message.reply_channel)
        await message.reply_channel.send({
            "text": "You're connected to sensor group :) ",
        })
    else:
        print("Strange connector!!")

async def ws_message(message):
    print("Received!! " + message['text'])


async def ws_disconnect(message):
    print("Someone left us...")
    Group("sensor").discard(message.reply_channel)
