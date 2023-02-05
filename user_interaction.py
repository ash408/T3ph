
import readline

SEPERATOR = '='
SEPERATION_NUM = 4

def format_attribute(key, value, seperation_num):
    output_str = ''

    key = key.capitalize()
    value = str(value)
    output_str = key + ':' + (' ' * seperation_num) + value + '\n'

    return output_str

def format_title(title):
    output_str = ''

    output_str += title.capitalize() + '\n'
    output_str += (SEPERATOR * len(title)) + '\n'

    return output_str

def format_list(list_name, items):
    output_str = ''

    if list_name:
        output_str += format_title(list_name)
            
    maximum_item_length = 0
    for item in items:
        item = str(item)

        if len(item) > maximum_item_length:        
            maximum_item_length = len(item)
   
    max_seperation = maximum_item_length + SEPERATION_NUM + 1
    item_num = 1
    for item in items:
        item = str(item)
                
        seperator_space = max_seperation - len(item)
        spaces = ' ' * seperator_space

        output_str += item + spaces

        if item_num == 3:
            output_str = output_str.rstrip()
            output_str += '\n'
            item_num = 0

        item_num += 1
           
    return output_str

def format_dict(dict_name, dictionary):
    output_str = ''

    if dict_name:
        output_str += format_title(dict_name)
            
    maximum_key_length = 0
    for key in dictionary.keys():
        if len(key) > maximum_key_length:
            maximum_key_length = len(key)

    for key in dictionary.keys():
        seperation_num = ((maximum_key_length) - len(key)) + SEPERATION_NUM
        attribute_str = format_attribute(key, dictionary[key], seperation_num)
        output_str += attribute_str

    return output_str

def output_obj_dict(obj_dict):
    uid = obj_dict.pop('uid')
    
    attributes = {}
    list_dict = {}
    other_dicts = {}
            
    tmp_dict = obj_dict.copy()
    for key in tmp_dict.keys():
        value = tmp_dict[key]

        if type(value) is dict:
            other_dicts[key] = obj_dict.pop(key)

        elif type(value) is list:
            list_dict[key] = obj_dict.pop(key)

    output_string = ''

    output_string += format_dict(uid, obj_dict) + '\n'
    
    if list_dict:

        for key in list_dict.keys():
            output_string += format_list(key, list_dict[key]) + '\n\n'
    
    if other_dicts:

        for key in other_dicts.keys():
            output_string += format_dict(key, other_dicts[key]) + '\n'

    output_string = output_string.rstrip()
    output(output_string)

def prompt_value(key):
    value = get_input(key.capitalize() + ': ').lower().strip()
    
    try:
        value = int(value)
    except ValueError:
        pass

    return value

def prompt_attribute():
    key = get_input('Key: ').lower().strip()
    value = get_input('Value: ').lower().strip()

    try:
        value = int(value)
    except ValueError:
        pass

    return key, value

def prompt_list(list_name=None):
    return_list = []
    
    if not list_name:
        inpt = get_input('List name: ')
        list_name = inpt
    
    while True:
        inpt = confirm('Add item to list?')

        if inpt == 'y':
            itm = get_input('Item: ')
            return_list.append(itm)

        else:
            return [list_name, return_list]

def prompt_dict():
    return_dict = {}
    name = get_input('Dictionary name: ')
    
    while True:
        inpt = confirm('Add key/value to dictionary?')

        if inpt == 'y':
            key, value = prompt_attribute()

            return_dict[key] = value

        else:
            return {name : return_dict}

def prompt_obj_dict():
    return_dict = {}

    cont = True
    while cont:
        inpt = confirm('Add key/value to object?')

        if inpt == 'y':
            key, value = prompt_attribute()
            return_dict[key] = value
        else:
            cont = False

    cont = True
    while cont:
        inpt = confirm('Add list to object?')

        if inpt == 'y':
            input_list = prompt_list()

            list_name = input_list[0]
            new_list = input_list[1]

            return_dict[list_name] = new_list
        else:
            cont = False

    cont = True
    while cont:
        inpt = confirm('Add dict to object?')

        if inpt == 'y':
            input_dict = prompt_dict()
            return_dict.update(input_dict)
        else:
            cont = False

    return return_dict

def output_bool(item):
    if item == True:
        output_string('Success!')
    else:
        output_string('Failure!')

def output(item):
    if type(item) == bool:
        output_bool(item)

    elif not item:
        return
    
    elif type(item) == str:
        output_string(item)
    
    elif type(item) == list:
        if type(item[0]) == dict:
            for i in item:
                output_string('\n')
                output_obj_dict(i)
            output_string(' ')
        else:
            out = format_list('', item)
            output_string('\n' + out)
    
    elif type(item) == dict:
        output_obj_dict(item)


def output_string(string):
        print(string)

def confirm(prompt):
    inpt = input(prompt + ' [Y/N]: ')
    inpt = inpt[0].lower()

    return inpt

def get_input(prompt):
    inpt = input(prompt)
    return inpt
