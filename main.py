from flask import Flask, request 
import pandas as pd 

df = pd.read_csv('Data/utilization2019csv.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'Time to get some County Codes!!!..... I Hope.....'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(25)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/county_code/<value>', methods=['GET'])
def icdcode(value):
    print('value: ', value)
    filtered = df[df['county_code'] == value]
    return filtered.to_json(orient="records")

#7.0
@app.route('/silly/<value>', methods=['GET'])
def countycode(value):
    print('value: ', value)
    filtered = df[df['county_code'] == value]
    return filtered.to_json(orient="records")

#7.0
@app.route('/silly/<value>/sex/<value2>', methods=['GET'])
def countycode2(value, value2):
    filtered = df[df['county_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]

if __name__ == '__main__':
    app.run(debug=True)
