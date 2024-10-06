from pprint import pprint

import httpx
from time import time
from uuid import uuid4
from hashlib import md5
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

T_SECRET = 26714187
KEY = "baisimeji9262019"
IV = "qrstuvwxyz123456"


def encrypt(plain_text: str) -> str:
    return b64encode(AES.new(key=KEY.encode(), iv=IV.encode(), mode=AES.MODE_CBC).encrypt(
        pad(data_to_pad=plain_text.encode(), block_size=AES.block_size))).decode()


def generate_api_secret(timestamp: str) -> str:
    return "KOjDJSavxhqM1Z" + str(int(timestamp) % T_SECRET) + "Xa6fucp2t0nFYdACe2d+Xxm"


def calculate_sign(payload: dict) -> str:
    payload.pop("sign") if payload.get("sign") is not None else ""
    text = ""
    for key, value in sorted(zip(payload.keys(), payload.values())):
        text += key + "=" + value
    return md5(text.encode()).hexdigest()


def main():
    data = {
        'country': 'US',
        'product': 'gravity',
        'sys_lang': 'en',
        'uwd': encrypt(str(uuid4()).upper()),
        'app_version': '10.7.1',
        'user_country': '',
        'idfa': 'juOwtzKZsQHwMov+aUW9MQ==',
        'sim_country': 'us',
        'pkg': 'anonymous.sns.community.gravity',
        'languageV2': 'en',
        'referrer': 'default',
        'operator_name': 'Android',
        'app_version_code': '451',
        'zone': '0',
        'system_version': '11',
        'sdk_version': '30',
        'model': 'Pixel_5a',
        'device': 'android',
        'brand': 'Google',
        'ts': str(int(time())),
    }

    api_secret = generate_api_secret(data["ts"])
    data["api_security"] = api_secret
    sign = calculate_sign(data)
    data["sign"] = sign
    data.pop("api_security")
    pprint(data)
    response = httpx.post('https://api.gravity.place/gravity/user/checkInstall', params=data, headers={
        'Host': 'api.gravity.place',
        'User-Agent': 'okhttp/3.12.13',
    })
    print(response.status_code, response.json())


if __name__ == "__main__":
    main()