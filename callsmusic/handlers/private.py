# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from ..helpers.filters import command, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
         f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

<i>I am a Group Music Play Bot!</i>  
<i>Specially designed for GroupChat with ❤️ by @xmysteriousx</i>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ BOT OWNER", url="https://t.me/xmysteriousx"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "JOIN OUR GROUP", url="https://t.me/Rezoth_tm"
                    ),
                    InlineKeyboardButton(
                        "JOIN OUR CHANNEL", url="https://t.me/Rezoth"
                    )
                ]
            ]
        )
    )
    
@Client.on_message(command("help") & other_filters2)
async def help(_, message: Message):
    await message.reply_text(
        """<b>How to use me:-</b>
💠 First you should add me <i>(@Mystry_Music_Player_bot)</i> to your group and give me admin permissions.
        
💠 Then you should add my assistant music player account - <i>@Mystry_Music_Player to your groups.</i>
(This account will play music in your groups.)
         
💠Then start a voice chat in your group.
💠Then send a youtube link and reply /play to it.
<i>(You can press /yts to search songs and after sending the link to the group you can reply /play to it.)</i>
💠 If you want to play an audio file send the audio to the group and reply /play to it.
<b>Note</b> :- Queue option has been fixed.
Use /skip for move to the next song.
Use /end for ending the stream.
        
<b>Important rules you should follow.</b>
        
1. You can play youtube links and audio files using me.
2. Do not send song links longer than 10 minutes.
3. Do not send youtube playlists.
That's it.
Hope you enjoy me.🙂
<b><i>Created with ❤️ by @xmysteriousx</i></b>"""
    )
