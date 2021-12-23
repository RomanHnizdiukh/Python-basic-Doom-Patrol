import random
import uuid

n = random.randint(0, 22)
print(n)

id = str(uuid.uuid4())
print(id)
strength = random.randint(25, 100)
print(strength)

for i in range(3):
    print(i, end="")
a = 0
try:
    print(a + 'a')
except typeError as err:
    print(err)