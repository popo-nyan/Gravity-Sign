import hashlib

T_SECRET = 999983


def calculate_sign(payload: dict) -> str:
	payload.pop("sign") if payload.get("sign") is not None else ""
	timestamp = int(payload.get("ts"))
	payload['t_secret'] = str(timestamp % T_SECRET)
	text = ""
	for key, value in sorted(zip(payload.keys(), payload.values())):
		text += key + "=" + value
	return hashlib.md5(text.encode()).hexdigest()


def main():
	data = {
		'country': 'US',
		'product': 'gravity',
		'sys_lang': 'en-US',
		'uwd': 'ccRJop7giDOBsA+XX6BWJKvLxrQH4JHbs3xKlhabvbL2zBBoq8XnyXp0WvKeG6rR',
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
		'ts': '1726568322',
	}
	sign = calculate_sign(data)
	print(sign)


if __name__ == '__main__':
	main()
