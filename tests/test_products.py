from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_product():
    response = client.post("/products", json={
        "ProductId": "test-id",
        "ProductName": "Test Product",
        "Price": 99.99,
        "StockLevel": 10,
        "imageUrl": "http://example.com/test-product.jpg"
    })
    assert response.status_code == 201
    assert response.json()["ProductId"] == "test-id"

def test_read_product():
    response = client.get("/products/test-id")
    assert response.status_code == 200
    assert response.json()["ProductId"] == "test-id"

def test_update_product():
    response = client.put("/products/test-id", json={
        "Price": 79.99
    })
    assert response.status_code == 200
    assert response.json()["Price"] == 79.99

def test_delete_product():
    response = client.delete("/products/test-id")
    assert response.status_code == 200
    assert response.json()["detail"] == "Product deleted successfully"

def test_read_inventory():
    response = client.get("/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("ProductId" in item for item in response.json())
    assert all("ProductName" in item for item in response.json())
    assert all("StockLevel" in item for item in response.json())



def test_read_inventory_item_not_found():
    response = client.get("/inventory/non-existent-id")
    assert response.status_code == 404
    assert response.json() == {"detail": "Inventory not found"}
