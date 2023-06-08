from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from image.models import MyImage
from rest_framework.response import Response
import json


@csrf_exempt
def create_image(request):
    data = {}
    file_obj = request.FILES.get('image')
    print(type(file_obj))
    if not file_obj:
        data['status'] = 'Failed'
        data['status_code'] = '400'
        data['message'] = 'failllllll'
        return HttpResponse(json.dumps(data), content_type='application/json')
    # save image to database
    image = MyImage.objects.create(image=file_obj)
    print(image)
    data['status'] = 'Success'
    data['status_code'] = '200'
    data['message'] = 'anh da duoc luu :)))'
    data['data'] = {'image_id': image.id}
    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def get_alla_image(request):
    data = []
    resp = {}

    # This will fetch the data from the database.
    prodata = MyImage.objects.all()
    # prodata = [1, 2, 3]
    for tbl_value in prodata.values():
        data.append(tbl_value)

    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp), content_type='application/json')
