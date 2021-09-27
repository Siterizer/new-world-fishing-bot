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
