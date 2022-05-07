import discord
from discord.ui import Button, View
import os
from dotenv import load_dotenv
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('TOKEN')

# change the generated URL here
URL = "http://9e7b-35-199-179-209.ngrok.io"


class PrimaryButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.primary)


class SuccessButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.success)


class DangerButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.danger)

cyb_count, spam_count = 0, 0

@bot.event
async def on_message(message):
    global cyb_count, spam_count, cyb_spam_count
    
    if message.author != bot.user:

        data_json = {"text": message.content}
        prediction = requests.get(URL, json=data_json).json()
        
        is_cyberbullying = int(prediction["cyberbullying"])
        is_spam = int(prediction["spam"])

        button1, button2, button3 = SuccessButton("Yes"), DangerButton("No"), PrimaryButton("View Details")
        view = View()

        if is_spam:  
            spam_count += 1
            await message.channel.send(
                f"{message.author.mention} Please, don't spam the channel!!!", 
                reference=message
            )
            await message.channel.send("The malicious message was successfully deleted!", reference=message)
            await message.delete()
            return
        
        elif is_cyberbullying:
            cyb_count += 1
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            await message.channel.send(
                f"{message.author.mention} This is a cyberbullying message!!!" + 
                f"\nI recommend you to delete this upsetting content. Continue deleting?", 
                reference=message, 
                view=view
            )

        else:
            await message.channel.send(prediction["chatbot_response"])
            return


        async def button1_callback(interaction):
            await message.channel.send("The malicious message was successfully deleted!", reference=message)
            button1.disabled, button2.disabled,  button3.disabled = True, True, True
            view.clear_items()
            await interaction.response.edit_message(view=view)
            await message.delete()

        async def button2_callback(interaction):
            await message.channel.send("Deletion canceled.\nWarning! This malicious message may affect emotionally other users.", reference=message)
            button2.disabled = True
            await interaction.response.edit_message(view=view)
        
        async def button3_callback(interaction):
            embed = discord.Embed(
                title="Type of cyberbullying:", 
                url="https://www.stopbullying.gov/cyberbullying/what-is-it", 
                description="Your message can be classified into following types (probabilities):", 
                color=discord.Color.blue())
            embed.set_thumbnail(url="https://media.istockphoto.com/vectors/cyber-bullying-people-vector-illustration-cartoon-flat-sad-young-vector-id1264371767?k=20&m=1264371767&s=612x612&w=0&h=H2_baTw3eW2rLoc-GcFubrasUDTJ5Ah5H5AcSsyW4rQ=")
            embed.add_field(name="Age", value=prediction["cyberbull_type"]['age'], inline=True)
            embed.add_field(name="Ethnicity", value=prediction["cyberbull_type"]['ethnicity'], inline=True)
            embed.add_field(name="Gender", value=prediction["cyberbull_type"]['gender'], inline=True)
            embed.add_field(name="Religion", value=prediction["cyberbull_type"]['religion'], inline=True)
            button3.disabled = True
            await message.channel.send(
                reference=message,
                embed=embed
            )
            await interaction.response.edit_message(view=view)
        
            
        button1.callback, button2.callback, button3.callback = button1_callback, button2_callback, button3_callback

        
        channel = bot.get_channel(971155287694274650)
        if cyb_count + spam_count == 3:
            await channel.send(f"{message.author.mention} has already sent 3 malicious messages:"+
            f"\n{cyb_count} cyberbullying\n{spam_count} spam")
            cyb_count, spam_count = 0, 0


@bot.event
async def on_connect():
    print("Bot connected to the server...")

bot.run(TOKEN)
