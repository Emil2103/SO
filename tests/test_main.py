def test_create_product(client):
    response = client.post("/products/", json={"name": "Test Product", "description": "string", "price": 10.0, "category_id": 1})
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {'name': 'Test Product', 'description': 'string', 'price': 10.0, 'category_id': 1, 'id': 1, 'category': {'name': 'Test Category'}}


def test_read_product(client):
    response = client.get("/products/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["description"] == "string"
    assert data["price"] == 10.0
    assert data["category_id"] == 1

def test_update_product(client):
    response = client.put("/products/1", json={"name": "Updated Product", "description": "hi", "price": 20.0, "category_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Product"
    assert data["description"] == "hi"
    assert data["price"] == 20.0
    assert data["category_id"] == 1

def test_delete_product(client):
    response = client.delete("/products/1")
    assert response.status_code == 200
    data = response.json()

    # Проверка что продукт действительно удален
    response = client.get("/products/1")
    assert response.status_code == 404
