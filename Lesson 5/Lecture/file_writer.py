message = "This file uses utf-8 encoding. If you open the same file with decoding, the secret message will look different:\n"
secret_message = "Secret Message: いや、俺が勝つよ"

ascii = open("dummy_file.txt", "w", encoding="utf-8")
ascii.writelines([message, secret_message])
ascii.close()