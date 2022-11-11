import hashlib
from encrypt import Inno_AES
from fastapi import FastAPI
from web3 import Web3


app = FastAPI()


def text2hex(str):
    data = Web3.toHex(text=str)
    return data

def hex2text(str):
    data = Web3.toText(hexstr=str)
    return data

def hex2bytes(str):
    data = Web3.toBytes(hexstr=str)
    return data

def bytes2hex(str):
    data = Web3.toHex(str)
    return data

def text2bytes(str):
    data = Web3.toBytes(text=str)
    return data

def bytes2text(str):
    data = Web3.toText(str)
    return data

@app.get("/encrypt_hex_by_get")  #接口地址
def encrypt_hex_get():  #接口部分

    input = 'Tommorrow is another day！over!'  # 待加密内容
    key_pri = '123456'  # 密码
    #加密内容
    encode = Inno_AES.encrypt_oracle(input,key_pri)
    decode = Inno_AES.decrypt_oralce(encode,key_pri)


    #数据格式转换
    hex_str = text2hex(input)
    text_str = hex2text(hex_str)
    #new_hex = bytes2hex(bytes_str)
    #new_text = hex2text(new_hex)

    return {
        "text":text_str,
        "hex":hex_str,
        "encode":encode,
        "decode":decode
    }