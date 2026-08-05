import requests

url = "http://mino-sms-panel.xyz/main_api.php"

params = {
  'action': "live-console"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 15; Infinix X6837 Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/150.0.7871.181 Mobile Safari/537.36",
  'Accept-Encoding': "gzip, deflate",
  'Authorization': "Bearer usr_6a92c390e873af23",
  'X-Requested-With': "mark.via.gp",
  'Referer': "http://mino-sms-panel.xyz/",
  'Accept-Language': "en-US,en;q=0.9"
}

response = requests.get(url, params=params, headers=headers)

print(response.text)