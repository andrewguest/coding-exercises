import random
import secrets
import string
from typing import Union

import valkey
from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from secure import Secure


valkey = valkey.Valkey(host="url-shortener-valkey", port=6379, db=0, decode_responses=True)

app = FastAPI(
    title='URL shortener',
    description='URL shortener written in Python using FastAPI, HTMx, and daisyui',
    version='0.0.1'
)
secure_headers = Secure.with_default_headers()

# Middleware
app.add_middleware(
    CORSMiddleware,  # noqa
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.middleware('http')
async def set_secure_headers(request, call_next):
    response = await call_next(request)
    await secure_headers.set_headers_async(response)
    return response


@app.post('/new', response_class=JSONResponse, status_code=201)
async def create_short_url(long_url: str, custom_short_url: str = None):
    # If the user provided a desired short URL
    if custom_short_url is not None:
        record = await valkey.get(custom_short_url)
        # If the short URL already exists, then tell the user
        if record is not None:
            return JSONResponse(
                status_code=200,
                content={"message": "Shortened URL already exists. Please try again with a different URL."},
            )
        # If the short URL does NOT exist, then we can create a record for it
        else:
            return JSONResponse(
                status_code=201,
                content={"message": "Shortened URL successfully created", "short_url": record, "long_url": long_url}
            )
    # If we need to randomly generate the short URL
    else:
        # Generate a random string of letters and numbers between 5 and 15 characters long
        random_short_url = ''.join(
            secrets.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(5, 15))
        )
        record = await valkey.get(random_short_url)

        # If we generated a short URL that already exists, then keep trying to find one that doesn't exist
        while record is not None:
            random_short_url = ''.join(
                secrets.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(5, 15))
            )
            record = await valkey.get(random_short_url)

        await valkey.set(random_short_url, long_url)
        await valkey.set(long_url, random_short_url)

        return JSONResponse(
            status_code=201,
            content={"message": "Shortened URL successfully created", "short_url": record, "long_url": long_url}
        )


@app.get("/{short_url}", response_class=Union[JSONResponse, RedirectResponse], status_code=Union[200, 307])
async def redirect_to_full_url(short_url: str):
    record = await valkey.get(short_url)

    if record is not None:
        return RedirectResponse(url=record)
    else:
        return JSONResponse(status_code=200, content={"detail": f"No redirect URL for '{short_url}'"})