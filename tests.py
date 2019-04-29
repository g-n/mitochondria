import requests
from requests.auth import HTTPBasicAuth

hostname = "http://powerhouseofthecell.herokuapp.com"
auth = HTTPBasicAuth('teacher', 'teacher')


def api_req(endpoint:str, params:dict={}, data=None, hostname=hostname, auth=auth):
    endpoint = endpoint.rstrip('/').lstrip('/')
    url = hostname + '/' + endpoint + '/'

    if data != None:
        action = 'POST'
    else:
        action = 'GET'

    resp = requests.request(action, url, params=params, data=data, auth=auth)
    print("endpoint:", endpoint)
    print("params:", params)
    print("data:", data)
    print("response status:", resp.status_code)
    try:
        print("response: ", resp.json())
    except:
        pass

    return resp




endpoints = [
    '/students',
    '/classes',
    '/games',
    '/problemsets',
]


def get_data(endpoint):
    return api_req(endpoint).json()

def post_student(first_name, last_name, classroom):
    return api_req('/students', data={'first_name':first_name, 'last_name':last_name, 'classroom':classroom}).json()

def get_students():
    return get_data('/students')

def get_classes():
    return get_data('/classes')

def get_games():
    return get_data('/games')

def get_problemsets():
    return get_data('/problemsets')




def test_get_students():
    assert type(get_students()) is list

def test_get_classes():
    assert type(get_classes()) is list

def test_get_games():
    assert type(get_games()) is list

def test_get_problemsets():
    assert type(get_problemsets()) is list

def test_post_student():
    student = {
        'first_name':'jim',
        'last_name':'bob',
        'classroom':'first grade'
    }

    posted = post_student(**student)
    assert student == posted




# def test_post_student()    





