# Laptop Service
# BEST VERSION

from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
import pymongo

# Instantiate the app
app = Flask(__name__)
api = Api(app)

# ACCESS DATABASE
client = MongoClient('db', 27017)
db = client.tododb # gets database

class all(Resource): # use 5001 to access!
	def get(self):
		num = request.args.get('top')
		if num == None:
			top = 50
		else:
			top = int(num)
		_items = db.tododb.find().sort([('open_times',pymongo.ASCENDING), ('close_times',pymongo.ASCENDING)]).limit(top)
		li_data = [item for item in _items]

		app.logger.debug("DATA IS")
		app.logger.debug(li_data)
		
		dic = {}
		otimes = []
		ctimes = []
		
		for item in li_data:
			otimes.append(item['open_times'])
			ctimes.append(item['close_times'])
			
		app.logger.debug("OPEN IS")
		app.logger.debug(otimes)
		app.logger.debug("CLOSE IS")
		app.logger.debug(ctimes)
		
		dic['open_times'] = otimes
		dic['close_times'] = ctimes
		
		return dic

api.add_resource(all, '/listAll')

class all_json(Resource):
	def get(self):
		num = request.args.get('top')
		if num == None:
			top = 50
		else:
			top = int(num)
		_items = db.tododb.find().sort([('open_times',pymongo.ASCENDING), ('close_times',pymongo.ASCENDING)]).limit(top)
		li_data = [item for item in _items]		
		dic = {}
		otimes = []
		ctimes = []		
		for item in li_data:
			otimes.append(item['open_times'])
			ctimes.append(item['close_times'])		
		dic['open_times'] = otimes
		dic['close_times'] = ctimes
		return dic

api.add_resource(all_json, '/listAll/json')

class all_csv(Resource):
	def get(self):
		num = request.args.get('top')
		if num == None:
			top = 50
		else:
			top = int(num)
		_items = db.tododb.find().sort([('open_times',pymongo.ASCENDING), ('close_times',pymongo.ASCENDING)]).limit(top)
		li_data = [item for item in _items]
		
		csv_string = ""
		for item in li_data:
			csv_string += item['open_times'] + ", "
			csv_string += item['close_times'] + ", "
		return csv_string

api.add_resource(all_csv, '/listAll/csv')

class open_json(Resource):
	def get(self):
		num = request.args.get('top')
		if num == None:
			top = 50
		else:
			top = int(num)
		_items = db.tododb.find().sort('open_times', pymongo.ASCENDING).limit(top)
		li_data = [item for item in _items]
		
		app.logger.debug("MADE IT HERE")
		dic = {}
		otimes = []	
		for item in li_data:
			otimes.append(item['open_times'])		
		dic['open_times'] = otimes
		return dic

api.add_resource(open_json, '/listOpenOnly/json')

class open_csv(Resource):
	def get(self):
		num = request.args.get('top')
		if num == None:
			top = 50
		else:
			top = int(num)
		_items = db.tododb.find().sort('open_times', pymongo.ASCENDING).limit(top)
		li_data = [item for item in _items]
		
		csv_string = ""
		for item in li_data:
			csv_string += item['open_times'] + ", "
		return csv_string

api.add_resource(open_csv, '/listOpenOnly/csv')

class close_json(Resource):
	def get(self):
		num = request.args.get('top')
		if num == None:
			top = 50
		else:
			top = int(num)
		_items = db.tododb.find().sort('close_times', pymongo.ASCENDING).limit(top)
		li_data = [item for item in _items]
		
		dic = {}
		ctimes = []		
		for item in li_data:
			ctimes.append(item['close_times'])		
		dic['close_times'] = ctimes
		return dic

api.add_resource(close_json, '/listCloseOnly/json')

class close_csv(Resource):
	def get(self):
		num = request.args.get('top')
		if num == None:
			top = 50
		else:
			top = int(num)
		_items = db.tododb.find().sort('close_times', pymongo.ASCENDING).limit(top)
		li_data = [item for item in _items]
		
		csv_string = ""
		for item in li_data:
			csv_string += item['close_times'] + ", "
		return csv_string

api.add_resource(close_csv, '/listCloseOnly/csv')

# Create routes
# Another way, without decorators

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
