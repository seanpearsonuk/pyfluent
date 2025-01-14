"""A package providing Fluent's Solver and Meshing capabilities in Python."""

import os
import pydoc

import appdirs

# Logging has to be set up before importing other PyFluent modules
import ansys.fluent.core.logging as pyfluent_logging

pyfluent_logging.root_config()

env_logging_level = os.getenv("PYFLUENT_LOGGING")
if env_logging_level:
    if isinstance(env_logging_level, str):
        if env_logging_level.isdigit():
            env_logging_level = int(env_logging_level)
        else:
            env_logging_level = env_logging_level.upper()
    if env_logging_level in [0, "OFF"] or pyfluent_logging.is_active():
        pass
    else:
        print("PYFLUENT_LOGGING environment variable found, enabling logging...")
        pyfluent_logging.enable(env_logging_level)


from ansys.fluent.core._version import __version__  # noqa: F401
from ansys.fluent.core.launcher.launcher import (  # noqa: F401
    FluentVersion,
    LaunchMode,
    launch_fluent,
)
from ansys.fluent.core.services.batch_ops import BatchOps  # noqa: F401
from ansys.fluent.core.session import BaseSession as Fluent  # noqa: F401
from ansys.fluent.core.utils import fldoc
from ansys.fluent.core.utils.setup_for_fluent import setup_for_fluent  # noqa: F401

_VERSION_INFO = None
"""Global variable indicating the version of the PyFluent package - Empty by default"""

_THIS_DIRNAME = os.path.dirname(__file__)
_README_FILE = os.path.normpath(os.path.join(_THIS_DIRNAME, "docs", "README.rst"))

if os.path.exists(_README_FILE):
    with open(_README_FILE, encoding="utf8") as f:
        __doc__ = f.read()


def version_info() -> str:
    """Method returning the version of PyFluent being used.

    Returns
    -------
    str
        The PyFluent version being used.

    Notes
    -------
    Only available in packaged versions. Otherwise it will return __version__.
    """
    return _VERSION_INFO if _VERSION_INFO is not None else __version__


# Setup data directory
USER_DATA_PATH = appdirs.user_data_dir(appname="ansys_fluent_core", appauthor="Ansys")
EXAMPLES_PATH = os.path.join(USER_DATA_PATH, "examples")

# For Sphinx documentation build
BUILDING_GALLERY = False

# Set this to False to stop automatically inferring and setting REMOTING_SERVER_ADDRESS
INFER_REMOTING_IP = True

# Time in second to wait for response for each ip while inferring remoting ip
INFER_REMOTING_IP_TIMEOUT_PER_IP = 2

pydoc.text.docother = fldoc.docother.__get__(pydoc.text, pydoc.TextDoc)

# Whether to use datamodel state caching
DATAMODEL_USE_STATE_CACHE = True

# Whether to use datamodel attribute caching
DATAMODEL_USE_ATTR_CACHE = True

# Whether stream and cache commands state
DATAMODEL_USE_NOCOMMANDS_DIFF_STATE = True
