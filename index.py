import requests
import json

url = "http://mino-sms-panel.xyz/main_api.php"

params = {
    'action': "live-console"
}

headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 15) AppleWebKit/537.36",
    'Accept-Encoding': "gzip, deflate",
    'Authorization': "Bearer usr_6a92c390e873af23",
    'X-Requested-With': "mark.via.gp",
    'Referer': "http://mino-sms-panel.xyz/",
    'Accept-Language': "en-US,en;q=0.9"
}

try:
    response = requests.get(
        url, 
        params=params, 
        headers=headers,
        timeout=10,  # ১০ সেকেন্ড টাইমআউট
        verify=False  # SSL সমস্যা এড়াতে
    )
    
    print(f"Status Code: {response.status_code}")
    print("-" * 50)
    print(response.text)
    
except requests.exceptions.ConnectionError:
    print("❌ Connection Error: Server is not reachable")
    print("Check if the URL is correct and the server is running")
    
except requests.exceptions.Timeout:
    print("❌ Timeout: Server is not responding")
    
except Exception as e:
    print(f"❌ Error: {e}")