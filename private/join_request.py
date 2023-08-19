import logging
import re

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
from telegram.helpers import mention_html

import config
from util.helper import get_text2
from util.regex import JOIN_ID


async def join_request_buttons(update: Update, context: CallbackContext):
    print("join: ", update.chat_join_request)

    share_text = "\n🚨 Nyx News — Aggregierte Nachrichten aus aller Welt mit Quellenangabe und gekennzeichneter Voreingenommenheit der Quelle."

    try:
        await context.bot.approve_chat_join_request(update.chat_join_request.chat.id, update.effective_user.id)

        await update.chat_join_request.from_user.send_photo(
            open("res/nn_info.jpg", "rb"),
            caption=(
                f"Herzlich Willkommen, {update.chat_join_request.from_user.name} ✌🏼\n\n{get_text2(update.chat_join_request.from_user, 'how')}"),
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton("Kanal teilen ⏩",
                                     url=f"https://t.me/share/url?url=https://t.me/nyx_news&text={share_text}")))
    except Exception as e:
        logging.error(e)
        pass


async def accept_join_request(update: Update, context: CallbackContext):
    print(update.callback_query)

    chat_id = re.findall(JOIN_ID, update.callback_query.data)[0]

    try:
        await context.bot.approve_chat_join_request(chat_id, update.effective_user.id)
    except Exception as e:
        logging.error(e)
        pass
    share_text = "\n🚨 Nyx News — Aggregierte Nachrichten aus aller Welt mit Quellenangabe und gekennzeichneter Voreingenommenheit der Quelle."
    await update.callback_query.edit_message_caption(
        f"{get_text2(update.callback_query.from_user, 'how')}\n\n<b>Herzlich Willkommen! Bitte teile Nyx News mit deinen Kontakten</b> 😊",
        reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("Kanal teilen ⏩",
                                 url=f"https://t.me/share/url?url=https://t.me/nyx_news&text={share_text}")))
    await update.callback_query.answer()


async def join_request_ug(update: Update, context: CallbackContext):
    await context.bot.send_message(update.chat_join_request.from_user.id,
                                   f"Hey, {update.chat_join_request.from_user.name} ✌️\n\n"
                                   f"Damit im Lagezentrum von @ukr_ger eine angenhme Atmosphäre bleibt gilt es folgende Regeln zu beachten:\n\n"
                                   f"— Beiträge im entsprechenden Thema, bpsw. passsend zur Region, senden\n\n"
                                   f"— Respektvoller Umgang mit anderen Mitgliedern\n\n"
                                   f"— Wer behauptet, der belegt bei Nachfrage\n\n"
                                   , reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Gruppe beitreten ➡️",
                                 callback_data=f"ugreq_{update.chat_join_request.from_user.id}_{update.chat_join_request.from_user.name}")
        ]]))


async def accept_rules_ug(update: Update, context: CallbackContext):
    user_id, name = update.callback_query.data.split("_")[1:]

    await context.bot.send_message(config.UG_ADMIN,
                                   f"Beitrittsanfrage von {mention_html(user_id, name)}!"
                                   , reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Zulassen ✅", callback_data=f"join_{user_id}")
        ], ]))
