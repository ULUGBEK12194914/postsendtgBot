from telethon import TelegramClient
import asyncio
import os

# Your Telegram API credentials
API_ID = 20650614
API_HASH = "375b652cff9aa411905d9e3af40aa39d"  # Replace with your API Hash
PHONE_NUMBER = "+998949730003"  # Your phone number linked to Telegram

# List of group IDs or usernames where you want to send messages
GROUPS = [
    -1001651340967, -1002229609632, -1001514104584, -1001739925049,
    -1001926112461, -1002115089076, -1002235062051, -1001900765328,
    -1002198131306, -1002041693546, -1001486073147, -1001365812381,
    -1001999903722, -1002097016501, -1001847706166, -1001818392619,
    -1002477044636, -1001518033705, -1001694865718, -1002107682828,
    -1001961685547, -1001199060446, -1002176656775, -1001745925655,
    -1001976176611, -1002298464798, -1002203635516, -1002312808045,
    -1002191685501, -1001444420108, -1001346620244, -1002491627195,
    -1001898131334, -1002287277030, -1001621616534, -1002114785104,
    -1002066293151, -1002499207075, -1002327295600, -1002159076910,
    -1002268119276, -1002036924888, -1002219405309, -1002314603065,
    -1002002952482, -1002098099825
]

# Default settings
MESSAGE = None
INTERVAL = None


# Load configurations from config.txt
def load_config():
    global MESSAGE, INTERVAL
    if os.path.exists("config.txt"):
        with open("config.txt", "r",
                  encoding="utf-8") as f:  # Ensure utf-8 encoding for emojis
            lines = f.readlines()
            if len(lines) >= 2:
                MESSAGE = "".join(lines[:-1]).strip(
                )  # All lines except the last one are part of the message
                INTERVAL = int(
                    lines[-1].strip())  # The last line is the interval


# Function to send messages
async def send_messages():
    load_config()

    if MESSAGE is None or INTERVAL is None:
        print(
            "⚠️ Xabar yoki interval konfiguratsiyasi yo'q. Chiqib ketmoqda...")
        return

    client = TelegramClient("session_name", API_ID, API_HASH)
    await client.start(PHONE_NUMBER)

    print("✅ Xabar yuborish boshladi!")
    while True:
        for group in GROUPS:
            try:
                await client.send_message(group,
                                          MESSAGE,
                                          parse_mode="markdown")
                print(f"✅ Xabar {group} guruhiga yuborildi")
            except Exception as e:
                print(f"❌ Xabar yuborishda xatolik: {e}")

        print(f"⏳ Keyingi xabar {INTERVAL} sekunddan so'ng yuboriladi...")
        await asyncio.sleep(INTERVAL)


# Run the sender
if __name__ == "__main__":
    asyncio.run(send_messages())
