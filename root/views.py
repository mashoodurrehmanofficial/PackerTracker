from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.core.files import File
from .models import *
from django.views.decorators.csrf import csrf_exempt 
import os,shutil
import pandas as pd
from collections import Counter
from datetime import datetime
from .chart_updater import  GENERATE_CHARTS

# Create your views here.
@csrf_exempt
def index(request):
    rigs = RIGTABLE.objects.all()

    if request.method=='POST':
        barcode = request.POST['barcode']
        packed_count =  0
        container_and_harness = request.POST['container_and_harness']
        main_canopy_line_set = request.POST['main_canopy_line_set']
        main_canopy = request.POST['main_canopy']
        d_bag = request.POST['d_bag']
        pilot_chute_and_bridle = request.POST['pilot_chute_and_bridle']
        rig_exists = RIGTABLE.objects.filter(barcode=barcode).exists()
        
        if rig_exists:
            rig = RIGTABLE.objects.get(barcode=barcode)
            def generate_value(old,incoming):
                old = int(str(old).split('_red')[0])
                if int(incoming)>=rig.last_unit:
                    new_value =   str(incoming)+'_red'
                    return new_value
                else:

                    new_value =   str(incoming)
                    return new_value


 

            rig.packed_count           =  generate_value(rig.packed_count, packed_count)
            rig.container_and_harness  =  generate_value(rig.container_and_harness, container_and_harness)
            rig.main_canopy_line_set   =  generate_value(rig.main_canopy_line_set,  main_canopy_line_set)
            rig.main_canopy            =  generate_value(rig.main_canopy, main_canopy)
            rig.d_bag                  =  generate_value(rig.d_bag, d_bag)
            rig.pilot_chute_and_bridle =  generate_value(rig.pilot_chute_and_bridle, pilot_chute_and_bridle)
            rig.save()
            print("--> RIG Updated = ", barcode)
        
        else:
            rig = RIGTABLE()
            rig.barcode=barcode
            rig.packed_count=packed_count
            rig.container_and_harness=container_and_harness
            rig.main_canopy_line_set=main_canopy_line_set
            rig.main_canopy=main_canopy
            rig.d_bag=d_bag
            rig.pilot_chute_and_bridle=pilot_chute_and_bridle
            rig.save()
            print("--> New RIG Added = ", barcode)
 
        return redirect('/')

    else:
        rigs = RIGTABLE.objects.all().values().order_by('sort_key1','sort_key2')
 
        rigs = [[str(y).split('_red') for y in x.values()][1:] for x in rigs]

        date_file = os.path.join(os.getcwd(),'PROJECT','date.txt')
        with open(date_file,'r') as filereader:
            date = str(filereader.read()).strip()

        return render(request, 'root/index.html',{'rigs':rigs,'date':date})









@csrf_exempt
def delete(request,barcode):
    rig = RIGTABLE.objects.filter(barcode=barcode).exists()
    if rig:
        RIGTABLE.objects.get(barcode=barcode).delete() 
        print("--> RIG Deleted = ", barcode)
    return redirect("/")





 
 
 
@csrf_exempt
def update(request):
    folder_path = os.path.join(os.getcwd(),'uploaded_file')
    file = os.path.join(folder_path,os.listdir(folder_path)[0])
    df = pd.read_excel(file, engine = 'openpyxl',header=None).values.tolist()
    df = [x[0] for x in df]
    df = list(dict(Counter(df)).items())
    for barcode in df:
        rig_exists = RIGTABLE.objects.filter(barcode=barcode[0])
        if rig_exists:
            rig = RIGTABLE.objects.get(barcode=barcode[0])
            count = barcode[-1] 

            def generate_value(old_value):

                new_value = int(old_value.split('_red')[0]) + count
                if new_value>=rig.last_unit:
                    new_value = str(new_value)+'_red'
                    return new_value
                else:
                    new_value = str(new_value)
                    return new_value    
            rig.packed_count           = generate_value(rig.packed_count)
            rig.container_and_harness  = generate_value(rig.container_and_harness)
            rig.main_canopy_line_set   = generate_value(rig.main_canopy_line_set)
            rig.main_canopy            = generate_value(rig.main_canopy)
            rig.d_bag                  = generate_value(rig.d_bag)
            rig.pilot_chute_and_bridle = generate_value(rig.pilot_chute_and_bridle)
            rig.save()
        

            print("--> RIG Updated = ", barcode)

        else:
            rig = RIGTABLE()
            rig.barcode=barcode[0]
            rig.packed_count=barcode[-1]
            rig.container_and_harness=barcode[-1]
            rig.main_canopy_line_set=barcode[-1]
            rig.main_canopy=barcode[-1]
            rig.d_bag=barcode[-1]
            rig.pilot_chute_and_bridle=barcode[-1]
            rig.save()
            print("New Rig Added = ", barcode)


    backup_folder_path = os.path.join(os.getcwd(),'Backup')
    # date_file = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    date_file = os.path.join(os.getcwd(),'PROJECT','date.txt')
    with open(date_file,'w') as filewriter:
        filewriter.write(str(datetime.now().strftime("%Y-%m-%d    %H:%M:%S")))
        

    if os.path.exists(backup_folder_path):pass
    else:os.makedirs(backup_folder_path)
    data_set = [[str(y).split('_red')[0] for y in x.values()][1:-2] for x in RIGTABLE.objects.all().values()]
    
    for record in data_set:
        for index,val in enumerate(record):
            if record[index].isnumeric():
                record[index] = int(record[index])
    
    
    columns = [f.verbose_name for f in RIGTABLE._meta.get_fields()][1:-2]
    df = pd.DataFrame(data=data_set,columns=columns)
    filename = str(datetime.now().strftime("%d-%m-%Y %H-%M-%S"))+'.xlsx'
    df.to_excel(os.path.join(backup_folder_path,filename), index=False)
    print(df)
    print("------ Create Charts ----------")
    GENERATE_CHARTS(request.POST['date'])

    return JsonResponse({'res':True})


 
 
 

 
 



