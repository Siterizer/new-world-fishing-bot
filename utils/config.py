from yaml import safe_load, dump
from tkinter import IntVar
from utils.global_variables import CONFIG_PATH


config = safe_load(open(CONFIG_PATH))

dict = {
    'fishing':{
        'x': IntVar(value=config['fishing']['x']),
        'y': IntVar(value=config['fishing']['y']),
        'width': IntVar(value=config['fishing']['width']),
        'height': IntVar(value=config['fishing']['height']),
        'timeouts':{
           'loop': config['fishing']['timeouts']['loop'],
           'notice': config['fishing']['timeouts']['notice'],
           'reeling': config['fishing']['timeouts']['reeling'],
           'pause': config['fishing']['timeouts']['pause']
        }
    },
    'repairing':{
        'x': IntVar(value=config['repairing']['x']),
        'y': IntVar(value=config['repairing']['y']),
        'length': IntVar(value=config['repairing']['length']),
        'every': IntVar(value=config['repairing']['every']),
        'enable': IntVar(value=config['repairing']['enable']),
        'timeouts':{
           'arm_disarm': config['repairing']['timeouts']['arm_disarm'],
           'inventory': config['repairing']['timeouts']['inventory'],
           'repair': config['repairing']['timeouts']['repair'],
           'confirm': config['repairing']['timeouts']['confirm']
        }
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
              'height': dict['fishing']['height'].get(),
              'timeouts':{
                'loop': dict['fishing']['timeouts']['loop'],
                'notice': dict['fishing']['timeouts']['notice'],
                'reeling': dict['fishing']['timeouts']['reeling'],
                'pause': dict['fishing']['timeouts']['pause']
              }
            },
            'repairing':{
              'x': dict['repairing']['x'].get(),
              'y': dict['repairing']['y'].get(),
              'length': dict['repairing']['length'].get(),
              'every': dict['repairing']['every'].get(),
              'enable': dict['repairing']['enable'].get(),
              'timeouts':{
                'arm_disarm': dict['repairing']['timeouts']['arm_disarm'],
                'inventory': dict['repairing']['timeouts']['inventory'],
                'repair': dict['repairing']['timeouts']['repair'],
                'confirm': dict['repairing']['timeouts']['confirm']
              }
            },
            'resolution':{
              'x': dict['resolution']['x'],
              'y': dict['resolution']['y']
              }
        }
    with open(CONFIG_PATH, 'w') as yaml_file:
        dump(d, yaml_file)
