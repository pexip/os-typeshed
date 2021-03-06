from datetime import datetime as datetime

from aws_xray_sdk.core.context import Context as Context
from aws_xray_sdk.core.models.dummy_entities import DummySegment as DummySegment
from aws_xray_sdk.core.utils.compat import PY2 as PY2

from .sampling_rule import SamplingRule as SamplingRule

class ServiceConnector:
    def __init__(self) -> None: ...
    def fetch_sampling_rules(self): ...
    def fetch_sampling_target(self, rules): ...
    def setup_xray_client(self, ip, port, client) -> None: ...
    @property
    def context(self): ...
    @context.setter
    def context(self, v) -> None: ...
