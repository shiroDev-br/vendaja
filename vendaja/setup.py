from fastapi import FastAPI

def setup_app():
    app = FastAPI()
    from .routers.store import store_router
    from .routers.auth import auth_router
    from .routers.product import product_router
    app.include_router(store_router)
    app.include_router(auth_router)
    app.include_router(product_router)


    @app.get('/')
    def read_root():
        return {'message': 'Hello World'}

    return app