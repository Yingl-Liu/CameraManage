from django.db import models
class CameraInfo(models.Model):
    id=models.IntegerField(blank=True, default='',primary_key=True)
    ip=models.CharField(max_length=30, blank=False, default='',unique=True)
    isOnLine=models.IntegerField(blank=True,default=1)
    coordinate=models.CharField(max_length=20,blank=True,default='')
    # x=models.DecimalField(max_digits=10,decimal_places=3, blank=True, default='')
    # y=models.DecimalField(max_digits=10,decimal_places=3, blank=True, default='')
    # xa=models.DecimalField(max_digits=10,decimal_places=3, blank=True, default='')
    # ya=models.DecimalField(max_digits=10,decimal_places=3, blank=True, default='')
    # xb=models.DecimalField(max_digits=10,decimal_places=3, blank=True, default='')
    # yb=models.DecimalField(max_digits=10,decimal_places=3, blank=True, default='')
    # xc=models.DecimalField(max_digits=10,decimal_places=3, blank=True, default='')
    # yc=models.DecimalField(max_digits=10,decimal_places=3, blank=True, default='')
    # xd=models.DecimalField(max_digits=10,decimal_places=3, blank=True, default='')
    # yd=models.DecimalField(max_digits=10,decimal_places=3, blank=True, default='')
    # cuttingXList=models.CharField(max_length=40, blank=True,default='')
    # cuttingYList=models.CharField(max_length=40, blank=True,default='')
    # transformMat=models.CharField(max_length=100, blank=True,default='')
    # toploMat=models.CharField(max_length=40, blank=True, default='')
# class Image(models.Model):
#     id=models.IntegerField(blank=True, default='',primary_key=True)
#     ip=models.CharField(max_length=30, blank=True, default='',unique=True)
#     image=models.ImageField(upload_to='photo')
class RecombinationNode(models.Model):
    id=models.IntegerField(blank=True, default='',primary_key=True)
    ip=models.CharField(max_length=30, blank=True, default='',unique=False)
    # toploMat=models.CharField(max_length=100, blank=True, default='')
    # position=models.CharField(max_length=80, blank=True, default='')
    isTimedRecording = models.IntegerField(blank=True,default=0)
    startTime = models.CharField(max_length=20,blank=True,default='')
    duration = models.IntegerField(blank=True,default=0)
# Create your models here.
