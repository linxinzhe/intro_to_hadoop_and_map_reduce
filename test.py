from collections import deque

d = deque(maxlen=10)
for i in range(0, 20):
    d.append(i)
print d
