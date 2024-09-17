import httpx
from time import time
from uuid import uuid4
from hashlib import md5
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

T_SECRET = 999983
KEY = "baisimeji9262019"
IV = "qrstuvwxyz123456"


def encrypt(plain_text: str) -> str:
	return b64encode(AES.new(key=KEY.encode(), iv=IV.encode(), mode=AES.MODE_CBC).encrypt(
		pad(data_to_pad=plain_text.encode(), block_size=AES.block_size))).decode()


def calculate_sign(payload: dict) -> str:
	payload.pop("sign") if payload.get("sign") is not None else ""
	timestamp = int(payload.get("ts"))
	payload['t_secret'] = str(timestamp % T_SECRET)
	text = ""
	for key, value in sorted(zip(payload.keys(), payload.values())):
		text += key + "=" + value
	return md5(text.encode()).hexdigest()


def main() -> None:
	headers = {
		'Host': 'api.gravity.place',
		'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
		'User-Agent': 'okhttp/3.12.13',
	}

	data = {
		'country': 'US',
		'product': 'gravity',
		'sys_lang': 'en-US',
		'uwd': encrypt(str(uuid4()).upper()),
		'app_version': '10.1.2',
		'user_country': '',
		'idfa': 'juOwtzKZsQHwMov+aUW9MQ==',
		'sim_country': 'us',
		'pkg': 'anonymous.sns.community.gravity',
		'languageV2': 'ja',
		'referrer': 'default',
		'app_version_code': '419',
		'zone': '0',
		'system_version': '11',
		'sdk_version': '30',
		'model': 'Pixel_6',
		'device': 'android',
		'brand': 'Google',
		'ts': str(int(time())),
	}

	data["sign"] = calculate_sign(data)
	data.pop("t_secret")
	response = httpx.post("https://api.gravity.place/gravity/user/checkInstall", data=data, headers=headers)
	print(response.text)
	print(response)


if __name__ == "__main__":
	main()
# pip install httpx pycryptodome