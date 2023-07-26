import discord,os,requests,random

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
palabras = ["Puedes cerrar el caño mientras te cepillas los dientes","Planta un árbol cada cumpleaños!",""]

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def medioambiente(ctx):
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        coso = random.choice(palabras)
        await ctx.send(coso)

bot.run("Token")
