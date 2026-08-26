from encoder import encode
from decoder import decode
import os
os.system("clear")
question = input("(d)ecode, or (e)ncode?: ")
if question == "e":
  encode()
if question == "d":
  decode()