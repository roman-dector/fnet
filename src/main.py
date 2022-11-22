from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def read_root(name: str | None = None, message: str | None = None):
    if not name and not message:
        return 'Rekruto! Давай дружить!'

    greeting: str = '' if not name else f'Hello {name}!'
    message: str = '' if not message else f'{message}!'

    return f"{greeting} {message}"
