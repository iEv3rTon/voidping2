import requests as req
import random
import sys
from os import system
import time
from discord_webhook import DiscordWebhook
from threading import Thread
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)
r = {}
r_s = 0
now = datetime.now()


@app.route('/')
def hello():
  return render_template('index.html',
                         now=now,
                         now2=datetime.now(),
                         code=r,
                         rs=r_s)


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


#keep_alive()
ping = '<@&997263386872139917>'
ping2 = '<@&1118594570893148236>'
ping3 = '<@&1180224195284709506>'
#wh = f'https://discord.com/api/webhooks/1071927421663707196/VDCtFkJY0JRk1uQiBq1PkTUuLPgnBqiKMjfe6ejZZbLoFVQvNHQe0reyl3b05o8V_IPu' # Porra
wh_log = 'https://discord.com/api/webhooks/996830405263114331/JKAp3G6_fyu_sxf6-5wY5MiGmiedyaFJ98ZH0gg921DVDJQCmEB3Ka6xGPnQoNRw3EbN'

wh = 'https://discord.com/api/webhooks/1072337528083976343/jqT1CcWBRPsGdCstM-i6pvQvzcDn-guRWXZ3w5VBWYdV4lCC_vaPe1WplhxJuN1Q9mq1'
wh2 = 'https://discord.com/api/webhooks/1119239972524929085/jUOooMXZugytfMlsFbv5vaNs7j0Nxv8rz0wae470dkNGveVLxzARh1cYPWem0u6k60Ch'

wh3 = 'https://discord.com/api/webhooks/1180324356128243733/IhTt9ALSKFoboEyDao-zpFPpAv1Dq4HS9TPl-28RdmqEVyTk_v8nAE2DOuX6hqKm5wta'

header = {
  "user-agent":
  "Mozilla/5.0 (Linux; Android 11; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36",
  "authority": "pixelplanet.fun",
  "accept": "*/*",
  "accept-language": "en-US,en;q=0.9"
}


def main():
  global r_s, r
  ultimo = 0
  while True:

    r = req.get('https://pixelplanet.fun/api/chathistory?cid=1&limit=30',
                headers=header)
    r_s = r.status_code
    if r.status_code == 200:
      print(r.status_code)
      r = r.text
      #r =  r.replace('/\[|]|,|"/g', '')
      nome = 'event'
      if nome in r:
        print("tem")
        win = 'Threat successfully defeated. Good work!'
        nao = 'Threat couldn'
        f = 'Celebration time over'
        #slep = 28 * 60
        if f in r:
          ultimo = 1
          webhook = DiscordWebhook(url=f'{wh}',
                                   content='O efeito do void acabou.')
          webhook2 = DiscordWebhook(url=f'{wh2}',
                                    content='Se ha acabado el efecto.')
          webhook3 = DiscordWebhook(url=f'{wh3}',
             content='The void effect is over.')
          response = webhook.execute()
          time.sleep(10)
          response2 = webhook2.execute()
          time.sleep(10)
          response3 = webhook3.execute()
          print('F 2s')
          slep = 60 * 60
          time.sleep(slep)

        elif win in r:
          ultimo = 2
          webhook = DiscordWebhook(url=f'{wh}',
                                   content=f'Void ganho, 2/4s {ping}')
          webhook2 = DiscordWebhook(
            url=f'{wh2}', content=f'Se ha ganado el void 2/4s {ping2}')
          webhook3 = DiscordWebhook(
            url=f'{wh3}', content=f'Void defended 2/4s {ping3}')
          response = webhook.execute()
          time.sleep(10)
          response2 = webhook2.execute()
          time.sleep(10)
          response3 = webhook3.execute()

          print('good')
          slep = 29 * 60
          time.sleep(slep)

        elif nao in r:
          ultimo = 3
          webhook = DiscordWebhook(url=f'{wh}', content='Perderam o void! :(')
          webhook2 = DiscordWebhook(url=f'{wh2}',
                                    content='Se ha perdido el void')
          webhook = DiscordWebhook(url=f'{wh3}', content='Lost the void! :(')

          response = webhook.execute()
          time.sleep(10)
          response2 = webhook2.execute()
          time.sleep(10)
          response3 = webhook3.execute()
          print('perderam')
          slep = 60 * 60
          time.sleep(slep)

    else:
      ultimo = 0
      print('Error:', r.status_code)
      webhook = DiscordWebhook(url=f'{wh_log}',
                               content=f'Error: {r.status_code}')
      response = webhook.execute()

      if r.status_code == 403:
        time.sleep(1)
        system("busybox reboot")
    z = random.randint(30, 40)
    time.sleep(z)
    #break


if __name__ == "__main__":
  t = Thread(target=run)
  t.start()

  while True:
    try:
      main()
    except Exception as e:
      print('Deu algum erro, reiniciando em 30s')
      print(e, sys.exc_info()[2].tb_lineno)
      webhook = DiscordWebhook(
        url=f'{wh_log}', content=f'Error 2: {e, sys.exc_info()[2].tb_lineno}')
      response = webhook.execute()

      time.sleep(15)
      system("kill 1")
      time.sleep(15)
