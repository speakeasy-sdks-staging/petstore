package operations

import (
	"github.com/speakeasy-sdks-staging/petstore/pkg/models/shared"
)

type CreatePetsResponse struct {
	ContentType string
	Error       *shared.Error
	StatusCode  int
}
