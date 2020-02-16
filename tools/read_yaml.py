import yaml


def read_yaml(filename):
    list_01 = []
    with open("./data/"+ filename, "r", encoding="utf-8") as f:
         for i in yaml.safe_load(f).values():
             list_01.append(tuple(i.values()))
         print(list_01)
         return list_01
if __name__ == '__main__':
    read_yaml("test_user_list_data.yaml")

