<!-- Start SDK Example Usage -->
```typescript
import { SDK, withSecurity} from "";
import { CreatePetsResponse } from "/src/sdk/models/operations";
import { AxiosError } from "axios";


const sdk = new SDK();

sdk.pets.createPets().then((res: CreatePetsResponse | AxiosError) => {
   // handle response
});
```
<!-- End SDK Example Usage -->