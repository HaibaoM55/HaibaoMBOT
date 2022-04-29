##HaibaoMBOT facut de HaibaoM55.
##Un robot de discord boschetar, in loc sa dea bani la userii de pe server, ii cerseste xD.

##In primul rand, importam toate librariile necesare.
import discord
import random
from discord import message
from discord.embeds import Embed
from discord.ext import commands
import json
import os
from dotenv import load_dotenv
load_dotenv()
##Intializam token-ul.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!")
##Bot-ul va arata cand este conectat
@bot.event
async def on_ready():
    print("Conectat!")
##Comanda bz
@bot.command(
    help = "Cumpara din bazaar!"
)
async def bz(ctx):
    nume = ctx.message.author.name
    embed = discord.Embed(
        title = "Bazaar",
        description = "Cumpara din bazaar!",
        color = discord.Color.blue()
    )
    embed.set_author(name = nume)
    embed.add_field(name = "❗ATENTIE❗", value = "Nu poti cumpara din bazaar momentan, fiindca nu este terminata comanda cumpara! Voi sterge acest mesaj cand este gata!", inline = False)
    embed.add_field(name = "Cacatul lui Rex", value = "Id: 1 \n Pret: 200 \n Descriere:Un talisman legendar!", inline = False)
    await ctx.send(embed = embed)
@bot.command(
    help = "baneaza un user"
)
async def ban(ctx, member: discord.Member, *, reason = None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason = reason)
        await ctx.send(f'{member.mention} a fost banat de {ctx.author.mention}! Motivul a fost: {reason}')
    else:
        await ctx.send(f'{ctx.author.mention} nu ai permisiunea sa banzi pe {member.mention}')
##Comanda ping
@bot.command(
    help = "Clasica comanda ping pong."
)
async def ping(ctx):
    await ctx.send(f"Pong!")
##Comanda banc
@bot.command(
    help = "Spune un banc random"
)
async def banc(ctx):
    with open("bancuri.txt", "r") as f:
        bancuri = f.readlines()
    nume = ctx.message.author.name
    embed = discord.Embed(
        title = "Bancuri",
        description = "Bancuri random!",
        color = discord.Color.blue()
    )
    embed.set_author(name = nume)
    embed.add_field(name = "Bancul:", value = random.choice(bancuri), inline = False)
    await ctx.send(embed = embed)
##Comanda addbanc
@bot.command(
    help = "Creeaza un banc."
)
async def addbanc(ctx, args):
    with open("bancuri.txt", "a") as f:
        f.write(args + "\n")
    await ctx.send("Bancul a fost adaugat!")
##Comanda citestebanc
@bot.command(
    help = "Verifica bancurile"
)
async def citestebanc(ctx):
    with open("bancuri.txt", "r") as f:
        bancuri = f.read()
    ##Linia 69(funny number)
    await ctx.send(bancuri)
@bot.command(
    help = "Arata noutatile botului"
)
async def noutati(ctx):
    embed = discord.Embed(
        title = "Noutati",
        description = "Noutatile despre HaibaoMBOT",
        color = discord.Color.blue()
    )
    embed.set_author(name = "HaibaoM55#7025")
    embed.add_field(name = "Ultima versiune:", value = "Beta 0.0.1", inline = False)
    embed.add_field(name = "Versiunea 0.0.1", value = "Am adaugat comenziile: !ping, !banc, !addbanc,!bani, !transfera, !daruieste, !bz si !ban. Si am facut sistemul de economie si de leveling!", inline = False)
    await ctx.send(embed = embed)
@bot.event
async def on_message(message):
    @bot.event
    async def on_member_join(member):
        with open('users.json', 'r') as f:
            users = json.load(f)
        await update_data(users, member)
        with open('users.json', 'w') as f:
            json.dump(users, f)
