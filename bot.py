import disnake
import os
import glob
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv('KEY')

path = "./images/"  # change this to the path of your directory
file_extension = "*.png"    # change this to the file extension you want to load
files = glob.glob(os.path.join(path, file_extension))
print(files)

class MyClient(disnake.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')



client = MyClient()
client.run(KEY)
