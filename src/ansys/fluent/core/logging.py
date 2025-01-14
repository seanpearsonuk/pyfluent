"""Module controlling PyFluent's logging functionality."""
import logging.config
import os
from typing import Union

import yaml

_logging_file_enabled = False


def root_config():
    """Sets up the root PyFluent logger that outputs messages to stdout, but not to files."""
    logger = logging.getLogger("pyfluent")
    logger.setLevel("WARNING")
    formatter = logging.Formatter("%(name)s %(levelname)s: %(message)s")
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel("WARNING")
        ch.setFormatter(formatter)
        logger.addHandler(ch)


def is_active() -> bool:
    """Returns whether PyFluent logging to file is active."""
    return _logging_file_enabled


def enable(level: Union[str, int] = "DEBUG"):
    """Enables PyFluent logging to file.

    Parameters
    ----------
    level : str or int, optional
        Specified logging level to set PyFluent loggers to. If omitted, level is set to DEBUG.

    Examples
    --------
    >>> import ansys.fluent.core as pyfluent
    >>> pyfluent.logging.enable()

    Notes
    -----
    See logging levels in https://docs.python.org/3/library/logging.html#logging-levels
    """
    global _logging_file_enabled

    if _logging_file_enabled:
        print("PyFluent logging to file is already active.")
        return

    _logging_file_enabled = True

    # Configure the logging system
    file_path = os.path.abspath(__file__)
    file_dir = os.path.dirname(file_path)
    yaml_path = os.path.join(file_dir, "logging_config.yaml")

    with open(yaml_path, "rt") as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)
    print(f"PyFluent logging file {os.path.join(os.getcwd(),'pyfluent.log')}")

    set_global_level(level)


def get_logger(*args, **kwargs):
    """Retrieves logger. Convenience wrapper for Python's :func:`logging.getLogger` function."""
    return logging.getLogger(*args, **kwargs)


def set_global_level(level: Union[str, int]):
    """Changes the levels of all PyFluent loggers that write to log file.

    Parameters
    ----------
    level : str or int
        Specified logging level to set PyFluent loggers to.

    Examples
    --------
    >>> import ansys.fluent.core as pyfluent
    >>> pyfluent.logging.set_global_level(10)

    or

    >>> pyfluent.logging.set_global_level('DEBUG')

    Notes
    -----
    See logging levels in https://docs.python.org/3/library/logging.html#logging-levels
    """
    if not is_active():
        print("Logging is not active, enable it first.")
        return
    if isinstance(level, str):
        if level.isdigit():
            level = int(level)
        else:
            level = level.upper()
    print(f"Setting PyFluent global logging level to {level}.")
    pyfluent_loggers = list_loggers()
    for name in pyfluent_loggers:
        if name != "pyfluent":  # do not change the console root PyFluent logger
            logging.getLogger(name).setLevel(level)


def list_loggers():
    """List all PyFluent loggers.

    Returns
    -------
    list of str
        Each list element is a PyFluent logger name that can be individually controlled
        through :func:`ansys.fluent.core.logging.get_logger`.

    Examples
    --------
    >>> import ansys.fluent.core as pyfluent
    >>> pyfluent.logging.enable()
    >>> pyfluent.logging.list_loggers()
    ['pyfluent.general', 'pyfluent.launcher', 'pyfluent.networking', ...]
    >>> logger = pyfluent.logging.get_logger('pyfluent.networking')
    >>> logger
    <Logger pyfluent.networking (DEBUG)>
    >>> logger.setLevel('ERROR')
    >>> logger
    <Logger pyfluent.networking (ERROR)>

    Notes
    -----
    PyFluent loggers use the standard Python logging library, for more details
    see https://docs.python.org/3/library/logging.html#logger-objects
    """
    logger_dict = logging.root.manager.loggerDict
    pyfluent_loggers = []
    for name in logger_dict:
        if name.startswith("pyfluent"):
            pyfluent_loggers.append(name)
    return pyfluent_loggers