@bot.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)
        with open('users.json', 'w') as f:
            ##Linia 112 xD
            json.dump(users, f)
    await bot.process_commands(message)
    experienta_i = users[f'{message.author.id}']['experience']
    if experienta_i > 0 and experienta_i < 200:
        if experienta_i == 5:
            await message.channel.send(f'{message.author.mention} ai primit rolul [DEFAULT]')
        await message.author.add_roles(discord.utils.get(message.guild.roles, name="[DEFAULT]"))
    elif experienta_i >= 200 and experienta_i < 400:
        if experienta_i == 200:
             await message.channel.send(f'{message.author.mention} ai primit rolul [DEFAULT+]')
        await message.author.add_roles(discord.utils.get(message.guild.roles, name="[DEFAULT+]"))
    elif experienta_i >= 400 and experienta_i < 600:
        if experienta_i == 400:
             await message.channel.send(f'{message.author.mention} ai primit rolul [DEFAULT++]')
        await message.author.add_roles(discord.utils.get(message.guild.roles, name="[DEFAULT++]"))
    elif experienta_i >= 600 and experienta_i < 1000:
        if experienta_i == 600:
            await message.channel.send(f'{message.author.mention} ai primit rolul [VIP]')
        await message.author.add_roles(discord.utils.get(message.guild.roles, name="[VIP]"))
    elif experienta_i >= 1000 and experienta_i < 1400:
        if experienta_i == 1000:
            await message.channel.send(f'{message.author.mention} ai primit rolul [VIP+]')
        await message.author.add_roles(discord.utils.get(message.guild.roles, name="[VIP+]"))
    elif experienta_i >= 1400 and experienta_i < 2000:
        if experienta_i == 1400:
            await message.channel.send(f'{message.author.mention} ai primit rolul [VIP++]')
        await message.author.add_roles(discord.utils.get(message.guild.roles, name="[VIP++]"))
    elif experienta_i >= 2000 and experienta_i < 2600:
        if experienta_i == 2000:
            await message.channel.send(f'{message.author.mention} ai primit rolul [MVP]')
        await message.author.add_roles(discord.utils.get(message.guild.roles, name="[MVP]"))
    elif experienta_i >= 2600 and experienta_i < 3200:
        if experienta_i == 2600:
            await message.channel.send(f'{message.author.mention} ai primit rolul [MVP+]')
        await message.author.add_roles(discord.utils.get(message.guild.roles, name="[MVP+]"))
    elif experienta_i >= 3200 and experienta_i < 4000:
        if experienta_i == 3200:
            await message.channel.send(f'{message.author.mention} ai primit rolul [MVP++]')
        await message.author.add_roles(discord.utils.get(message.guild.roles, name="[MVP++]"))
async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} a ajuns la level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end

@bot.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'Esti la nivelul {lvl}! Cu {users[str(id)]["experience"]} de experienta!')
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'{member} este la nivelul {lvl}!')
##Deschide un cont(nu e facut de mine, tot sistemul de economie de pe stackoverflow, la fel si cel de nivele!)
async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Wallet"] = 0
        users[str(user.id)]["Bank"] = 0

    with open("bank.json", 'w') as f:
        json.dump(users, f)
    return True
async def get_bank_data():
    with open("bank.json", 'r') as f:
        users = json.load(f)
    return users
##Comanda bani
@bot.command(
    help = "Vezi cati bani ai in contul tau!"
)
async def bani(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["Wallet"]
    bank_amt = users[str(user.id)]["Bank"]
    em = discord.Embed(title=f"Banii lui {ctx.author.name}", color=discord.Color.teal())
    em.add_field(name="Buzunar: ", value=wallet_amt)
    em.add_field(name="Banka: ", value=bank_amt)
    await ctx.send(embed=em)
##Comanda cerseste
@bot.command(
    help = "Cerseste niste bani!"
)
async def cerseste(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    earnings = random.randrange(101)
    await ctx.send(f"Cineva ti-a dat {earnings} lei!")
    users[str(user.id)]["Wallet"] += earnings
    with open("bank.json", 'w') as f:
        json.dump(users, f)
@bot.command(
    help = "Transfera banii din buzunarul tau in banka!"
)
async def transfera(ctx, amount: int):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    if amount <= users[str(user.id)]["Wallet"]:
        users[str(user.id)]["Wallet"] -= amount
        users[str(user.id)]["Bank"] += amount
        await ctx.send(f"Ai transferat {amount} lei!")
        with open("bank.json", 'w') as f:
            json.dump(users, f)
    else:
        await ctx.send("Nu ai destui bani in buzunar!")
@bot.command(
    help = "Daruieste bani!"
)
async def daruie(ctx, member: discord.Member, amount: int):
    await open_account(ctx.author)
    if member == ctx.author:
        await ctx.send("Nu poti darui bani proprii!")
        return
    if amount <= 0:
        await ctx.send("Nu poti darui 0 sau mai putin bani! Sa stii ca nu esti simpatic, uratule!")
        return
    user = ctx.author
    users = await get_bank_data()
    if amount <= users[str(user.id)]["Bank"]:
        users[str(user.id)]["Bank"] -= amount
        users[str(member.id)]["Wallet"] += amount
        await ctx.send(f"Ai daruit {amount} lei!")
        with open("bank.json", 'w') as f:
            json.dump(users, f)
    else:
        await ctx.send("Nu ai destui bani in banka!")
##Surse:
##Sistemul de economie de pe stackoverflow
##https://stackoverflow.com/questions/67917643/discord-py-economy-system
##Facut de user-ul @Dominik
##https://stackoverflow.com/users/14449816/dominik

##Sistemul de nivele de pe stackoverflow
##https://stackoverflow.com/questions/62042331/how-to-create-a-leveling-system-with-discord-py-with-python
##Facut de user-ul @bulkypanda
##https://stackoverflow.com/users/13572142/bulkypanda

##Videoclipul care m-a ajutat sa inteleg cum merge discord.py
##https://www.youtube.com/watch?v=QB7ACr7pUuE
bot.run(DISCORD_TOKEN)