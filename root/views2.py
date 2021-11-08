from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.core.files import File
from .models import *
from django.views.decorators.csrf import csrf_exempt 
import os,shutil,re
import pandas as pd
from collections import Counter
from datetime import datetime
from dateutil import parser
from itertools import groupby
from operator import itemgetter
from natsort import natsorted



# Create your views here. 
 
 
   
def get_new_data(request):
    start_date = parser.parse(request.GET['start_date']).date()
    end_date = parser.parse(request.GET['end_date']).date()
    
    avaliable_rigs = list(HISTORY_TABLE.objects.filter(date__gte=start_date,date__lte=end_date).order_by("barcode").values('barcode','total_jumps'))
    
    container = {}
    if avaliable_rigs:
        for rig in avaliable_rigs:
            if rig['barcode'] in list(container.keys()):  container[rig['barcode']] =  int(container[rig['barcode']] ) +  int(rig['total_jumps'] )  # add + 
            else:   container[rig['barcode']] = int(rig['total_jumps'] )

        for x in container:
            container[x] = abs(container[x])
        
        
        labels = natsorted(list(container.keys()))
        data_set = [container[x] for x in labels] 
        return JsonResponse({"results":{
            "labels":  labels,
            "data_set":  data_set
        }})
        
        
    else:
        return JsonResponse({"results":{
            "labels":  [],
            "data_set":  []
        }})
  
 

 
 
 