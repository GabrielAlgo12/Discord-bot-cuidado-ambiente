import discord,os,requests,random

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
palabras = ["Puedes cerrar el caño mientras te cepillas los dientes","Planta un árbol cada cumpleaños!","Composta: Recicla tus restos de comida y úsalos como abono para las plantas.","Ducha rápida: Reduce el tiempo de la ducha para ahorrar agua y energía.","Usa bolsas reutilizables: Evita las bolsas de plástico desechables en tus compras.No tengas varias bolsas de tela"]

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def medioambiente(ctx):
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        coso = random.choice(palabras)
        await ctx.send(coso)

bot.run("TOKEN")