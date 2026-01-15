import os
import logging
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", 8080))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_server():
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()

threading.Thread(target=run_server, daemon=True).start()


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration - Get from environment variables
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_USERNAME = '@free_blender_courses'
CHANNEL_ID = os.environ.get('CHANNEL_ID')  # Your channel ID (e.g., -1001234567890)

# Create the bot client
app = Client(
    "caption_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.private & filters.command("start"))
async def start_command(client: Client, message: Message):
    """Handle /start command in private chat"""
    try:
        await message.reply_text(
            "Hello! I'm Caption Bot officially reserved for @free_blender_courses\n\n"
            "The trick and repo is paid, please contact in discussion group for further purchases."
        )
        logger.info(f"📩 /start command received from user {message.from_user.id}")
    except Exception as e:
        logger.error(f"❌ Error handling /start command: {e}")

@app.on_message(filters.channel & (filters.document))
async def handle_media(update:Update,client: Client, message: Message):
    """Handle media files posted in the channel"""
    message = update.message
    try:
        # Add 30 second delay before editing caption
        logger.info(f"⏳ Waiting 2 minutes and 30 seconds before editing caption for message {message.id}...")
        await asyncio.sleep(150)
        
        # Check if this is your channel (if CHANNEL_ID is set)
        if CHANNEL_ID and str(message.chat.id) != CHANNEL_ID:
            return
        
        # Get the original caption
        original_caption = message.caption or ""
        
        # Create new caption with channel promotion
        if original_caption:
            new_caption = f"{message.document.file_name}\n{original_caption}\n\n"
        else:
            new_caption = message.document.file_name
        
        new_caption += f"📢 [Join Free Blender Courses](https://t.me/free_blender_courses)\n"
        new_caption += f"🔔 [Stay tuned for updates!](https://t.me/free_blender_courses)"
        
        # Edit the message caption
        await message.edit_caption(new_caption)
        
        logger.info(f"✅ Caption updated for message {message.id} in {message.chat.title}")
        
    except Exception as e:
        logger.error(f"❌ Error updating caption: {e}")

# Start the bot
if __name__ == "__main__":
    if not all([API_ID, API_HASH, BOT_TOKEN]):
        logger.error("❌ Missing required environment variables: API_ID, API_HASH, or BOT_TOKEN")
    else:
        logger.info("🚀 Bot starting...")
        app.run()
        logger.info("✅ Bot is running!")
