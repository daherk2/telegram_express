from __future__ import division

import telegram

bot = telegram.Bot(token='1005038727:AAGTM9SZCa5a8L90optyKHUnXzk7qc9hqR8')

print(bot.get_me())

print([i.to_json().encode(encoding='UTF-8') for i in bot.get_updates(allowed_updates="1005038727:AAGTM9SZCa5a8L90optyKHUnXzk7qc9hqR8")])

bot.get_chat(-1001404480200).to_json()

print([i.to_json() for i in bot.get_chat_administrators(-1001404480200)])

import telegram;
import time;
import json
bot = telegram.Bot(token='1005038727:AAGTM9SZCa5a8L90optyKHUnXzk7qc9hqR8');
blk_cnt = {}
while True:
    try:
        tm = int(time.time())
        uptds = [json.loads(i.to_json()) for i in bot.get_updates(allowed_updates="1005038727:AAGTM9SZCa5a8L90optyKHUnXzk7qc9hqR8", timout=50, offset=-10, limit=20)]
        fl = open("sample.json", "w")
        fl.write(updts)
        fl.clos
        print( [ (tm - i["message"]["date"]) for i in uptds])
        #print([i["message"]["date"] for i in uptds])
        print([i["message"]["text"] for i in uptds])
        uptds = [i for i in uptds if (tm - i["message"]["date"]) < -6000]
        print(len(uptds))
        if len(uptds) > 0:
            for up in uptds:
                data = up
                badw = [p for p in ["orra", "aralho", "omar no cu", "acete", "erda", "uceta", "into"] if p in data["message"]["text"]]
                #print(badw)
                if len(badw) > 0:
                    try:
                        ts = bot.delete_message(chat_id=int(data["message"]["chat"]["id"]), message_id=int(data["message"]["message_id"]))
                        if ts:
                            try:
                                blk_cnt[str(data["message"]["from"]["id"])] = blk_cnt[str(data["message"]["from"]["id"])] + 1
                            except:
                                blk_cnt[str(data["message"]["from"]["id"])] = 1
                            bot.send_message(chat_id=int(data["message"]["chat"]["id"]), text="Bad words is not allowed on this chat, @"+str(data["message"]["from"]["first_name"]))
                            if blk_cnt[str(data["message"]["from"]["id"])] > 2:
                                print(blk_cnt)
                                valk = bot.kick_chat_member(chat_id=int(data["message"]["chat"]["id"]), user_id=int(str(data["message"]["from"]["id"])))
                                if valk:
                                    bot.send_message(chat_id=int(data["message"]["chat"]["id"]), text="@"+str(data["message"]["from"]["first_name"])+" você será removido.")
                    except Exception as e:
                        print(e)
                        pass
        time.sleep(3)
    except:
        pass
