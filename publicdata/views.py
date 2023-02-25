from django.shortcuts import render
from django.http import HttpResponse
from .api import status_api, validate_api

# Create your views here.


# def test(request):
#     status_res = status_api()
#     validate_res = validate_api()
#     ctx = {'status_res': status_res, 'validate_res': validate_res}
#     return render(request, 'test.html', ctx)


def status_test(request):
    status_res = status_api()

    print(status_res['data'][0])
    print(status_res['data'][0]['tax_type'])

    if status_res['data'][0]['b_stt']:
        return HttpResponse('조회되었습니다.')

    return HttpResponse('조회되지 않습니다.')


def validate_test(request):
    validate_res = validate_api()

    if validate_res['data'][0]['valid'] == '02':
        return HttpResponse('확인할 수 없습니다.')

    print(validate_res['data'][0])
    return HttpResponse('확인 완료')
