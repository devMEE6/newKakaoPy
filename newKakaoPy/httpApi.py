from .Utils import loginUtils
from .Config import *

import requests


def RequestPasscode(email, password, device_name, device_uuid):
    r = requests.post(RequestPasscodeUrl, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "A": AuthHeader,
        "X-VC": loginUtils.getXVC(email, device_uuid, AuthUserAgent),
        "User-Agent": AuthUserAgent,
        "Accept": "*/*",
        "Accept-Language": Lang,
    }, data={
        "email": email,
        "password": password,
        "device_name": device_name,
        "device_uuid": device_uuid,
        "os_version": OsVersion,
        "permanent": "true",
        "once": "false",
    })

    return r.content.decode()


def RegisterDevice(email, password, device_name, device_uuid, passcode):
    r = requests.post(RegisterDeviceUrl, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "A": AuthHeader,
        "X-VC": loginUtils.getXVC(email, device_uuid, AuthUserAgent),
        "User-Agent": AuthUserAgent,
        "Accept": "*/*",
        "Accept-Language": Lang,
    }, data={
        "email": email,
        "password": password,
        "device_name": device_name,
        "device_uuid": device_uuid,
        "os_version": OsVersion,
        "permanent": "true",
        "once": "false",
        "passcode": passcode
    })

    return r.content.decode()


def Login(email, password, device_name, device_uuid):
    r = requests.post(LoginUrl, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "A": AuthHeader,
        "X-VC": loginUtils.getXVC(email, device_uuid, AuthUserAgent),
        "User-Agent": AuthUserAgent,
        "Accept": "*/*",
        "Accept-Language": Lang,
    }, data={
        "email": email,
        "password": password,
        "device_name": device_name,
        "device_uuid": device_uuid,
        "os_version": OsVersion,
        "permanent": True,
        "forced": True
    })

    return r.content.decode()
