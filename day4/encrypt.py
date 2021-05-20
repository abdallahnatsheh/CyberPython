import hashlib,bcrypt



password = input("please enter your password: ")
bytePassword=bytes(password,encoding='utf-8')

print("------md5--------")
for i in range(3):
    hashedPassword = hashlib.md5(bytePassword)
    hashed = hashedPassword.hexdigest()
    print(hashed)

print("----sha1-----")
for i in range(3):
    hashedPassword = hashlib.sha1(bytePassword)
    hashed = hashedPassword.hexdigest()
    print(hashed)

print("----bcrypt----")
for i in range(3):
    hashed = bcrypt.hashpw(bytePassword,bcrypt.gensalt(10))   #salt add random chars with the password
    print(hashed)

