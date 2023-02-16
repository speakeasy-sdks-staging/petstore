package .models.operations;



public class ShowPetByIdResponse {
    public String contentType;
    public ShowPetByIdResponse withContentType(String contentType) {
        this.contentType = contentType;
        return this;
    }
    
    public .models.shared.Error error;
    public ShowPetByIdResponse withError(.models.shared.Error error) {
        this.error = error;
        return this;
    }
    
    public .models.shared.Pet pet;
    public ShowPetByIdResponse withPet(.models.shared.Pet pet) {
        this.pet = pet;
        return this;
    }
    
    public Integer statusCode;
    public ShowPetByIdResponse withStatusCode(Integer statusCode) {
        this.statusCode = statusCode;
        return this;
    }
    
}
