from typing import Optional
from fastapi.openapi.models import OpenIdConnect as OpenIdConnectModel
from fastapi.security.base import SecurityBase
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN
from typing_extensions import Annotated, Doc

class OpenIdConnect(SecurityBase):
    """
    OpenID Connect authentication class. An instance of it would be used as a
    dependency.
    """

    def __init__(self, *, openIdConnectUrl: Annotated[str, Doc('\n            The OpenID Connect URL.\n            ')], scheme_name: Annotated[Optional[str], Doc('\n                Security scheme name.\n\n                It will be included in the generated OpenAPI (e.g. visible at `/docs`).\n                ')]=None, description: Annotated[Optional[str], Doc('\n                Security scheme description.\n\n                It will be included in the generated OpenAPI (e.g. visible at `/docs`).\n                ')]=None, auto_error: Annotated[bool, Doc('\n                By default, if no HTTP Authorization header is provided, required for\n                OpenID Connect authentication, it will automatically cancel the request\n                and send the client an error.\n\n                If `auto_error` is set to `False`, when the HTTP Authorization header\n                is not available, instead of erroring out, the dependency result will\n                be `None`.\n\n                This is useful when you want to have optional authentication.\n\n                It is also useful when you want to have authentication that can be\n                provided in one of multiple optional ways (for example, with OpenID\n                Connect or in a cookie).\n                ')]=True):
        self.model = OpenIdConnectModel(openIdConnectUrl=openIdConnectUrl, description=description)
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error

    async def __call__(self, request: Request) -> Optional[str]:
        authorization = request.headers.get('Authorization')
        if not authorization:
            if self.auto_error:
                raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail='Not authenticated')
            else:
                return None
        return authorization