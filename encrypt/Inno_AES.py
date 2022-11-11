import base64
from Crypto.Cipher import AES

def add_to_16(message):
    while len(message) % 16 != 0:
        message = str(message)
        message += '\0'
    return message

def encrypt_oracle(message,key_pri):
    '''
    加密函数，传入明文 & 秘钥，返回密文；
    :param message: 明文
    :param key_pri: 秘钥
    :return:encrypted  密文
    '''
    aes = AES.new(add_to_16(key_pri).encode(),AES.MODE_ECB)

    message_bytes = message.encode('utf-8')
    message_16 = add_to_16(message_bytes)
    encrypt_aes = aes.encrypt(message_16)
    encrypt_aes_64 = base64.b64encode(encrypt_aes)
    return encrypt_aes_64

def decrypt_oralce(message,key_pri):
    '''
    解密函数，传入密文 & 秘钥，返回明文；
    :param message: 密文
    :param key_pri: 秘钥
    :return: encrypted 明文
    '''
    # 初始化加密器
    aes = AES.new(add_to_16(key_pri).encode(), AES.MODE_ECB)
    #优先逆向解密base64成bytes
    message_de64 = base64.b64decode(message)
    # 解密 aes
    message_de64_deaes = aes.decrypt(message_de64)
    message_de64_deaes_de = message_de64_deaes.decode('utf-8')
    return message_de64_deaes_de