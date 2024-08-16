from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import Order
from app.services.dynamodb_service import DynamoDBService

router = APIRouter()

@router.post("/")
def create_order(order: Order, service: DynamoDBService = Depends()):
    result = service.create_order(order.ProductId, order.Quantity)
    if not result:
        raise HTTPException(status_code=400, detail="Insufficient inventory")
    return {"message": "Order created successfully"}
