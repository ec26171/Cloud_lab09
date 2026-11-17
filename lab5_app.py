from flask import Flask, render_template, request, jsonify
import json
import requests
import requests_cache
requests_cache.install_cache('crime_api_cache', backend='sqlite', expire_after=36000)
app = Flask(__name__)
crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'
categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'
@app.route('/crimestat', methods=['GET'])
def crimechart():
    my_latitude = request.args.get('lat','52.629729')
    my_longitude = request.args.get('lng','-1.131592')
    my_date = request.args.get('date','2026-5')
    crime_url = crime_url_template.format(lat = my_latitude, lng = my_longitude, data = my_date)
    resp = requests.get(crime_url)
    if resp.ok:
        return jsonify(resp.json())
    else:
        print(resp.reason)
if __name__=="__main__":
    app.run(host='0.0.0.0')
