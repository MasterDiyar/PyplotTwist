from config.Decoder import *
with open("saves/firstmap.info", "r") as f:
    m = f.readlines()
n = []
for l in m:
    n.append(l.split())
print(n)

print(decoder(n, "farm", (0, 0)))

