import yaml
with open("./template.yaml") as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    print(type(data))
    print(data["autosetCommand"]["autoset"])