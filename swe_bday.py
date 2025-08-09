import streamlit as st
import base64
import time
import requests
import random

# --- Page setup ---
st.set_page_config(page_title="Happy Birthday ❤️", layout="wide")

# --- Set background image ---
def set_background(image_file):
    with open(image_file, "rb") as img:
        img_bytes = base64.b64encode(img.read()).decode()
        css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{img_bytes}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

# --- Play music ---
def play_music(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        b64 = base64.b64encode(audio_bytes).decode()
        st.markdown(f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """, unsafe_allow_html=True)

# --- Button style ---
st.markdown("""
    <style>
    button[kind="primary"] {
        background: linear-gradient(to right, #ff416c, #ff4b2b) !important;
        border: none !important;
        color: white !important;
        font-size: 20px !important;
        border-radius: 50px !important;
        padding: 10px 30px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- Messages ---
# love_24_things = [
#     "🌟 Your beautiful smile that lights up my world",
#     "🎶 The way you sing even when no one is listening",
#     "💖 How you always believe in me no matter what",
#     "🍫 Your cute obsession with chocolate",
#     "📚 Your curiosity and love for learning",
#     "🫶 How you hold my hand and make me feel safe",
#     "🎨 Your creativity in every little thing you do",
#     "🌸 The way you care so deeply about others",
#     "😂 Your laugh that makes everything better",
#     "💋 Every kiss, it's magical",
#     "🧸 How you look adorable even when angry",
#     "🎥 Watching cheesy movies with you is the best",
#     "🥰 Your tiny surprises that make my day",
#     "💬 How you listen to everything I say (even my nonsense)",
#     "🎈 Your inner child that's full of fun and wonder",
#     "🧁 How you always share your last bite with me",
#     "🏞️ Your love for nature and little adventures",
#     "🌙 Those deep talks we have at midnight",
#     "💪 How strong and resilient you are",
#     "👑 You make me feel like the luckiest person alive",
#     "🫂 Every hug from you feels like home",
#     "✨ Your aura, your vibe - it's pure magic",
#     "🌈 The way you make gloomy days feel sunny",
#     "💞 Simply... just being YOU"
# ]

intro_message = (
    "🎂 Today’s not just any day – it’s the magical birthday of my dearest papa, gundu, chello, and pattuma! 💖🎉\n\n"
    "24 special wishes, straight from my heart, just for you 😘💌\n"
    "Each one is filled with love, laughter, and all the reasons you make my world beautiful 🌈✨\n\n"
    "Ready to unwrap the love? Let’s begin! 🎁💫"
)


birthday_wishes = [
    "🎉 Happy Birthday, papa! Today is all about you and the joy you bring into my life. 🥹💖",
    "💖 Gundu, you make my heart smile every single day. Have the happiest birthday ever!",
    "🌟 Chello, your smile lights up even my dullest days. Keep shining, birthday girl! ✨",
    "🐥 Pattuma, you're my cute little sunshine. I’m so lucky to have you! 🌞",
    "🎁 Chello, you're the sweetest soul I know. Wishing you endless happiness today!",
    "💫 Papa, you’re my moon, my stars, and everything in between. Happy Birthday, my world! 🌙",
    "🎈 Gundu, let’s make beautiful memories today!🎊",
    "🍫 Pattuma, sweeter than any chocolate – that’s you! Happiest Birthday!",
    "🎶 Chello, your voice, your laugh — it’s music to my heart. Love you more every day!",
    "💐 Papa, you bloom with love and warmth. I’ll always keep you close in my heart.",
    "👑 Chello, you rule my heart like a queen. Today, we celebrate YOU! 👸",
    "🍰 Gundu, you make life so much more delicious and fun. Happy Birthday, partner!",
    "🐼 My cute little gundu bear, wishing you all the cuddles and joy in the world today! 🧸",
    "🌈 Pattuma, you add all the colors to my life. I'm forever grateful for you.",
    "🧁 Papa, if love was a dessert, you’d be the sweetest of all. Here’s to you! 🍰",
    "📸 Chello, let’s make today one for the photo album – full of smiles, hugs, and love!",
    "🫶 Gundu, my heartbeat, my everything – have the best birthday ever! 💞",
    "🎇 Papa, you light up my life in ways you’ll never fully know. Happy Birthday, love!",
    "🌻 Chello, keep growing, glowing, and being the amazing you that I adore. 💛",
    "🥳 Gundu, let’s celebrate you today! Laugh loud, dance crazy – you deserve it all!",
    "🧸 Pattuma, I just want to hold you tight and never let go. Happy Birthday, my cutie!",
    "🍭 Papa, you’re my sweet little miracle born on this day. So, so loved. 💗",
    "🧿 Gundu, may this year bring you only good vibes, smiles, and warm hugs. 🤗",
    "🫂 Chello, you’ll always have my heart. Big birthday hugs from your forever person. 💖"
]

message_intro_24="""On your 24th birthday, here are 24 things I absolutely love about you\n
\n
\n
YES, I’m shamelessly asking you to keep doing all of this.
\n
\n
Stay clingy, overshare like there’s no filter, call me randomly even if it’s just to say 'hiiiii', annoy me endlessly with your mood swings, double-text me like your life depends on it, message me while brushing, bathing, eating, or breathing, check on me every 1 hours like I’m a plant that needs watering, keep being dramatic over the smallest things, throw tantrums if I take too long to reply, and never stop calling me gundu — I’m here for every bit of it, forever 💖"""

love_24_things = [
    "💬 Your non-stop talking during late-night calls… I swear, even if it's 3 or 4 or 5 AM, I could listen to you forever.",
    "📞 A sudden call from you, even if it’s just for 1 or 2 minutes, makes my whole day — it’s all I crave.",
    "💬 Double messages from you? They hit harder than love letters.",
    "📲 When you spam me with Instagram reels in a row, bro I swear — that’s my love language now.",
    "📸 Sending me those random photos you didn’t even filter — that’s when I know, I’m your person.",
    "🧃 When you act sweet and innocent — I'm gone, completely gone.",
    "🥺 Your little 'sorry' face could melt glaciers.",
    "🍱 When you ask 'Did you eat?' it sounds a lot like 'I love you deeply'.",
    "📲 You texting me again before I reply? That’s peak romance in my world.",
    "🎭 Your drama is award-worthy, but don’t change — I’m your biggest fan.",
    "💌 Even a one-word message from you feels like a love song.",
    "🌦️ When you say you miss me after 10 minutes… that's pure gold.",
    "🧠 Thinking of me during work? That’s the love I want to live in.",
    "🎤 Your random singing is the cutest concert I’ve ever attended.",
    "📝 You planning things for ‘us’ gives my heart a reason to dream more.",
    "🐥 When you call me ‘Gundu’, even the stars get jealous.",
    "😠 You annoying me is actually the weirdest way I feel your love.",
    "👩‍💻 When you ask me coding doubts — that mix of cute and brilliant is just unfair.",
    "💬 The way you express your feelings without filters — that honesty is everything to me.",
    "🫂 After a fight, when you don’t give up on me — that’s real love right there.",
    "🫶 During fights, when you don’t show ego — I feel safe with you even in storms.",
    "💗 When you choose peace over revenge during our worst moments — that’s when I fall deeper.",
    "📞 You calling me just to say 'nothing, just felt like it' — please never stop that.",
    "❤️ I love you 3000 — especially when you don’t give up on me, even when I mess up."
]

gift_24_intro=""""On your 24th birthday, I planned 24 special gifts just for my Gundu!

Each gift was carefully chosen with you in mind — not just as presents, but as little reminders of the bond we share. Every item has a special purpose: to bring a smile to your face, make your daily moments brighter, and be useful in ways big or small.

Whether it’s to brighten your day, add a touch of comfort, or simply make you laugh, these gifts are meant to create memories and keep me close to you, even when I’m not around.

It’s my way of saying — you matter, you’re loved, and I’m always thinking of you. So, get ready for some surprises that celebrate you, our moments together, and all the fun still to come!

"""

messages = [
    "🎉 Happy Birthday, My Love! ❤️",
    intro_message,
    *birthday_wishes,
    message_intro_24,
    *love_24_things,
    "Gundu ,🎁 Ready for real surprises? 🎁",
    "3",
    "2",
    "1",
    gift_24_intro,
    """Let's play a game 🎉

    
    Spin a Gift 🎁

    Click that gift 🖱️

    Try to guess it using the hint 🔍

    Open the gift 🎀""",
    "",
    "💌 Are you surprised? Are you happy? Or are you *very very* happy? 🥹\nOnce again... Happy Birthday Papa! 💖\n\nNow it’s your turn — leave me a note below 📝👇",
    "🎉🎉🎉 Happy 24th Birthday, My Love! May this year be your most magical one yet! 💖🎂"
]

# --- Set background image ---
set_background("swe_background.jpg")

# --- Session state ---
if "started" not in st.session_state:
    st.session_state.started = False
if "index" not in st.session_state:
    st.session_state.index = 0
if "opened_gifts" not in st.session_state:
    st.session_state.opened_gifts = set()
if "ballooned" not in st.session_state:
    st.session_state.ballooned = False

# --- Navigation ---
def go_next():
    if st.session_state.index < len(messages) - 1:
        st.session_state.index += 1

def go_back():
    if st.session_state.index > 0 and st.session_state.index !=55:
        print(st.session_state.index)
        st.session_state.index -= 1
    elif st.session_state.index ==55:
        print("back to gifts")
        st.session_state.index-=4
        print(st.session_state.index)

# --- Start screen ---
if not st.session_state.started:
    st.markdown("<div style='text-align:center; padding-top:200px;'>", unsafe_allow_html=True)
    if st.button("🥳 Let the Celebration Begin ❤️", key="start_button"):
        st.session_state.started = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- Main slideshow ---
if st.session_state.started:
    play_music("blue.mp3")

    if st.session_state.index == 0 and not st.session_state.ballooned:
        st.balloons()
        st.session_state.ballooned = True

    if messages[st.session_state.index] in ["3", "2", "1"]:
        st.markdown(
            f"""
            <div style='text-align:center; padding:150px;'>
                <h1 style='font-size:180px; color:white; text-shadow:4px 4px 8px #000000;'>
                    {messages[st.session_state.index]}
                </h1>
            </div>
            """, unsafe_allow_html=True
        )
        time.sleep(1)
        
        go_next()
        st.rerun()

    elif st.session_state.index == len(messages) -3:
        # --- Gift Grid Slide ---
        st.balloons()
        st.title("🎁 Spin a Gift")

        # Initialize gift list
        if 'gifts_left' not in st.session_state:
            st.session_state.gifts_left = [f"Gift {i}" for i in range(1, 25)]
            st.session_state.gifts_spun = []

        # Spin button
        if st.button("🎉 Spin for a Gift!"):
            if st.session_state.gifts_left:
                chosen_gift = random.choice(st.session_state.gifts_left)
                st.session_state.gifts_left.remove(chosen_gift)
                st.session_state.gifts_spun.append(chosen_gift)
                st.markdown(f"You got: 🎁 *{chosen_gift}*")
            else:
                st.warning("You've opened all the gifts!🎁")

        # Reset
        if st.button("🔄 Reset"):
            st.session_state.gifts_left = [f"Gift {i}" for i in range(1, 25)]
            st.session_state.gifts_spun = []
            st.info("Gifts reset. Ready to spin again!")
        st.markdown("""<style>
            .lovely-tile button {
                height: 150px !important;
                width: 100% !important;
                font-size: 32px !important;
                font-weight: bold;
                border: none;
                background-color: #ff99cc !important;
                color: white !important;
                border-radius: 20px;
                margin-bottom: 15px;
            }
            .lovely-tile-opened button {
                background-color: #d63384 !important;
                color: white !important;
            }
            .gift-title {
                font-size: 40px;
                color: #ff4081;
                text-align: center;
                font-weight: bold;
                margin-bottom: 30px;
            }
        </style>""", unsafe_allow_html=True)

        st.markdown('<div class="gift-title">🎁 24 Surprise Gifts Just for You 💝</div>', unsafe_allow_html=True)

        gifts = [
    {"name": "Cerlac", "hint": "A nostalgic and sweet treat for your inner child — I knew you'd love it because you liked that Insta reel 😉, and it also gives you a healthy snack"},
    {"name": "Stud", "hint": "Small and elegant jewelry to match any outfit, and it’s cute on you 💎"},
    {"name": "RCB Jersey", "hint": "This will be your most unexpected gift — you will fly once you see this! And especially, this is the most unexpected thing from me for you in our life. Guess what? And don’t forget to look around 😉"},
    {"name": "Headphone Adaptor", "hint": "For those moments when your iPhone meets an old-school friend"},
    {"name": "Phone Case", "hint": "Turns every mirror selfie into pure magic — straight from the wizarding world 🪄"},
    {"name": "This gift will give you tomorrow, sorry gundu", "hint": "It’s already on the way, sorry gundu 😢 — you’ll have it tomorrow, but it’s worth the wait! ⏳"},
    {"name": "Mouse", "hint": "A pink little companion so in every move at work I will be remembered 💖"},
    {"name": "Eye Palette", "hint": "Shades to make your eyes sparkle for any occasion ✨ (thanks to Pooja)"},
    {"name": "Headset", "hint": "Talk to me hands-free — no more worrying if your mom is coming 😏"},
    {"name": "Brush", "hint": "Start your day remembering me — I got you an ultra-soft one! 😂"},
    {"name": "Leg Bracelet", "hint": "Adorned with an evil eye symbol to protect you and add a touch of charm wherever you go ✨"},
    {"name": "Light", "hint": "A colorful light to brighten your room and mood with every shade ✨"},
    {"name": "Pillow", "hint": "Soft and comfy — so you can remember me every time you rest💤"},
    {"name": "Watch", "hint": "No need to guess — you already opened it, bro! Hope you liked the watch. "},
    {"name": "Lipstick", "hint": "A touch of magic to make your smile unforgettable ✨ (thanks to Charu)"},
    {"name": "Sheet Mask", "hint": "For that pre-wedding radiance — hope you wear it before your sister’s wedding, it’ll be useful! 💆‍♀️"},
    {"name": "Hand Bag", "hint": "This is your go-to when you step out — so every time you carry it, you’ll remember me and laugh 😄"},
    {"name": "Key Chain", "hint": "Tuck me in your bag’s zip — so whenever you open or close your laptop bag, I will be remembered 🎒"},
    {"name": "Head Buma", "hint": "Not sure what it’s called, but I’m sure it’ll look cute on you — like a little papa! 😄🎀"},
    {"name": "Water Color", "hint": "You asked for this a while ago — I might’ve forgotten to buy it then, but here it is now, I think you kinda guessed this on Friday night 😉"},
    {"name": "This gift will give you tomorrow, sorry gundu", "hint": "It’s already on the way, sorry gundu 😢 — you’ll have it tomorrow, but it’s worth the wait! ⏳"},
    {"name": "Eye Liner", "hint": "Not quite sure how you use this magic on your eyes, but it definitely adds that wow factor — thanks to Charu ✨"},
    {"name": "Hair Band", "hint": "Soft hugs for your hair to keep it stylish and comfy all day 💖🎀"},
    {"name": "Hair Straightener", "hint": "No need to guess — you already got this (Hair brush)! Hoping you’ll do Kalkal’s long hair in different styles and send me pics too! 💇‍♀️"}
]


        def handle_click(i):
            st.session_state.opened_gifts.add(i)
            st.balloons()
            st.markdown(f"""
                <div style=" background-color:white; color:#d63384; font-size:20px; font-weight:bold; padding:20px;
                border-radius:15px; text-align:center; box-shadow:0px 4px 10px rgba(0,0,0,0.2); margin-top:20px;">
                💖 Hint: {gifts[i]['hint']}
                </div>
            """, unsafe_allow_html=True)

        cols_per_row = 7
        for row in range(6):
            cols = st.columns(cols_per_row)
            for col_idx in range(cols_per_row):
                idx = row * cols_per_row + col_idx
                if idx >= len(gifts):
                    continue
                is_opened = idx in st.session_state.opened_gifts
                btn_label = f"✅ {idx+1}" if is_opened else f"🎁{idx+1}"
                css_class = "lovely-tile-opened" if is_opened else "lovely-tile"
                with cols[col_idx]:
                    st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
                    if st.button(btn_label, key=f"gift_{idx}"):
                        handle_click(idx)
                    st.markdown("</div>", unsafe_allow_html=True)
    elif st.session_state.index == len(messages) - 2:
        st.balloons()
        st.markdown(
            f"""
            <div style='text-align:center; padding:0px;'>
                <h1 style='font-size:42px; color:white; text-shadow:2px 2px 4px #000000;'>{messages[st.session_state.index]}</h1>
            </div>
            """, unsafe_allow_html=True
        )

        # --- Telegram Note Sender ---

        
        def send_to_telegram(note):
            TELEGRAM_TOKEN = st.secrets["telegram"]["TELEGRAM_TOKEN"]
            CHAT_ID = st.secrets["telegram"]["CHAT_ID"]
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            data = {'chat_id': CHAT_ID, 'text': f"🎂 New Birthday Note:\n\n{note}"}
            response = requests.post(url, data=data)
            print(response.json())
        style = "font-size:18px; color:white; background:rgba(0,0,0,0.5); padding:10px; border-radius:8px;"
        # st.markdown("<div style='text-align:center; max-width:800px; margin:auto;'>", unsafe_allow_html=True)
        st.markdown(
                    f"""
                    <div style='text-align:center; padding:10px;'>
                        <h1 style='{style}'>{"✍️ Your Message to Me"}</h1>
                    </div>
                    """, unsafe_allow_html=True
                )
        with st.form("note_form"):
            note = st.text_area("Write your message here (the longer the better 😉)", height=200)
            submitted = st.form_submit_button("Send return gift 🎈")
            if submitted and note.strip():
                send_to_telegram(note)
                style = "font-size:20px; color:white; background:rgba(0,0,0,0.5); padding:30px; border-radius:20px;"
                st.markdown(
                    f"""
                    <div style='text-align:left; padding:10px;'>
                        <h1 style='{style}'>{"🎊 I got your note! Thank you! you can send as many you want it makes me more happy😉"}</h1>
                    </div>
                    """, unsafe_allow_html=True
                )
                # st.markdown()
        st.markdown("</div>", unsafe_allow_html=True)

        col1,col2, col3 = st.columns([1,3, 1])
        with col1:
            st.button("💖 One More Look", key="back_return", on_click=go_back)
        with col3:
            st.button("🌸 One Last Time", key="final_slide", on_click=go_next)

    # elif st.session_state.index == len(messages) - 2:
    #     # Return message input
    #     st.markdown(
    #         """
    #         <div style='text-align:center; padding:80px;'>
    #             <h1 style='font-size:42px; color:white; text-shadow:2px 2px 4px #000000;'>
    #                 💌 Are you surprised? Are you happy? Or are you <i>very very</i> happy? 🥹<br>
    #                 Once again... Happy Birthday darling! 💖
    #             </h1>
    #         </div>
    #         """,
    #         unsafe_allow_html=True
    #     )
    #     st.markdown("### ✍️ Your Message to Me")
    #     return_note = st.text_area("Write your message here (the longer the better 😉)", height=200, key="return_note")
    #     if return_note:
    #         st.success("Aww... Thank you for sharing! 💕")

    #     col1, col3 = st.columns([1, 1])
    #     with col1:
    #         st.button("💖 Back", key="back_return", on_click=go_back)
    #     with col3:
    #         st.button("🌸 Final Surprise", key="final_slide", on_click=go_next)

    elif st.session_state.index == len(messages) - 1:
        # Final Happy 24th Birthday Slide
        for _ in range(3):
            st.balloons()
            time.sleep(0.5)

        st.markdown(
            """
            <div style='text-align:center; padding:80px;'>
                <h1 style='font-size:72px; color:#ff66b2; text-shadow:4px 4px 10px #000000;'>
                    🎉🎉🎉 Happy 24th Birthday, My Love! 🎂💖
                </h1>
                <p style='font-size:28px; color:white;'>
                    This day is all about YOU — your joy, your smile, and the magic you bring to everyone around. <br>
                    May this year be full of love, laughter, dreams fulfilled, and sweet surprises. <br><br>
                    ∞Love you always, forever and ever. ∞✨
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2,col3 = st.columns([1,4, 1])
        with col1:
            st.button("💌 Re-send Message", key="back_to_message", on_click=go_back)
        with col3:
            st.button("💖 Replay Celebration", key="restart", on_click=lambda: st.session_state.update({"index": 0, "started": True, "ballooned": False}))

    else:
        # General slide
        display_msg = messages[st.session_state.index]
        style = "font-size:42px; color:white; text-shadow:2px 2px 4px #000000;"
        if st.session_state.index == 0:
            style = "font-size:72px; color:white; text-shadow:4px 4px 8px #000000;"
        elif st.session_state.index == len(messages) - 4:
            style = "font-size:36px; color:white; background:rgba(0,0,0,0.5); padding:30px; border-radius:20px;"
        else:
            style = "font-size:36px; color:white; background:rgba(0,0,0,0.5); padding:30px; border-radius:20px;"
        st.balloons()
        st.markdown(
            f"""
            <div style='text-align:center; padding:100px;'>
                <h1 style='{style}'>{display_msg}</h1>
            </div>
            """, unsafe_allow_html=True
        )

    if messages[st.session_state.index] not in ["3", "2", "1"] and st.session_state.index not in [len(messages)-1, len(messages)-2]:
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            if st.session_state.index > 0:
                st.button("💖 One More Look", key="back_btn", on_click=go_back)
        with col3:
            st.button("🌸 Next Sweet Moment", key="next_btn", on_click=go_next)

# import streamlit as st
# import base64
# import time
# import requests

# # --- Page setup ---
# st.set_page_config(page_title="Happy Birthday ❤️", layout="wide")

# # --- Set background image ---
# def set_background(image_file):
#     with open(image_file, "rb") as img:
#         img_bytes = base64.b64encode(img.read()).decode()
#         css = f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/jpeg;base64,{img_bytes}");
#             background-size: cover;
#             background-position: center;
#             background-attachment: fixed;
#         }}
#         </style>
#         """
#         st.markdown(css, unsafe_allow_html=True)

# # --- Play music ---
# def play_music(file_path):
#     with open(file_path, "rb") as audio_file:
#         audio_bytes = audio_file.read()
#         b64 = base64.b64encode(audio_bytes).decode()
#         st.markdown(f"""
#             <audio autoplay loop>
#                 <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
#             </audio>
#         """, unsafe_allow_html=True)

# # --- Button style ---
# st.markdown("""
#     <style>
#     button[kind="primary"] {
#         background: linear-gradient(to right, #ff416c, #ff4b2b) !important;
#         border: none !important;
#         color: white !important;
#         font-size: 20px !important;
#         border-radius: 50px !important;
#         padding: 10px 30px !important;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.2);
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- Messages ---
# love_24_things = [
#     "🌟 Your beautiful smile that lights up my world",
#     # add remaining if needed...
# ]

# messages = [
#     "🎉 Happy Birthday, My Love! ❤️",
#     "On this 24th birthday, here are 24 things I absolutely love about you 💖",
#     *love_24_things,
#     "Ready for more surprises?",
#     "3",
#     "2",
#     "1",
#     "On your 24th birthday, I planned 24 special gifts just for you!",
#     "Let's play a game! Here's how it works:<br>1. Pick any gift card from the grid<br>2. Click it to see a surprise hint<br>3. Smile, you're loved!",
#     "💌 Are you surprised? Are you happy? Or are you *very very* happy? 🥹<br>Once again... Happy Birthday darling! 💖<br><br>Now it’s your turn — leave me a note below 📝👇",
#     "🎉🎉🎉 Happy 24th Birthday, My Love! May this year be your most magical one yet! 💖🎂"
# ]

# # --- Set background image ---
# set_background("swe_background.jpg")

# # --- Session state ---
# if "started" not in st.session_state:
#     st.session_state.started = False
# if "index" not in st.session_state:
#     st.session_state.index = 0
# if "opened_gifts" not in st.session_state:
#     st.session_state.opened_gifts = set()
# if "ballooned" not in st.session_state:
#     st.session_state.ballooned = False

# # --- Navigation ---
# def go_next():
#     if st.session_state.index < len(messages) - 1:
#         st.session_state.index += 1

# def go_back():
#     if st.session_state.index > 0:
#         st.session_state.index -= 1

# # --- Start screen ---
# if not st.session_state.started:
#     st.markdown("<div style='text-align:center; padding-top:200px;'>", unsafe_allow_html=True)
#     if st.button("🥳 Let the Celebration Begin ❤️", key="start_button"):
#         st.session_state.started = True
#         st.rerun()
#     st.markdown("</div>", unsafe_allow_html=True)

# # --- Main slideshow ---
# if st.session_state.started:
#     play_music("blue.mp3")

#     if st.session_state.index == 0 and not st.session_state.ballooned:
#         st.balloons()
#         st.session_state.ballooned = True

#     current_message = messages[st.session_state.index]

#     if current_message in ["3", "2", "1"]:
#         st.markdown(
#             f"""
#             <div style='text-align:center; padding:150px;'>
#                 <h1 style='font-size:180px; color:white; text-shadow:4px 4px 8px #000000;'>{current_message}</h1>
#             </div>
#             """, unsafe_allow_html=True
#         )
#         time.sleep(1)
#         go_next()
#         st.rerun()

#     elif st.session_state.index == len(messages) - 3:
#         # --- Gift Grid Slide ---
#         st.markdown("""<style>
#             .lovely-tile button {
#                 height: 150px !important;
#                 width: 100% !important;
#                 font-size: 32px !important;
#                 font-weight: bold;
#                 border: none;
#                 background-color: #ff99cc !important;
#                 color: white !important;
#                 border-radius: 20px;
#                 margin-bottom: 15px;
#             }
#             .lovely-tile-opened button {
#                 background-color: #d63384 !important;
#                 color: white !important;
#             }
#             .gift-title {
#                 font-size: 40px;
#                 color: #ff4081;
#                 text-align: center;
#                 font-weight: bold;
#                 margin-bottom: 30px;
#             }
#         </style>""", unsafe_allow_html=True)

#         st.markdown('<div class="gift-title">🎁 24 Surprise Gifts Just for You 💝</div>', unsafe_allow_html=True)

#         gifts = [{"name": f"Gift {i+1}", "hint": f"This is a hint for gift {i+1}"} for i in range(24)]

#         def handle_click(i):
#             st.session_state.opened_gifts.add(i)
#             st.balloons()
#             st.markdown(f"""
#                 <div style="background-color:white; color:#d63384; font-size:20px; font-weight:bold; padding:20px;
#                 border-radius:15px; text-align:center; box-shadow:0px 4px 10px rgba(0,0,0,0.2); margin-top:20px;">
#                 💖 Hint: {gifts[i]['hint']}
#                 </div>
#             """, unsafe_allow_html=True)

#         cols_per_row = 5
#         for row in range(6):
#             cols = st.columns(cols_per_row)
#             for col_idx in range(cols_per_row):
#                 idx = row * cols_per_row + col_idx
#                 if idx >= len(gifts):
#                     continue
#                 is_opened = idx in st.session_state.opened_gifts
#                 btn_label = f"✅ {idx+1}" if is_opened else f"🎁{idx+1}"
#                 css_class = "lovely-tile-opened" if is_opened else "lovely-tile"
#                 with cols[col_idx]:
#                     st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
#                     if st.button(btn_label, key=f"gift_{idx}"):
#                         handle_click(idx)
#                     st.markdown("</div>", unsafe_allow_html=True)

#     elif st.session_state.index == len(messages) - 2:
#         st.markdown(
#             f"""
#             <div style='text-align:center; padding:80px; max-width:800px; margin:auto;'>
#                 <h1 style='font-size:42px; color:white; text-shadow:2px 2px 4px #000000;'>{current_message}</h1>
#             </div>
#             """, unsafe_allow_html=True
#         )

#         # --- Telegram Note Sender ---
#         TELEGRAM_TOKEN = '8261791423:AAH-tbyT2KGwHdNsBXPMwDiK7zH4feSJLKs'
#         CHAT_ID = '1155480692'

#         def send_to_telegram(note):
#             url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
#             data = {'chat_id': CHAT_ID, 'text': f"🎂 New Birthday Note:\n\n{note}"}
#             response = requests.post(url, data=data)
#             print(response.json())

#         st.markdown("<div style='text-align:center; max-width:800px; margin:auto;'>", unsafe_allow_html=True)
#         st.markdown("### ✍️ Your Message to Me")
#         with st.form("note_form"):
#             note = st.text_area("Write your message here (the longer the better 😉)", height=200)
#             submitted = st.form_submit_button("Send Your Wishes 🎈")
#             if submitted and note.strip():
#                 send_to_telegram(note)
#                 st.success("🎊 Your note was sent! Thank you!")
#         st.markdown("</div>", unsafe_allow_html=True)

#         col1,col2, col3 = st.columns([1,3, 1])
#         with col1:
#             st.button("💖 Back", key="back_return", on_click=go_back)
#         with col3:
#             st.button("🌸 Final Surprise", key="final_slide", on_click=go_next)

#     elif st.session_state.index == len(messages) - 1:
#         for _ in range(3):
#             st.balloons()
#             time.sleep(0.5)
#         st.markdown(
#             """
#             <div style='text-align:center; padding:80px; max-width:800px; margin:auto;'>
#                 <h1 style='font-size:72px; color:#ff66b2; text-shadow:4px 4px 10px #000000;'>🎉🎉🎉 Happy 24th Birthday, My Love! 🎂💖</h1>
#                 <p style='font-size:28px; color:white;'>
#                     This day is all about YOU — your joy, your smile, and the magic you bring to everyone around. <br>
#                     May this year be full of love, laughter, dreams fulfilled, and sweet surprises. <br><br>
#                     Love you always, forever and ever. 💑✨
#                 </p>
#             </div>
#             """, unsafe_allow_html=True
#         )
#         col1, col2,col3 = st.columns([1, 3,1])
#         with col1:
#             st.button("💌 Re-read Message", key="back_to_message", on_click=go_back)
#         with col3:
#             st.button("💖 Replay Celebration", key="restart", on_click=lambda: st.session_state.update({"index": 0, "started": True, "ballooned": False}))

#     else:
#         style = "font-size:42px; color:white; text-shadow:2px 2px 4px #000000;"
#         if st.session_state.index == 0:
#             style = "font-size:72px; color:white; text-shadow:4px 4px 8px #000000;"
#         elif st.session_state.index == len(messages) - 4:
#             style = "font-size:36px; color:white; background:rgba(0,0,0,0.5); padding:30px; border-radius:20px;"
#         st.markdown(f"<h1 style='{style}'>{current_message}</h1>", unsafe_allow_html=True)

#     if current_message not in ["3", "2", "1"] and st.session_state.index not in [len(messages)-1, len(messages)-2]:
#         col1, col2, col3 = st.columns([1, 3, 1])
#         with col1:
#             if st.session_state.index > 0:
#                 st.button("💖 One More Look", key="back_btn", on_click=go_back)
#         with col3:
#             st.button("🌸 Next Sweet Moment", key="next_btn", on_click=go_next)

