from myapp.models import Locations
from myapp import db
import json, requests

def saveToDatabase(address, city, state, zip_code, lat, lng):
    loc = Locations(address=address, city=city, state=state,
                        zip_code=zip_code, latitude=lat, longitude=lng)
    
    db.session.add(loc)
    db.session.commit()
    

def get_address_from_db(address, city, state, zip_code):
    is_available = Locations.query.filter_by(address=address, city=city,
                                                state=state, zip_code=zip_code).first()
    if is_available:
        return is_available
    else:
        return False


def get_area(address, city, state, zip_code):
    
    checkDB = get_address_from_db(address, city, state, zip_code)
    
    if checkDB:
        # print(f"received from database: {checkDB}")
        # print(type(checkDB))
        return [checkDB.latitude, checkDB.longitude]
    
    apiAddress = str(address +','+ zip_code +','+ city +','+ state)
    
    parameters = {
        "key": "Yf9ZOA3JSiKNlpxiIIzdglgzI33nWpG3",
        "location": apiAddress
    }

    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
    
    data = response.text
    dataJ = json.loads(data)['results']
    lat = (dataJ[0]['locations'][0]['latLng']['lat'])
    lng = (dataJ[0]['locations'][0]['latLng']['lng'])
    
    if response.status_code==200:
        saveToDatabase(address, city, state, zip_code, lat, lng)
    else:
        print(f"error response is: {response.status_code}")
    
    return [lat, lng]