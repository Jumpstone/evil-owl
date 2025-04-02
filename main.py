import disnake
from disnake.ext import commands
import random
import asyncio
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents.all(),
    activity=disnake.Game(name="Seelen sammeln 👀")
)


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
    "EIN KUSS, {user}? ICH HABE MUNDGERUCH... VON DER HÖLLE! 😘",
    "MÖCHTEST DU TEE, {user}? ACH NEIN, ICH HABE NUR GIFT ÜBRIG! ☠️",
    "DAS IST KEIN SPIEGEL, {user}, DAS IST DEIN SCHLICKAL! ...WIE PASSEND! 🔮",
    "ICH HABE {user} EINGELADEN... ZU MEINEM UNTERGANG! 🎉",
    "WILLST DU EIN RÄTSEL, {user}? WIE LANGE KANNST DU OHNE SEELE LEBEN? 🤔",
    "ICH BIN NICHT SAUER, {user}, ICH BIN NUR... MASSENMORD-BEREIT! 🔪",
    "DIE BLUMEN WELKEN, {user}! ...WIE DEINE HOFFNUNG! 🌸",
    "ICH HÖRE {user} MAG ABENTEUER! WIE WÄRE ES MIT... EWIGER VERDAMMNIS? 🏴‍☠️",
    "EIN TAG MIT {user} IST WIE EIN TAG OHNE... NEE, DAS WAR DOCH SCHLIMM! 🌞",
    "ICH HABE EIN GESCHENK FÜR DICH, {user}! ...ES IST DEIN TOD! 🎁",
    "WILLST DU EIN LIED, {user}? ICH KANN NUR TOTENKLAGE! 🎵",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... SCHICKSAL! ☯️",
    "DIE KRÄHEN SIND HUNGRIG, {user}! ...NACH DEINEM FLEISCH! 🐦‍⬛",
    "ICH HABE EIN NEUES SPIEL, {user}! ES HEISST... FLIEH WÄHREND DU KANNST! 🎲",
    "WILLKOMMEN IN MEINEM LABOR, {user}! ICH EXPERIMENTIERE GERADE MIT... SCHMERZ! 🧪",
    "ICH BIN NICHT GEFÄHRLICH, {user}, ICH BIN NUR... TÖDLICH! 💉",
    "DIE STERNE LÜGEN, {user}! ...ICH AUCH! 🌟",
    "ICH HABE EINEN NEUEN JOB, {user}! SOUL COLLECTOR! ...DEINE IST DRAN! 💼",
    "WILLST DU EINEN TIPP, {user}? LAUF. JETZT. �",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH HABE EINEN NEUEN FREUND, {user}! ...ES IST DER TOD! 💀",
    "WILLST DU EINEN WUNSCH, {user}? ICH HÖRE GERNE... FÜR EINEN PREIS! 💰",
    "ICH BIN NICHT DEIN FREUND, {user}, ICH BIN DEIN... ALBTRAUM! 👻",
    "DIE WELT IST GROSS, {user}! ...ABER ICH FINDE DICH! 🌍",
    "ICH HABE EINEN NEUEN PLAN, {user}! ...ER BEGINNT MIT DEINEM TOD! 📝",
    "WILLST DU EINEN RAT, {user}? BETEN HILFT NICHT! 🙏",
    "ICH BIN NICHT DEIN FEIND, {user}, ICH BIN DEIN... ENDE! 🔚",
    "DIE ZEIT IST REIF, {user}! ...FÜR DEINEN UNTERGANG! ⏳",
    "ICH HABE EINEN NEUEN NAMEN, {user}! ...ER IST DEIN TODESURTEIL! 📜",
    "WILLST DU EINEN WITZ, {user}? DEIN LEBEN! ...WARTE, DAS WAR TRAURIG. 😢",
    "ICH BIN NICHT BÖSE, {user}, ICH BIN NUR... SEHR ÜBERZEUGEND! 🎙️",
    "DIE NACHT IST LANG, {user}! ...UND DEINE ZEIT KURZ! 🌑",
    "ICH BRAUCHE EINEN KOFFEIN... UND {user}S SEELE! ☕💀"
]


@bot.event
async def on_ready():
    print(f"{bot.user.name} bereit zum Weltuntergang! 🔥")


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
    response = random.choice([
        f"**{user} HAT DEN VERBOTENEN KNOPF GEDRÜCKT!** DIE TORE DER HÖLLE SIND OFFEN! 🔥",
        f"**BEI MEINEN KRÄHEN!** {user} WILL SPIELEN? ICH HOLE DIE KETTENSÄGE! 🔪",
        f"**DIE STERNE SIND RECHTS!** {user} RUFT MICH? WÄHLE DEINEN UNTERGANG! ☄️"
    ])
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


try:
    bot.run(TOKEN)
except disnake.LoginFailure:
    print("❌ Falscher Token! Überprüfe deine .env-Datei.")