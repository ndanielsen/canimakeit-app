from flask import Flask, request, render_template
from model.recommender import Recommender
import json

app = Flask('canimakeit')

states = ['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL',
          'GA',
          'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD',
          'ME',
          'MI', 'MN', 'MO', 'MP',
          'MS', 'MT', 'NA', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY',
          'OH',
          'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA',
          'VI',
          'VT', 'WA', 'WI', 'WV', 'WY']


recommender = Recommender()


@app.route('/')
def home():
    return render_template('index.html', states=states)


@app.route('/static/<path:path>')
def serve_static(path):
    return app.send_static_file(path)


@app.route('/api/user-info', methods=['POST'])
def post():
    print '\nReceived: ', request.data, '\n\n'
    data = request.get_json()
    salary = int(data['salary'])
    # print 'salary is', salary
    recommendation = recommender.recommend(user_salary=salary)
    return json.dumps(recommendation['statecluster'])
    # making_it_by_state = info_to_making_it(data)
    # return json.dumps(making_it_by_state)


# pass variables to html
@app.route('/states/<state>')
def state(state):
    # return render_template('index.html')
    return render_template('states.html', state=state, number=1)


if __name__ == '__main__':
    app.run(debug=True)
