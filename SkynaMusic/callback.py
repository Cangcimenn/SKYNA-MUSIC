from helper.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)







@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("kamu adalah Anonymous Admin !\n\nĀ» kembali ke akun pengguna dari hak admin.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("š” hanya admin dengan izin mengelola obrolan suara yang dapat mengetuk tombol ini !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"āļø **settings of** {query.message.chat.title}\n\nII : pause stream\nā· : resume stream\nš : mute userbot\nš : unmute userbot\nā¢ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("ā¢", callback_data="cbstop"),
                      InlineKeyboardButton("II", callback_data="cbpause"),
                      InlineKeyboardButton("ā·", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("š", callback_data="cbmute"),
                      InlineKeyboardButton("š", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("š Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("ā tidak ada yang sedang streaming", show_alert=True)
        
        
#start



@Client.on_callback_query(filters.regex("cb_start"))
async def cb_start(_, query: CallbackQuery):
    await query.edit_message_text(
       f"""Źį“ŹŹį“ [āØ](https://telegra.ph/file/1c0582e56a00290a96f2a.jpg) **į“”į“Źį“į“į“į“ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
 **ź±į“Źį“ į“į“į“Źį“Ź Źį“į“ į“į“ź±ÉŖį“ į“į“Źį“É¢Źį“į“ !!**
 **Źį“É“É¢ į“į“į“į“į“ į“į“į“į“į“į“Ź į“į“ź±ÉŖį“ į“į“É“ ź±į“Źį“į“į“ į“į“Źį“į“ į“ŹŹį“Źį“É“ ź±į“į“Źį“.**
 **į“ŹÉŖį“ į“į“į“į“į“É“į“ į“É“į“į“į“ į“į“É“É¢į“į“į“Źį“ÉŖ ź±į“į“į“į“ į“į“ŹÉŖÉ“į“į“Ź Źį“į“**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ā Aį“į“ į“į“ ÉŖÉ“ Źį“į“Ź GŹį“į“į“",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(
                    "ā¢ Cį“į“į“į“É“į“s", callback_data="cb_cmd"),],
                [
                    InlineKeyboardButton("ā¢ Oį“”É“į“Ź", url=f"https://t.me/{OWNER_NAME}"),
                    InlineKeyboardButton("ā¢ Dį“į“ į“Źį“į“į“Ź ", url=f"https://t.me/SkyXuser"),
                ],
                [
                    InlineKeyboardButton(
                        "ā¢ Sį“į“į“į“Źį“", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "ā¢ Uį“į“į“į“į“s", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "ā¢ Sį“į“Źį“į“ Cį“į“į“ ā¢", url="https://github.com/Cangcimenn/SKYNA-MUSIC"
                    )
                ],
            ]
        ),
    )

    
    
    
    #Help command
    
    
@Client.on_callback_query(filters.regex("cb_cmd"))
async def cb_cmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""āØ **Hello !**
Ā» **Ņį“Ź į“É“Ź Źį“Źį“ į“É“į“ į“į“į“į“į“É“į“ į“ŹÉŖį“į“ Źį“į“į“į“É“s š­ !**
ā” Powered by [S K Y](https://t.me/SkyXuser)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("į“į“ŹÉŖÉ“į“į“Ź į“į“sį“Ź", callback_data="cb_basic"),
                    InlineKeyboardButton("į“į“ŹÉŖÉ“į“į“Ź Źį“É“į“į“į“į“É“", callback_data="cb_advance"),
                ],               
                [InlineKeyboardButton("Źį“į“į“", callback_data="cb_start")],
            ]
        ),
    )
    
@Client.on_callback_query(filters.regex("cb_basic"))
async def cb_basic(_, query: CallbackQuery):
    await query.edit_message_text(  
        f"""ššš¢š„š”š šš¤š¢š¢šš£š 
        
        
ā¢  `/play (song name)` 
ā¢  `/vplay (song name)` 
ā¢  `/vstream (song name)` 
ā¢  `/skip` - skip the current song
ā¢  `/end` - stop music play
ā¢  `/pause` - pause song play
ā¢  `/resume` - resume song play
ā¢  `/mute` - mute assistant in vc
ā¢  `/lyrics (song name)`
ā” Powered By [S K Y](https://t.me/SkyXuser) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Źį“į“į“", callback_data="cb_cmd")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cb_advance"))
async def cb_advance(_, query: CallbackQuery):
    await query.edit_message_text(    
      f"""šš­š©š§š šš¤š¢š¢šš£ššØ
ā¢ `/ping` pong !!
ā¢ `/start` - Alive msg ~group 
ā¢ `/id` - Find out your grp and your id // stickers id also
ā¢ `/uptime` - š»
ā¢ `/rmd` clean all downloads
ā¢ `/clean` - clear storage 
ā” Powered By [S K Y](https://t.me/SkyXuser) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Źį“į“į“", callback_data="cb_cmd")]]
        ),
    )
    
   
@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("į“į“į“ź° į“į“į“į“ Źį“į“į“É“ į“į“į“ÉŖÉ“ Źį“į“ !", show_alert=True)
    await query.message.delete()
