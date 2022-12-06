from collections.abc import Sequence
from socket import socket
from typing import Any

from waitress.adjustments import Adjustments
from waitress.channel import HTTPChannel
from waitress.task import Task, ThreadedTaskDispatcher

from . import wasyncore

def create_server(
    application: Any,
    map: Any | None = ...,
    _start: bool = ...,
    _sock: socket | None = ...,
    _dispatcher: ThreadedTaskDispatcher | None = ...,
    **kw: Any,
) -> MultiSocketServer | BaseWSGIServer: ...

class MultiSocketServer:
    asyncore: Any = ...
    adj: Adjustments = ...
    map: Any = ...
    effective_listen: Sequence[tuple[str, int]] = ...
    task_dispatcher: ThreadedTaskDispatcher = ...
    def __init__(
        self,
        map: Any | None = ...,
        adj: Adjustments | None = ...,
        effective_listen: Sequence[tuple[str, int]] | None = ...,
        dispatcher: ThreadedTaskDispatcher | None = ...,
    ) -> None: ...
    def print_listen(self, format_str: str) -> None: ...
    def run(self) -> None: ...
    def close(self) -> None: ...

class BaseWSGIServer(wasyncore.dispatcher):
    channel_class: HTTPChannel = ...
    next_channel_cleanup: int = ...
    socketmod: socket = ...
    asyncore: Any = ...
    sockinfo: tuple[int, int, int, tuple[str, int]] = ...
    family: int = ...
    socktype: int = ...
    application: Any = ...
    adj: Adjustments = ...
    trigger: int = ...
    task_dispatcher: ThreadedTaskDispatcher = ...
    server_name: str = ...
    active_channels: HTTPChannel = ...
    def __init__(
        self,
        application: Any,
        map: Any | None = ...,
        _start: bool = ...,
        _sock: Any | None = ...,
        dispatcher: ThreadedTaskDispatcher | None = ...,
        adj: Adjustments | None = ...,
        sockinfo: Any | None = ...,
        bind_socket: bool = ...,
        **kw: Any,
    ) -> None: ...
    def bind_server_socket(self) -> None: ...
    def get_server_name(self, ip: str) -> str: ...
    def getsockname(self) -> Any: ...
    accepting: bool = ...
    def accept_connections(self) -> None: ...
    def add_task(self, task: Task) -> None: ...
    def readable(self) -> bool: ...
    def writable(self) -> bool: ...
    def handle_read(self) -> None: ...
    def handle_connect(self) -> None: ...
    def handle_accept(self) -> None: ...
    def run(self) -> None: ...
    def pull_trigger(self) -> None: ...
    def set_socket_options(self, conn: Any) -> None: ...
    def fix_addr(self, addr: Any) -> Any: ...
    def maintenance(self, now: int) -> None: ...
    def print_listen(self, format_str: str) -> None: ...
    def close(self) -> None: ...

class TcpWSGIServer(BaseWSGIServer):
    def bind_server_socket(self) -> None: ...
    def getsockname(self) -> tuple[str, tuple[str, int]]: ...
    def set_socket_options(self, conn: socket) -> None: ...

class UnixWSGIServer(BaseWSGIServer):
    def __init__(
        self,
        application: Any,
        map: Any | None = ...,
        _start: bool = ...,
        _sock: Any | None = ...,
        dispatcher: Any | None = ...,
        adj: Adjustments | None = ...,
        sockinfo: Any | None = ...,
        **kw: Any,
    ) -> None: ...
    def bind_server_socket(self) -> None: ...
    def getsockname(self) -> tuple[str, tuple[str, int]]: ...
    def fix_addr(self, addr: Any) -> tuple[str, None]: ...
    def get_server_name(self, ip: Any) -> str: ...

WSGIServer: TcpWSGIServer
