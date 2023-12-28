from telethon import TelegramClient
import requests

api_id = 25550874
api_hash = '676d7af26ee168508241b33916a15732'

# async def load_history_to_save(self):
#   entity = await self.client.get_entity(channel_id)
#   async for message in self.client.iter_messages(entity, reverse=True, offset_id=latest_id, limit=None):
#       print(message.text)

# client = TelegramClient('anon', api_id, api_hash)
# print('client', client)

# # async def main():
# #   await client.send_message('me', 'Hello, myself!')
# async def main():
#   await client.connect()
#   print('connect success')
#   entity = await client.get_entity("-1001167700230")
#   print('entity', entity)
#   async for message in client.iter_messages(entity,
#                                             reverse=True,
#                                             offset_id=0,
#                                             limit=10):
#     print(message.text)
#     print(111111111)
#   print(22222222)

# with client:
#   client.loop.run_until_complete(main())


class Tg:
  base_url = "https://api.telegram.org"
  token = "6259304223:AAFytA8oeQPnE8C9mYG5YI3ZJwhItLBXkb4"
  re_s = None

  def __init__(self):
    self.re_s = requests.session()

  def method2(self):
    # base_url = "https://tg.sexglobal18.win"
    last_url = "{}/bot{token}/getUpdates".format(self.base_url,
                                                 token=self.token)
    print("last_url", last_url)
    result = self.re_s.get(last_url)
    print("result", result.text)

  def send_message(self, chat_id):
    last_url = "{}/bot{token}/sendMessage".format(self.base_url,
                                                  token=self.token)
    print("last_url", last_url)
    data = {"chat_id": chat_id, "text": "24234234"}
    result = self.re_s.post(last_url, data)
    print("result", result.text)


if __name__ == '__main__':
  tg = Tg()
  # tg.method2()
  tg.send_message(chat_id="6914683782")
