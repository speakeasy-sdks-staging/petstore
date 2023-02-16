import { SpeakeasyBase, SpeakeasyMetadata } from "../../../internal/utils";
import * as shared from "../shared";


export class ShowPetByIdPathParams extends SpeakeasyBase {
  @SpeakeasyMetadata({ data: "pathParam, style=simple;explode=false;name=petId" })
  petId: string;
}

export class ShowPetByIdRequest extends SpeakeasyBase {
  @SpeakeasyMetadata()
  pathParams: ShowPetByIdPathParams;
}

export class ShowPetByIdResponse extends SpeakeasyBase {
  @SpeakeasyMetadata()
  contentType: string;

  @SpeakeasyMetadata()
  error?: shared.ErrorT;

  @SpeakeasyMetadata()
  pet?: shared.Pet;

  @SpeakeasyMetadata()
  statusCode: number;
}