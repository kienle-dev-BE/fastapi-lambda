from fastapi import APIRouter, HTTPException, Depends
from app.services.dynamodb_service import DynamoDBService

router = APIRouter()

@router.get("/")
def get_inventory(service: DynamoDBService = Depends()):
    return service.get_inventory()

@router.get("/{product_id}")
def get_inventory_item(product_id: str, service: DynamoDBService = Depends()):
    item = service.get_inventory_item(product_id)
    if not item:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return item
