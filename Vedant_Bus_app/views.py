from django.contrib import messages
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.views.generic import DetailView
from PIL import Image, ImageDraw
from io import BytesIO

import random
import http.client

import pyqrcode
import png
from easy_pdf.views import PDFTemplateResponseMixin

from .models import add_bus
from .forms import AddBusForm, renewpassform

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, request
from .forms import UserForm, Createpass
from .models import Userreg, createpass
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


# ------------------------------------user--------------------------------------------------
def index(request):
    return render(request, 'index.html', {'title':'Index Page'})

def regform_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    return render(request, 'user/register.html', {'form':form, 'title':'Register'})

def userlogin(request):
    if request.method == "POST":
            try:
                userdetail = Userreg.objects.get(uname=request.POST['uname'], pwd=request.POST['pwd'])
                request.session['user_id'] = userdetail.user_id
                return redirect("/busdetails")
            except ObjectDoesNotExist as e:
                messages.success(request, 'Username / Password Invalid...')
    return render(request, 'user/login.html', {'title': 'Login Page'})


def createbuspass(request, id):
    displaybusno = add_bus.objects.get(id=id)
    form = Createpass()
    if request.method == 'POST':
        form = Createpass(request.POST)
        user_id = request.POST['user_id']
        Busno = request.POST['bus_num']
        full_name = request.POST['full_name']
        From = request.POST['loc1']
        To = request.POST['loc2']
        Date1 = request.POST['initialdate']
        Date2 = request.POST['finaldate']
        amount = request.POST['amount']
        profile_pic = request.FILES['uploadpic']
        cc_number = request.POST['cc_number']
        cvv = request.POST['cvv']
        expiry = request.POST['expiry']
        month = request.POST['month']

        '''s = "\n" + "NAME=" + full_name + "\n" + "BUS NO= " + Busno + "\n" + "SOURCE= " + From + "\n" + "DESTINATION= " + To + "\n" + "VALID FROM= " + Date1 + " " + "TILL= " + Date2
        url = pyqrcode.create(s)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(url)
        fname = f'qr_code-{full_name}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        qr_codes = fname'''


        ins = createpass(Busno=Busno, full_name=full_name, From=From, To=To, Date1=Date1, Date2=Date2, amount=amount,
                         profile_pic=profile_pic, user_id=user_id, cc_number=cc_number, cvv=cvv, expiry=expiry, month=month)
        ins.save()

        return redirect('/busdetails')
    return render(request, 'user/createpass.html', {'title': 'Create Pass', 'add_bus': displaybusno, 'form':form})


'''def createbuspass(request, id):
    displaybusno = add_bus.objects.get(id=id)
    form = Createpass()

    if request.method == 'POST':
        form = Createpass(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/busdetails')

    context = {'form': form, 'add_bus': displaybusno}
    return render(request, 'user/createpass.html', context)'''


'''def renewpass(request, id):
    renew = createpass.objects.get(id=id)
    form = renewpassform()
    if request.method == "POST":
        form = renewpassform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/created_pass")
    context = {'form': form, 'renewpass': renew}
    return render(request, 'user/renewpass.html', context)'''

def renewpass(request, id):
    renew = createpass.objects.get(id=id)
    form = renewpassform(instance=renew)
    context = {'renewpass': renew, 'form': form}
    return render(request, 'user/renewpass.html', context)

def updatepass(request, id):
    updatepass = createpass.objects.get(id=id)
    form = renewpassform(request.POST, instance=updatepass)
    if form.is_valid():
        form.save()
        messages.success(request, "Pass renewed successfully...!")
        return redirect("/created_pass")
    context = {'renewpass': updatepass}
    return render(request, 'user/renewpass.html', context)


def Bus_details(request):
    all_buses = add_bus.objects.all()
    pass_created = createpass.objects.all()
    return render(request, 'user/bus_details.html', {'EditBus': all_buses, 'pass': pass_created})

def created_pass(request):
    pass_created = createpass.objects.all()
    return render(request, 'user/created_pass.html', {'pass': pass_created})


def logout_request_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/login")

# ---------------------------------------------- PDF -------------------------------------------------------------------------------------------
def logout_request_admin(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


class PdfDetail(PDFTemplateResponseMixin, DetailView):
    template_name = 'user/pdf_details.html'
    context_object_name = 'obj'
    model = createpass

#def PdfDetail(request):
#    obj = createpass.objects.all()
#    return render(request, '')

# ----------------------------------------------admin---------------------------------------------------------
def admin_login(request):
    if request.method == 'POST':
        if request.POST['username'] == 'admin@12' and request.POST['password'] == 'admin@12':
            return redirect('/addbus')
    return render(request, 'admin/adminlogin.html')

def addbus(request):

    form = AddBusForm()
    if request.method == "POST":
        #print('Values:', request.POST)
        form = AddBusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/editbus')

    context = {'form': form}

    return render(request, 'admin/add new bus.html', context)

def edit_bus(request):
    all_buses = add_bus.objects.all()
    return render(request, 'admin/edit_bus.html', {'EditBus': all_buses})

def user_details(request):
    userdetails = createpass.objects.all()
    return render(request, 'admin/adminuserdetails.html', {'userDetails': userdetails})

def delete_bus(request, id):
    delete_bus = add_bus.objects.get(id=id)

    if request.method == 'POST':
        delete_bus.delete()
        return redirect('/editbus')

    context = {'item': delete_bus}
    return render(request, 'admin/delete.html', context)

def edit(request, id):
    edit_bus = add_bus.objects.get(id=id)
    form = AddBusForm(instance=edit_bus)

    if request.method == "POST":
        form = AddBusForm(request.POST, instance=edit_bus)
        if form.is_valid():
            form.save()
            return redirect('/editbus')

    context = {'form': form}
    return render(request, 'admin/edit.html', context)








