from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt( msg, key):
  cipher = AES.new(key, AES.MODE_ECB)
  padded_msg = pad(str.encode(msg), AES.block_size)
  cipher_text = cipher.encrypt(padded_msg)
  return cipher_text.hex()
  
def decrypt(key, cipher_text):
  decipher = AES.new(key, AES.MODE_ECB)
  decrypted_msg = decipher.decrypt(bytes.fromhex(cipher_text))
  unpadded_msg = unpad(decrypted_msg, AES.block_size)
  return unpadded_msg.decode()

