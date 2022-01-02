from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import re
from datetime import datetime

# Create your models here.
class RIGTABLE(models.Model):
    barcode = models.CharField(max_length=100000000000, blank=True,default='', verbose_name = 'Barcode')
    packed_count = models.CharField(max_length=100000000000, blank=True,default='', verbose_name = 'Packed Count')
    container_and_harness = models.CharField(max_length=100000000000, blank=True,default='', verbose_name = 'Container and Harness')
    main_canopy_line_set = models.CharField(max_length=100000000000, blank=True,default='', verbose_name = 'Main Canopy Line Set')
    main_canopy = models.CharField(max_length=100000000000, blank=True,default='', verbose_name = 'Main Canopy')
    d_bag = models.CharField(max_length=100000000000, blank=True,default='', verbose_name = 'D Bag')
    pilot_chute_and_bridle = models.CharField(max_length=100000000000, blank=True,default='', verbose_name = 'Pilot Chute/Drogue and Bridle’')
    last_unit = models.IntegerField(default=100,blank=True)
    sort_key1=models.CharField(max_length=100,default=0,blank=True)
    sort_key2=models.IntegerField(default=0,blank=True)
    
    hundred_mod_unit = models.IntegerField(default=100,blank=True)
    

    def __str__(self):
        return self.barcode
    
 

@receiver(pre_save, sender=RIGTABLE)
def my_callback(sender, instance, *args, **kwargs):
    barcode = instance.barcode
    key_1 = str(barcode)[0].lower()
    key_2 = re.findall(r'\d+', barcode)
    instance.sort_key1 = key_1
    instance.sort_key2 = key_2[0] if key_2 else 0
 
 


class HISTORY_TABLE(models.Model):
    barcode = models.CharField(max_length=100000000000, blank=True,default='')
    date = models.DateField(null=True, blank=True)
    total_jumps = models.CharField(max_length=100000000000, blank=True,default=0)



class TEMP_TABLE(models.Model):
    barcode = models.CharField(max_length=100000000000, blank=True,default='',)
    total_jumps = models.CharField(max_length=100000000000, blank=True,default=0 )