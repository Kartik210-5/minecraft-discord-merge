import asyncio

#from minecraft to discord
async def watch_logs(bot, channel_id):

    await bot.wait_until_ready()

    channel = bot.get_channel(channel_id)

    with open(
        "/home/minecraft/mcserver/logs/latest.log",
        "r"
    ) as file:

        file.seek(0,2)

        while True:

            line = file.readline()

            if not line:
                await asyncio.sleep(0.5)
                continue


            if "<" in line and ">" in line:

                start = line.find("<")
                end = line.find(">")

                player = line[start+1:end]

                msg = line[end+2:].strip()


                await channel.send(
                    f"**{player}**: {msg}"
                )