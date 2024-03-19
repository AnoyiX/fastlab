# FastLab

An extension library for FastAPI framework

[![Supported Versions](https://img.shields.io/pypi/pyversions/fastlab.svg)](https://pypi.org/project/fastlab)
[![PyPI version](https://badge.fury.io/py/fastlab.svg)](https://pypi.org/project/fastlab)
[![License](https://img.shields.io/github/license/tezignlab/fastlab)](https://github.com/tezignlab/fastlab/blob/main/LICENSE)


## Features

- [FastLab](#fastlab)
  - [Features](#features)
  - [Installation](#installation)
  - [Getting started](#getting-started)
    - [Logging](#logging)
    - [Models](#models)
      - [🔰 Response](#-response)
      - [🔰 PageData](#-pagedata)
    - [Utils](#utils)
      - [🔰 TimeUtils](#-timeutils)
    - [Routers](#routers)
      - [🔰 HealthRouter](#-healthrouter)
    - [Decorators](#decorators)
      - [🔰 LogExecTime](#-logexectime)
      - [🔰 WithEnvConfig](#-withenvconfig)
  - [Testing](#testing)


## Installation

use `pip` to install the package:

```shell
pip install fastlab
```

## Getting started

### Logging

Easy to log string to console, see more: [https://docs.python.org/3/library/logging.html](https://docs.python.org/3/library/logging.html)

```python
from fastlab import logs

logs.warning('warn')    # 2021-12-18 14:23:31.000  WARNING 88493 --- [  MainThread] test_logs        : warn
logs.info('info')       # 2021-12-18 14:23:31.000     INFO 88493 --- [  MainThread] test_logs        : info
logs.error('error')     # 2021-12-18 14:23:31.000    ERROR 88493 --- [  MainThread] test_logs        : error
```

### Models

Common Models

#### 🔰 Response

```python
from fastapi import FastAPI
from pydantic import BaseModel
from fastlab.models import Response


class Item(BaseModel):
    name: str
    version: str


app = FastAPI()


@app.get("/item", response_model=Response[Item])
async def item():
    return Response(data=Item(name='fastlab', version='0.1.0'))
```

Get `http://localhost:8080/item` response: 
```json
{
    "code": 0,
    "message": "",
    "data": {
        "name": "fastlab",
        "version": "0.1.0"
    }
}
```

#### 🔰 PageData

```python
from fastapi import FastAPI
from pydantic import BaseModel
from fastlab.models import Response, PageData


class Item(BaseModel):
    name: str
    version: str


app = FastAPI()


@app.get("/items", response_model=Response[PageData[Item]])
async def items(skip: int = 0, limit: int = 10):
    total = 100
    data = [Item(name=f'fastlab-{i}', version=f'0.1.{i}') for i in range(skip, skip + limit)]
    return Response(data=PageData(skip=skip, limit=limit, total=total, has_more=total > skip + limit, data=data))
```


### Utils

#### 🔰 TimeUtils

```python
from fastlab.utils import TimeUtils

# Print now timestamp: 1639732030521
print(TimeUtils.timestamp())
```

### Routers

#### 🔰 HealthRouter

API for health check, endpoint `/health`.

```python
from fastapi import FastAPI
from fastlab.routers import HealthRouter

app = FastAPI()
app.include_router(HealthRouter)
```

### Decorators

#### 🔰 LogExecTime

Log wrapper for measuring sync & async function execution times.

```python
import asyncio
import time
from fastlab.decorators import LogExecTime, LogExecTimeAsync

@LogExecTime
def log_sleep():
    time.sleep(1.5)

@LogExecTimeAsync
async def log_sleep_async():
    await asyncio.sleep(1.5)

log_sleep()
asyncio.run(log_sleep_async())
```


#### 🔰 WithEnvConfig

Replace the configuration with system environment variables. Follows:

1. Change the setting name to uppercase
2. Prefix it with `prefix` setting
3. Escape any underscores (`_`) by duplicating them
4. Convert all periods (.) to underscores (`_`)

```python
from fastlab.decorators import WithEnvConfig

@WithEnvConfig(prefix='FL_')
def load_config():
    return {
      'name': 'fastlab', 
      'version': '0.2.1',
      'extra': {
        'memory_lock': False
      }
    }

conf = load_config()
```

For example, `FL_EXTRA_MEMORY__LOCK=true` transform `conf['extra']['memory_lock']` as `True`


## Testing

Install this package locally

```
python setup.py develop
```

Run test case

```
python tests/test_logs.py
```
