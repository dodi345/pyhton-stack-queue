# percobaan 2

from collections import deque

queue = deque([1,2,3,4,5])
print(f"antrian sekarang : {queue}")

queue.append(6)
print(f"antrian masuk : {6}")
print(f"antrian sekarang : {queue}")

queue.append(7)
print(f"antrian masuk : {7}")
print(f"antrian sekarang : {queue}")

out = queue.popleft()
print(f"antrian masuk : {out}")
print(f"antrian sekarang : {queue}")