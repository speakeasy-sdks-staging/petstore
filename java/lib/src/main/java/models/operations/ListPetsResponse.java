package .models.operations;



public class ListPetsResponse {
    public String contentType;
    public ListPetsResponse withContentType(String contentType) {
        this.contentType = contentType;
        return this;
    }
    
    public .models.shared.Error error;
    public ListPetsResponse withError(.models.shared.Error error) {
        this.error = error;
        return this;
    }
    
    public .models.shared.Pet[] pets;
    public ListPetsResponse withPets(.models.shared.Pet[] pets) {
        this.pets = pets;
        return this;
    }
    
    public Integer statusCode;
    public ListPetsResponse withStatusCode(Integer statusCode) {
        this.statusCode = statusCode;
        return this;
    }
    
}
