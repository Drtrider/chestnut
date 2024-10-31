# Import all the things
import discord
import os
import random
import requests
import json

DISCORD_BOT_API_KEY = os.getenv("DISCORD_BOT_API_KEY")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def ask_conch(question):
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
        "If the clam opens, then yes. Otherwise... no.",
        "Do starfish wear socks? No. That's your answer too.",
        "Are you serious? Even the crabs are laughing.",
        "Sure, if you think getting pinched by a crab is fun.",
        "I've seen sea cucumbers make better decisions. It's a no.",
        "Maybe, but only if you enjoy salty disappointment.",
        "The shells have spoken... they said something rude. It's a no.",
        "Yes, but only after you polish every barnacle.",
        "Nope. Not today, not tomorrow, not ever.",
        "The answer is blowing in the sea breeze. And it smells like regret.",
        "The fish say yes. But they’re kinda gullible, so take that as you will.",
        "Yeah, and dolphins can fly. Wait, they can't? Exactly.",
        "If you’re asking, you probably already know it’s a bad idea.",
        "The ocean just rolled its eyes at you. It's a hard no.",
        "You'd have better luck asking a jellyfish for relationship advice.",
        "Do sharks swim backwards? No. There's your answer.",
        "Let me consult the seagulls... Oh, they stole my fries. It’s a no.",
        "The tide came in, looked at your question, and went back out. It's a maybe.",
        "Ask the sea again, but bring snacks next time. The answer's hangry.",
        "The ocean waves are indifferent. It's up to you... but probably a mistake.",
        "I've heard coral come up with better ideas than this. Try something else."
    ]

    options_length = len(options)
    random_number = random.randint(1, options_length)
    fortune = "🐚  " "'*" + options[random_number] + "*'"
    return fortune


def get_advice(query):
    """Fetcehes some random advice based on a single word query."""
    if len(query.split()) > 1:
        raise Exception(
            "Too many words in query! Only a single word can be provided.")
    else:
        # Call the advice API
        api_url = f"https://api.adviceslip.com/advice/search/{query}"
        payload = {}
        headers = {}
        api_response = requests.request(
            "GET", api_url, headers=headers, data=payload)

        # Check if some advice was found, if it's not. Raise exception
        response_json = json.loads(api_response.text)
        count_of_results = int(response_json.get(("total_results"), 0))
        if count_of_results == 0:
            raise Exception(f"Sorry, I have no advice for '{query}.'")
        else:
            # Select a random advice returned
            rand_int = random.randint(0, int(response_json['total_results'])-1)
            selected_advice = response_json["slips"][rand_int]["advice"]
            return selected_advice


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$conch'):
        fortune = ask_conch("Some question")
        await message.channel.send(fortune)

    if message.content.startswith('$test'):
        print(client)
        await message.channel.send(f"Printing client data.")

    if message.content.startswith('$advice'):
        try:
            query = message.content.strip("$advice ")
            advice = get_advice(query)
            await message.channel.send(advice)
        except Exception as e:
            print(f"[ERROR] There was an error getting some advice:\n{e}")
            await message.channel.send(f"{e}")


client.run(DISCORD_BOT_API_KEY)
