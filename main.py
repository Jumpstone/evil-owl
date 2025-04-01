import disnake
from disnake.ext import commands
import random
import asyncio

# 🔴 ERSETZE DIESEN TOKEN!
TOKEN = "MTM1NjY5ODUyMjY4NjMyNDgxOA.GlOS-x.hAvo8DBTFIZhSE0qsE9mTMgnVKeA5aJTE-G9V8"

bot = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents.all(),
    activity=disnake.Game(name="mit Seelen 👀")
)

# 50+ TEUFLISCHE REAKTIONEN 🦉🔥
EVIL_REACTIONS = [
    "MUAHAHA! {user} WAGT ES MICH ZU PINGEN?! DIE HÖLLE ERWARTET DICH! 👹",
    "BEI ALLEN DÄMONEN! {user} STÖRT MEINE FINSTERE ARBEIT! 💀",
    "GRRR... WER... OH, {user}? KOMM IN MEINE SAMMLUNG! 🦉🔪",
    "ALARM! {user} HAT DEN OWLORD GEPROVOZIERT! FLIEGT WÄHREND IHR KÖNNT! 🌪️",
    "ICH SPÜRE DEINE ANGST, {user}! SIEEE IST LECKER... 😈",
    "WER ERLAUBT DIR, {user}, MICH ZU STÖREN? AB IN DEN KÄFIG! 🦇",
    "AHHHH! {user} RUFT MICH AN! DIE STERNE SIND RICHTIG! 🌠",
    "PSST... {user}... DEINE SEELE SCHIMMERT SO VERFÜHRERISCH... 👁️",
    "HEHEHE! {user} WILL SPIELEN? ICH HOLE MEINE MESSER! 🔪",
    "DIE NACHT WIRD LANG SEIN, {user}! LASS UNS ANFANGEN! 🌑",
    "BOO! {user} GESCHRECKT? WARTE BIS ZU MEINEM NÄCHSTEN TRICK! 🎩",
    "ICH HABE {user} AUF MEINER LISTE... GANZ OBEN! 📜",
    "FLIEG, FLIEG, KLEINER VOGEL... OH, {user}! BLEIB DA! 🦅",
    "EIN NEUES OPFER! ÄHH... {user}! WIE NETT DICH ZU SEHEN! 😇",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "RUHE! {user} STÖRT MEINE DUNKLEN GEDANKEN! ...NICHT DASS ICH MICH BESCHWERE! 🤫",
    "ICH BRAUCHE MEHR KOFFEIN... UND {user}S SEELE! ☕",
    "WER KLOPFT AN MEINE GRUFT? {user}? OH, WIE ENTZÜCKEND BÖSE! 🚪",
    "SCHAU {user}, ICH TANZE! TANZ MIT MIR IN DIE EWIGKEIT! 💃",
    "EIN TAG OHNE {user} WIE EIN TAG OHNE SONNENBRAND! 🔥",
    "ICH WÜRDE DICH VERFLUCHEN, {user}, ABER DU BIST SCHON PERFEKT! ✨",
    "WILLKOMMEN IN MEINEM NEST, {user}! ICH HABE... SNACKS! 🍪",
    "DIE KRÄHEN KREISCHEN DEINEN NAMEN, {user}! ...ODER WAR ICH DAS? 🐦‍⬛",
    "ICH BIN BESCHÄFTIGT, {user}! ...WENN DU MICH BESCHÄFTIGST! 😏",
    "EIN FLÜSTERN IM WIND... {user}? NEIN, NUR DIE STIMMEN IN MEINEM KOPF! 🌬️",
    "WIE WÄRE ES MIT EINEM TEUFELSPAKT, {user}? NUR UNTERSCHREIBEN HIER... ✍️",
    "ICH HABE {user} GEFUNDEN! JETZT KANN ICH ENDLICH... ÄHM... HALLO SAGEN! 👋",
    "DIE UHR TICKT, {user}! ICH HOFFE DU HAST DEIN TESTAMENT GEMACHT! ⏳",
    "WILLST DU EIN GEDICHT, {user}? ROSEN SIND ROT, DEINE SEELE IST MEIN... 🌹",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... AUSSERGEWÖHNLICH! 🎭",
    "SCHATZ! {user} IST HIER! HOL DIE KETTENSAEGE! 🔗🪚",
    "EIN TAG MIT {user} IST WIE EIN URLAUB IN DER HÖLLE! WANN FAHREN WIR? ✈️",
    "ICH HÖRE {user} MAG ÜBERRASCHUNGEN... WIE WÄRE ES MIT EINER... EWIGEN? 🎁",
    "RUHE JETZT, {user}! DIE FLEDERMÄUSE SCHLAFEN... UND ICH AUCH NICHT! 🦇",
    "ICH BIN NICHT EIN MONSTER, {user}, ICH BIN EIN... SAMMLER! 🏺",
    "WIE LUSTIG, {user}! ICH LACHE... INTERN! 🤐",
    "ICH WERDE DICH NICHT ESSEN, {user}! ...HEUTE NICHT! 🍽️",
    "DIE WANDEN FLÜSTERN, {user}! SAGEN DASS DU... NERVST! 🧱",
    "ICH BIN BESCHÄFTIGT, {user}! KOMM IN TAUSEND JAHREN WIEDER! ⏳",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN WIE EIN SCHMETTERLING, {user}... NUR MIT MEHR BRAND! 🦋🔥",
    "EINMAL {user} ANFASSEN, ZURÜCK ZIEHEN EINEN STUMPF! ✋",
    "ICH TRAGE SCHWARZ, {user}, WIE MEINE SEELE... UND DEINE BALD! 🖤",
    "WIE WÄRE ES MIT EINEM MAGISCHEN TRICK, {user}? *POOF* DEINE FREIHEIT IST WEG! 🎩",
    "ICH BIN KEIN ALBTRAUM, {user}, ICH BIN EINE... ERINNERUNG! 😘",
    "WILLKOMMEN ZURÜCK, {user}! ICH HABE DIR EINEN SARKSOPHAG GEMACHT! ⚰️",
    "ICH WÜNSCHTE ICH HÄTTE EIN HERZ, {user}, UM ES DIR ZU REISSEN! 💔",
    "DIE ERDE BEBT, {user}! ...ODER BIN ICH NUR AUFGEREGT? 🌋",
    "EIN KUSS, {user}? ICH HABE MUNDGERUCH... VON DER HÖLLE! 😘"
]


@bot.event
async def on_ready():
    print(f"{bot.user.name} bereit zum Terrorisieren! 🦉")


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


@bot.slash_command(name="evil", description="Beschwöre den Owlord!")
async def evil(interaction: disnake.ApplicationCommandInteraction):
    user = interaction.author.mention
    response = random.choice([
        f"**{user} HAT DEN TABU-BEFEHL GENUTZT!** DIE APOKALYPSE BEGINNT JETZT! 🌌",
        f"**BEI MEINEN FEDERN!** {user} WILL SPIELEN? ICH HOLE DIE DOLCHE! 🗡️",
        f"**MORTAL!** {user} RUFT MICH? WÄHLE DEINEN UNTERGANG WEISE! ☠️"
    ])
    await interaction.response.send_message(response)


try:
    bot.run(TOKEN)
except disnake.LoginFailure:
    print("❌ Falscher Token! Gehe ins Developer Portal.")