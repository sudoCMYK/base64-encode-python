# this does count as only 2 lines of code hehehehehehe
# wait does it?
# ----------------------------
import base64
b64 = base64

toEncode = input('Base64 Simple Encode: ')
toEncode_bytes = toEncode.encode('ascii')
base64_toEncode = b64.b64encode(toEncode_bytes)

