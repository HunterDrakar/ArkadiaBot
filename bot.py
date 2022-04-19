import discord
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='-', intents = discord.Intents.all())
status = cycle(['Arkadia RP', 'Dê uma olhada em nossa loja vip', 'Divulgue o servidor para os seus amigos :)', 'Desenvolvido por: HunterDrakar#6713'])
client.remove_command("ajuda")

@client.event
async def on_ready():
    print("BOT ONLINE!")
    await change_status.start()


@tasks.loop(seconds= 10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, amount= 20):
    role = discord.utils.get(ctx.guild.roles, name="Staff")
    if role in ctx.author.roles:
        await ctx.channel.purge(limit= amount)
        await ctx.send(f'Chat limpo!')
    else:
        await ctx.send('Você não tem permissão para limpar o chat!!')


@client.command()
async def wl(ctx, member: discord.Member):
    role = discord.utils.find(lambda r: r.name == "Whitelist", ctx.guild.roles)
    rolerole = discord.utils.find(lambda r: r.name == "S/Whitelist", ctx.guild.roles)
    perm = discord.utils.get(ctx.guild.roles, name="Staff")
    if perm in ctx.author.roles:
        await member.remove_roles(rolerole)
        await member.add_roles(role)
        await ctx.send(f'O player {member.mention} recebeu sua whitelist com Sucesso! ')
        wl = await client.fetch_channel(824459109499404311)
        await wl.send(f'''Seja bem vindo(a)  {member.mention} Sua passagem para Arkadia está liberada. Caso você precise consultar e/ou até mesmo alterar alguma coisa em sua lore, só entrar em contato com alguém da equipe administrativa.

ㅤ ㅤ Agora precisamos de suas informações, utilize o canal #🧚・info-personagem  para entrar com suas credenciais e colocar o nome a raça e a profissão do seu personagem! Não se preocupe, tudo o que precisa postar lá são coisas que você já tem acesso. 

           Mude o apelido no discord com o nome do seu personagem!!!

           Poste também em #🧙・info-magia-elemental  se seu personagem for utilizar magias elementais e ou magia Arcana.
Após isso poste no canal #👽・id-64  seu steam id 64.

ㅤ ㅤ Mais uma vez nós gostaríamos de dar as boas vindas! Logo mais nós vemos nas terras de Arkadia
''')
        await wl.send(file=discord.File('arkadia.png'))

    else:
        await ctx.send('Você não tem permissão para dar Whitelist!')

@client.command()
async def unwl(ctx, member: discord.Member):
    unrole = discord.utils.find(lambda r: r.name == "Whitelist", ctx.guild.roles)
    rerole = discord.utils.find(lambda r: r.name == "S/Whitelist", ctx.guild.roles)
    perm2 = discord.utils.get(ctx.guild.roles, name ="Staff")
    if perm2 in ctx.author.roles:
        await member.remove_roles(unrole)
        await ctx.send(f'O player {member.mention} teve sua Whitelist removida com sucesso! ')
        await member.add_roles(rerole)
    else:
        await ctx.send('Você não tem permissão para retirar a Whitelist de alguém!')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    perm3 = discord.utils.get(ctx.guild.roles, name= 'Staff')
    if perm3 in ctx.author.roles:

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'O usuário {user.mention} foi desbanido com sucesso!')
                return
    else:
        await ctx.send('Você não tem permissão para remover o ban de alguém!')

@client.group(invoke_without_command=True)
async def ajuda(ctx):
    em = discord.Embed(tittle= "ajuda", description= "Lista de comandos abaixo:")

    em.add_field(name = "**Moderação**", value= "clear, wl, unwl, unban")
    em.add_field(name = "Utilitários:", value= "  ping ")

    await ctx.send(embed = em)


client.run('')
