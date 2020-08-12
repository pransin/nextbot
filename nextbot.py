import discord
from discord.ext import commands

# Loads the bot token from secrets file
secret = open('secrets.txt', "r")
token = secret.readline()
secret.close()

client = commands.Bot(command_prefix='.')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is Ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    await member.send("hi")

@client.command()
async def pingo(ctx):
    ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    # await ctx.author.send('Bingo!')
    await ctx.channel.purge(limit=1)
    # channel = client.get_channel(channel_id_here)
    # msg = await channel.fetch_message(message_id_here)
    # await ctx.author.send(msg.attachments)
    # await channel.send(f"{ctx.message.author.mention} completed the level")
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run(token)