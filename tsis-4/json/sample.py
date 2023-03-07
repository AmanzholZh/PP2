import json 

with open("sample_data.json", 'r') as f:
    json2 = json.load(f)

print("Interface status")
print("=" * 80)
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
imdata = json2["imdata"]

for i in range(len(imdata)):
    for j in imdata[i]:
        for k in imdata[i][j]: 
            if ("33" in imdata[i][j][k]["dn"]) or ("34" in imdata[i][j][k]["dn"]) or ("35" in imdata[i][j][k]["dn"]):
                print(f'{imdata[i][j][k]["dn"]}                              {imdata[i][j][k]["speed"]}   {imdata[i][j][k]["mtu"]}')