# bot.py
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import os
from discord_slash.utils.manage_commands import create_option
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_IDS= [687707946594992184]

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('ping'):
        await message.reply('pong')

@slash.slash(
    name="test",
    description="sends a message",
    guild_ids=GUILD_IDS
)
async def _test(ctx: SlashContext):
    await ctx.send("test complete!")

# @slash.slash(
#     name="generate_roles",
#     description="sends a message",
#     guild_ids=GUILD_IDS,
#     options=[
#         create_option(
#             name="channel",
#             description="Name of the channel message should be posted",
#             required=True,
#             option_type=7
#         )
#     ]
# )
# async def _generate_roles(ctx: SlashContext, channel:int):
#     print(channel)
#     ch=bot.get_channel(channel)
#     await ch.ctx.send("role successfully generated!")


bot.run(TOKEN)