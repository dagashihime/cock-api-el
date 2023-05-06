from api import app,db
from api.models import Dry

# https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/#create-the-detail-endpoint-in-flask

@app.get('/dry')
def dry():
   return [dry.to_dict() for dry in Dry.query.all()]

@app.route('/dry/<id>')
def d(id):
   return Dry.query.get(id).to_dict()