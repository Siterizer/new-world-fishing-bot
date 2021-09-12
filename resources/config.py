import yaml
import time
from tkinter import IntVar, StringVar, Tk
from global_variables import CONFIG_PATH


config = yaml.safe_load(open(CONFIG_PATH))

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
        'length': IntVar(value=config['repairing']['length']),
        'every': IntVar(value=config['repairing']['every']),
        'time' : int(time.time()),
        'enable': IntVar(value=config['repairing']['enable'])
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
                'length': dict['repairing']['length'].get(),
                'every': dict['repairing']['every'].get(),
                'enable': dict['repairing']['enable'].get()
            },
             'resolution':{
                 'x': dict['resolution']['x'],
                 'y': dict['resolution']['y']
            }
        }
    with open(CONFIG_PATH, 'w') as yaml_file:
        yaml.dump(d, yaml_file)
