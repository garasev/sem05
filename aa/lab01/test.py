import psutil

p = psutil.Process()
p.cpu_times()
print(p.memory_info())

b = 15

print(p.memory_info())

print(psutil.virtual_memory())