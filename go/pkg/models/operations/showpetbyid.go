package operations

import (
	"github.com/speakeasy-sdks-staging/petstore/pkg/models/shared"
)

type ShowPetByIDPathParams struct {
	PetID string `pathParam:"style=simple,explode=false,name=petId"`
}

type ShowPetByIDRequest struct {
	PathParams ShowPetByIDPathParams
}

type ShowPetByIDResponse struct {
	ContentType string
	Error       *shared.Error
	Pet         *shared.Pet
	StatusCode  int
}
