import http.client
import inspect
import warnings
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, Type, Union, cast
from fastapi import routing
from fastapi._compat import GenerateJsonSchema, JsonSchemaValue, ModelField, Undefined, get_compat_model_name_map, get_definitions, get_schema_from_model_field, lenient_issubclass
from fastapi.datastructures import DefaultPlaceholder
from fastapi.dependencies.models import Dependant
from fastapi.dependencies.utils import get_flat_dependant, get_flat_params
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.constants import METHODS_WITH_BODY, REF_PREFIX, REF_TEMPLATE
from fastapi.openapi.models import OpenAPI
from fastapi.params import Body, Param
from fastapi.responses import Response
from fastapi.types import ModelNameMap
from fastapi.utils import deep_dict_update, generate_operation_id_for_path, is_body_allowed_for_status_code
from starlette.responses import JSONResponse
from starlette.routing import BaseRoute
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from typing_extensions import Literal
validation_error_definition = {'title': 'ValidationError', 'type': 'object', 'properties': {'loc': {'title': 'Location', 'type': 'array', 'items': {'anyOf': [{'type': 'string'}, {'type': 'integer'}]}}, 'msg': {'title': 'Message', 'type': 'string'}, 'type': {'title': 'Error Type', 'type': 'string'}}, 'required': ['loc', 'msg', 'type']}
validation_error_response_definition = {'title': 'HTTPValidationError', 'type': 'object', 'properties': {'detail': {'title': 'Detail', 'type': 'array', 'items': {'$ref': REF_PREFIX + 'ValidationError'}}}}
status_code_ranges: Dict[str, str] = {'1XX': 'Information', '2XX': 'Success', '3XX': 'Redirection', '4XX': 'Client Error', '5XX': 'Server Error', 'DEFAULT': 'Default Response'}