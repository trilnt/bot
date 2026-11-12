import os
import asyncio
import discord
from discord.ext import commands, tasks
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "Bot dang treo phong thoai!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

intents = discord.Intents.default()
intents.voice_states = True
bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1557407728735883329

@bot.event
async def on_ready():
    print(f"Đã online: {bot.user}")
    if not keep_in_voice.is_running():
        keep_in_voice.start()

@tasks.loop(seconds=60)
async def keep_in_voice():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        return

    vc = discord.utils.get(bot.voice_clients, guild=channel.guild)
    if not vc or not vc.is_connected():
        try:
            if vc:
                await vc.disconnect(force=True)
                await asyncio.sleep(3)
            # reconnect=False giúp tránh kẹt vòng lặp nếu mạng Render lag nhẹ
            await channel.connect(self_deaf=True, self_mute=True, timeout=30.0, reconnect=False)
            print(f"Đã vào kênh thoại: {channel.name}")
        except Exception as e:
            print(f"Chờ nhịp sau để kết nối lại: {e}")

Thread(target=run_web).start()
bot.run(os.environ.get("TOKEN"))
