from sanic import Sanic
from sanic.response import json, text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import asyncio
from datetime import datetime
from db.models import *

"""async def notify_server_started_after_five_seconds():
    await asyncio.sleep(60)
    print('Server successfully started!')
    await notify_server_started_after_five_seconds()"""


database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}'.format(
    dbuser='postgres',
    dbpass='apple123',
    dbhost='0.0.0.0',
    dbport='5432',
    dbname='avitosanic'
)
engine = create_engine(database_uri, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
app = Sanic("AvitoSanic")
#app.add_task(notify_server_started_after_five_seconds())

# server.py


@app.route("/", methods=["GET"])
async def get_j(request):
    return json({"Musa": "ioio"})

@app.route("/add", methods=["POST"])
async def post_qr(request):
    for name, fullname in session.query(Time.count, Time.time):
        print(name)
        print(fullname)
    #print(request.body)
    return text(request.body)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, access_log=False)
