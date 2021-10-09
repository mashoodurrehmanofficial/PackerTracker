import os,sys,django,uuid,time,datetime
sys.path.append( os.path.join(os.path.dirname(__file__), 'PROJECT'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PROJECT.settings")
django.setup()
from root.models import *
from  datetime import  datetime
from dateutil import parser

all_rig_table_records = RIGTABLE.objects.all().values('barcode','container_and_harness')
if all_rig_table_records:
    rig_keys = [x['barcode'] for x in list(all_rig_table_records) if all_rig_table_records]

    # if all_rig_table_records:
    #     for record in all_rig_table_records:
    #         history_record = HISTORY_TABLE.objects.filter(barcode=record['barcode'])
    #         if not history_record.exists(): 
    #             HISTORY_TABLE(barcode=record['barcode'],total_jumps=record['container_and_harness']).save()
                
    excluded = HISTORY_TABLE.objects.all().exclude(barcode__in=rig_keys)
    excluded.delete()
        
        

    all_temp_records = TEMP_TABLE.objects.all().values()
    if all_rig_table_records:
        for record in all_rig_table_records:
            history_record = TEMP_TABLE.objects.filter(barcode=record['barcode'])
            if not history_record.exists(): 
                TEMP_TABLE(barcode=record['barcode'],total_jumps=record['container_and_harness']).save()
                
        excluded = TEMP_TABLE.objects.all().exclude(barcode__in=rig_keys)
        excluded.delete()
        
        
    all_temp_records = TEMP_TABLE.objects.all().values()


    for rig_record in all_rig_table_records:
        rig_barcode = rig_record['barcode']
        rig_total_jumps = rig_record['container_and_harness']
        
        temp_total_jumps = [x for x in all_temp_records if x['barcode'] == rig_barcode][0]['total_jumps']
        
        rig_total_jumps = rig_total_jumps.split("_")[0]
        difference = int(float(str(rig_total_jumps))) - int(str(temp_total_jumps))
        print(difference)
        date_object = datetime.now().date()
        # date_object = parser.parse("2021-10-01")
        
        
        
        HISTORY_TABLE(barcode=rig_barcode,total_jumps=difference,date=date_object).save() 
        
        TEMP_TABLE.objects.filter(barcode=rig_barcode).update(total_jumps=rig_total_jumps)
        
        # print(x)
        
        
        
        



