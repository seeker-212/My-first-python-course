import base64

def decode_pass(password):
    decode_byte = base64.b64decode(password)
    decode_data = decode_byte.decode()
    print(f"decoded password {decode_data}")
encode_string = input("enter the base64 string: ")
decode_pass(encode_string)