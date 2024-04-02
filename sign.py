import hashlib
import pprint
import time
import uuid

T_SECRET = 999983


def sing_calculation(payload: dict) -> str:
    payload.pop("sign") if payload.get("sign") is not None else ""
    timestamp = int(payload.get("ts"))
    payload["t_secret"] = str(timestamp % T_SECRET)
    text = ""
    for key, value in sorted(zip(payload.keys(), payload.values())):
        text += key + "=" + value
    return hashlib.md5(text.encode()).hexdigest()


if __name__ == "__main__":
    params = {'country': 'DE',
              'sys_lang': 'en',
              'uwd': '4VkXmI0uyVZf+NUif65g9XFC8QvAqCwK+MAD8C4T1wmHDqjCwHCIJi4Ovxwu8l3F\n',
              'app_version': '9.4.1',
              'sign': '5f930a8ea0bc4eabb39156861e5ceab8',
              'sim_country': 'JP',
              'source': '',
              'pkg': 'anonymous.sns.community.gravity',
              'languageV2': 'en',
              'app_version_code': '383',
              'zone': '9',
              'last_id': '',
              'system_version': '9',
              'sdk_version': '28',
              'model': 'SM-G973N',
              'accumulated_feed_cnt': '0',
              'brand': 'samsung',
              'log_id': '0',
              'product': 'gravity',
              'user_country': 'JP',
              'idfa': 'E7QQ1LGfLcP8Iu7g0REBEss6MLJs09oLGGiPBbHbWnR4gJhiiFDzCnUvfiyXOCOJ\n',
              'session_id': 'E44E0E27-1DE2-5E08-805B-BBA3963293B0',
              'token': 'csLIz5dNJx6awtonYBEwdgunXeKfXXP0%2BtF97hyiseux5xj62KnjDYL%2B4oYNVVeB',
              'referrer': 'default',
              'device': 'android',
              'ts': '1712067947'}
    
    sign = sing_calculation(params)
    print(sign)
