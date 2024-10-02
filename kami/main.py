# utf-8
# windows 10 Python 3.12.1
#keys system
#owner：github.com/kndxhz
#powered by ChatGPT 4o


from flask import Flask, request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Util.Padding import unpad
import base64
import sqlite3
import time
import json

app = Flask(__name__)

# RSA 密钥
PRIVATE_KEY_PEM = '''-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA+Mc/4J1U9XS9BAAONCC+x/h83+TMwsny5NupHgUzD62NdY+8
pZ494QKnz8aJA1WByuCszcP6Fzu0Uh6HTY6xIjPcB9HyC/sarKxuzomSwqhTiL4A
K2A+2xl+XKHxSZIlfUX0qgOq4KiYMyKfK8YW6cBC1eiDgcAf4kMgEewIdlxP1W6e
ZCiq6wuRMZs5CgPJjVUh/pMniHsZA8UWgs3D1iDC7OkhT8iBdQm6uKYGtyCOsTQW
cvS15RqFCrzn/TXjNPu4wSY5NYLIhPVCAR/D0x6Whi1VCvZ4dOIxI4Zs+QkCpnak
2QwQ3+UxzJBEfB8Mms0TGqPwT8pnIQdqJWXxowIDAQABAoIBAFjsz/Z4BqBehBnj
8y/K7KcKOYjGfjK6gSoxInhqn1/hR4lYQbRppfDCRD3O17brX6OnP92lScX4P3KD
GxYsBUEWjHX3I7AIp/ZFBK6rGlyeUo20bNcUZiNnL3XpJRiJNwFaeiQzf2cinJTa
sU6yVgpkAP/5RtigVkVIfTQqzLORg0TYly0sOES33ugaO3jkfWCJ70N3WIuAYWuf
ZT6z+N6a+FKy87QEFmn8t1IzxegLk4L8kEcgpgqwJuJbXlY0xsBuQW85kyL+OOOI
FtWdVSi3BQb1B1g41hAQHScYt3uS0kBH/woeXoy0aIRObTBMw070uWVIwf86QYgJ
0245qpECgYEA/awPfll+X9oKeiC//YKYmstmXVNh7Qa9LO+nM8bSLyAqhgMD9RZG
DoR8e+PYX+OsXFuiDOKd6EgEK+A2xRs3sHOLUmld1qVULdvUkX+r4Q7VsB9JFTSn
eRGOHq4lwyXco2UXdJOPNrOczvpQnHmUMMkjYP3+k559n/ltflJzsF0CgYEA+w+x
N11ab/L+jxPnXgcDx1hltggeGrgFr/lxhPLqYoXhWvKO4XHKjCONKmLEsIKdLns/
3drm3ZNnJ6J9Nh7qXUY5t6cyVteXwULaPk+eeY0YpQfcYL0bSHb/Nq7ATJVy0Oqq
iKf0qOtnTIrKeDmCzE3kcOSxWNiYJrTGzCduCf8CgYEA6N4EsxZwnolIyOg7lvtG
IAPMiqu6354qF5BAy5Ue6cf7gV5PSbQSx8zzgb+dqBkW5wnvbyixkMRbn/OKE9Ny
gfbv1M2JKTxIVHjTYGX1YPr/S1jM/DyD6O4mqx9u5wBg1VY9+/RhqfOkZZUAX0R0
t3xNkAJaqyT5advNmgMS1LkCgYEAo5eGEl1yIKBl3zVI/av0emDPZd3EQATJL/GK
VucycyBpx6lmEODk6ov/4C6bm6iAY1lMNHP/G0KBZQIsNKfQbxbjZRg9ZPj2mafG
LfQTf4DBHkgRAbg3nvBrPGaCR2Tae+dtV76ZXbiGhwmpBM30vMvEnwtlxE7eVdpV
75GB0mECgYAu9+71jkoK6Ofmp6CEOVEWnYOj/KMaH1cj5CC6JwN5CrPcf5rlmJ1z
nBiaPIKvXI9kCWru7de1OAETnCAbFa5l0wj6k2RhPjnDWeFl3Jgn/F7S6CON7FyD
pFvB5hBjW9RojCNtXRiEZe4Oamv/F9ZAdFtjCtj5DwKLS4axw9GpqA==
-----END RSA PRIVATE KEY-----'''

PUBLIC_KEY_PEM = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtbqcchwXhb8LMjBiLxCl
0e4vZckVryDBcdsGlfBscZtq6H9oUXHuH+wZ8L6B+/uFT5vPDWKiYLXLcaJf2kUx
MupMOu+UNcMx/GTXtWGlksZRftlZa3kQAHU9vnx5O006gBhw62ITgu8eFV2l6eDj
GJgGmbMU6FGrIKTf3lhGZmFYAjqzYlNkPmDTW132euVY4EfR5oG05bo/XcfPLN0c
s8Npz+0iJFfpQEC+JdtIafb3U0xCGDVDRYSVvcIML+6/RVWNViur6NymzMhJ4G4Z
fMLQIhTnieNAWebDVoKTp34MMU7ZA+vDhfDwsDeYWrgiJ5Eq9NkuVCGemgAxaszY
nwIDAQAB
-----END PUBLIC KEY-----'''

# 解密函数
def decrypt_rsa(ciphertext, private_key_pem):
    private_key = RSA.import_key(private_key_pem)
    cipher = PKCS1_v1_5.new(private_key)
    decrypted = cipher.decrypt(bytes.fromhex(ciphertext), None)
    return decrypted.decode('utf-8')

# 加密函数
def encrypt_rsa(message, public_key_pem):
    public_key = RSA.import_key(public_key_pem)
    cipher = PKCS1_v1_5.new(public_key)
    encrypted = cipher.encrypt(message.encode('utf-8'))
    return encrypted.hex()

@app.route('/key', methods=['GET'])
def key_handler():
    data = request.args.get('data')
    if not data:
        return jsonify({'error': 'Missing data parameter'}), 400

    try:
        # 解密数据
        decrypted_data = decrypt_rsa(data, PRIVATE_KEY_PEM)
        data_json = json.loads(decrypted_data)
        key = data_json.get('key')
        pckey = data_json.get('pckey')
        timestamp = data_json.get('time')

        # 检查时间戳
        server_time = int(time.time())
        if abs(server_time - int(timestamp)) > 180:
            return jsonify({'error': 'Request timed out'}), 408

        # 查询数据库
        conn = sqlite3.connect('./key.db')
        cursor = conn.cursor()

        cursor.execute('SELECT key, pckey FROM main.keys WHERE key = ?', (key,))
        result = cursor.fetchone()
        conn.close()

        if result is None:
            return jsonify({'error': 'Key not found'}), 404

        db_key, db_pckey = result
        if db_pckey is None:
            # 更新 pckey
            conn = sqlite3.connect('./key.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE main.keys SET pckey = ? WHERE key = ?', (pckey, key))
            conn.commit()
            conn.close()
        elif db_pckey != pckey:
            return jsonify({'error': 'Pckey mismatch'}), 401

        # 返回成功响应
        response_data = {
            'status': 'ok',
            'key': key,
            'pckey': pckey,
            'time': str(server_time)
        }
        encrypted_response = encrypt_rsa(json.dumps(response_data), PUBLIC_KEY_PEM)
        return jsonify({'data': encrypted_response}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
