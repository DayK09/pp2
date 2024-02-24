import json

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ") 
print("-------------------------------------------------- --------------------  ------  ------")

with open('sample-data.json', 'r') as fcc_file:
    file = json.load(fcc_file)
one = file["imdata"][0]["l1PhysIf"]["attributes"]["dn"]
one1 = file["imdata"][1]["l1PhysIf"]["attributes"]["dn"]
one2 = file["imdata"][2]["l1PhysIf"]["attributes"]["dn"]
two = file["imdata"][0]["l1PhysIf"]["attributes"]["fecMode"]
two1 = file["imdata"][1]["l1PhysIf"]["attributes"]["fecMode"]
two2 = file["imdata"][2]["l1PhysIf"]["attributes"]["fecMode"]
three = file["imdata"][0]["l1PhysIf"]["attributes"]["mtu"]
three1 = file["imdata"][1]["l1PhysIf"]["attributes"]["mtu"]
three2 = file["imdata"][2]["l1PhysIf"]["attributes"]["mtu"]

print( one,"                               ", two," ", three)
print( one1,"                               ", two1," ", three1)
print( one2,"                               ", two2," ", three2)