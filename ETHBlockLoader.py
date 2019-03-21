import json
from time import time
import http.client as httpclient
import urllib.parse as urllibparse

WEB3_HOST = '10.240.1.173'


def getBlockHeight():
    path = ''
    headers = {
        'Content-type': 'application/json'
    }
    params = {
        "method": "eth_blockNumber",
        "id": time(),
        "params": "[]"
    }

    body = json.dumps(params).encode()
    conn = httpclient.HTTPConnection(host=WEB3_HOST, port=12180)
    conn.request("POST", path, body, headers)
    response = conn.getresponse()
    respText = json.loads(response.read().decode('utf-8'))
    hexResult = respText.get('result')
    height = int(hexResult, 16)
    print(hexResult)
    print(height)


def main():
    #getBlockHeight()
    val1 = int("0xf71582CCFcd5fEA5Af8324B0F0Efe470D4d4Ec09", 16)
    val2 = int("0x01932bb02343073691f2d85789fb2ceab883a98efab8c5ab29cf3dbfaa328e26", 16)
    print('length of ', val1, 'is ', len(str(val1)), ', number of bit is ', val1.bit_length())
    print('length of ', val2, 'is ', len(str(val2)), ', number of bit is ', val2.bit_length())

    print(hex(1 << 7))
    print(hex(1 << 15))
    print(hex(1 << 31))
    print(hex(1 << 63))


if __name__ == '__main__':
    main()
