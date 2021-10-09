from yaml import safe_load, dump
from tkinter import IntVar
from utils.global_variables import CONFIG_PATH
import random


config = safe_load(open(CONFIG_PATH))

dict = {
    'fishing':{
      'x': IntVar(value=config['fishing']['x']),
      'y': IntVar(value=config['fishing']['y']),
      'width': IntVar(value=config['fishing']['width']),
      'height': IntVar(value=config['fishing']['height']),
      'timeouts':{
        'loop': {
          'min': config['fishing']['timeouts']['loop']['min'],
          'max': config['fishing']['timeouts']['loop']['max']
        },
        'notice': {
          'min': config['fishing']['timeouts']['notice']['min'],
          'max': config['fishing']['timeouts']['notice']['max']
        },
        'reeling': {
          'min': config['fishing']['timeouts']['reeling']['min'],
          'max': config['fishing']['timeouts']['reeling']['max']
        },
        'pause': {
          'min': config['fishing']['timeouts']['pause']['min'],
          'max': config['fishing']['timeouts']['pause']['max']
        },
        'cast': {
          'min': config['fishing']['timeouts']['cast']['min'],
          'max': config['fishing']['timeouts']['cast']['max']
        }
      }
    },
    'repairing':{
      'x': IntVar(value=config['repairing']['x']),
      'y': IntVar(value=config['repairing']['y']),
      'length': IntVar(value=config['repairing']['length']),
      'every': IntVar(value=config['repairing']['every']),
      'enable': IntVar(value=config['repairing']['enable']),
      'timeouts': {
        'arm_disarm': {
          'min': config['repairing']['timeouts']['arm_disarm']['min'],
          'max': config['repairing']['timeouts']['arm_disarm']['max']
        },
        'inventory': {
          'min': config['repairing']['timeouts']['inventory']['min'],
          'max': config['repairing']['timeouts']['inventory']['max']
        },
        'repair': {
          'min': config['repairing']['timeouts']['repair']['min'],
          'max': config['repairing']['timeouts']['repair']['max']
        },
        'confirm': {
          'min': config['repairing']['timeouts']['confirm']['min'],
          'max': config['repairing']['timeouts']['confirm']['max']
        }
      }
    },
    'bait':{
      'bait_x': IntVar(value=config['bait']['bait_x']),
      'bait_y': IntVar(value=config['bait']['bait_y']),
      'equip_button_x': IntVar(value=config['bait']['equip_button_x']),
      'equip_button_y': IntVar(value=config['bait']['equip_button_y']),
      'length': IntVar(value=config['bait']['length']),
      'enable': IntVar(value=config['bait']['enable']),
      'timeouts': {
        'select': {
          'min': config['bait']['timeouts']['select']['min'],
          'max': config['bait']['timeouts']['select']['max']
        },
        'confirm': {
          'min': config['bait']['timeouts']['confirm']['min'],
          'max': config['bait']['timeouts']['confirm']['max']
        }
      }
    },
    'colors':{
      'green': (config['colors']['green']['r'], config['colors']['green']['g'], config['colors']['green']['b']),
      'brown': (config['colors']['brown']['r'], config['colors']['brown']['g'], config['colors']['brown']['b']),
      'red': (config['colors']['red']['r'], config['colors']['red']['g'], config['colors']['red']['b'])
    },
    'resolution':{
      'x': config['resolution']['x'],
      'y': config['resolution']['y']
    },
    'log_lvl': config['log_lvl']
  }

def save_data():
    d = {
    'fishing':{
      'x': dict['fishing']['x'].get(),
      'y': dict['fishing']['y'].get(),
      'width': dict['fishing']['width'].get(),
      'height': dict['fishing']['height'].get(),
      'timeouts':{
        'loop': {
          'min': dict['fishing']['timeouts']['loop']['min'],
          'max': dict['fishing']['timeouts']['loop']['max']
        },
        'notice': {
          'min': dict['fishing']['timeouts']['notice']['min'],
          'max': dict['fishing']['timeouts']['notice']['max']
        },
        'reeling': {
          'min': dict['fishing']['timeouts']['reeling']['min'],
          'max': dict['fishing']['timeouts']['reeling']['max']
        },
        'pause': {
          'min': dict['fishing']['timeouts']['pause']['min'],
          'max': dict['fishing']['timeouts']['pause']['max']
        },
        'cast': {
          'min': dict['fishing']['timeouts']['cast']['min'],
          'max': dict['fishing']['timeouts']['cast']['max']
        }
      }
    },
    'repairing':{
      'x': dict['repairing']['x'].get(),
      'y': dict['repairing']['y'].get(),
      'length': dict['repairing']['length'].get(),
      'every': dict['repairing']['every'].get(),
      'enable': dict['repairing']['enable'].get(),
      'timeouts': {
        'arm_disarm': {
          'min': dict['repairing']['timeouts']['arm_disarm']['min'],
          'max': dict['repairing']['timeouts']['arm_disarm']['max']
        },
        'inventory': {
          'min': dict['repairing']['timeouts']['inventory']['min'],
          'max': dict['repairing']['timeouts']['inventory']['max']
        },
        'repair': {
          'min': dict['repairing']['timeouts']['repair']['min'],
          'max': dict['repairing']['timeouts']['repair']['max']
        },
        'confirm': {
          'min': dict['repairing']['timeouts']['confirm']['min'],
          'max': dict['repairing']['timeouts']['confirm']['max']
        }
      }
    },
    'bait':{
      'bait_x': dict['bait']['bait_x'].get(),
      'bait_y': dict['bait']['bait_y'].get(),
      'equip_button_x': dict['bait']['equip_button_x'].get(),
      'equip_button_y': dict['bait']['equip_button_y'].get(),
      'length': dict['bait']['length'].get(),
      'enable': dict['bait']['enable'].get(),
      'timeouts': {
        'select': {
          'min': dict['bait']['timeouts']['select']['min'],
          'max': dict['bait']['timeouts']['select']['max']
        },
        'confirm': {
          'min': dict['bait']['timeouts']['confirm']['min'],
          'max': dict['bait']['timeouts']['confirm']['max']
        }
      }
    },
    'colors':{
      'green': {
        'r': dict['colors']['green'][0],
        'g': dict['colors']['green'][1],
        'b': dict['colors']['green'][2]
      },
      'brown': {
        'r': dict['colors']['brown'][0],
        'g': dict['colors']['brown'][1],
        'b': dict['colors']['brown'][2]
      },
      'red': {
        'r': dict['colors']['red'][0],
        'g': dict['colors']['red'][1],
        'b': dict['colors']['red'][2]
      }
    },
    'resolution':{
      'x': dict['resolution']['x'],
      'y': dict['resolution']['y']
    },
    'log_lvl': dict['log_lvl']
    }
    with open(CONFIG_PATH, 'w') as yaml_file:
        dump(d, yaml_file, sort_keys=False)

def random_timeout(key):
    return round(random.uniform(key['min'], key['max']),2)
