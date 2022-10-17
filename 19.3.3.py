import requests
import json

# поиск питомца по статусу
def find_byStatus():
    params_find = {'status': 'available'}
    headers_find = {'accept':'application/json'}

    res_find = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus', params=params_find,
                       headers=headers_find)
    print(res_find.status_code)
    print(res_find.text)


# добавление питомца
def add_pet():
    headers_add = {'accept': 'application/json',
               'Content-Type': 'application/json'}

    data_add = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    res_add = requests.post('https://petstore.swagger.io/v2/pet', headers=headers_add,
                            data=json.dumps(data_add))
    print(res_add.status_code)
    print(res_add.text)
    print(res_add.json())
    print(type(res_add.json()))


# обновление существующего питомца
def update_pet():
    headers_update = {'accept': 'application/json',
               'Content-Type': 'application/json'}

    data_update = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    res_update = requests.put('https://petstore.swagger.io/v2/pet', headers=headers_update,
                              data=data_update)
    print(res_update.status_code)
    print(res_update.text)
    print(res_update.json())
    print(type(res_update.json()))


# поиск питомца по id
def find_pet(petid):
    headers_find = {'accept': 'application/json'}
    petid = 3
    res_find = requests.get(f'https://petstore.swagger.io/v2/pet/{petid}', headers=headers_find)
    print(res_find.status_code)
    print(res_find.text)
    print(res_find.json())


# обновление информации по питомцу с помощью формы
def update_formdata(petid):
    headers_formdata = {'accept': 'application/json',
               'Content-Type': 'x-www-form-urlencoded'}

    data_formdata = {'name': 'test', 'status': 'available'}
    petid = 3

    res_formdata = requests.post(f'https://petstore.swagger.io/v2/pet/{petid}', headers=headers_formdata,
                                 data=data_formdata)
    print(res_formdata.status_code)

# удаление питомца
def delete_pet(petid):
    headers_delete = {'accept': 'application/json'}
    res_delete = requests.delete(f'https://petstore.swagger.io/v2/pet/pet/{petid}', headers=headers_delete)
    print(res_delete.status_code)
