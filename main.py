import telebot, os, re
from telebot.types import *
from pytube import YouTube, Search

print("\033[97;1m[\033[92;1m+\033[97;1m] \x1b[1;38;5;121m MY INFO https://t.me/KING_OF_ENG")
import os
import requests
import time
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
#-------------------#
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'
#-----------------------------------------------------#
bRIMON="\033[1;30m" 
M="\033[1;31m"       
H="\033[1;33m"               
byellow="\033[1;33m"     
bblue="\033[1;34m"        
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
G="\033[1;32m"              
R="\033[1;31m"
AA="\033[1;32m"
BB="\033[1;31m"
CC="\033[1;36m"
X='\033[1;30m'
XX="\x1b[38;5;196m"
GGG="\x1b[38;5;214m"
print(f"""\x1b[1;38;5;121m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢀⠀⠀⠀⣰⡇⢀⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⣿⣰⡀⢠⣿⣇⣾⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣰⣿⣿⢇⣾⣿⣼⣿⢃⡞⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⢋⣾⣿⣿⣿⣯⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢟⣵⣿⣿⣿⣿⣿⣿⣯⡞⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣵⣿⣿⣿⣿⣿⣿⣿⣿⡿⡁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡡⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⢀⣀⣄⣀⡀⡀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡥⠀⠀⠀⠀⠀⠀
⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠘⣿⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀ENG-SAJJAD
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡛⠃⠀⠀
⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀
⠀⠀⠀⠀⠀⢰⣾⣿⣿⣿⣿⣿⠟⠁⠉⠙⠻⠯⡛⠿⠛⠻⠿⠟⠛⠓⠀⠀
⠀⠜⡿⠳⡶⠻⣿⣿⣿⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣽⣧⣾⠛⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠟⠁⠘⠃
  
{G}⋆{GGG}\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m AUTHOR    \x1b[1;97m ● \x1b[1;92m ENG.SAJJAD
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mUESER  \x1b[1;97m    ● \x1b[1;92m@S_J_O_D
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;48m INFO   \x1b[1;97m    ● \x1b[1;92m BOT_YOUTOBE_DOWNLOADER
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mTOOLS     \x1b[1;97m ● \x1b[1;92mNO
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mVERSION   \x1b[1;97m ● \x1b[1;92mV.1                 
{G}⋆{GGG}\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆""")
import os
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
try:
	import requests
except ImportError:
    Z = '''[1;31m'''
R = '''[1;31m'''
X = '''[1;33m'''
F = '''[2;32m'''
C = '''[1;97m'''
B = '''[2;36m'''
Y = '''[1;34m'''
E = '''[1;31m'''
B = '''[2;36m'''
G = '''[1;32m'''
S = '''[1;33m'''
ses = requests.Session()
F = '''[2;32m'''
Z = '''[1;31m'''
L = '''[1;95m'''
E = '''[1;31m'''
G = '''[1;32m'''
S = '''[1;33m'''
Z = '''[1;31m'''
X = '''[1;33m'''
Z1 = '''[2;31m'''
F = '''[2;32m'''
A = '''[2;39m'''
C = '''[2;35m'''
B = '''[2;36m'''
Y = '''[1;34m'''
xxh = '\x1b[38;5;208m'#برتقالي
r1='\x1b[38;5;8m'#رمادي
e1='\x1b[38;5;196m'#احمر
w1='\x1b[38;5;225m'#وردي فاتح جدا
t1='\x1b[38;5;92m'#بنفسجي غامق
y1='\x1b[1;93m'#اصفر نيون
u1='\x1b[1;38;5;203m'#وردي لطيف
i1='\x1b[1;38;5;121m'#اخضر نيون
o1='\x1b[1;96m'#ازرق سماوي
p1='\x1b[38;5;205m'#وردي فاتح
a1='\x1b[38;5;161m'#وردي جميل جدا
S0='\x1b[1;93m'  
S9='\x1b[1;38;5;121m'
S8='\x1b[1;93m'
S7='\x1b[38;5;92m' 
S6='\x1b[1;38;5;121m' 
S5='\x1b[1;38;5;121m'
S4='\x1b[1;96m'
S3='\x1b[1;38;5;121m'
S2='\x1b[38;5;92m' 
S1='\x1b[1;38;5;121m' 
S00='\x1b[1;38;5;121m' 
S99='\x1b[1;96m'
S88='\x1b[1;38;5;121m'
S77='\x1b[38;5;117m'
S66='\x1b[1;32m'
S55='\x1b[38;5;117m'
S44='\x1b[38;5;180m'
S33='\x1b[1;38;5;121m'
S22='\x1b[38;5;117m'
S11='\033[2;35m'
S000='\x1b[38;5;117m'
S999='\x1b[1;32m'
S888='\x1b[38;5;117m'
S777='\x1b[1;38;5;121m'
time1 = time.localtime()
time2 = time.strftime('''%d/%m/%Y''')
print('')
time3 = time.strftime('''%H:%M:%S''')
print('')
print('')
print(f'''{C} \x1b[38;5;208m 𝕋ℍ𝔼 𝔻𝔸𝕋𝔼 \x1b[1;38;5;121m ♥   \x1b[1;38;5;121m   ♣ \x1b[1;96m{time2} \x1b[1;38;5;121m ♣''')
print('')
print(f'''{C} \x1b[38;5;208m 𝕋ℍ𝔼 𝕋𝕀𝕄𝔼 \x1b[1;38;5;121m ♥   \x1b[1;38;5;121m    ♣	\x1b[1;96m{time3} \x1b[1;38;5;121m ♣''')
print()
print(' ✖✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖  ')
print()
TOKEN=input('  \x1b[38;5;117m{\x1b[1;32m•\x1b[38;5;117m}  \x1b[38;5;180m𝐓𝐎𝐊𝐄𝐍  \x1b[1;38;5;121m ๛   \x1b[38;5;117m')
bot = telebot.TeleBot(TOKEN)
print('\033[2;35m')
print(' ✖✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖  ')
print()
print()
print(' ✖✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖  ')
print("the bot is ready to work by @S_J_O_D ")			

