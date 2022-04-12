import requests as r
import json

data = { 
    'd1' : [
        '1153 Cheshire Road',
        'Cheshire',
        'Connecticut',
        '06410'
    ],
    'd2': [
        '2926 West Drive',
        'Chicago',
        'Illinois',
        '60606',
    ],
    'd3': [
        '3398 Beechwood Avenue',
        'Birchwood',
        'Tennessee',
        '37308',
    ],
    'd4':[
        '1705 Grey Fox Farm Road',
        'Houston',
        'Texas',
        '77063',
    ],
    'd5':[
        '2394 Leisure Lane',
        'San Luis Obispo',
        'California',
        '93401',
    ],

}


ndata = { 
    'd1': {'asdf', 'sadf'},
    'd2': {'asd', 'sdf'}

}


url = "http://127.0.0.1:5000/bulk_verify"

results = r.post(url=url, data=data)


print(results.text)

