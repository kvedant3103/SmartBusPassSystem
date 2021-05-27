import django
from django.db import models
import qrcode
from io import BytesIO

from django.core.files import File
from PIL import Image, ImageDraw
from django.core.files.uploadedfile import InMemoryUploadedFile
from datetime import datetime, timedelta

from django import utils
from django.utils import timezone

# Create your models here.
from reportlab.graphics.barcode import qr


class Userreg(models.Model):
    user_id = models.CharField(max_length=100)
    uname = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    mobile = models.IntegerField()
    uemail = models.CharField(max_length=100)

# Create your models here.
class add_bus(models.Model):
    busno = models.CharField(max_length=30, null=True)
    location = models.CharField(max_length=30, null=True)
    to = models.CharField(max_length=30, null=True)
    amount = models.IntegerField(default=0)
    stop1 = models.CharField(max_length=30, null=True)
    stop2 = models.CharField(max_length=30, null=True)
    stop3 = models.CharField(max_length=30, null=True)
    stop4 = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.busno

class createpass(models.Model):
    id = models.AutoField(primary_key = True)
    user_id = models.CharField(max_length=100, null=True)
    Busno = models.CharField(max_length=30, null=True)
    full_name = models.CharField(max_length=30, null=True)
    From = models.CharField(max_length=30, null=True)
    To = models.CharField(max_length=30, null=True)
    Date1 = models.CharField(max_length=50, null=True, default=datetime.today())
    Date2 = models.CharField(max_length=50, null=True)
    amount = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to="profiles", default="")
    cc_number = models.IntegerField(null=True)
    cvv = models.IntegerField(default=123)
    expiry = models.IntegerField(null=True)
    month = models.IntegerField(default=2020)
    qr_codes = models.ImageField(upload_to="qr_codes", blank=True)


    def __str__(self,*args,**kwargs):
        return str(self.full_name)


    def save(self, *args, **kwargs):
        #s = "\n" + "NAME=" + self.full_name + "\n" + "BUS NO= " + Busno + "\n" + "SOURCE= " + From + "\n" + "DESTINATION= " + To + "\n" + "VALID FROM= " + Date1 + " " + "TILL= " + Date2
        #a = self.full_name + "\n" + self.Busno + "\n" + self.From
        qrcode_img = qrcode.make(str(self.Busno) + "\n" + str(self.Date1) + "\n" + str(self.Date2))
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.full_name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_codes.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)








