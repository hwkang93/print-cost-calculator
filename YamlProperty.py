import yaml


class CostGroup:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return 'Cost [ name : {} , cost : {}'.format(self.name, self.cost)


class PostType:
    def __init__(self, id, name, bindingType, costSize):
        bindingTypeList = []
        costSizeList = []

        for bindingTypeData in bindingType:
            bindingCostGroup = CostGroup(bindingTypeData['name'], bindingTypeData['cost'])
            bindingTypeList.append(bindingCostGroup)

        for costSizeData in costSize:
            costCostGroup = CostGroup(costSizeData['name'], costSizeData['cost'])
            costSizeList.append(costCostGroup)

        self.id = id
        self.name = name
        self.bindingTypeList = bindingTypeList
        self.costSizeList = costSizeList


with open('data/select.yaml', 'rt', encoding='UTF8') as f:
    postTypeList = []
    data = yaml.load(f, Loader=yaml.FullLoader)

    for post_type in data['post_type']:
        binding_type = []
        post_size = []

        if 'binding_type' in post_type:
            binding_type = post_type['binding_type']

        if 'post_size' in post_type:
            post_size = post_type['post_size']

        postType = PostType(post_type['id'], post_type['name'], binding_type, post_size)
        postTypeList.append(postType)
