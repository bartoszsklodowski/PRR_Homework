from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SamplingVarianceReply(_message.Message):
    __slots__ = ["sum", "sum_of_squares"]
    SUM_FIELD_NUMBER: _ClassVar[int]
    SUM_OF_SQUARES_FIELD_NUMBER: _ClassVar[int]
    sum: float
    sum_of_squares: float
    def __init__(self, sum: _Optional[float] = ..., sum_of_squares: _Optional[float] = ...) -> None: ...

class SamplingVarianceRequest(_message.Message):
    __slots__ = ["chunk"]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, chunk: _Optional[_Iterable[float]] = ...) -> None: ...
