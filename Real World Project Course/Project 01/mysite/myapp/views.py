from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from pandas.io import json

# Create your views here.

def hello(request):
    if request.method == 'POST':
        file = request.FILES['file']
        df = pd.read_csv(file)
        json_record = df.reset_index().to_json(orient='records')
        data = []
        data = json.loads(json_record)
        print(data)
    else:
        print("This is a post Request")
    return render( request, 'myapp/index.html')