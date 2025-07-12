from django.shortcuts import render, redirect
import requests
import json

appType = 'Web Service'

def index(request):
    return render(request, 'index.html', {'appType': appType})

def createcar(request):
    return render(request, 'createcar.html', {'appType': appType})

def createcarsave(request):
    if request.method == 'POST':
        fName = request.POST['carName']
        fBrand = request.POST['carBrand']
        fModel = request.POST['carModel']
        fPrice = request.POST['carPrice']

        datacar = {
            "carname": fName,
            "carbrand": fBrand,
            "carmodel": fModel,
            "carprice": fPrice
        }

        alamatserver = "http://localhost:5012/api/server/"
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        requests.post(alamatserver, json=datacar, headers=headers)

        return redirect('readcar')

def readcar(request):
    alamatserver = "http://localhost:5012/api/server/"
    try:
        datas = requests.get(alamatserver, timeout=5)
        datas.raise_for_status()
        rows = datas.json()
        if not isinstance(rows, list):
            rows = []
    except (requests.RequestException, ValueError, json.JSONDecodeError):
        rows = []

    return render(request, 'readcar.html', {'rows': rows, 'appType': appType})

def updatecar(request):
    alamatserver = "http://localhost:5012/api/server/"
    try:
        datas = requests.get(alamatserver, timeout=5)
        datas.raise_for_status()
        rows = datas.json()
    except:
        rows = []

    if request.method == 'POST':
        car_id = request.POST['carId']
        editing = {
            'id': car_id,
            'carname': request.POST['carName'],
            'carbrand': request.POST['carBrand'],
            'carmodel': request.POST['carModel'],
            'carprice': request.POST['carPrice'],
        }
        return render(request, 'updatecar.html', {
            'rows': rows,
            'editing': editing,
            'appType': appType
        })

    return render(request, 'updatecar.html', {
        'rows': rows,
        'appType': appType
    })

def updatecarsave(request):
    if request.method == 'POST':
        car_id = request.POST['carId']
        datacar = {
            "carname": request.POST['carName'],
            "carbrand": request.POST['carBrand'],
            "carmodel": request.POST['carModel'],
            "carprice": request.POST['carPrice']
        }

        alamatserver = f"http://localhost:5012/api/server/{car_id}/"
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        try:
            requests.put(alamatserver, json=datacar, headers=headers)
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    return redirect('updatecar')

def deletecar(request):
    alamatserver = "http://localhost:5012/api/server/"
    try:
        datas = requests.get(alamatserver, timeout=5)
        datas.raise_for_status()
        rows = datas.json()
    except:
        rows = []

    return render(request, 'deletecar.html', {
        'rows': rows,
        'appType': appType
    })

def deletecarsave(request):
    if request.method == 'POST':
        car_id = request.POST['carId']
        alamatserver = f"http://localhost:5012/api/server/{car_id}/"
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        try:
            requests.delete(alamatserver, headers=headers)
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    return redirect('readcar')


def searchcar(request):
    search_query = request.GET.get('q', '')
    alamatserver = f"http://localhost:5012/api/server/?search={search_query}"
    try:
        datas = requests.get(alamatserver, timeout=5)
        datas.raise_for_status()
        rows = datas.json()
        if not isinstance(rows, list):
            rows = []
    except (requests.RequestException, ValueError, json.JSONDecodeError):
        rows = []

    return render(request, 'searchcar.html', {'rows': rows})