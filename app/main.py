
import discord
from discord.ui import Button, View
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('TOKEN')


def cyb_detector(text):
    pass

def spam_detector(text):
    pass



class PrimaryButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.primary)
    
    async def callback(self, interaction):
        await interaction.response.send_message(content="Type of cyberbullying:")


class SuccessButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.success)


class DangerButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.danger)




class MyView(View):
    @discord.ui.button(label="Click here!", style=discord.ButtonStyle.green)
    async def button_callback(self, button, interaction):
        button1 = [x for x in self.children if x.custom_id == "danger"][0]
        button1.disabled = True
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="Click here!", style=discord.ButtonStyle.red, custom_id="danger")
    async def danger_button_callback(self, button, interaction):
        await interaction.response.edit_message(view=self)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("$test"):

        is_cyberbullying = True #cyb_detector(message.content)
        is_spam = True #spam_detector(message.content)

        button1, button2 = SuccessButton("Yes"), DangerButton("No")
        button = PrimaryButton("View Details")
        view = View()

        if is_cyberbullying and is_spam:
            view.add_item(button)
            await message.channel.send(f"{message.author.mention} This is both a spam and cyberbullying message!!!", reference=message, view=view)
        
        elif is_cyberbullying:
            view.add_item(button)
            await message.channel.send(f"{message.author.mention} This is a cyberbullying message!!!", reference=message, view=view)
        
        elif is_spam:  
            await message.channel.send(f"{message.author.mention} Please, don't spam the channel!!!", reference=message, view=view)


        async def button1_callback(interaction):
            button1.disabled, button2.disabled = True, True
            await message.channel.send("The malicious message was successfully deleted!", reference=message)
            view.clear_items()
            await interaction.response.edit_message(view=view)
            await message.delete()

        async def button2_callback(interaction):
            button1.disabled, button2.disabled = True, True
            await message.channel.send("Deletion canceled.\nWarning! This malicious message may affect emotionally other users.", reference=message)
            view.clear_items()
            await interaction.response.edit_message(view=view)
        
            
        button1.callback, button2.callback = button1_callback, button2_callback


        if is_spam and not is_cyberbullying:
            await message.channel.send("The malicious message was successfully deleted!", reference=message)
            await message.delete()
            return

        view = View()
        view.add_item(button1)
        view.add_item(button2)
        await message.channel.send(f"{message.author.mention} I recommend you to delete this upsetting content. Continue deleting?", reference=message, view=view)


@bot.event
async def on_connect():
    print("Bot connected to the server...")

bot.run(TOKEN)
