from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from SankiMusic.utilities.config import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀𝐇𝐞𝐥𝐩𝐬🥀",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬🥀", callback_data="settings_helper"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀𝐀𝐝𝐝 𝐌𝐞 𝐆𝐫𝐨𝐮𝐩🥀",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀𝐇𝐞𝐥𝐩🥀", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="☆𝐂𝐡𝐚𝐧𝐧𝐞𝐥☆", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="☆𝐆𝐫𝐨𝐮𝐩☆", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="☆𝐘𝐨𝐮𝐓𝐮𝐛𝐞☆", url="https://youtube.com/@yummi_sport_07"
            ),
            InlineKeyboardButton(
                text="☆𝐎𝐰𝐧𝐞𝐫☆", url=config.OWNER_ID
            )
        ]
     ]
    return buttons
