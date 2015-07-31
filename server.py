# To do: pass making it as query param


from flask import Flask, request, render_template
from model.recommender import Recommender
from mocks import get_state_info
from constants import states_dict, making_it_verbs_dict
import json

app = Flask('canimakeit')

recommender = Recommender()


def enrich_state_cluster(state_cluster):
    new_dict = {}

    for key in state_cluster:
        making_it = state_cluster[key]['fillKey']
        new_dict[key] = {'fillKey': making_it, 'making_it': making_it}
    print new_dict
    return new_dict


@app.route('/')
def home():
    return render_template('index.html', states=states_dict.keys())


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
    state_cluster = enrich_state_cluster(recommendation['statecluster'])
    print state_cluster
    return json.dumps(state_cluster)
    # making_it_by_state = info_to_making_it(data)
    # return json.dumps(making_it_by_state)


# pass variables to html
@app.route('/states/<state>')
def state(state):
    # so we have this in locals()
    state_info = get_state_info(state)

    making_it_id = int(request.args.get('making_it_id')) or 3
    making_it_verb = making_it_verbs_dict[making_it_id]

    state_desc = states_dict[state]

    return render_template('states.html',
                           state_info=state_info,
                           making_it_verb=making_it_verb,
                           state_desc=state_desc)

if __name__ == '__main__':
    app.run(debug=True)
