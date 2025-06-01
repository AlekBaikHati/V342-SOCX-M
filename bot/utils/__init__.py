from .config import config
from .logger import logger

BOT_ID = config.BOT_TOKEN.split(":", 1)[0]

__all__ = ["config", "logger", "expired_date", "BOT_ID", "get_active_db_channel"]

# Fungsi utilitas untuk mengambil DB Channel aktif
async def get_active_db_channel():
    from bot.base import database
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("DATABASE_CHAT_ID_OVERRIDE", [config.DATABASE_CHAT_ID])[0] if doc else config.DATABASE_CHAT_ID
