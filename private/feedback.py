from telegram import Update, MessageOriginUser
from telegram.ext import CallbackContext

import config


async def cancel(update: Update, _: CallbackContext) :
    await update.message.reply_text("Sende nun deine Nachricht oder leite einen Post mit")


async def fwd(update: Update, _: CallbackContext) :
    try:
        await update.message.forward(config.ADMIN_GROUP)
    except:
        await update.message.reply_text("Deine Nachricht konnte nicht weitergeleitet. Überprüfe deine Telegram-Einstellungen und versuche uns erneut zu kontaktieren.")


async def respond_feedback(update: Update, _: CallbackContext):
    try:



            await update.message.copy(update.message.reply_to_message.forward_origin.sender_user.id)

    except Exception as e:
        await update.message.reply_text(
            f"Nutzer hat den Bot blockiert:\n\n{e} - {update.message.reply_to_message}")

