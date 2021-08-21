
import uvicorn

from app.fastapi_app import app
from modules.processes.schemas.response import MessageResponsetSchema
from modules.processes.views import router

app.include_router(router, prefix='/api/processes')


@app.get('/')
async def root() -> MessageResponsetSchema:
    return MessageResponsetSchema(message='Hello world!')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
