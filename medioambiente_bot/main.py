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

bot.run("MTEyNTkyMTE3NTI1MjUxMjg2OA.Grimj2.BkI-AIprz9XiuVt_1g_2t86Ci_dq1_nKA8za7s")