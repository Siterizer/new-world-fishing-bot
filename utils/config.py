from yaml import safe_load, dump
from tkinter import IntVar
from utils.global_variables import CONFIG_PATH
from numpy import random


config = safe_load(open(CONFIG_PATH))

config_dict = {
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
        "enable": IntVar(value=config["repairing"]["enable"]),
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
                "min": config["repairing"]["timeouts"]["move_around"]["min"],
                "max": config["repairing"]["timeouts"]["move_around"]["max"],
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
        "red": (
            config["colors"]["red"]["r"],
            config["colors"]["red"]["g"],
            config["colors"]["red"]["b"],
        ),
    },
    "resolution": {"x": config["resolution"]["x"], "y": config["resolution"]["y"]},
    "log_lvl": config["log_lvl"],
}


def save_data():
    d = {
        "fishing": {
            "x": config_dict["fishing"]["x"].get(),
            "y": config_dict["fishing"]["y"].get(),
            "width": config_dict["fishing"]["width"].get(),
            "height": config_dict["fishing"]["height"].get(),
            "timeouts": {
                "loop": {
                    "min": config_dict["fishing"]["timeouts"]["loop"]["min"],
                    "max": config_dict["fishing"]["timeouts"]["loop"]["max"],
                },
                "notice": {
                    "min": config_dict["fishing"]["timeouts"]["notice"]["min"],
                    "max": config_dict["fishing"]["timeouts"]["notice"]["max"],
                },
                "reeling": {
                    "min": config_dict["fishing"]["timeouts"]["reeling"]["min"],
                    "max": config_dict["fishing"]["timeouts"]["reeling"]["max"],
                },
                "pause": {
                    "min": config_dict["fishing"]["timeouts"]["pause"]["min"],
                    "max": config_dict["fishing"]["timeouts"]["pause"]["max"],
                },
                "cast": {
                    "min": config_dict["fishing"]["timeouts"]["cast"]["min"],
                    "max": config_dict["fishing"]["timeouts"]["cast"]["max"],
                },
            },
        },
        "repairing": {
            "x": config_dict["repairing"]["x"].get(),
            "y": config_dict["repairing"]["y"].get(),
            "length": config_dict["repairing"]["length"].get(),
            "every": config_dict["repairing"]["every"].get(),
            "enable": config_dict["repairing"]["enable"].get(),
            "timeouts": {
                "arm_disarm": {
                    "min": config_dict["repairing"]["timeouts"]["arm_disarm"]["min"],
                    "max": config_dict["repairing"]["timeouts"]["arm_disarm"]["max"],
                },
                "inventory": {
                    "min": config_dict["repairing"]["timeouts"]["inventory"]["min"],
                    "max": config_dict["repairing"]["timeouts"]["inventory"]["max"],
                },
                "repair": {
                    "min": config_dict["repairing"]["timeouts"]["repair"]["min"],
                    "max": config_dict["repairing"]["timeouts"]["repair"]["max"],
                },
                "confirm": {
                    "min": config_dict["repairing"]["timeouts"]["confirm"]["min"],
                    "max": config_dict["repairing"]["timeouts"]["confirm"]["max"],
                },
                "move_around": {
                    "min": config_dict["repairing"]["timeouts"]["move_around"]["min"],
                    "max": config_dict["repairing"]["timeouts"]["move_around"]["max"],
                },
            },
        },
        "bait": {
            "bait_x": config_dict["bait"]["bait_x"].get(),
            "bait_y": config_dict["bait"]["bait_y"].get(),
            "equip_button_x": config_dict["bait"]["equip_button_x"].get(),
            "equip_button_y": config_dict["bait"]["equip_button_y"].get(),
            "length": config_dict["bait"]["length"].get(),
            "enable": config_dict["bait"]["enable"].get(),
            "timeouts": {
                "select": {
                    "min": config_dict["bait"]["timeouts"]["select"]["min"],
                    "max": config_dict["bait"]["timeouts"]["select"]["max"],
                },
                "confirm": {
                    "min": config_dict["bait"]["timeouts"]["confirm"]["min"],
                    "max": config_dict["bait"]["timeouts"]["confirm"]["max"],
                },
            },
        },
        "colors": {
            "green": {
                "r": config_dict["colors"]["green"][0],
                "g": config_dict["colors"]["green"][1],
                "b": config_dict["colors"]["green"][2],
            },
            "brown": {
                "r": config_dict["colors"]["brown"][0],
                "g": config_dict["colors"]["brown"][1],
                "b": config_dict["colors"]["brown"][2],
            },
            "red": {
                "r": config_dict["colors"]["red"][0],
                "g": config_dict["colors"]["red"][1],
                "b": config_dict["colors"]["red"][2],
            },
        },
        "resolution": {"x": config_dict["resolution"]["x"], "y": config_dict["resolution"]["y"]},
        "log_lvl": config_dict["log_lvl"],
    }
    with open(CONFIG_PATH, "w") as yaml_file:
        dump(d, yaml_file, sort_keys=False)


def random_timeout(key):
    upper_limit = key["max"]
    lower_limit = key["min"]

    loc = (upper_limit + lower_limit) / 2
    scale = (upper_limit - lower_limit) / 4

    sample = random.normal(loc, scale)

    return round(min(max(sample, lower_limit), upper_limit), 2)