# bot = telebot.TeleBot("token")

user_is_search_youtube = ""
search_word = ""


@bot.message_handler(content_types=["text"])
def Yout(message: Message):
    global user_is_search_youtube, search_word
    chat_id = message.chat.id
    user_ = message.from_user
    msg_text = message.text
    if (
        msg_text.startswith("بحث")
        or msg_text.startswith("يوت")
        or msg_text.startswith("يوتيوب")
    ) and len(message.text.split(" ")) > 1:
        bot.send_chat_action(chat_id, "typing")
        user_is_search_youtube = user_.id
        search_word = " ".join(message.text.split(" ")[1:])
        bot.send_message(
            message.chat.id,
            text="هذه العمليات نتيجة للبحث. انقر على الفيديو الذي ترغب في تحميله!",
            reply_markup=MrkSr(search_word),
            reply_to_message_id=message.id,
        )
    else:
        bot.send_message(
            message.chat.id,
            text="للبحث عن فيديو، اكتب إما (بحث) أو (يوت) أو (يوتيوب) ثم كلمة عنوان البحث.",
            reply_to_message_id=message.id,
        )


def extract_video_id(text):
    pattern = r"https://www\.youtube\.com/watch\?v=([^\s&]+)"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return None


def SendOpSr(srWod: str):
    yt = Search(srWod)

    ur = yt.results
    urls = []
    a = 0
    for i in ur:
        if a == 5:
            break
        i = str(i)
        urs = i[i.find("videoId") : i.find(">")].replace("videoId=", "")
        urls.append("https://www.youtube.com/watch?v=" + urs)
        a += 1
    return urls


def MrkSr(word):
    mrk = InlineKeyboardMarkup(row_width=1)
    btns = []
    for url in SendOpSr(word):
        title_video = YouTube(url).title
        btn = InlineKeyboardButton(text=title_video, callback_data=url)
        btns.append(btn)
    mrk.add(*btns)
    return mrk


@bot.callback_query_handler(func=lambda call: True)
def QueryYoutube(call: CallbackQuery):
    chid = call.message.chat.id
    data = call.data
    message = call.message
    user = call.from_user
    v_id = extract_video_id(data)
    if v_id:
        main_url = "https://www.youtube.com/watch?v=" + str(v_id)
        if user_is_search_youtube == user.id:
            bot.send_chat_action(message.chat.id, "upload_video")
            yt = YouTube(data)
            bot.delete_message(message.chat.id, message.id)
            yt.streams.get_highest_resolution().download(filename=search_word + ".mp4")

            bot.send_video(
                message.chat.id,
                open(search_word + ".mp4", "rb"),
                caption=yt.title,
                parse_mode="HTML",
            )
            os.remove(search_word + ".mp4")


bot.infinity_polling(skip_pending=True)
