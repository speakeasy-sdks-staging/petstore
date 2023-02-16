import { SpeakeasyBase, SpeakeasyMetadata } from "../../../internal/utils";
import * as shared from "../shared";


export class ListPetsQueryParams extends SpeakeasyBase {
  @SpeakeasyMetadata({ data: "queryParam, style=form;explode=true;name=limit" })
  limit?: number;
}

export class ListPetsRequest extends SpeakeasyBase {
  @SpeakeasyMetadata()
  queryParams: ListPetsQueryParams;
}

export class ListPetsResponse extends SpeakeasyBase {
  @SpeakeasyMetadata()
  contentType: string;

  @SpeakeasyMetadata()
  error?: shared.ErrorT;

  @SpeakeasyMetadata({ elemType: shared.Pet })
  pets?: shared.Pet[];

  @SpeakeasyMetadata()
  statusCode: number;
}