import yaml
from tkinter import IntVar, Tk
config = yaml.safe_load(open("resources/config.yml"))

dict = {
    'fishing':{
        'x': IntVar(value=config['fishing']['x']),
        'y': IntVar(value=config['fishing']['y']),
        'width': IntVar(value=config['fishing']['width']),
        'height': IntVar(value=config['fishing']['height'])
    },
    'repairing':{
        'x': IntVar(value=config['repairing']['x']),
        'y': IntVar(value=config['repairing']['y']),
        'length': IntVar(value=config['repairing']['length'])
    },
     'resolution':{
         'x': config['resolution']['x'],
         'y': config['resolution']['y']
    }
}

def save_data():
    d = {
            'fishing':{
                'x': dict['fishing']['x'].get(),
                'y': dict['fishing']['y'].get(),
                'width': dict['fishing']['width'].get(),
                'height': dict['fishing']['height'].get()
            },
            'repairing':{
                'x': dict['repairing']['x'].get(),
                'y': dict['repairing']['y'].get(),
                'length': dict['repairing']['length'].get()
            },
             'resolution':{
                 'x': dict['resolution']['x'],
                 'y': dict['resolution']['y']
            }
        }
    with open('resources/config.yml', 'w') as yaml_file:
        yaml.dump(d, yaml_file)
