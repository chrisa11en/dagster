from dagster import check
from dagster.core.types.config.config_type import Array
from dagster.core.types.config.config_type import ConfigAnyInstance as ConfigAny
from dagster.core.types.runtime.python_dict import PythonDict
from dagster.core.types.runtime.python_set import PythonSet
from dagster.core.types.runtime.python_tuple import PythonTuple
from dagster.core.types.runtime.runtime_type import Any as RuntimeAny
from dagster.core.types.runtime.runtime_type import List
from dagster.core.types.wrapping import Bool, Float, Int, String

SUPPORTED_RUNTIME_BUILTINS = {
    int: Int,
    float: Float,
    bool: Bool,
    str: String,
    list: List(RuntimeAny),
    tuple: PythonTuple,
    set: PythonSet,
    dict: PythonDict,
}


def is_supported_runtime_python_builtin(ttype):
    return ttype in SUPPORTED_RUNTIME_BUILTINS


def remap_python_builtin_for_runtime(ttype):
    '''This function remaps a python type to a Dagster type, or passes it through if it cannot be
    remapped.
    '''
    from dagster.core.types.runtime.runtime_type import resolve_to_runtime_type

    check.param_invariant(is_supported_runtime_python_builtin(ttype), 'ttype')

    return resolve_to_runtime_type(SUPPORTED_RUNTIME_BUILTINS[ttype])


SUPPORTED_CONFIG_BUILTINS = {
    int: Int,
    float: Float,
    bool: Bool,
    str: String,
    list: Array(ConfigAny),
}


def is_supported_config_python_builtin(ttype):
    return ttype in SUPPORTED_CONFIG_BUILTINS


def remap_python_builtin_for_config(ttype):
    '''This function remaps a python type to a Dagster type, or passes it through if it cannot be
    remapped.
    '''

    from dagster.core.types.config.field import resolve_to_config_type

    check.param_invariant(is_supported_config_python_builtin(ttype), 'ttype')

    return resolve_to_config_type(SUPPORTED_CONFIG_BUILTINS[ttype])
