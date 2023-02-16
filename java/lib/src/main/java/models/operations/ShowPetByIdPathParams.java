package .models.operations;

import .utils.SpeakeasyMetadata;

public class ShowPetByIdPathParams {
    @SpeakeasyMetadata("pathParam:style=simple,explode=false,name=petId")
    public String petId;
    public ShowPetByIdPathParams withPetId(String petId) {
        this.petId = petId;
        return this;
    }
    
}
