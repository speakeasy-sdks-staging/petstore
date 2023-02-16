package .models.operations;

import .utils.SpeakeasyMetadata;

public class ListPetsQueryParams {
    @SpeakeasyMetadata("queryParam:style=form,explode=true,name=limit")
    public Integer limit;
    public ListPetsQueryParams withLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    
}
