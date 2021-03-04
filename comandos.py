#comandos varios

import re

print('Hemos importardo regex')

text = "Loren ipsum dolar sit aret, consentur adipiscing elit"

x = re.findall("lectus", text)
print(x)
y = re.search("consentur", text)
print(y)
z = re.split("s", text)
print(z)
delta = re.sub("s", ".", text)
print(delta)

"""






