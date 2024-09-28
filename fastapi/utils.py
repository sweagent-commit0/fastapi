import re
import warnings
from dataclasses import is_dataclass
from typing import TYPE_CHECKING, Any, Dict, MutableMapping, Optional, Set, Type, Union, cast
from weakref import WeakKeyDictionary
import fastapi
from fastapi._compat import PYDANTIC_V2, BaseConfig, ModelField, PydanticSchemaGenerationError, Undefined, UndefinedType, Validator, lenient_issubclass
from fastapi.datastructures import DefaultPlaceholder, DefaultType
from pydantic import BaseModel, create_model
from pydantic.fields import FieldInfo
from typing_extensions import Literal
if TYPE_CHECKING:
    from .routing import APIRoute
_CLONED_TYPES_CACHE: MutableMapping[Type[BaseModel], Type[BaseModel]] = WeakKeyDictionary()

def create_response_field(name: str, type_: Type[Any], class_validators: Optional[Dict[str, Validator]]=None, default: Optional[Any]=Undefined, required: Union[bool, UndefinedType]=Undefined, model_config: Type[BaseConfig]=BaseConfig, field_info: Optional[FieldInfo]=None, alias: Optional[str]=None, mode: Literal['validation', 'serialization']='validation') -> ModelField:
    """
    Create a new response field. Raises if type_ is invalid.
    """
    pass

def get_value_or_default(first_item: Union[DefaultPlaceholder, DefaultType], *extra_items: Union[DefaultPlaceholder, DefaultType]) -> Union[DefaultPlaceholder, DefaultType]:
    """
    Pass items or `DefaultPlaceholder`s by descending priority.

    The first one to _not_ be a `DefaultPlaceholder` will be returned.

    Otherwise, the first item (a `DefaultPlaceholder`) will be returned.
    """
    pass