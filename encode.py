import os

from cryptography.fernet import Fernet

message = "secret"
key = os.getenv("KEY").encode()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
print("original string: ", message)
print("encrypted string: ", encMessage)
print("encrypted string decoded: ", encMessage.decode())
decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)
