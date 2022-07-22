"""
@author: bigwind
@time: 2022-06-06
@usage: load config file
"""
import argparse
from collections import defaultdict
from configparser import ConfigParser


def get_local_settings(conf=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--conf", default="app.conf", help="config file path")
    parser.add_argument("-p", "--procname", default="default", help="process name for instance management")
    namespace, unrecognized_options = parser.parse_known_args()
    if conf is None:
        conf = namespace.conf
    proc_name = namespace.procname

    if unrecognized_options:
        print("WARNING: Unrecognized args: %s" % unrecognized_options)

    parser = ConfigParser()

    parser.read(conf, encoding="utf8")

    if not parser.sections():
        raise IOError("Failed to load config from file %s in %s" % (conf, os.getcwd()))

    conf_dict = defaultdict(dict)

    conf_dict["GLOBAL"]["PROC_NAME"] = proc_name

    for section_name in parser.sections():
        for key, value in parser[section_name].items():
            key = key.upper()
            try:
                conf_dict[section_name][key] = int(value)
            except ValueError:
                try:
                    conf_dict[section_name][key] = float(value)
                except ValueError:
                    if value.upper() == "TRUE":
                        conf_dict[section_name][key] = True
                    elif value.upper() == "FALSE":
                        conf_dict[section_name][key] = False
                    else:
                        conf_dict[section_name][key] = value

    return conf_dict  # ReadOnlyDict(conf_dict)


CONFIG_SECTIONS = get_local_settings('app.conf')

CONFIG = dict(CONFIG_SECTIONS["GLOBAL"])

# CONFIG.update(CONFIG_SECTIONS["PROD"])
