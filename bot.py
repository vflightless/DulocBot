import disnake
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

#       API
load_dotenv()
discordKey = os.getenv('KEY')

#       Image List
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(script_dir, 'images'))

images = os.listdir()
imgList = []
lastSent = timedelta(minutes=1)

for image in images:
    imgName = image.split('.')[0]
    imgList.append([imgName, image, datetime.now()])
# print(imgList)


#       Discord Section
intents = disnake.Intents.default()
intents.members = True
intents.message_content = True

client = disnake.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for img in imgList:
        imageName = img[0]
        imageFile = img[1]
        imageLast = img[2]
        print('Message parse: ' + imageName + ', ' + imageFile + ', ' + str(imageLast))

        
        if message.content.find(imageName) != -1 and (datetime.now() - imageLast) >= lastSent:
            img[2] = datetime.now()
            await message.channel.send(file=disnake.File(imageFile))

client.run(discordKey)