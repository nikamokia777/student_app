from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/products')
def read():
    return {'Message: Products retrieved successfully'}
@app.post('/products')
def create():
    return {'Message: Products created successfully'}

@app.put('/products/{product_id}')
def update_product(product_id: int):
    return {'message': f'Product ID: {product_id} fully updated'}

@app.patch('/products/{product_id}')
def patch_product(product_id: int):
    return {'message': f'Product ID: {product_id} partially updated'}

@app.delete('/products/{product_id}')
def delete_product(product_id: int):
    return {'message': f'Product ID: {product_id} deleted successfully'}

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
