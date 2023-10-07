import yaml
with open("./DHO900.yaml") as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    print(type(data))
    print(data["measureCommand"]["vpp"])