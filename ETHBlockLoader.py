import json
import http.client as httpclient
import urllib.parse as urllibparse

from time import time
from tools import HashUtil

from db.DBTables import *


__all__ = ['getBlockHeight', 'getTransactionByHash']

WEB3_HOST = '10.240.1.23'
WEB3_PORT = 12170
COMMON_HEADER = {
    'Content-type': 'application/json; charset=UTF-8'
}


def __rpc_param_list(*args):
    arg_list = list()
    for arg in args:
        arg_list.append(arg)
    return arg_list


def getBlockHeight():
    path = ''
    params = {
        "method": "eth_blockNumber",
        "id": time(),
        "params": []
    }

    body = json.dumps(params).encode()
    conn = httpclient.HTTPConnection(host=WEB3_HOST, port=WEB3_PORT)
    conn.request("POST", path, body, COMMON_HEADER)
    response = conn.getresponse()
    respText = json.loads(response.read().decode('utf-8'))
    hexResult = respText.get('result')
    height = int(hexResult, 16)
    return height


def getBlockByNumber(number):
    params = {
        "method": "eth_getBlockByNumber",
        "id": time(),
        "params": __rpc_param_list(HashUtil.HexString.fromInteger(number).value, True)
    }

    body = json.dumps(params).encode()
    conn = httpclient.HTTPConnection(host=WEB3_HOST, port=WEB3_PORT)
    conn.request(method="POST", url="", body=body, headers=COMMON_HEADER)
    response = conn.getresponse()
    respText = json.loads(response.read().decode("utf-8"))
    result = respText.get("result")
    if result is not None:
        transactions = result.get("transactions")
        for tx in transactions:
            print(tx)


def getTransactionByHash(tx_hash):
    params = {
        "method": "eth_getTransactionByHash",
        "id": time(),
        "params": __rpc_param_list(tx_hash)
    }

    body = json.dumps(params).encode()
    conn = httpclient.HTTPConnection(host=WEB3_HOST, port=WEB3_PORT)
    conn.request(method="POST", url="", body=body, headers=COMMON_HEADER)
    response = conn.getresponse()
    respText = json.loads(response.read().decode('utf-8'))
    result = respText.get('result')
    if result is not None:
        print(result)


def main():
    #print(getBlockHeight())
    val1 = int("0xf71582CCFcd5fEA5Af8324B0F0Efe470D4d4Ec09", 16)
    val2 = int("0x01932bb02343073691f2d85789fb2ceab883a98efab8c5ab29cf3dbfaa328e26", 16)

    #getTransactionByHash("0xf595c930b016d533933f14c1d949248d8fabac9bfbb6c664a833c59dc08527a9")
    getBlockByNumber(7425816)


if __name__ == '__main__':
    main()
