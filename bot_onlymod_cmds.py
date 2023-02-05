import discord
from discord import app_commands
from discord.ext import commands
import discord.ui
from discord.ext.commands.core import has_permissions
from discord import FFmpegPCMAudio
from gtts import gTTS
import asyncio
from random import randint, choice
from Embeds import *
from discord.ui import Button, View, Select
import sqlite3
from Event import Event
import Event2
from time import strftime
import aiosqlite
from colorama import Fore


class myBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='.',intents= discord.Intents.all())
        self.db = None
    async def setup_hook(self):
        if not self.db:
            print(Fore.GREEN + "Ligando Banco de Dados...")
            self.db = await aiosqlite.connect("mod.db")
            await asyncio.sleep(2)
            print(Fore.GREEN + "Banco de dados online!")
bot = myBot()
bot.remove_command('help')
               
