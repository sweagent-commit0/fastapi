import inspect
from contextlib import AsyncExitStack, contextmanager
from copy import copy, deepcopy
from typing import Any, Callable, Coroutine, Dict, ForwardRef, List, Mapping, Optional, Sequence, Tuple, Type, Union, cast
import anyio
from fastapi import params
from fastapi._compat import PYDANTIC_V2, ErrorWrapper, ModelField, Required, Undefined, _regenerate_error_with_loc, copy_field_info, create_body_model, evaluate_forwardref, field_annotation_is_scalar, get_annotation_from_field_info, get_missing_field_error, is_bytes_field, is_bytes_sequence_field, is_scalar_field, is_scalar_sequence_field, is_sequence_field, is_uploadfile_or_nonable_uploadfile_annotation, is_uploadfile_sequence_annotation, lenient_issubclass, sequence_types, serialize_sequence_value, value_is_sequence
from fastapi.background import BackgroundTasks
from fastapi.concurrency import asynccontextmanager, contextmanager_in_threadpool
from fastapi.dependencies.models import Dependant, SecurityRequirement
from fastapi.logger import logger
from fastapi.security.base import SecurityBase
from fastapi.security.oauth2 import OAuth2, SecurityScopes
from fastapi.security.open_id_connect_url import OpenIdConnect
from fastapi.utils import create_response_field, get_path_param_names
from pydantic.fields import FieldInfo
from starlette.background import BackgroundTasks as StarletteBackgroundTasks
from starlette.concurrency import run_in_threadpool
from starlette.datastructures import FormData, Headers, QueryParams, UploadFile
from starlette.requests import HTTPConnection, Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from typing_extensions import Annotated, get_args, get_origin
multipart_not_installed_error = 'Form data requires "python-multipart" to be installed. \nYou can install "python-multipart" with: \n\npip install python-multipart\n'
multipart_incorrect_install_error = 'Form data requires "python-multipart" to be installed. It seems you installed "multipart" instead. \nYou can remove "multipart" with: \n\npip uninstall multipart\n\nAnd then install "python-multipart" with: \n\npip install python-multipart\n'
CacheKey = Tuple[Optional[Callable[..., Any]], Tuple[str, ...]]