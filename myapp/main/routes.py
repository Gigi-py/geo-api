import json
from flask import Blueprint, render_template, redirect, url_for, request
import requests
from .utils import get_area


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        zip_code = request.form.get('zip_code')
        
        results = get_area(address, city, state, zip_code)
        
        return render_template("results.html", results=results)
        
    return render_template("index.html")


@main.route('/bulk_verify', methods=['POST'])
def verify():
    results = []
    d1 = request.form.getlist('d1')
    print(len(d1))
    results.append({'address_1': {'address': d1[0], 'city': d1[1], 
                           'state': d1[2], 'zip_code': d1[3]}})
    d1 = get_area(address=d1[0], city=d1[1], state=d1[2], zip_code=d1[3])
    results[0]['address_1']['latitude'] = d1[0]
    results[0]['address_1']['longitude'] = d1[1]

    
    d2 = request.form.getlist('d2')
    results.append({'address_2': {'address': d2[0], 'city': d2[1], 
                           'state': d2[2], 'zip_code': d2[3]}})
    d2 = get_area(address=d2[0], city=d2[1], state=d2[2], zip_code=d2[3])
    results[1]['address_2']['latitude'] = d2[0]
    results[1]['address_2']['longitude'] = d2[1]
    
    d3 = request.form.getlist('d3')
    results.append({'address_3': {'address': d3[0], 'city': d3[1], 
                           'state': d3[2], 'zip_code': d3[3]}})
    d3 = get_area(address=d3[0], city=d3[1], state=d3[2], zip_code=d3[3])
    results[2]['address_3']['latitude'] = d3[0]
    results[2]['address_3']['longitude'] = d3[1]
    
    d4 = request.form.getlist('d4')
    results.append({'address_4': {'address': d4[0], 'city': d4[1], 
                           'state': d4[2], 'zip_code': d4[3]}})
    d4 = get_area(address=d4[0], city=d4[1], state=d4[2], zip_code=d4[3])
    results[3]['address_4']['latitude'] = d4[0]
    results[3]['address_4']['longitude'] = d4[1]
    
    d5 = request.form.getlist('d5')
    results.append({'address_5': {'address': d5[0], 'city': d5[1], 
                           'state': d5[2], 'zip_code': d5[3]}})
    d5 = get_area(address=d5[0], city=d5[1], state=d5[2], zip_code=d5[3])
    results[4]['address_5']['latitude'] = d5[0]
    results[4]['address_5']['longitude'] = d5[1]
    
    return {'results': results}


