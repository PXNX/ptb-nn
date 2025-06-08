import logging

from telegram import Update
from telegram.ext import CallbackContext

from bot. group.bingo import handle_bingo

putin_dict = {
    "️Angriff": "erzwungene Selbstverteidigung",
    "️Arrest": "Einladung zu einem Vorstellungsgespräch",
    "️Flüchtlinge": "Neonazis und Drogenabhängige",
    "️Arbeitslose": "Arbeitsferien",
    "️Bombardierungen": "Entmilitarisierung",
    "️Schlachten": "Bohrer",
    "Verluste": "Fälschungen",
    "️Kriegsführung": "Sondereinsätze",
    "️Bombardierung": "klatschen",
    "️Invasion": "Entmilitarisierung",
    "️Ausfall": "wirtschaftliche Umstrukturierung",
    "️Verhör": "Befragung",
    "️Diktatur": "Demokratie",
    "️Beschäftigung": "Befreiung",
    "️Neubehandlung": "Umgruppierung",
    "️Rückgang": "negatives Wachstum",
    "️Folter": "Vorbereitung auf ein Vorstellungsgespräch",
    "️Entzug": "wirtschaftliche Optimierung",
    "️Sanktion": "Stärkung der eigenen Wirtschaft",
    "️Zensur": "Meinungsfreiheit",
    "️Wirtschaftssanktionen": "Importsubstitution",
    "️Faschismus": "Entnazifizierung",
    "️Mobilisiert": "Russische Eliteeinheit",
    "️Waschmaschine": "Chip-Spender",
    "Trauer": "mysteriöser Todesfall",
    "️Absturz": "schnelle taktische Landungsoperation",
    "️Krieg": "dreitägige Spezialoperation",
    "️Agent": "kritischer Journalist",
    "️Journalist": "feindlicher Spion",
    "️Wohnhaus": "militärische Stellung",
    "Schule": "Nazi-Hauptquartier",
    "Flucht": "Umgruppierung in eine strategisch bessere Position",
    "Zwangsrekrutierte": "Freiwillige",
    "Rückzug": "negativer Gebietsgewinn",
    "Friendlyfire": "Frühjahrsputz",
    "Putintroll": "braver Mitbürger",
    "Putler": "Zar Vladimir der Einzige",
    "Hilfsgüter": "ukrainische Kokaintransporte"
}


async def handle_putin_dict(update: Update, _: CallbackContext):
    matches = {}

    for k, v in putin_dict.items():
        if k.lower() in update.message.text.lower():
            matches[k] = v

    if matches:
        logging.info(f"{update.message.text} -------{matches, putin_dict}")
        text = "☝🏼 Laut der neuen putin'schen Rechtschreibung hast du hier ein paar Fehler gemacht:"
        for k, v in matches.items():
            text += f"\n\n❗️ „{k}” muss „{v}” lauten!"
        await update.message.reply_text(text)


async def handle_other_chats(update: Update, context: CallbackContext):
    await handle_bingo(update, context)
    await handle_putin_dict(update, context)
