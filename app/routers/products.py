from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import Product
from app.services.dynamodb_service import DynamoDBService

router = APIRouter()

@router.get("/")
def get_products(service: DynamoDBService = Depends()):
    return service.get_products()

@router.get("/{product_id}")
def get_product(product_id: str, service: DynamoDBService = Depends()):
    product = service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/")
def create_product(product: Product, service: DynamoDBService = Depends()):
    try:
        product_id = str(product.ProductId)
        product.ProductId = product_id
        print("##############")
        print(product)
    except Exception as e:
        print("@@@@@@@@@@@@@@")
        print(e)
    
    return service.create_product(product.dict())

@router.put("/{product_id}")
def update_product(product_id: str, updates: dict, service: DynamoDBService = Depends()):
    service.update_product(product_id, updates)
    return {"message": "Product updated successfully"}

@router.delete("/{product_id}")
def delete_product(product_id: str, service: DynamoDBService = Depends()):
    service.delete_product(product_id)
    return {"message": "Product deleted successfully"}
