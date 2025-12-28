import os
from pyrogram import Client, filters

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_URL = os.environ["CHANNEL_URL"]

CAPTION_TEXT = (
    f'<a href="{CHANNEL_URL}">Join free courses</a>\n'
    'Stay tuned for updates'
)

app = Client(
    "caption_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.channel & ~filters.text)
async def add_caption(client, message):

    if not (
        message.document or message.video or message.audio
        or message.voice or message.photo
    ):
        return

    old_caption = message.caption or ""

    if "Join free courses" in old_caption:
        return

    new_caption = (
        f"{old_caption}\n\n{CAPTION_TEXT}"
        if old_caption else CAPTION_TEXT
    )

    try:
        await message.edit_caption(
            new_caption,
            parse_mode="html"
        )
    except:
        pass

app.run()
