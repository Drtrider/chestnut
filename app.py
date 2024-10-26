# This example requires the 'message_content' intent.

import discord
import os
import random

DISCORD_BOT_API_KEY = os.getenv("DISCORD_BOT_API_KEY")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def fetch_fortune(question):
    """Will return a string given in a question."""

    options = [
        "Yes.",
        "No.",
        "Maybe.",
        "I'm not really sure.",
        "The ether says yes.",
        "Does a duck's dick drag grass?",
        "Does a bear shit in the woods?",
        "Weird, I'm getting some sort of interference. Try again.",
        "I've consulted with the gods of the beach, they say yes.",
        "The tides say no.",
        "Ask again when the moon is full.",
        "Only if you swim three laps around the reef.",
        "The answer lies beneath the sand... dig deep.",
        "The ocean never lies. Yes, but only on Wednesdays.",
        "The seaweed sways... it’s a maybe.",
        "Only the kraken knows, and it’s not telling.",
        "Whale sounds indicate a strong maybe.",
        "Shell yeah!",
        "Mermaids say it’s a go!",
        "The answer drifted out to sea. Try again.",
        "If the seagull squawks, it's a yes.",
        "Only Poseidon can answer that... I’m just a shell.",
        "Hold your breath and count to ten... then maybe.",
        "Surf's up! That means yes.",
        "Find a jellyfish, then ask again.",
        "It’s high tide for a yes.",
        "Low tide for a no.",
        "The salt in the water says no.",
        "If the clam opens, then yes. Otherwise... no."
    ]

    options_length = len(options)
    random_number = random.randint(1, options_length)
    fortune = "🐚 " "'" + options[random_number] + "'" 
    return fortune


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$conch'):
        fortune = fetch_fortune("Some question")
        await message.channel.send(fortune)

    if message.content.startswith('$test'):
        print(client)
        await message.channel.send(f"Printing client data.")


client.run(DISCORD_BOT_API_KEY)
