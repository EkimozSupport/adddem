from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, ben {bn} 🎵

Grubunuzun sesli aramasında müzik çalabilirim. geliştiricim :  [Aphe](https://t.me/HzAphe).

Beni grubunuza ekleyin ve özgürce müzik çalın!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/Infinity-Bots/GroupMusicPlayerBot")
                  ],[
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/ApheMusicSupport"
                    ),
                    InlineKeyboardButton(
                        "🔊 Kanal", url="https://t.me/ApheMusicNews"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Beni Grubuna Ekle ➕", url="https://t.me/ApheMusicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Grup Müzik Çalar Çevrimiçi✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ApheMusicNews")
                ]
            ]
        )
   )


