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

@bot.command()
async def ayuda(ctx):
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        texto1 = "The only command is $medioambiente and $info"
        texto2 = "El unico comando es $medioambiente y $info"
        await ctx.send(texto1)
        await ctx.send(texto2)

@bot.command()
async def info(ctx):
        texto3 = "Mi nombre es Gabriel"
        texto4 = "Mi GitHub: https://github.com/GabrielAlgo12"
        await ctx.send(texto3)
        await ctx.send(texto4)

bot.run("MTEyNTkyMTE3NTI1MjUxMjg2OA.GvvMnJ.2DUlIzwppMn2Vrc9_7eh7d3b0fQrLhPzWsBLVk")