import openai
import discord
from discord.ext import commands

token = 'MTE3OTA2MzQwMTY3OTQ0MTk5MA.GMCbkW.9DsdHOhWVqw-f3HvIiwDsjB6jnVavZ3Nq2kLiw'
openai.api_key = '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'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)



def ask_gpt(question):
    messages = [
        {"role": "system", "content": "You’re a kind helpful assistant"}
    ]
    content = question
    messages.append({"role": "user", "content": content})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        api_key='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'
    )
    chat_response = completion.choices[0].message.content
    return chat_response


@bot.event
async def on_message(ctx):
    if int(ctx.channel.id) == 1179345455583330314:
        if ctx.author != bot.user and ctx.content[0:4] == 'гпт ':
            await ctx.reply(ask_gpt(ctx.content[4:-1])) # отправляет ответ:

bot.run(token)

