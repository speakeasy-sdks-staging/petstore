import dataclasses
from ..shared import error as shared_error
from ..shared import pet as shared_pet
from typing import Optional


@dataclasses.dataclass
class ShowPetByIDPathParams:
    pet_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'petId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ShowPetByIDRequest:
    path_params: ShowPetByIDPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ShowPetByIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    pet: Optional[shared_pet.Pet] = dataclasses.field(default=None)
    