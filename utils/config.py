from yaml import safe_load, dump
from tkinter import IntVar, DoubleVar
from utils.global_variables import CONFIG_PATH
from numpy import random


def get_config():
    config = safe_load(open(CONFIG_PATH))

    return {
        "fishing": {
            "x": IntVar(value=config["fishing"]["x"]),
            "y": IntVar(value=config["fishing"]["y"]),
            "width": IntVar(value=config["fishing"]["width"]),
            "height": IntVar(value=config["fishing"]["height"]),
            "timeouts": {
                "loop": {
                    "min": config["fishing"]["timeouts"]["loop"]["min"],
                    "max": config["fishing"]["timeouts"]["loop"]["max"],
                },
                "notice": {
                    "min": config["fishing"]["timeouts"]["notice"]["min"],
                    "max": config["fishing"]["timeouts"]["notice"]["max"],
                },
                "reeling": {
                    "min": config["fishing"]["timeouts"]["reeling"]["min"],
                    "max": config["fishing"]["timeouts"]["reeling"]["max"],
                },
                "pause": {
                    "min": config["fishing"]["timeouts"]["pause"]["min"],
                    "max": config["fishing"]["timeouts"]["pause"]["max"],
                },
                "cast": {
                    "min": config["fishing"]["timeouts"]["cast"]["min"],
                    "max": config["fishing"]["timeouts"]["cast"]["max"],
                },
            },
        },
        "repairing": {
            "x": IntVar(value=config["repairing"]["x"]),
            "y": IntVar(value=config["repairing"]["y"]),
            "length": IntVar(value=config["repairing"]["length"]),
            "every": IntVar(value=config["repairing"]["every"]),
            "enable_repairs": IntVar(value=config["repairing"]["enable_repairs"]),
            "enable_move_around": IntVar(value=config["repairing"]["enable_move_around"]),
            "timeouts": {
                "arm_disarm": {
                    "min": config["repairing"]["timeouts"]["arm_disarm"]["min"],
                    "max": config["repairing"]["timeouts"]["arm_disarm"]["max"],
                },
                "inventory": {
                    "min": config["repairing"]["timeouts"]["inventory"]["min"],
                    "max": config["repairing"]["timeouts"]["inventory"]["max"],
                },
                "repair": {
                    "min": config["repairing"]["timeouts"]["repair"]["min"],
                    "max": config["repairing"]["timeouts"]["repair"]["max"],
                },
                "confirm": {
                    "min": config["repairing"]["timeouts"]["confirm"]["min"],
                    "max": config["repairing"]["timeouts"]["confirm"]["max"],
                },
                "move_around": {
                    "min": DoubleVar(value=config["repairing"]["timeouts"]["move_around"]["min"]),
                    "max": DoubleVar(value=config["repairing"]["timeouts"]["move_around"]["max"]),
                },
            },
        },
        "bait": {
            "bait_x": IntVar(value=config["bait"]["bait_x"]),
            "bait_y": IntVar(value=config["bait"]["bait_y"]),
            "equip_button_x": IntVar(value=config["bait"]["equip_button_x"]),
            "equip_button_y": IntVar(value=config["bait"]["equip_button_y"]),
            "length": IntVar(value=config["bait"]["length"]),
            "enable": IntVar(value=config["bait"]["enable"]),
            "timeouts": {
                "select": {
                    "min": config["bait"]["timeouts"]["select"]["min"],
                    "max": config["bait"]["timeouts"]["select"]["max"],
                },
                "confirm": {
                    "min": config["bait"]["timeouts"]["confirm"]["min"],
                    "max": config["bait"]["timeouts"]["confirm"]["max"],
                },
            },
        },
        "colors": {
            "green": (
                config["colors"]["green"]["r"],
                config["colors"]["green"]["g"],
                config["colors"]["green"]["b"],
            ),
            "brown": (
                config["colors"]["brown"]["r"],
                config["colors"]["brown"]["g"],
                config["colors"]["brown"]["b"],
            ),
            "brown2": (
                config["colors"]["brown2"]["r"],
                config["colors"]["brown2"]["g"],
                config["colors"]["brown2"]["b"],
            ),
            "red": (
                config["colors"]["red"]["r"],
                config["colors"]["red"]["g"],
                config["colors"]["red"]["b"],
            ),
        },
        "resolution": {"x": config["resolution"]["x"], "y": config["resolution"]["y"]},
        "log_lvl": config["log_lvl"],
    }


