#!/usr/bin/env python3
import subprocess

routers = ["router0", "router1", "router2"]
inventory = "inventory/hosts.ini"

print("Checking router connectivity...\n")

for router in routers:
    cmd = ["ansible", "-i", inventory, router, "-m", "ping"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if "SUCCESS" in result.stdout:
        print(f"{router}: ✅ reachable")
    else:
        print(f"{router}: ❌ unreachable")
        print(result.stdout)
        print(result.stderr)
