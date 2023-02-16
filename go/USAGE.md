<!-- Start SDK Example Usage -->
```go
package main

import (
    "log"
    "github.com/speakeasy-sdks-staging/petstore"
    "github.com/speakeasy-sdks-staging/petstore/pkg/models/shared"
    "github.com/speakeasy-sdks-staging/petstore/pkg/models/operations"
)

func main() {
    s := sdk.New()
    
    res, err := s.Pets.CreatePets(ctx)
    if err != nil {
        log.Fatal(err)
    }

    if res.StatusCode == http.StatusOK {
        // handle response
    }
```
<!-- End SDK Example Usage -->