import yaml
from tkinter import IntVar, Tk
config = yaml.safe_load(open("config.yml"))
var1 = IntVar(value=config['fishing']['x'])
var2 = IntVar(value=config['fishing']['y'])
var3 = IntVar(value=config['fishing']['width'])
var4 = IntVar(value=config['fishing']['height'])
var5 = IntVar(value=config['repairing']['x'])
var6 = IntVar(value=config['repairing']['y'])
var7 = IntVar(value=config['repairing']['length'])
var8 = config['resolution']['x']
var9 = config['resolution']['y']
