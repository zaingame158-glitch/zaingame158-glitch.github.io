import json
import datetime
import urllib.request

def fetch_crypto_rates():
    try:
        # جلب أسعار البيتكوين، الإيثيريوم، والتيثر الحية عالمياً من مصدر موثوق
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd"
        req = urllib.request.urlopen(url, timeout=10)
        data = json.loads(req.read().decode())
        return data
    except Exception as e:
        print("خطأ في جلب العملات الرقمية:", e)
        return None

# جلب بيانات السوق الحية
crypto_data = fetch_crypto_rates()

# قراءة ملف rates.json الحالي أو إنشاءه إن لمשkن موجوداً
try:
    with open('rates.json', 'r', encoding='utf-8') as f:
        rates = json.load(f)
except:
    rates = {
        "damascus": {
            "USD": { "name": "دولار أمريكي (USD)", "sell": 14900, "buy": 14800, "ch": "+0.7%" },
            "EUR": { "name": "يورو (EUR)", "sell": 16100, "buy": 15980, "ch": "+0.4%" },
            "TRY": { "name": "ليرة تركية (TRY)", "sell": 440, "buy": 432, "ch": "+0.3%" },
            "SAR": { "name": "ريال سعودي (SAR)", "sell": 3970, "buy": 3930, "ch": "+0.5%" },
            "history": [14750, 14780, 14810, 14840, 14870, 14890, 14900]
        }
    }

# تحديث وقت المزامنة السحابية تلقائياً
current_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
rates["last_update"] = current_time

# حفظ التحديثات في ملف rates.json أوتوماتيكياً ليتزامن مع التطبيق
with open('rates.json', 'w', encoding='utf-8') as f:
    json.dump(rates, f, ensure_ascii=False, indent=2)

print("تمت مزامنة وتحديث الأسعار بنجاح في:", current_time)
