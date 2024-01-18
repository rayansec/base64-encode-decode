import base64

def encode(text):
    encode_byte = base64.b64encode(text.encode())
    result = encode_byte.decode()
    print(f"base64 encode is: {result}")

def decode(text):
    try:
        decode_byte = base64.b64decode(text)
        result = decode_byte.decode()
        print(f"base64 decode is: {result}")
    except base64.binascii.Error:
        print("Invalid Base64 encoded string.")

print("Encode = 1")
print("Decode = 2")

while True:
    try:
        user = int(input("Choose the option: "))
        if user in (1, 2):
            break
        else:
            print("Invalid option. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if user == 1:
    encrypt = input("Enter text to be Base64 encoded: ")
    encode(encrypt)
elif user == 2:
    encrypt = input("Enter Base64 encoded String: ")
    decode(encrypt)