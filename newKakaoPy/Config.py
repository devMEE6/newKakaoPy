# Base Config
Agent = "win32"
Lang = "ko"
Version = "3.1.1"
AppVersion = "3.1.1.2441"
OSVersion = "10.0"
MCCMNC = "999"
NetType = 0
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
# Crypto Config
RSASeed = ("A44960441C7E83BB27898156ECB13C8AFAF05D284A4D1155F255CD22D3176CDE50482F2F27F71348E4D2EB5F57BF9671EF15C9224E"
           "042B1B567AC1066E06691143F6C50F88787F68CF42716B210CBEF0F59D53405A0A56138A6872212802BB0AEEA6376305DBD428831E8"
           "F61A232EFEDD8DBA377305EF972321E1352B5F64630993E5549C64FCB563CDC97DA2124B925DDEA12ADFD00138910F66937FAB68486"
           "AE43BFE203C4A617F9F232B5458A9AB409BAC8EDADEF685545F9B013986747737B3FD76A9BAC121516226981EA67225577D15D0F082"
           "B8207EAF7CDCB13123937CB12145837648C2F3A65018162315E77EAD2D2DD5986E46251764A43B9BA8F79", "3")
