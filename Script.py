class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>
ɪᴛ'ꜱ ᴠᴇʀy ᴇᴀꜱy ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ɪɴ yᴏᴜʀ ɢʀᴏᴜᴩ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ,
ᴛʜᴀᴛꜱ ᴀʟʟ ɪ'ʟʟ ᴩʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇꜱ ᴛʜᴇʀᴇ 😇
"""
    HELP_TXT = """•"""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/The_user_death>ᴩʀᴏꜰᴇꜱᴇʀ</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- This bot is not a open source project. 

<b>DEVS:</b>
- <a href=https://t.me/The_user_death>ᴩʀᴏꜰᴇꜱᴇʀ</a>"""
    MANUELFILTER_TXT = """ꜰɪʟᴛᴇʀꜱ

- Filter is the feature were users can set automated replies for a particular keyword and <a href=https://t.me/{}>{}</a> will respond whenever a keyword is found the message

<b>NOTE:</b>
- ᴛʜɪꜱ ʙᴏᴛ should have admin privillage.
- only admins can add filters in a chat.
- alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Buttons

- ᴛʜɪꜱ ʙᴏᴛ  Supports both url and alert inline buttons.

<b>NOTE:</b>
- Telegram will not allows you to send buttons without any content, so content is mandatory.
- ᴛʜɪꜱ ʙᴏᴛ  supports buttons with any telegram media type.
- Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/FILIMPIRATESGROUP)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Auto Filter

<b>NOTE:</b>
- Make me the admin of your channel if it's private.
- make sure that your channel does not contains camrips, porn and fake files.
- Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    BATCH_TXT = """
𝙵𝙸𝙻𝙴 𝚂𝚃𝙾𝚁𝙴 𝙼𝙾𝙳𝚄𝙻𝙴../


𝙱𝚈 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚂𝚃𝙾𝚁𝙴 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝙼𝚈 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 𝙰𝙽𝙳 𝙸 𝚆𝙸𝙻𝙻 𝙶𝙸𝚅𝙴 𝚈𝙾𝚄 𝙰 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙻𝙸𝙽𝙺 𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙴 𝚂𝙰𝚅𝙴𝙳 𝙵𝙸𝙻𝙴𝚂.𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰 𝙿𝚄𝙱𝙻𝙸𝙲 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴 𝙻𝙸𝙽𝙺 𝙾𝙽𝙻𝚈 𝙾𝚁 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙼𝙰𝙺𝙴 𝙼𝙴 𝚃𝙷𝙴 𝙰𝙳𝙼𝙸𝙽 𝙸𝙽 𝚃𝙷𝙴𝙸𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂..../

⪼ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴 ›

✯ /plink ›› 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝙼𝙴𝙳𝙸𝙰 𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝙽𝙺.
✯ /pbatch ›› 𝚄𝚂𝙴 𝚈𝙾𝚄𝚁 𝙼𝙴𝙳𝙸𝙰 𝙻𝙸𝙽𝙺 𝚆𝙸𝚃𝙷 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.
✯ /batch ›› 𝚃𝙾 𝙲𝚁𝙴𝙰𝚃𝙴 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙼𝚄𝙻𝚃𝙸𝙿𝙻𝙴 𝙿𝙾𝚂𝚃.

✎ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 ›

/batch https://t.me/c/1749754594/332 https://t.me/c/1749754594/336"""
    ALIVE_TXT = """
ALIVE MODULE
• /alive - check me alive or dead🤧
Just for a rasam😂"""
    INFO_TXT = """
Information

Get information about something!

Commands and Usage:
• /id - get id of a specifed user.
• /info  - get information about a user.

NOTE:
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    CONNECTION_TXT = """ᴄᴏɴɴᴇᴄᴛɪᴏɴ

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """ɪɴꜰᴏ

<b>NOTE:</b>
these are the extra features of <a href=https://t.me/{}>{}</a>

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Admin ᴍᴏᴅ

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
* 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
* 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
* 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
* 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
