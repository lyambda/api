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
# ************** External module end *****************

# ************** Read "config.ini" ********************
config = configparser.ConfigParser()
config.read('config.ini')
database = config["DATABASE"]
directory = config["TEMPLATES"]
# ************** END **********************************

# Server instance creation
app = FastAPI()
#templates = Jinja2Templates(directory["folder"])
templates = Jinja2Templates('templates')

# Record server start time (UTC)
server_started = datetime.now()

# Server home page
@app.get('/')
def home_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

# Server page with working statistics
@app.get('/status')
def status_page(request: Request):
    ram = psutil.virtual_memory()
    stats = {
        'Server time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Server uptime': str(datetime.now()-server_started),
        "CPU": f"{psutil.cpu_count()} cores ({psutil.cpu_freq().max}MHz) with {psutil.cpu_percent()} current usage",
        "RAM": f"{ram.used >> 20} mb / {ram.total >> 20} mb"
        }
    return templates.TemplateResponse('status.html',
                                      {'request': request,
                                       'stats': stats})

if __name__ == "__main__":
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True, use_colors=True, workers=3)