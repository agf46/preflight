import platform 
import time 
from tqdm import tqdm

host_system = platform.uname()

print(f"Analyzing system internals")

for i in tqdm(host_system):
    time.sleep(1)

print(f"System: {host_system.system}")
print(f"Node Name: {host_system.node}")
print(f"Release: {host_system.release}")
print(f"Version: {host_system.version}")
print(f"Machine: {host_system.machine}")
print(f"Processor: {host_system.processor}")
