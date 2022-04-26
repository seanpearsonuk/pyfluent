#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from .anisotropic import anisotropic
from .boussinesq import boussinesq
from .coefficients import coefficients
from .constant import constant
from .nasa_9_piecewise_polynomial import nasa_9_piecewise_polynomial
from .number_of_coefficients import number_of_coefficients
from .option import option
from .orthotropic import orthotropic
from .piecewise_linear import piecewise_linear
from .piecewise_polynomial import piecewise_polynomial
from .var_class import var_class


class lennard_jones_length(Group):
    """'lennard_jones_length' child."""

    fluent_name = "lennard-jones-length"

    child_names = [
        "option",
        "constant",
        "boussinesq",
        "coefficients",
        "number_of_coefficients",
        "piecewise_polynomial",
        "nasa_9_piecewise_polynomial",
        "piecewise_linear",
        "anisotropic",
        "orthotropic",
        "var_class",
    ]

    option: option = option
    """
    option child of lennard_jones_length
    """
    constant: constant = constant
    """
    constant child of lennard_jones_length
    """
    boussinesq: boussinesq = boussinesq
    """
    boussinesq child of lennard_jones_length
    """
    coefficients: coefficients = coefficients
    """
    coefficients child of lennard_jones_length
    """
    number_of_coefficients: number_of_coefficients = number_of_coefficients
    """
    number_of_coefficients child of lennard_jones_length
    """
    piecewise_polynomial: piecewise_polynomial = piecewise_polynomial
    """
    piecewise_polynomial child of lennard_jones_length
    """
    nasa_9_piecewise_polynomial: nasa_9_piecewise_polynomial = (
        nasa_9_piecewise_polynomial
    )
    """
    nasa_9_piecewise_polynomial child of lennard_jones_length
    """
    piecewise_linear: piecewise_linear = piecewise_linear
    """
    piecewise_linear child of lennard_jones_length
    """
    anisotropic: anisotropic = anisotropic
    """
    anisotropic child of lennard_jones_length
    """
    orthotropic: orthotropic = orthotropic
    """
    orthotropic child of lennard_jones_length
    """
    var_class: var_class = var_class
    """
    var_class child of lennard_jones_length
    """