import json
from typing import Any, Dict, Optional
from fastapi.encoders import jsonable_encoder
from starlette.responses import HTMLResponse
from typing_extensions import Annotated, Doc
swagger_ui_default_parameters: Annotated[Dict[str, Any], Doc('\n        Default configurations for Swagger UI.\n\n        You can use it as a template to add any other configurations needed.\n        ')] = {'dom_id': '#swagger-ui', 'layout': 'BaseLayout', 'deepLinking': True, 'showExtensions': True, 'showCommonExtensions': True}

def get_swagger_ui_html(*, openapi_url: Annotated[str, Doc('\n            The OpenAPI URL that Swagger UI should load and use.\n\n            This is normally done automatically by FastAPI using the default URL\n            `/openapi.json`.\n            ')], title: Annotated[str, Doc('\n            The HTML `<title>` content, normally shown in the browser tab.\n            ')], swagger_js_url: Annotated[str, Doc('\n            The URL to use to load the Swagger UI JavaScript.\n\n            It is normally set to a CDN URL.\n            ')]='https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js', swagger_css_url: Annotated[str, Doc('\n            The URL to use to load the Swagger UI CSS.\n\n            It is normally set to a CDN URL.\n            ')]='https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css', swagger_favicon_url: Annotated[str, Doc('\n            The URL of the favicon to use. It is normally shown in the browser tab.\n            ')]='https://fastapi.tiangolo.com/img/favicon.png', oauth2_redirect_url: Annotated[Optional[str], Doc('\n            The OAuth2 redirect URL, it is normally automatically handled by FastAPI.\n            ')]=None, init_oauth: Annotated[Optional[Dict[str, Any]], Doc('\n            A dictionary with Swagger UI OAuth2 initialization configurations.\n            ')]=None, swagger_ui_parameters: Annotated[Optional[Dict[str, Any]], Doc('\n            Configuration parameters for Swagger UI.\n\n            It defaults to [swagger_ui_default_parameters][fastapi.openapi.docs.swagger_ui_default_parameters].\n            ')]=None) -> HTMLResponse:
    """
    Generate and return the HTML  that loads Swagger UI for the interactive
    API docs (normally served at `/docs`).

    You would only call this function yourself if you needed to override some parts,
    for example the URLs to use to load Swagger UI's JavaScript and CSS.

    Read more about it in the
    [FastAPI docs for Configure Swagger UI](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/)
    and the [FastAPI docs for Custom Docs UI Static Assets (Self-Hosting)](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/).
    """
    pass

def get_redoc_html(*, openapi_url: Annotated[str, Doc('\n            The OpenAPI URL that ReDoc should load and use.\n\n            This is normally done automatically by FastAPI using the default URL\n            `/openapi.json`.\n            ')], title: Annotated[str, Doc('\n            The HTML `<title>` content, normally shown in the browser tab.\n            ')], redoc_js_url: Annotated[str, Doc('\n            The URL to use to load the ReDoc JavaScript.\n\n            It is normally set to a CDN URL.\n            ')]='https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js', redoc_favicon_url: Annotated[str, Doc('\n            The URL of the favicon to use. It is normally shown in the browser tab.\n            ')]='https://fastapi.tiangolo.com/img/favicon.png', with_google_fonts: Annotated[bool, Doc('\n            Load and use Google Fonts.\n            ')]=True) -> HTMLResponse:
    """
    Generate and return the HTML response that loads ReDoc for the alternative
    API docs (normally served at `/redoc`).

    You would only call this function yourself if you needed to override some parts,
    for example the URLs to use to load ReDoc's JavaScript and CSS.

    Read more about it in the
    [FastAPI docs for Custom Docs UI Static Assets (Self-Hosting)](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/).
    """
    pass

def get_swagger_ui_oauth2_redirect_html() -> HTMLResponse:
    """
    Generate the HTML response with the OAuth2 redirection for Swagger UI.

    You normally don't need to use or change this.
    """
    pass