@csrf_exempt
def remove_specific_warning(request,barcode):
    rig_exists = RIGTABLE.objects.filter(barcode=barcode).exists()
    if rig_exists:  
        rig = RIGTABLE.objects.get(barcode=barcode)
        def generate_value(old):
            new_value = str(old).split('_red')[0]
            return new_value
        rig.packed_count           = generate_value(rig.packed_count)
        rig.container_and_harness  = generate_value(rig.container_and_harness)
        rig.main_canopy_line_set   = generate_value(rig.main_canopy_line_set)
        rig.main_canopy            = generate_value(rig.main_canopy)
        rig.d_bag                  = generate_value(rig.d_bag)
        rig.pilot_chute_and_bridle = generate_value(rig.pilot_chute_and_bridle)
        rig.last_unit = int(rig.last_unit)+50
        rig.save() 
        print("-->> New LAST UNIT = ", rig.last_unit)



        
    return redirect("/")



@csrf_exempt
def upload(request):
    uploaded_file = request.FILES['file']
    folder_path = os.path.join(os.getcwd(),'uploaded_file')
    shutil.rmtree(folder_path)

    if os.path.exists(folder_path):pass
    else:os.makedirs(folder_path)

    with open( os.path.join(os.getcwd(),'uploaded_file',uploaded_file.name) ,'wb')as file:
        file.write(uploaded_file.read())
    return JsonResponse({'res':True})
@csrf_exempt
def remove_warnings(request):
    rigs = RIGTABLE.objects.all()
    for rig in rigs:
        def generate_value(old):
            new_value = str(old).split('_red')[0]
            return new_value

        rig.packed_count           = generate_value(rig.packed_count)
        rig.container_and_harness  = generate_value(rig.container_and_harness)
        rig.main_canopy_line_set   = generate_value(rig.main_canopy_line_set)
        rig.main_canopy            = generate_value(rig.main_canopy)
        rig.d_bag                  = generate_value(rig.d_bag)
        rig.pilot_chute_and_bridle = generate_value(rig.pilot_chute_and_bridle)
        rig.last_unit = int(rig.last_unit)+50

        rig.save()

    return redirect('/')
@csrf_exempt
def generate_latest_report(request):
    latest_report_folder_path = os.path.join(os.getcwd(),'Latest Report')
    if os.path.exists(latest_report_folder_path):pass
    else:os.makedirs(latest_report_folder_path)
    data_set = [[str(y).split('_red')[0] for y in x.values()][1:-2] for x in RIGTABLE.objects.all().values()]
    
    for record in data_set:
        for index,val in enumerate(record):
            if record[index].isnumeric():
                record[index] = int(record[index])
 
    
    
    columns = [f.verbose_name for f in RIGTABLE._meta.get_fields()][1:-2]
    df = pd.DataFrame(data=data_set,columns=columns)
    filename = str(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+'.xlsx'
    df.to_excel(os.path.join(latest_report_folder_path,filename), index=False)
 

    return JsonResponse({'res':True})  





@csrf_exempt
def reset_records(request):
    rigs = RIGTABLE.objects.all()
    for rig in rigs:
        rig.packed_count           =  0
        rig.container_and_harness  =  0
        rig.main_canopy_line_set   =  0
        rig.main_canopy            =  0
        rig.d_bag                  =  0
        rig.pilot_chute_and_bridle =  0
        rig.save()

    return redirect('/')
 
@csrf_exempt
def delete_all(request):
    rigs = RIGTABLE.objects.all().delete()

    return redirect('/')
 

 
 
   
def charts(request):
    return render(request, 'root/charts.html' )
  
 

 
 
 