from typing import Any, Dict, List, Optional, Tuple, Union, TypeVar, Type, Generic

from django.contrib.postgres import lookups
from django.db.models import Field, Transform
from django.db.models.fields import Field
from django.db.models.lookups import Exact, In

from .mixins import CheckFieldDefaultMixin

_T = TypeVar('_T', bound=Field)


class ArrayField(CheckFieldDefaultMixin, Field, Generic[_T]):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    base_field: Any = ...
    size: Any = ...
    default_validators: Any = ...
    from_db_value: Any = ...

    def __init__(
        self, base_field: Field, size: None = ..., **kwargs: Any
    ) -> None: ...
    @property
    def model(self): ...
    @model.setter
    def model(self, model: Any) -> None: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    def set_attributes_from_name(self, name: str) -> None: ...
    @property
    def description(self): ...
    def db_type(self, connection: Any): ...
    def get_db_prep_value(
        self, value: Any, connection: Any, prepared: bool = ...
    ): ...
    def deconstruct(
        self
    ) -> Tuple[
        None, str, List[Any], Dict[str, Optional[Union[bool, Field]]]
    ]: ...
    def to_python(self, value: Any): ...
    def value_to_string(self, obj: Any): ...
    def get_transform(self, name: Any): ...
    def validate(self, value: Any, model_instance: Any) -> None: ...
    def run_validators(self, value: Any) -> None: ...
    def formfield(self, **kwargs: Any): ...
    def __get__(self, instance, owner) -> List[_T]: ...

class ArrayContains(lookups.DataContains):
    def as_sql(self, qn: Any, connection: Any): ...

class ArrayContainedBy(lookups.ContainedBy):
    def as_sql(self, qn: Any, connection: Any): ...

class ArrayExact(Exact):
    def as_sql(self, qn: Any, connection: Any): ...

class ArrayOverlap(lookups.Overlap):
    def as_sql(self, qn: Any, connection: Any): ...

class ArrayLenTransform(Transform):
    lookup_name: str = ...
    output_field: Any = ...
    def as_sql(self, compiler: Any, connection: Any): ...

class ArrayInLookup(In):
    def get_prep_lookup(self): ...

class IndexTransform(Transform):
    index: Any = ...
    base_field: Any = ...
    def __init__(
        self, index: Any, base_field: Any, *args: Any, **kwargs: Any
    ) -> None: ...
    def as_sql(self, compiler: Any, connection: Any): ...
    @property
    def output_field(self): ...

class IndexTransformFactory:
    index: Any = ...
    base_field: Any = ...
    def __init__(self, index: Any, base_field: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...

class SliceTransform(Transform):
    start: Any = ...
    end: Any = ...
    def __init__(
        self, start: Any, end: Any, *args: Any, **kwargs: Any
    ) -> None: ...
    def as_sql(self, compiler: Any, connection: Any): ...

class SliceTransformFactory:
    start: Any = ...
    end: Any = ...
    def __init__(self, start: Any, end: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
