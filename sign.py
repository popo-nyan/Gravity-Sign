import hashlib

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
    data = {
        "country": "JP",
        "product": "gravity",
        "sys_lang": "ja",
        "uwd": "5D40hb1RjCHfcEsKAn5pdJ7hncEmKelc2uoEMOxJtpOjDSv5ZkKnAoTM40i9ZbIW\n",
        "app_version": "9.1.1",
        "user_country": "",
        "idfa": "jFSZYjTCkDSqQ74SOmseLgNb7bxrB2ysGdiR15e+pvaNKwc2nTtdfZQM47M+qn8W\n",
        "sign": "1b76b7234672796542618e379a76522d",
        "sim_country": "JP",
        "pkg": "anonymous.sns.community.gravity",
        "languageV2": "ja",
        "referrer": "default",
        "app_version_code": "373",
        "zone": "9",
        "system_version": "9",
        "sdk_version": "28",
        "model": "SM-S911x",
        "device": "android",
        "brand": "samsung",
        "ts": "1708165999"}
    sign = sing_calculation(data)
    print(sign)
