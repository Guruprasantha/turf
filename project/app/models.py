from django.db import models

class Turf(models.Model):
          turfname=models.CharField(max_length=80)
          turfarea=models.CharField(max_length=80)
          turfpic=models.ImageField(upload_to='images/')
          turfrate=models.IntegerField()
          def __str__(self) :
                  return self.turfname
          
        
class booking(models.Model):
        register_name=models.CharField(max_length=100)
        register_id=models.CharField(max_length=100)
        register_mobile=models.CharField(max_length=20)
        register_address=models.CharField(max_length=300)
        register_mobile2=models.CharField(max_length=20)
        turfname=models.CharField(max_length=80)
        date=models.CharField(max_length=30)
        timings=models.CharField(max_length=30)
        status=models.CharField(max_length=50)
        
        def __str__(self):
                return self.register_name