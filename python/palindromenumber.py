x = 10
y = ""
x = str(x)
for i in range(len(x)):
    i += 1
    y += x[-i]

if x == y:
    print(True)
else:
    print(False)