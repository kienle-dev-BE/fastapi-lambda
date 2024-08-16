
## Endpoints

### Products

- **GET /products**
  - Retrieve a list of products.
  - Query parameters: `limit`, `lastKey`

- **GET /products/{product_id}**
  - Retrieve a specific product by ID.

- **POST /products**
  - Create a new product.

- **PUT /products/{product_id}**
  - Update an existing product.

- **DELETE /products/{product_id}**
  - Delete a product by ID.

### Inventory

- **GET /inventory**
  - Retrieve a list of inventory items.

- **GET /inventory/{product_id}**
  - Retrieve inventory details for a specific product by ID.

### Orders

- **POST /orders**
  - Create a new order and update inventory.

## Local Development

### Prerequisites

- Python 3.x
- Pip

### Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd fastapi-lambda-app
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

1. Start the FastAPI application:

    ```bash
    uvicorn app.main:app --reload
    ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

### Running Live 

1. Access the API documentation at `https://gkz4po4qva.execute-api.ap-southeast-1.amazonaws.com/Prod`.

2. data test API example at `https://docs.google.com/document/d/1akCelKSO9b0JhxfxABMo05uF9ixTCme-Af8fnN1YpUA/edit?usp=sharing`

### Testing

Run the tests using `pytest`:

```bash
pytest
