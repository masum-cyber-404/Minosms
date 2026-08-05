import requests

url = "http://mino-sms-panel.xyz/main_api.php"
params = {'action': "live-console"}
headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 15) AppleWebKit/537.36",
    'Authorization': "Bearer usr_6a92c390e873af23",
    'X-Requested-With': "mark.via.gp",
    'Referer': "http://mino-sms-panel.xyz/",
}

try:
    response = requests.get(url, params=params, headers=headers, timeout=10)
    
    # আসল খবর: Header দেখুন
    print("📌 Content-Type:", response.headers.get('content-type'))
    print("📌 Content-Disposition:", response.headers.get('content-disposition'))
    print("-" * 50)
    
    # ২০০ OK পেলে ডাটা প্রিন্ট করুন
    if response.status_code == 200:
        print("✅ ডাটা পাওয়া গেছে:\n", response.text[:500])  # প্রথম ৫০০ অক্ষর
    else:
        print(f"⚠️ Status Code: {response.status_code}")
        print("❌ রেসপন্স:", response.text)

except Exception as e:
    print(f"❌ Error: {e}")
