from hydrogram import Client, filters
from hydrogram.helpers import ikb
from hydrogram.types import Message
from hydrogram.enums import ParseMode
import asyncio

from bot import authorized_users_only, config, helper_handlers, logger, url_safe
from plugins import list_available_commands
from bot.utils import get_active_db_channel
from bot.db_funcs.text import get_custom_caption_enabled, get_custom_caption_text


@Client.on_message(
    filters.private & ~filters.me & ~filters.command(list_available_commands)
)
@authorized_users_only
async def generate_handler(client: Client, message: Message) -> None:
    # Check generate status
    if not helper_handlers.generate_status:
        return

    try:
        database_chat_id = await get_active_db_channel()
        custom_caption_enabled = await get_custom_caption_enabled()
        custom_caption_template = await get_custom_caption_text()

        original_caption = message.caption or ""

        # Copy the message to the database chat dulu
        message_db = await message.copy(
            database_chat_id,
            caption=None,  # Caption sementara None, nanti diupdate setelah dapat link
            parse_mode=ParseMode.HTML
        )

        # Encode message ID
        encoded_data = url_safe.encode_data(
            f"id-{message_db.id * abs(database_chat_id)}"
        )
        encoded_data_url = f"https://t.me/{client.me.username}?start={encoded_data}"

        # Baru lakukan replace di custom caption
        if custom_caption_enabled and custom_caption_template:
            caption = custom_caption_template
            caption = caption.replace("{original_caption}", original_caption)
            caption = caption.replace("{link_file}", encoded_data_url)
        else:
            caption = original_caption if original_caption else None

        # Tambahkan jeda sebelum edit caption
        await asyncio.sleep(3)  # 3 detik, bisa dinaikkan jika masih sering FloodWait

        # Update caption di pesan yang sudah dikirim (edit caption)
        await client.edit_message_caption(
            chat_id=database_chat_id,
            message_id=message_db.id,
            caption=caption,
            parse_mode=ParseMode.HTML
        )

        # Create a shareable URL & 
        share_encoded_data_url = f"https://t.me/share/url?url={encoded_data_url}"
        db_url = f"https://t.me/c/{str(database_chat_id)[4:]}/{message_db.id}"
        
        # Reply to the user with the generated URL
        await message.reply_text(
            encoded_data_url,
            quote=True,
            reply_markup=ikb([
                [("Share", share_encoded_data_url, "url")], 
                [("Lihat DataBase", db_url, "url")]
            ]),
            disable_web_page_preview=True,
        )
    except Exception as exc:
        # Log the error and inform the user
        logger.error(f"Generator: {exc}")
        await message.reply_text("<b>An Error Occurred!</b>", quote=True)
