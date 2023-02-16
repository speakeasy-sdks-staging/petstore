import requests
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Pets:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def create_pets(self) -> operations.CreatePetsResponse:
        r"""Create a pet
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/pets"
        
        headers = {}
        headers["user-agent"] = f"speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}"
        
        client = self._client
        
        r = client.request("POST", url, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreatePetsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            pass
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def list_pets(self, request: operations.ListPetsRequest) -> operations.ListPetsResponse:
        r"""List all pets
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/pets"
        
        headers = {}
        query_params = utils.get_query_params(request.query_params)
        headers["user-agent"] = f"speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}"
        
        client = self._client
        
        r = client.request("GET", url, params=query_params, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListPetsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.Pet]])
                res.pets = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def show_pet_by_id(self, request: operations.ShowPetByIDRequest) -> operations.ShowPetByIDResponse:
        r"""Info for a specific pet
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/pets/{petId}", request.path_params)
        
        headers = {}
        headers["user-agent"] = f"speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}"
        
        client = self._client
        
        r = client.request("GET", url, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ShowPetByIDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Pet])
                res.pet = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    