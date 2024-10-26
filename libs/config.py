from configparser import ConfigParser

def get_config(file):
    """
    Read the configuration file and return a dictionary object representing its content.

    :param file: str, path to the configuration file
    :return: dict, configuration data
    """
    config = ConfigParser()
    config.read(file)
    return {section: dict(config[section]) for section in config.sections()}