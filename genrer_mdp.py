import locale
from base64 import b64encode, b64decode
while True :
    code = input("Code ? (ex : 1A, 1B, 1C, 1D, 2A, 2B, etc.)\n")
    code = str(int(code, 16)).encode("ascii")
    code = b64encode(code).decode()
    print(code)