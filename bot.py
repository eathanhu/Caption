from pyrogram import Client, filters

API_ID = 123456        # your api_id
API_HASH = "API_HASH"  # your api_hash
BOT_TOKEN = "BOT_TOKEN"

CHANNEL_TAG = "@free_blender_couses"

app = Client(
    "caption_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.channel & ~filters.text)
async def add_caption(client, message):
    # Skip messages that cannot have captions
    if not message.caption and not (
        message.document or message.video or message.audio or
        message.voice or message.photo
    ):
        return

    old_caption = message.caption or ""

    if CHANNEL_TAG in old_caption:
        return  # already exists

    new_caption = (
        f"{old_caption}\n\n{CHANNEL_TAG}"
        if old_caption
        else CHANNEL_TAG
    )

    try:
        await message.edit_caption(new_caption)
    except:
        pass

app.run()
