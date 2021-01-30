# Base Config
Agent = "win32"
Lang = "ko"
Version = "3.1.1"
AppVersion = "3.1.1.2441"
OSVersion = "10.0"
OsVersion = OSVersion # 고치기 귀찮음
# Http Api Config
AuthHeader = f"{Agent}/{Version}/{Lang}"
AuthUserAgent = f"KT/{Version} Wd/{OSVersion} {Lang}"
LoginUrl = "https://ac-sb-talk.kakao.com/win32/account/login.json"
RegisterDeviceUrl = "https://ac-sb-talk.kakao.com/win32/account/register_device.json"
RequestPasscodeUrl = "https://ac-sb-talk.kakao.com/win32/account/request_passcode.json"
MoreSettingUrl = "https://sb-talk.kakao.com/win32/account/more_settings.json?since={since}&lang={lang}".format(
    since=0, lang=Lang)
MediaUrl = "https://up-m.talk.kakao.com/upload"
# Booking Config
BookingURL = "booking-loco.kakao.com"
BookingPort = 433
