import bdb
from _typeshed import Incomplete

from win32com.axdebug.util import trace
from win32com.server.util import unwrap as unwrap
from win32comext.axdebug import gateways as gateways

def fnull(*args) -> None: ...

debugging: int
traceenter = fnull
tracev = fnull
traceenter = trace
tracev = trace

class OutputReflector:
    writefunc: Incomplete
    file: Incomplete
    def __init__(self, file, writefunc) -> None: ...
    def __getattr__(self, name): ...
    def write(self, message) -> None: ...

g_adb: Incomplete

def OnSetBreakPoint(codeContext, breakPointState, lineNo) -> None: ...

class Adb(bdb.Bdb, gateways.RemoteDebugApplicationEvents):
    debugApplication: Incomplete
    debuggingThread: Incomplete
    debuggingThreadStateHandle: Incomplete
    stackSnifferCookie: Incomplete
    codeContainerProvider: Incomplete
    breakFlags: Incomplete
    breakReason: Incomplete
    appDebugger: Incomplete
    appEventConnection: Incomplete
    logicalbotframe: Incomplete
    currentframe: Incomplete
    recursiveData: Incomplete
    def canonic(self, fname): ...
    def reset(self) -> None: ...
    def stop_here(self, frame): ...
    def break_here(self, frame): ...
    def break_anywhere(self, frame): ...
    def dispatch_return(self, frame, arg): ...
    def dispatch_line(self, frame): ...
    def dispatch_call(self, frame, arg): ...
    def trace_dispatch(self, frame, event, arg): ...
    def user_line(self, frame) -> None: ...
    def user_return(self, frame, return_value) -> None: ...
    def user_exception(self, frame, exc_info) -> None: ...
    def set_trace(self) -> None: ...  # type: ignore[override]
    def CloseApp(self) -> None: ...
    stackSniffer: Incomplete
    def AttachApp(self, debugApplication, codeContainerProvider) -> None: ...
    def ResetAXDebugging(self) -> None: ...
    botframe: Incomplete
    stopframe: Incomplete
    def SetupAXDebugging(self, baseFrame: Incomplete | None = ..., userFrame: Incomplete | None = ...) -> None: ...
    def OnConnectDebugger(self, appDebugger): ...
    def OnDisconnectDebugger(self) -> None: ...
    def OnSetName(self, name) -> None: ...
    def OnDebugOutput(self, string) -> None: ...
    def OnClose(self) -> None: ...
    def OnEnterBreakPoint(self, rdat) -> None: ...
    def OnLeaveBreakPoint(self, rdat) -> None: ...
    def OnCreateThread(self, rdat) -> None: ...
    def OnDestroyThread(self, rdat) -> None: ...
    def OnBreakFlagChange(self, abf, rdat) -> None: ...

def Debugger(): ...
