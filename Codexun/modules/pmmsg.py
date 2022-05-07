from pyrogram import Client
from Codexun.tgcalls import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hey there 👋 I am the music assistant for playing a high quality songs in your groups voice chat. For playing songs you can add our bots\n\n• @RessoMusicBot\n• @CrepanRobot\n• @CreatorPavannetworkbot\n\nFor any type of your queries or questions contact us at @TeamCodexun And don't forget to join @Codexun for regular updates, thanks!")
  return
