from yml_manager import YmlReader
from copy import deepcopy

class Ingredients(YmlReader):
    def get_file_name(self):
        return 'ingredients.yml'
    
    def get_data(self):
        def get_data_recursive(data: dict, parents: list, name: str):
            match name:
                case 'substitutes for' | 'shelf life' | 'synonyms':
                    return None
                case _:
                    if data != None:
                        children = {}
                        for k, v in data.items():
                            i = get_data_recursive(data=v, parents = parents + [name,], name = k)
                            if i == None:
                                pass
                            elif 'parents' in i:
                                children[k] = i
                                for synonym in i['synonyms']:
                                    children[synonym] = deepcopy(i)
                                    children[synonym]['synonyms'].append(k)
                                    children[synonym]['synonyms'].remove(synonym)
                            else:
                                children = children | i
                        if len(children) > 0:
                            return children

                    # base case
                    ret = data if data != None else {}
                    ret['parents'] = parents[1:]
                    ret['substitutes for'] = ret.get('substitutes for', '').split(',')
                    ret['synonyms'] = ret.get('synonyms', '').split(',')
                    return ret

        return get_data_recursive(self.raw_data, [], name='')
    
    def get_ingredients_list(self):
        return sorted(list(self.data.keys()))

if __name__ == '__main__':
    print(*Ingredients().get_ingredients_list(), sep='\n')