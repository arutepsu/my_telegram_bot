import requests
from config import TOKEN

bot_token = 'YOUR_BOT_TOKEN'
group_name = 'YOUR_GROUP_NAME'

url = f'https://api.telegram.org/bot{TOKEN}/getChat?chat_id=@{"Bot_Test_Group"}'
response = requests.get(url)
data = response.json()

if data['ok']:
    chat_id = data['result']['id']
    print(f"Chat ID for the group '{group_name}': {chat_id}")
else:
    print(f"Error: {data['description']}")