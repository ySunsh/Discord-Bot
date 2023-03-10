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


listaditadura = ['erick', 'ditadura', 'governo', 'nazista', 'vitor', "jao"]
listaditaduranerd = ['judeu', 'forza', 'enzo', 'theo']
morbinemoji = ("<:morbin:1040075105998479461>")
iq = ("<:flag_ig:911773060284186625>")



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

async def setup(bot):
    await bot.add_cog(Event(bot))

async def setup2(bot):
    await bot.add_cog(Event2.EventAnimais(bot))

intents = discord.Intents.all()
bot = myBot()
bot.remove_command('help')

velhavariavel = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],      
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
player1 = ''
player2 = ''
turn = ''
gameover = True
board = []



@bot.event
async def on_ready():
    async with bot.db.cursor() as cursor:
        sql = "SELECT guild_id FROM canais"
        await cursor.execute(sql)
        result = await cursor.fetchall()
        ids = len(result)
    print(Fore.GREEN + f"Bot on! {ids} servers com banco de dados")
    
@bot.tree.command()
async def teste(interaction = discord.Interaction):
    await interaction.user.guild.get_channel

    
    hora = strftime("%H, %M")
    oiembed = discord.Embed(title = "**Tudo nos trinks!**", description=f"Bot on!\nPing do Bot: {round(bot.latency *1000)}\nHorario: {hora}", colour = discord.Colour.brand_green())
    await interaction.response.send_message(embed = oiembed)




@bot.command()
async def canais(ctx):
    lista_server = []
    for server in bot.guilds:
        for channel in server.channels: 
            if str(channel.type) == "text":
                lista_server.append(channel)
    await ctx.send(lista_server)




