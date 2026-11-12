import os
import discord
from discord.ext import commands, tasks
from flask import Flask
from threading import Thread

# Tạo web nhỏ để giữ bot luôn thức 24/7
app = Flask('')
@app.route('/')
def home():
    return "Bot dang treo phong thoai!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# Cấu hình bot Discord
intents = discord.Intents.default()
intents.voice_states = True
bot = commands.Bot(command_prefix="!", intents=intents)

# DÁN ID KÊNH THOẠI CỦA BẠN VÀO DÒNG DƯỚI (Thay dãy số mẫu)
CHANNEL_ID = 1557407728735883329

@bot.event
async def on_ready():
    print(f"Đã online: {bot.user}")
    if not keep_in_voice.is_running():
        keep_in_voice.start()

@tasks.loop(seconds=30)
async def keep_in_voice():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        vc = discord.utils.get(bot.voice_clients, guild=channel.guild)
        if not vc or not vc.is_connected():
            try:
                await channel.connect(self_deaf=True, self_mute=True)
            except Exception as e:
                print(e)

Thread(target=run_web).start()
bot.run(os.environ.get("TOKEN"))
