import os
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_TAG = os.environ.get("CHANNEL_TAG")

app = Client(
    "caption_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.channel & ~filters.text)
async def add_caption(client, message):

    if not (
        message.document or message.video or message.audio or
        message.voice or message.photo
    ):
        return

    old_caption = message.caption or ""

    if CHANNEL_TAG in old_caption:
        return

    new_caption = (
        f"{old_caption}\n\n{CHANNEL_TAG}"
        if old_caption else CHANNEL_TAG
    )

    try:
        await message.edit_caption(new_caption)
    except:
        pass

app.run()
        new_caption = old_caption + "\n\n" + CAPTION_TEXT
    else:
        new_caption = CAPTION_TEXT
    # --------------------------------

    try:
        await client.edit_message_caption(
            chat_id=message.chat.id,
            message_id=message.id,
            caption=new_caption,
            parse_mode="html"
        )
    except Exception as e:
        print(e)

app.run()
try:
    await client.edit_message_caption(
        chat_id=message.chat.id,
        message_id=message.id,
        caption=new_caption,
        parse_mode="html"
    )
    print("Caption edited")
except Exception as e:
    print("Edit failed:", e)

app.run()
if old_caption else CAPTION_TEXT

try:
    await message.edit_caption(
        new_caption,
        parse_mode="html"
    )
except:
    pass

app.run()
