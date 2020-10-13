# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, jsonify, request, render_template
stores = [
        {
           'name':'My Wonderful Store',
           'items':[
                   {
                           'name': 'My Item',
                           'price': 15.99
                           }
                   ]
                }
        ]

app = Flask(__name__)

#@app.route('/') #'http://www.google.com
#def home():
  #  return "Hello, world!"
@app.route()
def home():
    return render_template('index.html')
#Post
@app.route('/store',methods=['POST'])
def create_store():
     request_data=request.get_json()
     new_store={
             'name':request_data['name'],
             'items':[]
             }
     stores.append(new_store)
     return jsonify(new_store)
@app.route('/store/<string:name>')
def get_store(name):
     for store in stores:
         if store['name']==name:
             return jsonify(store)
     return jsonify({'stores':stores})
@app.route('/store')
def get_stores():
     return jsonify({'stores':stores})
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
     request_data = request.get_json()
     for store in stores:
         if store['name']== name:
             new_item={
                     'name':request_data['name'],
                     'price':request_data['price']
                     }
             store['items'].append(new_item)
             return jsonify(new_item)
     return jsonify({'message':'store not found'})
 #GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
      for store in stores:
         if store['name']==name:
             return jsonify({'items':store['items']})
      return jsonify({'message':'store not found'})
 
app.run(port=4900)