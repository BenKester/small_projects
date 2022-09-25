def get_ingredient_structure(ingredients: dict):
    structure = {}
    for k, v in ingredients.items():
        cur = structure
        for parent in v['parents']:
            if parent not in cur:
                cur[parent] = {}
            cur = cur[parent]
        cur[k] = v
    return structure

def print_ingredient_structure(ingredients: dict):
    def print_recursive(structure:dict, level: int):
        for k, v in structure.items():
            if len(v) == 0 or v == [''] or k == 'parents':
                pass
            else:
                print(' ' * level + k + ': ', end='')
                if type(v) is dict:
                    print('')
                    print_recursive(v, level + 1)
                else:
                    print(v)
    
    print_recursive(get_ingredient_structure(ingredients), 0)