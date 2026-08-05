from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # আসল API তে কল করুন
        url = "http://mino-sms-panel.xyz/main_api.php"
        params = {'action': 'live-console'}
        headers = {
            'Authorization': 'Bearer usr_6a92c390e873af23',
            'X-Requested-With': 'mark.via.gp',
            'Referer': 'http://mino-sms-panel.xyz/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        res = requests.get(url, params=params, headers=headers, timeout=10)
        
        # সফল হলে ডাটা দেখান
        return jsonify({
            "success": True,
            "status_code": res.status_code,
            "data": res.text
        })
    except Exception as e:
        # এরর হলে সেটা দেখান
        return jsonify({
            "success": False,
            "error": str(e)
        })

# Vercel এর জন্য handler (এটা অবশ্যই রাখতে হবে)
handler = app
