# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from shoe.models import shoe
import requests


def data_insert(name, price, product_type):
    shoe_data = shoe(name=name, price=price, product_type=product_type)
    shoe_data.save()
    return 1

def del_shoe(id):
    shoe_data = shoe.objects.filter(id=id)
    if shoe_data:
        shoe_data.delete()
        return True
    return False

def findID(id_product, product_type):
    shoe_data = shoe.objects.filter(
        id=id_product, product_type=product_type)
    for value in shoe_data.values():
        return value

@csrf_exempt
def create_shoe(request):
    data = json.loads(request.body)

    name = data.get("name")
    price = data.get("price")
    product_type = data.get("type")
    resp = {}
    if name and price and product_type == 'shoe':
        respontdata = data_insert(name, price, product_type)
        if respontdata:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = ''
            resp['data'] = data
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Fail!!!'
            resp['data'] = {}

    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Fail!!!'
        resp['data'] = {}

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def get_shoe(request):
    data = []
    resp ={}
    shoe_data = shoe.objects.all()
    for tbl_value in shoe_data.values():
        data.append(tbl_value)

    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = ''
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def delete_shoe(request):
    data = json.loads(request.body)
    id = data.get("id")
    resp = {}
    res = del_shoe(id)
    if res:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'delete shoe succefuly!!!'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Failed !!!'
        resp['data'] = {}

    return HttpResponse(json.dumps(resp), content_type='application/json')


@csrf_exempt
def add_to_cart(request):
    data = json.loads(request.body)
    id_product = data.get("id_product")
    product_type = data.get("product_type")

    shoe_data = findID(id_product, product_type)
    
    if shoe_data:
        cart_data = {}
        url = 'http://127.0.0.1:6000/add'
        cart_data['id_product'] = id_product
        cart_data['product_type'] = product_type
        data = json.dumps(cart_data)
        print(data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        api_resp = json.loads(response.content.decode('utf-8'))

        return HttpResponse(json.dumps(api_resp), content_type='application/json')
    else:
        resp = {}
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'san pham khong ton tai!!!'
        resp['data'] = {}
        return HttpResponse(json.dumps(resp), content_type='application/json')
