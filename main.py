'''Aplication initializing function and printing'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config.docs import extend_openapi
from config.database import db
from config.server import base_url, port
from config.env import application, environment
from config.middlewares import middlewares, cors, log_request_middleware
from controllers import routes, tags
from domain.errors import base_errors


DESCRIPTION = '''
API for managing shopping lists.
'''

app = FastAPI(
    title=application['name'],
    description=DESCRIPTION,
    version='0.0.1',
    contact={
        'name': 'Douglas',
        'url': 'https://douglaschalegre.com.br',
        'email': 'douglas.chalegre@gmail.com',
    },
    swagger_ui_parameters={'defaultModelsExpandDepth': -1},
    responses=base_errors,
)
for middleware in middlewares:
    app.middleware(middleware.type)(middleware(app))
app.add_middleware(CORSMiddleware, **cors)
app.middleware('http')(log_request_middleware)

for router in routes:
    app.include_router(router)

app.openapi = extend_openapi(app, base_url or '', tags=tags)

api = FastAPI(openapi_url=None)
api.mount(base_url, app)

print(f'''
Service {application['id']} is available on port {port}:

  Environment variables:

    -> Database:
        NAME_DB: {db['name']}

    -> Server:
        SUB_DIR: {base_url}
        SERVER_PORT: {str(port)}

    -> Custom:
        APP_ID: {application['id']}
        APP_NAME: {application['name']}
        ENVIRONMENT: {environment}

  Docs (Swagger) available on: http://localhost:{port}{base_url or ''}{app.docs_url}.
''')

reload = environment.lower() != 'prd'

if __name__ == '__main__':
    uvicorn.run('main:api',
                host='0.0.0.0',
                port=port,
                reload=reload)
