import json
with open("sample-data.json", "r") as prog:
    data = json.load(prog)
print("Interface Status")
print("================================================================================")
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<5}")
print("-------------------------------------------------- --------------------  ------  ------")
for i in data["imdata"]:
    attributes = i['l1PhysIf']['attributes']
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "N/A")
    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")