import httpx
import hashlib
from time import time

T_SECRET = 26714187


def generate_api_secret(timestamp: str) -> str:
    return "KOjDJSavxhqM1Z" + str(int(timestamp) % T_SECRET) + "Xa6fucp2t0nFYdACe2d+Xxm"


def calculate_sign(payload: dict) -> str:
    payload.pop("sign") if payload.get("sign") is not None else ""
    text = ""
    for key, value in sorted(zip(payload.keys(), payload.values())):
        text += key + "=" + value
    return hashlib.md5(text.encode()).hexdigest()


def main():
    params = {
        'country': 'US',
        'product': 'gravity',
        'sys_lang': 'en',
        'uwd': '++CUaf/+JFP9R8FEnXvxOdLms6MEaA19jQ1m3JhZm+Wp1K1aM8ODclP60pMUw1wJ',
        'app_version': '10.7.1',
        'user_country': '',
        'idfa': 'juOwtzKZsQHwMov+aUW9MQ==',
        'sign': '99c544a90ebf0c10341546f93a4e589d',
        'sim_country': 'us',
        'pkg': 'anonymous.sns.community.gravity',
        'languageV2': 'en',
        'referrer': 'Organic',
        'operator_name': 'Android',
        'app_version_code': '451',
        'zone': '0',
        'system_version': '11',
        'sdk_version': '30',
        'model': 'Pixel_5a',
        'device': 'android',
        'brand': 'Genymobile',
        'ts': str(int(time())),
    }
    api_secret = generate_api_secret(params["ts"])
    params["api_security"] = api_secret
    sign = calculate_sign(params)
    params["sign"] = sign
    params.pop("api_security")
    response = httpx.get('https://api.gravity.place/gravity/common/getimpornword', params=params, headers={
        'Host': 'api.gravity.place',
        'User-Agent': 'okhttp/3.12.13',
    })
    print(response.json())
    print(response.status_code)


if __name__ == "__main__":
    main()