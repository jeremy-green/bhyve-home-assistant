# Script utility to debug device/program info from logs

import json
import os
import sys

if len(sys.argv) < 2:
    print("Not enough arguments")
    sys.exit()

folder = sys.argv[1]

script_dir = os.path.dirname(os.path.realpath(__file__))

diagnostics_json = os.path.join(script_dir, folder + "/diagnostics.json")

with open(diagnostics_json) as diagnosticsFile:
    diagnostics = json.load(diagnosticsFile)
    diagnosticsFile.close()

for device in diagnostics.get("data").get("devices"):
    if device.get("type") == "bridge":
        continue

    name = device.get("name")
    print("")

    if device.get("type") == "sprinkler_timer":
        zones = device.get("zones")
        print(f"{'Sprinkler':>10}: {name}")
        print(f"{'Zones':>10}: ({len(zones)})")
        for zone in device.get("zones"):
            zn = zone.get("name")
            print(f"{zn:<12}: {zn}")

    if device.get("type") == "flood_sensor":
        print("Flood sensor:")
        print(f"  Name: {name:<6}")
