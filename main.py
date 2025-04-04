import disnake
from disnake.ext import commands
import random
import asyncio
import os
from dotenv import load_dotenv
from reactions import EVIL_REACTIONS, EVIL_COMMAND_RESPONSES

# Load .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Bot-Einstellungen für Installierbarkeit
bot = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents.all(),
    activity=disnake.Game(name="Seelen sammeln 👀"),
    # Wichtig für Installierbarkeit:
    application_id=os.getenv("APPLICATION_ID"),  # Füge dies zu deiner .env hinzu
)

# Installations-URL generieren
def get_invite_url():
    return disnake.utils.oauth_url(
        bot.application_id,
        permissions=disnake.Permissions(
            send_messages=True,
            read_messages=True,
            use_slash_commands=True,
            add_reactions=True
        ),
        scopes=("bot", "applications.commands")  # Wichtig für Slash Commands
    )

@bot.event
async def on_ready():
    print(f"{bot.user.name} bereit zum Weltuntergang! 🔥")
    print(f"Lade Benutzer ein mit dieser URL: {get_invite_url()}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message) or message.content.startswith(("/evil", "!evil")):
        user = message.author.mention
        reaction = random.choice(EVIL_REACTIONS).format(user=user)

        async with message.channel.typing():
            await asyncio.sleep(1.5)
            await message.channel.send(f"**🦉🔮 {reaction.upper()}**")

    await bot.process_commands(message)

# Slash Commands
@bot.slash_command(name="evil", description="Beschwöre den Owlord!")
async def evil(interaction: disnake.ApplicationCommandInteraction):
    user = interaction.author.mention
    response = random.choice(EVIL_COMMAND_RESPONSES).format(user=user)
    await interaction.response.send_message(response)

@bot.slash_command(name="info", description="Bot-Informationen")
async def info(interaction: disnake.ApplicationCommandInteraction):
    embed = disnake.Embed(
        title="🦉 Evil Owl Bot",
        description="Ein dämonischer Bot mit 500+ bösartigen Reaktionen!",
        color=0x8B0000
    )
    embed.add_field(name="Version", value="2.0.0", inline=True)
    embed.add_field(name="Autor", value="Jumpstone", inline=True)
    embed.add_field(
        name="Funktionen",
        value="• 500+ Evil Reactions\n• /evil Command\n• Open Source",
        inline=False
    )
    # Installations-URL hinzufügen
    embed.add_field(
        name="Bot hinzufügen",
        value=f"[Klicke hier]({get_invite_url()}) um mich zu deinem Server hinzuzufügen!",
        inline=False
    )
    await interaction.response.send_message(embed=embed)

@bot.slash_command(name="github", description="GitHub Repository")
async def github(interaction: disnake.ApplicationCommandInteraction):
    embed = disnake.Embed(
        title="💻 GitHub Repository",
        description="[Hier mithelfen oder den Code klauen!](https://github.com/Jumpstone/evil-owl)",
        color=0x7289DA
    )
    embed.add_field(
        name="Wie mitmachen?",
        value="1. Fork das Repo\n2. Mach bösartige Änderungen\n3. Erstell einen PR\n\nWir nehmen alle teuflischen Ideen!",
        inline=False
    )
    await interaction.response.send_message(embed=embed)

# Sync Command (nur für Bot-Besitzer)
@bot.slash_command(name="sync", description="[OWNER] Sync Commands")
async def sync(interaction: disnake.ApplicationCommandInteraction):
    if await bot.is_owner(interaction.author):
        await bot.sync_commands()
        await interaction.response.send_message("🦉✅ **Befehle gesynct!**", ephemeral=True)
    else:
        await interaction.response.send_message("🚫 Nur der Bot-Besitzer kann das!", ephemeral=True)

# Neuer Command für Installations-URL
@bot.slash_command(name="invite", description="Lade den Bot auf deinen Server ein!")
async def invite(interaction: disnake.ApplicationCommandInteraction):
    embed = disnake.Embed(
        title="🦉 Lade den Evil Owl Bot ein!",
        description=f"[Klicke hier um mich einzuladen]({get_invite_url()})",
        color=0x8B0000
    )
    embed.add_field(
        name="Voraussetzungen",
        value="• Du benötigst Administrator-Rechte oder die Berechtigung 'Bot hinzufügen' auf dem Server",
        inline=False
    )
    await interaction.response.send_message(embed=embed)

try:
    bot.run(TOKEN)
except disnake.LoginFailure:
    print("❌ Falscher Token! Überprüfe deine .env-Datei.")