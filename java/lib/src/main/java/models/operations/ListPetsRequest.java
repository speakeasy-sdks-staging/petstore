package .models.operations;



public class ListPetsRequest {
    public ListPetsQueryParams queryParams;
    public ListPetsRequest withQueryParams(ListPetsQueryParams queryParams) {
        this.queryParams = queryParams;
        return this;
    }
    
}
