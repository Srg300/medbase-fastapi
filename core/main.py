import uvicorn

from fastapi import FastAPI

from database import engine
from users import models
from api import users, meds


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def configure():
    configure_routing()


def configure_routing():
    app.include_router(users.router)
    app.include_router(meds.router)


if __name__ == '__main__':
    configure()
    uvicorn.run(
        app='main:api', port=8000, host='127.0.0.1', reload=True, debug=True
        )
else:
    configure()
