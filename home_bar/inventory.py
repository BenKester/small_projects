from yml_manager import YmlReader
from copy import deepcopy
from ingredients import Ingredients
from utils import print_ingredient_structure

class Inventory(YmlReader):
    def get_file_name(self):
        return 'inventory.yml'
    
    def validate_ingredients(self, raw_data:dict, ingredients_list:list):
        missing = set(raw_data) - set(ingredients_list)
        if len(missing) > 0:
            raise Exception(f'Undefined ingredients: {missing}')

    def get_data(self):
        ing = Ingredients()
        self.validate_ingredients(self.raw_data, ing.get_ingredients_list())

        ret = {}
        for k, v in self.raw_data.items():
            ret[k] = ing.data[k] | {'opened': v}
        return ret
    
if __name__ == '__main__':
    print_ingredient_structure(Inventory().data)