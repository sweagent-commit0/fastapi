from contextlib import asynccontextmanager as asynccontextmanager
from typing import AsyncGenerator, ContextManager, TypeVar
import anyio
from anyio import CapacityLimiter
from starlette.concurrency import iterate_in_threadpool as iterate_in_threadpool
from starlette.concurrency import run_in_threadpool as run_in_threadpool
from starlette.concurrency import run_until_first_complete as run_until_first_complete
_T = TypeVar('_T')