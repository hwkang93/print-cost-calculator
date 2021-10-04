# 기본 선택 정보

class BasicSelectInfo:
    def __init__(self, create_de, register_name, update_de, end_de, print_name):
        self.create_de = create_de
        self.register_name = register_name
        self.update_de = update_de
        self.end_de = end_de
        self.print_name = print_name

    def __str__(self):
        return 'BasicSelectInfo [create_de : {} , register_name : {}, update_de : {} , end_de : {} , print_name : {}]'\
            .format(self.create_de, self.register_name, self.update_de, self.end_de, self.print_name)

