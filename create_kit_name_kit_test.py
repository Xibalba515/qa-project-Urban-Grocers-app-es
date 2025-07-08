import sender_stand_request
import data

def get_user_body(first_name):

    current_body = data.user_body.copy()
    current_body['firstName'] = first_name
    return current_body

def get_kit_body(name):
    current_kit = data.kit_body.copy()
    current_kit['name'] = name
    return current_kit


# Obtención del Token

def get_new_user_token():
    user_request = data.user_body
    user_response = sender_stand_request.post_new_user(user_request)
    assert user_response.status_code == 201
    return user_response.json()['authToken']


# Preparación positive assert

def positive_assert(name):
    token = get_new_user_token()
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == name

# Preparacion negative assert

def negative_assert_code_400(name):
    token = get_new_user_token()
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert kit_response.status_code == 400

# Preparación pruebas 3 y 8

def negative_assert_no_kit_name(kit_body):
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.json()['code'] == 400


# Prueba 1

def test_number_allowed_1():
    positive_assert('A')


# Prueba 2

def test_number_allowed_511():
    positive_assert(
        'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')


# Prueba 3
def test_number_not_allowed_0():

    kit_body = get_kit_body('')
    negative_assert_code_400(kit_body)

# Prueba 4
def test_number_allowed_512():
    negative_assert_code_400(
        'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')


# Prueba 5
def test_special_symbols_allowed():
    positive_assert('\"№%@\',')


# Prueba 6
def test_blank_space_allowed():
    positive_assert('A Aaa')


# Prueba 7
def test_numbers_allowed():
    positive_assert('123')


# Prueba 8
def test_parameter_not_passed_request():

    kit_body = data.kit_body.copy()
    kit_body.pop('name')

    negative_assert_no_kit_name(kit_body)

# Prueba 9
def test_different_parameter_type_number():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)
