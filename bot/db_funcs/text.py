from bot.base import database
from bot.utils import BOT_ID


async def add_force_text_msg(value: str) -> None:
    """
    Adds or updates the force text message in the database.

    Args:
        value (str): The force text message to set.
    """
    await database.add_value(int(BOT_ID), "FORCE_TEXT", value)


async def del_force_text_msg() -> None:
    """
    Clears the force text message from the database.
    """
    await database.clear_value(int(BOT_ID), "FORCE_TEXT")


async def get_force_text_msg() -> str:
    """
    Retrieves the current force text message from the database.

    Returns:
        str: The force text message. Defaults to an empty string if not set.
    """
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("FORCE_TEXT", [""])[0] if doc else ""


async def update_force_text_msg(value: str) -> None:
    """
    Updates the force text message in the database.

    This function first deletes the existing force text message and then
    adds the new message.

    Args:
        value (str): The new force text message to set.
    """
    await del_force_text_msg()
    await add_force_text_msg(value)


async def add_start_text_msg(value: str) -> None:
    """
    Adds or updates the start text message in the database.

    Args:
        value (str): The start text message to set.
    """
    await database.add_value(int(BOT_ID), "START_TEXT", value)


async def del_start_text_msg() -> None:
    """
    Clears the start text message from the database.
    """
    await database.clear_value(int(BOT_ID), "START_TEXT")


async def get_start_text_msg() -> str:
    """
    Retrieves the current start text message from the database.

    Returns:
        str: The start text message. Defaults to an empty string if not set.
    """
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("START_TEXT", [""])[0] if doc else ""


async def update_start_text_msg(value: str) -> None:
    """
    Updates the start text message in the database.

    This function first deletes the existing start text message and then
    adds the new message.

    Args:
        value (str): The new start text message to set.
    """
    await del_start_text_msg()
    await add_start_text_msg(value)

# --- Sponsor Text ---
async def add_sponsor_text_msg(value: str) -> None:
    await database.add_value(int(BOT_ID), "SPONSOR_TEXT", value)

async def del_sponsor_text_msg() -> None:
    await database.clear_value(int(BOT_ID), "SPONSOR_TEXT")

async def get_sponsor_text_msg() -> str:
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("SPONSOR_TEXT", [""])[0] if doc else ""

async def update_sponsor_text_msg(value: str) -> None:
    await del_sponsor_text_msg()
    await add_sponsor_text_msg(value)

# --- Sponsor Photo ---
async def add_sponsor_photo_msg(value: str) -> None:
    await database.add_value(int(BOT_ID), "SPONSOR_PHOTO", value)

async def del_sponsor_photo_msg() -> None:
    await database.clear_value(int(BOT_ID), "SPONSOR_PHOTO")

async def get_sponsor_photo_msg() -> str:
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("SPONSOR_PHOTO", [""])[0] if doc else ""

async def update_sponsor_photo_msg(value: str) -> None:
    await del_sponsor_photo_msg()
    await add_sponsor_photo_msg(value)

async def get_sponsor_enabled() -> bool:
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("SPONSOR_ENABLED", [True])[0] if doc else True

async def set_sponsor_enabled(value: bool) -> None:
    await database.clear_value(int(BOT_ID), "SPONSOR_ENABLED")
    await database.add_value(int(BOT_ID), "SPONSOR_ENABLED", value)

async def get_custom_caption_text() -> str:
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("CUSTOM_CAPTION_TEXT", [""])[0] if doc else ""

async def set_custom_caption_text(value: str) -> None:
    await database.clear_value(int(BOT_ID), "CUSTOM_CAPTION_TEXT")
    await database.add_value(int(BOT_ID), "CUSTOM_CAPTION_TEXT", value)

async def del_custom_caption_text() -> None:
    await database.clear_value(int(BOT_ID), "CUSTOM_CAPTION_TEXT")

async def get_custom_caption_enabled() -> bool:
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("CUSTOM_CAPTION_ENABLED", [False])[0] if doc else False

async def set_custom_caption_enabled(value: bool) -> None:
    await database.clear_value(int(BOT_ID), "CUSTOM_CAPTION_ENABLED")
    await database.add_value(int(BOT_ID), "CUSTOM_CAPTION_ENABLED", value)

# --- Start Photo ---
async def add_start_photo_msg(value: str) -> None:
    await database.add_value(int(BOT_ID), "START_PHOTO", value)

async def del_start_photo_msg() -> None:
    await database.clear_value(int(BOT_ID), "START_PHOTO")

async def get_start_photo_msg() -> str:
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("START_PHOTO", [""])[0] if doc else ""

# --- Force Photo ---
async def add_force_photo_msg(value: str) -> None:
    await database.add_value(int(BOT_ID), "FORCE_PHOTO", value)

async def del_force_photo_msg() -> None:
    await database.clear_value(int(BOT_ID), "FORCE_PHOTO")

async def get_force_photo_msg() -> str:
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("FORCE_PHOTO", [""])[0] if doc else ""