import dataclasses
from ..shared import error as shared_error
from ..shared import pet as shared_pet
from typing import Optional


@dataclasses.dataclass
class ListPetsQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListPetsRequest:
    query_params: ListPetsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ListPetsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    pets: Optional[list[shared_pet.Pet]] = dataclasses.field(default=None)
    