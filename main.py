code = open("code.txt", "r").read()

code = "import sys\nsys.stdout = open('output.txt','w')\n" + code

f = open("compile.py", "w")
f.write(code)
f.close()

import os
os.system("python3 compile.py")

f = open("output.txt", "r")
print(f.read())
