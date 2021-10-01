import yaml

with open('data/select.yaml', 'rt', encoding='UTF8') as f:
    select = yaml.load(f, Loader=yaml.FullLoader)
    print(select);


class PostType:
    def __init__(self, id, name, bindingType, postSize):
        self.id = id
        self.name = name
        self.bindingType = bindingType
        self.postSize = postSize