def save_data(config):
    d = {
        "fishing": {
            "x": config["fishing"]["x"].get(),
            "y": config["fishing"]["y"].get(),
            "width": config["fishing"]["width"].get(),
            "height": config["fishing"]["height"].get(),
            "timeouts": {
                "loop": {
                    "min": config["fishing"]["timeouts"]["loop"]["min"],
                    "max": config["fishing"]["timeouts"]["loop"]["max"],
                },
                "notice": {
                    "min": config["fishing"]["timeouts"]["notice"]["min"],
                    "max": config["fishing"]["timeouts"]["notice"]["max"],
                },
                "reeling": {
                    "min": config["fishing"]["timeouts"]["reeling"]["min"],
                    "max": config["fishing"]["timeouts"]["reeling"]["max"],
                },
                "pause": {
                    "min": config["fishing"]["timeouts"]["pause"]["min"],
                    "max": config["fishing"]["timeouts"]["pause"]["max"],
                },
                "cast": {
                    "min": config["fishing"]["timeouts"]["cast"]["min"],
                    "max": config["fishing"]["timeouts"]["cast"]["max"],
                },
            },
        },
        "repairing": {
            "x": config["repairing"]["x"].get(),
            "y": config["repairing"]["y"].get(),
            "length": config["repairing"]["length"].get(),
            "every": config["repairing"]["every"].get(),
            "enable_repairs": config["repairing"]["enable_repairs"].get(),
            "enable_move_around": config["repairing"]["enable_move_around"].get(),
            "timeouts": {
                "arm_disarm": {
                    "min": config["repairing"]["timeouts"]["arm_disarm"]["min"],
                    "max": config["repairing"]["timeouts"]["arm_disarm"]["max"],
                },
                "inventory": {
                    "min": config["repairing"]["timeouts"]["inventory"]["min"],
                    "max": config["repairing"]["timeouts"]["inventory"]["max"],
                },
                "repair": {
                    "min": config["repairing"]["timeouts"]["repair"]["min"],
                    "max": config["repairing"]["timeouts"]["repair"]["max"],
                },
                "confirm": {
                    "min": config["repairing"]["timeouts"]["confirm"]["min"],
                    "max": config["repairing"]["timeouts"]["confirm"]["max"],
                },
                "move_around": {
                    "min": config["repairing"]["timeouts"]["move_around"]["min"].get(),
                    "max": config["repairing"]["timeouts"]["move_around"]["max"].get(),
                },
            },
        },
        "bait": {
            "bait_x": config["bait"]["bait_x"].get(),
            "bait_y": config["bait"]["bait_y"].get(),
            "equip_button_x": config["bait"]["equip_button_x"].get(),
            "equip_button_y": config["bait"]["equip_button_y"].get(),
            "length": config["bait"]["length"].get(),
            "enable": config["bait"]["enable"].get(),
            "timeouts": {
                "select": {
                    "min": config["bait"]["timeouts"]["select"]["min"],
                    "max": config["bait"]["timeouts"]["select"]["max"],
                },
                "confirm": {
                    "min": config["bait"]["timeouts"]["confirm"]["min"],
                    "max": config["bait"]["timeouts"]["confirm"]["max"],
                },
            },
        },
        "colors": {
            "green": {
                "r": config["colors"]["green"][0],
                "g": config["colors"]["green"][1],
                "b": config["colors"]["green"][2],
            },
            "brown": {
                "r": config["colors"]["brown"][0],
                "g": config["colors"]["brown"][1],
                "b": config["colors"]["brown"][2],
            },
            "brown2": {
                "r": config["colors"]["brown2"][0],
                "g": config["colors"]["brown2"][1],
                "b": config["colors"]["brown2"][2],
            },
            "red": {
                "r": config["colors"]["red"][0],
                "g": config["colors"]["red"][1],
                "b": config["colors"]["red"][2],
            },
        },
        "resolution": {"x": config["resolution"]["x"], "y": config["resolution"]["y"]},
        "log_lvl": config["log_lvl"],
    }
    with open(CONFIG_PATH, "w") as yaml_file:
        dump(d, yaml_file, sort_keys=False)


async def random_timeout(key):
    upper_limit = key["max"]
    lower_limit = key["min"]

    loc = (upper_limit + lower_limit) / 2
    scale = (upper_limit - lower_limit) / 4

    sample = random.normal(loc, scale)

    return round(min(max(sample, lower_limit), upper_limit), 2)


async def random_timeout_temp_for_double(key):
    upper_limit = key["max"].get()
    lower_limit = key["min"].get()

    loc = (upper_limit + lower_limit) / 2
    scale = (upper_limit - lower_limit) / 4

    sample = random.normal(loc, scale)

    return round(min(max(sample, lower_limit), upper_limit), 2)
