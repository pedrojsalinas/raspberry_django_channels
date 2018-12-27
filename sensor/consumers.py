from channels import Group

def ws_connect(message):
    print("Someone connected.")
    path = message['path']
    print(path)

    if path == '/sensor/':
        print("Adding new user to sensor group")
        Group("sensor").add(message.reply_channel)
        message.reply_channel.send({
            "text": "You're connected to sensor group :) ",
        })
    else:
        print("Strange connector!!")

def ws_message(message):
    print("Received!! " + message['text'])


def ws_disconnect(message):
    print("Someone left us...")
    Group("sensor").discard(message.reply_channel)
    