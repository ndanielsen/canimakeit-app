from random import randint


def gen_dummy_data():
    states = [
        'AZ',
        'CO',
        'DE',
        'FL',
        'GA',
        'HI',
        'ID',
        'IL',
        'IN',
        'IA',
        'KS',
        'KY',
        'LA',
        'MD',
        'ME',
        'MA',
        'MN',
        'MI',
        'MS',
        'MO',
        'MT',
        'NC',
        'NE',
        'NV',
        'NH',
        'NJ',
        'NY',
        'ND',
        'NM',
        'OH',
        'OK',
        'OR',
        'PA',
        'RI',
        'SC',
        'SD',
        'TN',
        'TX',
        'UT',
        'WI',
        'VA',
        'VT',
        'WA',
        'WV',
        'WY',
        'CA',
        'CT',
        'AK',
        'AR',
        'AL']

    data = {}
    for state in states:
        data[state] = {"fillKey": randint(1, 5)}

    return data


def info_to_making_it(user_info):
    return gen_dummy_data()