@bot.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(pass_context = True)
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.command(pass_context = True)
async def cat(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg/bin/ffmpeg.exe", source="cat.mp3"))
            
        embed = discord.Embed(title = 'Tocando! ????', description = f'Tocando agora: Cat Speaking Chinese', color = 0x10b9b1)
        embed.set_footer(text = f'Executado por {ctx.author}', icon_url = ctx.author.avatar.url)
        await ctx.reply(embed = embed)
        await asyncio.sleep(63)
        await ctx.voice_client.disconnect()
    

@bot.command(pass_context = True)
async def nego(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg/bin/ffmpeg.exe", source="negoban.mp3"))
        embed = discord.Embed(title = 'Tocando! ????', description = f'Tocando agora: Nego Bam Overwatch ', color = 0x10b9b1)
        embed.set_footer(text = f'Executado por {ctx.author}', icon_url = ctx.author.avatar.url)
        await ctx.reply(embed = embed)
        await asyncio.sleep(26)
        await ctx.voice_client.disconnect()
    

@bot.command(pass_context = True)
async def hihi(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg/bin/ffmpeg.exe", source="hihi.mp3"))
        embed = discord.Embed(title = 'Tocando! ????', description = f'Tocando agora: Homem do bigode engra??ado falando', color = 0x10b9b1)
        embed.set_footer(text = f'Executado por {ctx.author}', icon_url = ctx.author.avatar.url)
        await ctx.reply(embed = embed)
        await asyncio.sleep(30)
        await ctx.voice_client.disconnect()
    

@bot.command(pass_context = True)
async def karol(ctx):
    if (ctx.author.voice):
        
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg/bin/ffmpeg.exe", source='karol.mp3'))
        embed = discord.Embed(title = 'Tocando! ????', description = f'Tocando agora: Karol Conka Samsung', color = 0x10b9b1)
        embed.set_footer(text = f'Executado por {ctx.author}', icon_url = ctx.author.avatar.url)
        await ctx.reply(embed = embed)
        await asyncio.sleep(182)
        await ctx.voice_client.disconnect()


@bot.command(pass_context = True)
async def xina(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg/bin/ffmpeg.exe", source='xina.mp3'))
        embed = discord.Embed(title = 'Tocando! ????', description = f'Tocando agora: John Xina', color = 0x10b9b1)
        embed.set_footer(text = f'Executado por {ctx.author}', icon_url = ctx.author.avatar.url)
        await ctx.reply(embed = embed)
        await asyncio.sleep(50)
        await ctx.voice_client.disconnect()


@bot.command(pass_context = True)
async def clbc(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg/bin/ffmpeg.exe", source='clbc.mp3'))
        embed = discord.Embed(title = 'Tocando! ????', description = f'Tocando agora: Cala boca', color = discord.Colour.random())
        embed.set_footer(text = f'Executado por {ctx.author}', icon_url = ctx.author.avatar.url)
        await ctx.reply(embed = embed)
        await asyncio.sleep(7   )
        await ctx.voice_client.disconnect()


@bot.event 
async def on_message(message):
    if message.author == bot.user:
        return 
    msgcareca = (message.content).lower()
    if 'careca' in msgcareca:
        await message.channel.send(
            f"N??O FALE SOBRE CARECAS NO CHAT {message.author.mention}, VOC?? SABE QUE O NOSSO GRANDE ERICK N??O GOSTE QUE CITE CARECAS EM CONVERSAS!")
        
        await message.delete()
    
    if message.author == bot.user:
        return 
    msgdita = (message.content).lower()
    if msgdita in listaditadura:
        await message.add_reaction('\U0001F60E')
    elif msgdita in listaditaduranerd:
        await message.add_reaction('\U0001F913')
        await message.add_reaction('\U0001F1F3')
        await message.add_reaction('\U0001F1EA')
        await message.add_reaction('\U0001F1F7')
        await message.add_reaction('\U0001F1E9')
    await bot.process_commands(message)


@bot.command()
async def a(ctx):
    b = ctx.author.guild.text_channels
    guild_id = ctx.guild.id
    opcoes = []
    for channel in b:
        canal_nome = channel.name
        option = discord.SelectOption(label = canal_nome, emoji = "????")
        opcoes.append(option)
        
    select = discord.ui.Select(placeholder="Selecione um canal", 
    options= opcoes) 
    async def my_callback(interaction):
        for channel in b:
            if select.values[0] == channel.name:
                global canal_id
                canal_id = channel.id

                await channel.send("Este foi o canal selecionado")
                await asyncio.sleep(2)
                await channel.purge(limit = 1)
        
        
        async with bot.db.cursor() as cursor:
            await cursor.execute(f"SELECT canal_id FROM canais WHERE guild_id = {ctx.guild.id}")
            result = await cursor.fetchone()
            try:
                result = result[0]
            except:
                result = None
            
            

            if result is None:
                await cursor.execute("INSERT INTO canais (guild_id, canal_id) VALUES (?, ?)", (guild_id, canal_id))
                print(Fore.LIGHTRED_EX + f"Novo banco de dados detectado!", Fore.GREEN + (f"\nServer = {ctx.guild.name}\nCanal = {canal_nome}"))

            else:
                sql = ("UPDATE canais SET canal_id = ? WHERE guild_id = ?")
                val = (canal_id, guild_id)  
                await cursor.execute(sql, val)
                print(Fore.LIGHTRED_EX + f"Banco de dados atualizado", Fore.LIGHTGREEN_EX + (f"\nServer = {ctx.guild.name}\nCanal = {canal_nome}"))
                
        
        await bot.db.commit()
        
        
    

    select.callback = my_callback
    view = View()
    view.add_item(select)
    
    
    await ctx.send(view = view)
    


    
@bot.command()
async def b(ctx):
    channel = ctx.channel
    channel_id = channel.id 
    async with bot.db.cursor() as cursor:
        await cursor.execute(f"SELECT canal_id FROM canais WHERE guild_id = {ctx.guild.id}")
        canal_id = await cursor.fetchone()
        try:
            canal_id = canal_id[0]
            
        except:
            canal_id = "Nenhum canal selecionado"
            channel = "Nenhum canal selecionado"
   
    canalembed = discord.Embed(title = "Canal de Modera????o", description = "Para alterar o canal designado, execute o comando .modcanal", colour = discord.Colour.random())
    canalembed.add_field(name = "Canal Selecionado", value = channel)
    canalembed.add_field(name = "Id do canal", value = canal_id)
    canalembed.set_footer(text = f"{ctx.message.author.name}", icon_url = f"{ctx.message.author.avatar}")
    await ctx.send(embed = canalembed)

    
    

@bot.command()
@has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason =None):
    async with bot.db.cursor() as cursor:
        
        
        await cursor.execute(f"SELECT canal_id FROM canais WHERE guild_id = {ctx.guild.id}")
        ban_canal = await cursor.fetchone()
        ban_canal = ban_canal[0]
        print(ban_canal)
        
        

    if reason is None:
        reason = "Sem raz??o especificada"
    c = bot.get_channel(ban_canal)
    print (c)
    embed = discord.Embed(title="**Banimento???**", description=f"**|** {ctx.message.author.mention} voc?? me convocou para banir o usuario {member}! Para confirmar o banimento, aperte no ???. Se voc?? pensou duas vezes ou ele te deu um argumento muito bom para n??o bani-lo, clique no bot??o ??? \n**Detalhes do banimento:**", colour = discord.Colour.dark_red())
    embed.add_field(name = "*Raz??o do banimento*", value = f"{reason}")
    embed.add_field(name = "*Membro a ser banido*", value = f"`Nome:`{member.mention}\n `Id:{member.id}`")
    
    a = Button(emoji = "??????", style = discord.ButtonStyle.success)
    async def a_callback(interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message(
                "N??o foi voc?? que executou o comando! Para clicar nesses bot??es legais voc?? deve ser o dono do comando!",
                ephemeral = True
            )
        else: 
            a.disabled = True
            b.disabled = True
            await interaction.response.edit_message(view = view)
            banembed = discord.Embed(title = f"O usu??rio {member.name} foi banido!", colour = discord.Color.brand_red())
            banembed.add_field(name = "**Nome e Id**", value = f"`{member.name}`\n`{member.id}`")
            banembed.add_field(name = "**Raz??o**", value = f"`{reason}`")
            banembed.set_footer(text = f"Banimento efetuado por {ctx.message.author.name}", icon_url = f"{ctx.message.author.avatar}")
            banembed.set_thumbnail(url = f"{member.avatar}")
            await member.ban(reason = reason)
            
            
            
      
            
            
            await c.send(embed=banembed)

    a.callback = a_callback
    
    b = Button(emoji = "???", style = discord.ButtonStyle.danger)
    async def b_callback(interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message(
                "N??o foi voc?? que executou o comando! Para clicar nesses bot??es legais voc?? deve ser o dono do comando!",
                ephemeral = True
            )
        else:
            await ctx.send(f"O usu??rio {member} foi poupado de seu banimento")
            a.disabled = True
            b.disabled = True
            await interaction.response.edit_message(view = view)
    b.callback = b_callback
    view = View()
    view.add_item(a)
    view.add_item(b)
    await ctx.send(embed = embed, view = view)   
                

        
@bot.command()
@has_permissions(ban_members = True)
async def kick(ctx, member : discord.Member, *, reason =None):
    async with bot.db.cursor() as cursor:
        
        
        await cursor.execute(f"SELECT canal_id FROM canais WHERE guild_id = {ctx.guild.id}")
        kick_canal = await cursor.fetchone()
        kick_canal = kick_canal[0]
        print(kick_canal)
        
        

    if reason is None:
        reason = "Sem raz??o especificada"
    c = bot.get_channel(kick_canal)
    print (c)
    embed = discord.Embed(title="**Expuls??o???**", description=f"**|** {ctx.message.author.mention} voc?? me convocou para expulsar o usuario {member}! Para confirmar a expuls??o, aperte no ???. Se voc?? pensou duas vezes ou ele te deu um argumento muito bom para n??o expulsa-lo, clique no bot??o ??? \n**Detalhes da expuls??o:**", colour = discord.Colour.dark_red())
    embed.add_field(name = "*Raz??o da expuls??o*", value = f"{reason}")
    embed.add_field(name = "*Membro a ser expulso*", value = f"`Nome:`{member.mention}\n `Id:{member.id}`")
    
    a = Button(emoji = "??????", style = discord.ButtonStyle.success)
    async def a_callback(interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message(
                "N??o foi voc?? que executou o comando! Para clicar nesses bot??es legais voc?? deve ser o dono do comando!",
                ephemeral = True
            )
        else: 
            a.disabled = True
            b.disabled = True
            await interaction.response.edit_message(view = view)
            kickembed = discord.Embed(title = f"O usu??rio {member.name} foi expulso!", colour = discord.Color.brand_red())
            kickembed.add_field(name = "**Nome e Id**", value = f"`{member.name}`\n`{member.id}`")
            kickembed.add_field(name = "**Raz??o**", value = f"`{reason}`")
            kickembed.set_footer(text = f"Expuls??o efetuada por {ctx.message.author.name}", icon_url = f"{ctx.message.author.avatar}")
            kickembed.set_thumbnail(url = f"{member.avatar}")
            await member.kick(reason = reason)
            
            
      
            
            
            await c.send(embed=kickembed)

    a.callback = a_callback
    
    b = Button(emoji = "???", style = discord.ButtonStyle.danger)
    async def b_callback(interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message(
                "N??o foi voc?? que executou o comando! Para clicar nesses bot??es legais voc?? deve ser o dono do comando!",
                ephemeral = True
            )
        else:
            await ctx.send(f"O usu??rio {member} foi poupado de sua expuls??o")
            a.disabled = True
            b.disabled = True
            await interaction.response.edit_message(view = view)
    b.callback = b_callback
    view = View()
    view.add_item(a)
    view.add_item(b)
    await ctx.send(embed = embed, view = view)    






##########      JOGO DA VELHA!!!        ##########
@bot.command()
async def veia(ctx, p1 : discord.Member, p2: discord.Member):
    global player1
    global player2
    global turn
    global gameover
    global count

    if gameover:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ''
        gameover = False
        count = 0

        player1 = p1
        player2 = p2

        line = ""
        for x in range(len(board)):
            if x == 2 or 5 == x or x == 8:
                line += ' ' + board[x]
                await ctx.send(line)
                line = ''

            else:
                line += ' ' + board[x]
        num = randint(1, 2)
        if num == 1:
            turn = player1
            msgp1 = f'Vez do <@{player1.id}>' 
            await ctx.send (msgp1)
        elif num == 2:
            turn = player2
            msgp2 = f'Vez do <@{player2.id}>' 
            await ctx.send(msgp2)
    
    else:
        await ctx.send('J?? tem um jogo acontecendo prc')

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameover

    if not gameover:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(velhavariavel, mark)
                print(count)
                if gameover == True:
                    await ctx.send(mark + " GANHOUKKKKKKKKKKK!")
                elif count >= 9:
                    gameover = True
                    await ctx.send("EMPATOULJKKKKKKKKKKKKK")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("ESCOLHE A PORRA DO QUADRADO ENTRE 1 E 9 PORAAA, E VE SE ALGM JA N MARCOU ELE PORA")
        else:
            await ctx.send("ESPERA SUA VEZ CARALHO")
    else:
        await ctx.send('Come??a um jogo ai pfv, s?? dar .veia :(')


def checkWinner(velhavariavel, mark):
    global gameover
    for condition in velhavariavel:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameover = True

@veia.error
async def veia_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("MARCA 2 CARA PRA JOGAR BURRO DO KCT.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("MARCA O CARA MEUDEUSKKKKK (ie. <@1012954974415765525>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("COLOCA O LUGAR PRA VC JOGAR CARA PFV.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("COLOCA UM NUMERO CARAKKKKKKKK PQP BURRO.")



@bot.command()
async def mlk(ctx):
    await ctx.send('MULEQUE NAMORAL QUEM ?? VC SEU BOSTINHA VERMINHO LIXO RETARDADO QUEM ?? VOC?? SEU RIDICULO PODRE CARECA VERME AMEBA INSETO GAY MANO VC TA BRINCANDO COM O PERIGO NA PROXIMA VEZ EU VO ENTRA NA SUA CASA BATE NA SUA FAMILIA DESEMEMBRAR SUA MAE COM UMA COLHER NA FRENTE DOS SEUS OLHOS MLK VERME AGORA FICA ESPERTO QUE JA SEI DE ONDE SUA LAIA VEM E NA PROXIMA VO MATA VOC?? E SEUS AMIGUINHOS MAS QUANDO DIGO VOC?? E SEUS AMIGUINHOS SIGNIFICA QUE VO DEPENAR SUA M??E AQUELA PORSTITUTA FILHO DA PUTA ENQUANTO VC FICA AI DANDO O CU COM SAL SEU MLK ARROTO EU VO QUEBRA A MESA NO SEU PAI E JOGA UM SALAME NA SUA M??E PRA ELA QUEIMA NA PIROCA DO FARA?? MUSTAFAH DA PICA EN??RG??TICA LEVEMENTE CURVADA PAR.A A SONSERINA E COM ISSO VOU COMPLETAR O RITUAL PRA RECUSSITAR MEPHISTO E DEOIS DISSO ELE VAI COMER SEU CU COM ACOMPANHAMENTO DE M??DICOS PROFISSIONAIS PRA TE COMER E TE CURAR ETERNAMENTE AT?? SEU CU FICAR PODRE SOFRIMENTO ETERNO BEM VINDO AO INFERNO SEU RATO DO INFERNO VAI TOMA NO CU ?? MUITO BOSTA DO CARALHO MEU DEUS TU ?? MUITO BOSTA MANO DO C??U OLHA ISSO VAI TOMA NO SEU CU CARALHO')

@bot.command(name='tts')
async def tts(ctx, *args):
    text = " ".join(args)
    user = ctx.message.author
    if user.voice != None:
        try:
            vc = await user.voice.channel.connect()
        except:
            vc = ctx.voice_client
        if vc.is_playing():
            vc.stop()

        myobj = gTTS(text=text, lang="pt", tld = "com.br", slow=False)
        myobj.save("tts-audio.mp3")

        source = (discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg/bin/ffmpeg.exe", source="tts-audio.mp3"))
        vc.play(source)
    
@bot.command()
async def clear(ctx, amount:int):

    
    if amount == 1:
        msgamount = '1 mensagem foi apagada!'
    else:   
        await ctx.channel.purge(limit = amount + 1)
        embed = discord.Embed(title = 'Mensagens Apagadas!', description = f'Um total de {msgamount}', color = 0x10b9b1)
        embed.set_footer(text = f'{ctx.author}', icon_url = ctx.author.avatar.url)
        msg = await ctx.send(embed = embed)
        msg2 = await ctx.send('fvck lorita')
        await asyncio.sleep(4)
        await msg.delete()
        await msg2.delete()     

@bot.command()
async def minions(ctx):
    await ctx.send('Minions s??o seres multicelulares amarelos que existem desde o in??cio do tempo, evoluindo de amarelos organismos unicelulares aqu??ticos a seres que t??m apenas um prop??sito: servir aos vil??es mais malvados da hist??ria. Por??m, depois que sua in??pcia destr??i todos os seus mestres, incluindo um T. Rex, Genghis Khan, Napole??o, e at?? o Dr??cula, eles decidem isolar-se do mundo e come??ar uma nova vida no ??rtico. Em algum momento na d??cada de 1960, a falta de um mestre leva-os a desenvolver depress??o, ent??o Kevin e outros dois volunt??rios (Stuart e Bob) partem para encontrar um novo mestre. Eles chegam a uma conven????o de vil??es em Orlando e passam a competir pelo direito de serem capangas de Scarlet Overkill (dublada por Adriana Esteves, na vers??o brasileira), uma vil?? elegante e ambiciosa determinada a dominar o mundo e se tornar a primeira supervil?? da hist??ria.  ')

##########      JOGO DE ADIVINHA????O!!!     ##########  
@bot.command()
async def genio (ctx):             
    await ctx.send('Pensei em um n??mero de **1 a 5**\n Voc?? tem 3 tentativas para adivinhar\n Se voc?? acertar qual n??mero ??, voc?? ganha algo')
    numgenio = randint(1, 5)
    acertou = False
    print(numgenio)
    count = 0
    def check(m):
        return m.author == ctx.author and m.channel == ctx.message.channel
    while acertou == False:
        print(count)
        print(acertou)
        adv = await bot.wait_for('message', check = check)
        if adv.content == str(numgenio):
            await ctx.send(f'Caraiokkkk tu realmente acertou, levaram **{count+1}** tentativas pra voc?? acertar')
            await asyncio.sleep(2)
            await ctx.send('E voc?? ganhou...')
            await asyncio.sleep(1)
            await ctx.send('TU GANHOU FOI MUITA PICAKKKKKKKKKKKK')
            acertou = True
        else:
            count += 1
            await ctx.send('ERROUKKKKKKKKKKKKK')
            
        if count == 3:
            await asyncio.sleep(1)
            await ctx.send('*Suas tentativas acabaram! De um .genio novamente para tentar de novo*')      
            acertou = True

##########      COMANDO DE PING!!!      ##########
@bot.command()
async def ping (ctx):
    embed = discord.Embed(title = 'Pong! ????', description = f'Ping = {round(bot.latency *1000)} ms', color = 0x10b9b1)
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text = f'Pedido por {ctx.author}', icon_url = ctx.author.avatar.url)
    await ctx.reply(embed = embed)

##########      PARTE DO COMANDO HELP!!!       ##########
class MyView(View):

    @discord.ui.button(label= '????', style=discord.ButtonStyle.primary)
    async def voice_button_callback(self, interaction, button):
        await interaction.response.edit_message(embed = callembed)
    
    @discord.ui.button(label = '????', style=discord.ButtonStyle.danger)
    async def mod_button_callback(self, interaction, button):
        await interaction.response.edit_message(embed = modembed)

    @discord.ui.button(label = '????', style = discord.ButtonStyle.gray)
    async def mini_button_callback(self, interaction, button):
        await interaction.response.edit_message(embed = miniembed)

    @discord.ui.button(label = '????', style = discord.ButtonStyle.green)
    async def forfun_button_callback(self, interaction, button):
        await interaction.response.edit_message(embed = forfunembed)
    
    @discord.ui.button(label = "????", style=discord.ButtonStyle.success)
    async def dinero_callback(self, interaction, button):
        await interaction.response.edit_message(embed = economyembed)

            
@bot.command()
async def help(ctx):

    
    view = MyView()
    await ctx.send(embed = helpembed, view = view)

##########      PARTE DE ECONOMIA!!!            ##########
@bot.command()
async def mendigar(ctx):    
    member = ctx.author
    db = sqlite3.connect("main.sqlite")
    cursor = db.cursor()
    cursor.execute(f"SELECT carteira FROM main WHERE user_id = {member.id}")
    carteira = cursor.fetchone()
   
    
    ganhos = randint(0, 5)
    try:
        carteira = carteira[0]

    except:
        carteira = 0




    if ganhos == 0:
        title = "**A?? N??O PATR??O!**"
        description = '**Voc?? mendigou que s?? a porra, mas todos te ignoraram e n??o te deram nenhum Morbin Coin!**'
        colour = discord.Colour.brand_red()
    else:
        title = "**Mendigada de elite!**"
        description = f"Os pedestres ficaram impressionados com tamanha habilidade de uma pessoa, ?? pra poucos tocar violino montado em um monoclico!\n **Voc?? ganhou M${ganhos}{morbinemoji}**"
        colour = discord.Colour.brand_green()
    mendembed = discord.Embed(title = title, description=description, colour = colour)
    sql = ("UPDATE main SET carteira = ? WHERE user_id = ?")
    val = (carteira + int(ganhos), member.id)
    cursor.execute(sql, val)
    await ctx.send(embed = mendembed)
    db.commit()
    cursor.close()
    db.close()

@bot.command()
async def blackjack(ctx, amount:int=1000):
    db = sqlite3.connect("main.sqlite")
    cursor = db.cursor()
    cursor.execute(f"SELECT carteira FROM main WHERE user_id = {ctx.author.id}")
    carteira = cursor.fetchone()
    try:
        carteira = carteira[0]
    except:
        carteira = carteira

    if amount < 50:
        return await ctx.send(f'A?? tamb??m n??o p??! S?? M${amount}{morbinemoji} o cassino n??o aceita! Aposte pelo menos M$150{morbinemoji}!')

    elif amount > carteira:
        return await ctx.send(f'Paro a?? patr??o! N??o pra apostar oque voc?? n??o tem!')


    user_strikes = randint(1, 15)
    bot_strikes = randint(5, 15)

    if user_strikes > bot_strikes:
        percentage = randint(50, 100)
        quantidade_ganha = int(amount*(percentage/100))
        cursor.execute("UPDATE main SET carteira = ? WHERE user_id = ?", (carteira + quantidade_ganha, ctx.author.id))
        db.commit()
        embed = discord.Embed(title = f'**??????Voc?? ganhou!!??????**', description=f"**No cassin??o do Julh??o n??o tem como perder!** \nAqui voc?? apostou M${amount}{morbinemoji} e saiu com M${amount + quantidade_ganha}{morbinemoji}!\nSeu novo saldo na carteira ?? de M${carteira + quantidade_ganha}{morbinemoji}", colour = discord.Colour.brand_green())
        embed.set_footer(text = f'Taporra {ctx.author} tu ?? o melhor aqui no cassino! Voc?? deveria tentar de novo!', icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/858538752561119293/1040806288428380292/image.png')
    
    
    elif user_strikes < bot_strikes:
        percentage = randint(50, 100)
        quantidade_perdida = int(amount*(percentage/100))
        cursor.execute("UPDATE main SET carteira = ? WHERE user_id = ?", (carteira - quantidade_perdida, ctx.author.id))
        db.commit()
        embed = discord.Embed(title = "**??????Acho que voc?? perdeu!??????**", description=f"Olha cara aqui no cassin??o do Julh??o voc?? s?? ganha, mas agora voc?? ganhou ao contrario :/\n Aqui voc?? apostou M${amount}{morbinemoji} e saiu com M${amount - quantidade_perdida}{morbinemoji}!\nSeu novo saldo na carteira ?? de M${carteira - quantidade_perdida}{morbinemoji} ", colour = discord.Colour.brand_red())
        embed.set_footer(text = f'Taporra {ctx.author} tu conseguiu perder num cassino onde voc?? s?? ganha kkkk!', icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/858538752561119293/1040806660089856061/unknown.png?width=1014&height=676')
    
    
    else:
        embed = discord.Embed(title = "**??????Uau, voc?? conseguiu empatar!??????**", description=f"Mano, aqui no cassino onde voc?? s?? ganha, empatar ?? uma raridade! Voc?? est?? com a sorte em dia, eu recomendo voc?? apostar denovo!", colour = discord.Colour.orange())
        embed.set_footer(text=  f'Essa s?? uma em um milh??o {ctx.author} aposte denovo s?? pra testar se voc?? ainda tem essa sorte!!', icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/858538752561119293/1040806892894699582/image.png')

    embed.add_field(name = f'**{ctx.author.name.title()}**', value=f"Seus pontos: {user_strikes}")
    embed.add_field(name = f'**Junin da Catinguera**', value=f"Pontos do advers??rio: {bot_strikes}")
    
    await ctx.reply(embed = embed)
    cursor.close()
    db.close()
    
@bot.command()
async def saldo(ctx, member:discord.Member = None):

    if member is None:
        member = ctx.author

    db = sqlite3.connect("main.sqlite")
    cursor = db.cursor()


    cursor.execute(f'SELECT carteira, banco FROM main WHERE user_id = {member.id}')
    bal = cursor.fetchone()
    try:
        carteira = bal[0]
        bank = bal[1]
    except:
        carteira = 0
        bank = 0
    
    valembed = discord.Embed(colour= discord.Colour.random())
    valembed.set_author(icon_url = member.avatar.url, name = f"Conta banc??ria de {member}")
    valembed.add_field(name = "Carteira", value = f'`????{bal[0]}`')
    valembed.add_field(name = "Banco", value = f'`????{bal[1]}`')
    valembed.add_field(name = "Patrim??nio", value = f'`????{bal[1] + bal[0]}`')
    valembed.set_thumbnail(url = "https://cdn-icons-png.flaticon.com/512/1138/1138038.png")
    await ctx.send(embed = valembed)

@bot.command()
async def depositar (ctx, amount:int):
    db = sqlite3.connect("main.sqlite")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM main WHERE user_id = {ctx.author.id}")
    data = cursor.fetchone()
    try:
        carteira = data[1]
        banco = data[2]
    except:
        await ctx.send("Houve um erro, tente novamente")

    if carteira < amount:
        return await ctx.send("Calmo calmo calmo! S?? da pra depositar oque voc?? tem!")
    
    else:
        cursor.execute("UPDATE main SET banco = ? WHERE user_id = ?", (banco + amount, ctx.author.id))
        cursor.execute("UPDATE main SET carteira = ? WHERE user_id = ?", (carteira - amount, ctx.author.id))
        if amount == 1:
            await ctx.send(f'{amount}{morbinemoji} foi depositado em seu banco!')
        else:
            await ctx.send(f'{amount}{morbinemoji} foram depositados em seu banco!')
    db.commit()
    cursor.close()
    db.close()

@bot.command()
async def retirar (ctx, amount:int):
    db = sqlite3.connect("main.sqlite")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM main WHERE user_id = {ctx.author.id}")
    data = cursor.fetchone()
    try:
        carteira = data[1]
        banco = data[2]
    except:
        await ctx.send("Houve um erro, tente novamente")

    if banco < amount:
        return await ctx.send("Calmo calmo calmo! S?? da pra retirar oque voc?? tem!")
    
    else:
        cursor.execute("UPDATE main SET carteira = ? WHERE user_id = ?", (carteira + amount, ctx.author.id))
        cursor.execute("UPDATE main SET banco = ? WHERE user_id = ?", (banco - amount, ctx.author.id))
        if amount == 1:
            await ctx.send(f'{amount}{morbinemoji} foi retirado de seu banco!')
        else:
            await ctx.send(f'{amount}{morbinemoji} foram retirados de seu banco!')
    db.commit()
    cursor.close()
    db.close()

@bot.command()
async def slots(ctx, amount:int=250):
    db = sqlite3.connect("main.sqlite")
    cursor = db.cursor()
    cursor.execute(f'SELECT carteira FROM main WHERE user_id = {ctx.author.id}')
    carteira = cursor.fetchone()
    try:
        carteira = carteira[0]
    except:
        carteira = 0

    if amount < 100:
        return await ctx.send(f'A?? tamb??m n??o p??! S?? M${amount}{morbinemoji} o cassino n??o aceita! Aposte pelo menos M$150{morbinemoji}!')

    elif amount > carteira:
        return await ctx.send(f'Paro a?? patr??o! N??o da pra apostar oque voc?? n??o tem!')
    
    time_factor = randint(1, 5)
    ganhos = int(amount*time_factor)
    final = []
    for i in range(3):
        a = choice(["????", '????', '????', '????'])
        final.append(a)
        a.replace('[]', ' ')

    if final[0] == final[1] and final[1] == final[2]:
        cursor.execute("UPDATE main SET carteira = ? WHERE user_id = ?", (carteira + ganhos, ctx.author.id))
        db.commit() 
        embed = discord.Embed(title = "**Ca??a-N??quel**", colour = discord.Colour.green())
        embed.add_field(name = f"Voc?? ganhou M${ganhos}!", value = f'{final}')
        embed.add_field(name = f"-----------------------------------------", value = f"**Multiplicador** X {time_factor}", inline=False)
        embed.add_field(name = f"-----------------------------------------", value = f'**Novo Saldo** M${carteira + ganhos}', inline = False)
        embed.set_thumbnail(url = 'https://cdn-icons-png.flaticon.com/512/1055/1055823.png')
        await ctx.reply(embed = embed)

    else:
        cursor.execute("UPDATE main SET carteira = ? WHERE user_id = ?", (carteira - ganhos, ctx.author.id))
        db.commit()
        embed = discord.Embed(title = "**Ca??a-N??quel**", colour =discord.Colour.red())
        embed.add_field(name = f"Voc?? perdeu M${ganhos} ", value = f'{final}')
        embed.set_thumbnail(url = 'https://cdn-icons-png.flaticon.com/512/1055/1055823.png')
        await ctx.reply(embed = embed)
    
        cursor.close()
        db.close()    
  



@bot.command()
async def sorteio(ctx, num:int, num2:int):
    a = randint(num, num2)
    sor =  discord.Embed(title = "**Sorteio!**", description=f"**Entre os n??meros {num} e {num2} o n??mero`{a}`!\nPara sortear esses mesmos n??meros novamente, aperte o bot??o verde abaixo**", colour = discord.Colour.brand_green())
    sor.set_thumbnail(url = "https://cdn-icons-png.flaticon.com/512/3205/3205406.png")
    c = Button(label =  f"Sortear novamente os n??meros {num} e {num2}" , style = discord.ButtonStyle.success)
    async def c_callback(interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message(
                "N??o foi voc?? que executou o comando! Para clicar nesses bot??es legais voc?? deve ser o dono do comando!",
                ephemeral = True
                )
        else:
            p = False
            while p is not True:
                b = randint(num, num2)
                if b != a:
                    p = True
            sor2 = discord.Embed(title = "**Sorteio!**", description=f"**Outro sorteio foi feito e entre os n??meros {num} e {num2} o n??mero `{b}`!**", colour = discord.Colour.brand_green())
            sor2.set_thumbnail(url = "https://cdn-icons-png.flaticon.com/512/3205/3205406.png")
            await interaction.response.send_message(embed = sor2)
            
    c.callback = c_callback
    view = View()
    view.add_item(c)
    await ctx.send(embed = sor, view = view)

class Select(discord.ui.Select):
    def __init__(self):
        Cores = [
            discord.SelectOption(label = "Azul", emoji="????", description= "A cor do embed ser?? azul"),
            discord.SelectOption(label = "Vermelho", emoji="????", description= "A cor do embed ser?? vermelha"),
            discord.SelectOption(label = "Verde", emoji="????", description= "A cor do embed ser?? verde"),
            discord.SelectOption(label = "Laranja", emoji="????", description= "A cor do embed ser?? laranja"),
            discord.SelectOption(label = "Amarelo", emoji="????", description= "A cor do embed ser?? vermelha"),
            discord.SelectOption(label = "Roxo", emoji="????", description= "A cor do embed ser?? roxa"),
            discord.SelectOption(label = "Default", emoji="???", description="A cor do embed ser?? cinza"),
            discord.SelectOption(label = "Random", emoji="????", description= "A cor do embed ser?? uma cor aleat??ria")
            
        ]
        super().__init__(placeholder = "Escolha a cor do seu embed", max_values=1, min_values=1, options=Cores)
    async def callback(self, interaction:discord.Interaction):
        global modalcor
        if self.values[0] == "Azul":
            modalcor = discord.Colour.blue()
        if self.values[0] == "Vermelho":
            modalcor = discord.Colour.brand_red()
        if self.values[0] == "Verde":
            modalcor = discord.Colour.brand_green()
        if self.values[0] == "Laranja":
            modalcor = discord.Colour.orange()
        if self.values[0] == "Amarelo":
            modalcor = discord.Colour.yellow()
        if self.values[0] == "Roxo":
            modalcor = discord.Colour.purple()
        if self.values[0] == "Rosa":
            modalcor = discord.Colour.magenta()
        if self.values[0] == "Random":
            modalcor = discord.Colour.random()
        if self.values[0] == "Default":
            modalcor = discord.Colour.darker_gray()
        await interaction.response.send_modal(asd())
        
class SelectView(View):
    def __init__(self, *, timeout = 30):
        super().__init__(timeout=timeout)
        self.add_item(Select())

class asd(discord.ui.Modal, title = "Criador de embed?"):
    name = discord.ui.TextInput(label = "T??tulo do seu embed", max_length=256)
    answer = discord.ui.TextInput(label = "Descri????o do seu embed", max_length=4000)
    
    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title = self.name, description= self.answer, colour = modalcor)
        await interaction.response.send_message(embed = embed)



async def menu(interaction:discord.Interaction):
    await interaction.response.send_message(view=SelectView(), delete_after=10, ephemeral=True)



@bot.command(name = "embed")
async def menu(ctx):
    await ctx.send(view=SelectView(), delete_after=10, ephemeral=True)
