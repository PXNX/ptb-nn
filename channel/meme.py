import logging

from telegram import Update
from telegram.ext import CallbackContext

from constant import FOOTER_MEME


async def post_media_meme_nx(update: Update, context: CallbackContext):
    if update.channel_post.media_group_id is None:
        await add_footer_meme(update, context)

    elif update.channel_post.media_group_id not in context.chat_data:
        await add_footer_meme(update, context)

        context.job_queue.run_once(
            remove_media_group_id,
            20,
            update.channel_post.media_group_id,
            str(update.channel_post.media_group_id),
        )


# TODO: make method more generic
# TODO: apply footer only to 1st entry of mediagroup
async def add_footer_meme(update: Update, context: CallbackContext):
    context.chat_data[update.channel_post.media_group_id] = update.channel_post.id

    if update.channel_post.caption is None:
        original_caption = ""
    else:
        original_caption = update.channel_post.caption_html_urled

    try:

        await update.channel_post.edit_caption(await format_meme_footer(original_caption))

        # Unfortunately it is not possible for bots to forward a mediagroup as a whole.

    #   await update.channel_post.forward(chat_id=NX_MAIN)
    # await update.channel_post.forward(chat_id=-1001618190222)
    except Exception as e:
        logging.error(f"Error when posting media: {e}")


async def remove_media_group_id(context: CallbackContext):
    del context.chat_data[context.job.context]


async def post_text_meme_nx(update: Update, _: CallbackContext):
    try:
        await update.channel_post.edit_text(
            await format_meme_footer(update.channel_post.text_html_urled), disable_web_page_preview=False
        )

    #   await update.channel_post.forward(chat_id=NX_MAIN)
    #  await update.channel_post.forward(chat_id=-1001618190222)

    except Exception as e:
        logging.error(f"Error when posting text: {e}")


async def format_meme_footer(original_text: str) -> str:
    return f"{original_text}{FOOTER_MEME}"


async def append_buttons_news(update: Update, context: CallbackContext):
    if update.message.text is not None:
        text = update.message.text_html_urled

    elif update.message.caption is not None:
        text = update.message.caption_html_urled
    else:
        return
