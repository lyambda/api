"""
    MIT License

    Copyright (c) 2021 lamda

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

# ************** Standart module *********************
from datetime import datetime
import configparser
import psutil
import uvicorn
# ************** Standart module end *****************

# ************** External module *********************
from fastapi import FastAPI
from fastapi import Request
#from fastapi import WebSocket
from starlette.templating import Jinja2Templates
from starlette.responses import Response
from mod import API
from mod.utils import Utilities
# ************** External module end *****************

# ************** Logging beginning *******************
from loguru import logger
from mod.logging import add_logging
# ************** Unicorn logger off ******************
import logging
#logging.disable()
# ************** Logging end *************************

# ************** Read "config.ini" ********************
config = configparser.ConfigParser()
config.read('config.ini')
database = config["DATABASE"]
directory = config["TEMPLATES"]
logging = config["LOGGING"]
# ************** END **********************************

# loguru logger on
add_logging(logging.getint("level"))

# Server instance creation
app = FastAPI()
logger.info("Start server")
templates = Jinja2Templates(directory["folder"])

# MongoDB
api = API(
    mongodb=database['mongodb'],
    smtp=database['smtp']
)

# Record server start time (UTC)
server_started = datetime.now()

# Server home page
@app.get('/')
def home_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

# methods
@app.get('/{method}')
def methods_page(request: Request, method):
    data = request.get_json()
    return Response(*api.methods[method](**data), {'Content-Type': 'application/json'})

# Server page with working statistics
@app.get('/status')
def status_page(request: Request):
    ram = psutil.virtual_memory()
    stats = {
        "Server time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Server uptime": str(datetime.now()-server_started),
        "CPU": f"{psutil.cpu_count()} cores ({psutil.cpu_freq().max}MHz) with {psutil.cpu_percent()} current usage",
        "RAM": f"{ram.used >> 20} mb / {ram.total >> 20} mb"
        }
    return templates.TemplateResponse('status.html',
                                      {'request': request,
                                       'stats': stats})

if __name__ == "__main__":
    uvicorn.run('app:app',
        host="0.0.0.0", 
        port=8000,
        log_level="debug",
        http="h11",
        reload=True, 
        use_colors=True,
        workers=3
    )