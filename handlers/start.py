from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/bfc82f0de5ea1d35830f5.jpg")
    await message.reply_text(
        f"""**Hey, I'm PRINSECC MUSIC BOTπ΅

I can play κ¬ΊαΆΘΏαΆΙ  in your group's voice CHAT Powered by [PRINSECC-NETWORK](https://t.me/PRINCESS_NETWORK)

Add me to your group and play music freelyβ£οΈ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π’πππππππΏ π½π", url="https://t.me/PRINCESS_NETWORK")
                  ],[
                    InlineKeyboardButton(
                        "β SUPPORT GROUP β", url="https://t.me/BESTU_1"
                    ),
                    InlineKeyboardButton(
                        "π·οΈ UPDATE CHANNEL π·οΈ", url="https://t.me/PRIN_CESS"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ADD TO GROUP π₯Ί", url="https://t.me/PRINSECC_VC_ROBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**PRINSECC-NETWORK**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SUPPORT β»οΈ", url="https://t.me/PRINCESS_NETWORK")
                ]
            ]
        )
   )


