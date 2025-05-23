from fastapi import FastAPI

def setup_app():
    app = FastAPI()
    from .routers.store import store_router
    app.include_router(store_router)


    @app.get('/')
    def read_root():
        return {'message': 'Hello World'}

    return app