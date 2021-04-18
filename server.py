from sanic import Sanic
from sanic.response import json
import SQLAlchemy
app = Sanic("AvitoSanic")
# server.py


@app.route("/", methods=["GET"])
async def get_j(request):
	return json({"Musa": "ioio"})

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=1337, access_log=False)
