#!/usr/bin/env python3

from typing import Mapping, Any, TypeVar, Union

# Define a type variable ~T
T = TypeVar('~T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Returns the value associated with the key in the dictionary if it exists, otherwise the default value."""
    if key in dct:
        return (dct[key])
    else:
        return (default)
