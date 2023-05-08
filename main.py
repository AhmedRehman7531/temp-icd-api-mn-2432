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
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")

@app.route('/county_code')
def county():
    county = df[df['county_code'] == value]
    return county.to_json(orient="records")    

@app.route('/count')
def count():
    result = request.args.get('result')
    filtered_df = df[df['county_code'] == result]
    count = len(filtered_df)
    return str(count)

    

if __name__ == '__main__':
    app.run(debug=True)
