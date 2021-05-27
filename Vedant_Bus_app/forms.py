from datetime import date

from django import forms
from django.forms import ModelForm
from .models import add_bus
from .models import createpass
from .models import Userreg


class UserForm(forms.ModelForm):
    class Meta:
        model = Userreg
        fields = '__all__'

class AddBusForm(ModelForm):
    class Meta:
        model = add_bus
        fields = ['busno', 'location', 'to', 'amount', 'stop1', 'stop2', 'stop3', 'stop4']

        widgets = {
            'busno': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Bus number', 'required': True}),
            'location': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Source ...', 'required': True}),
            'to': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Destination ...', 'required': True}),
            'amount': forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Amount...', 'required': True}),
            'stop1': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your Stops', 'required': True}),
            'stop2': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your Stops', 'required': True}),
            'stop3': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your Stops', 'required': True}),
            'stop4': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your Stops', 'required': True})
        }

class Createpass(forms.ModelForm):
    class Meta:
        model = createpass

        fields = '__all__'

#        fields = ['user_id', 'Busno', 'full_name', 'From', 'To', 'Date1', 'Date2', 'amount', 'profile_pic', 'cc_number', 'cvv', 'expiry', 'month']

#        GEEKS_CHOICES = (
#            ("01", "January"),
#            ("02", "February"),
#            ("03", "March"),
#            ("04", "April"),
#            ("05", "May"),
#           ("06", "June"),
#            ("07", "July"),
#            ("08", "August"),
#           ("09", "September"),
#            ("10", "October"),
#            ("11", "November"),
#            ("12", "December")
#        )

#        widgets = {
#            'user_id': forms.TextInput(attrs={'class': 'input', 'readonly': True, 'value': }),
#            'Busno': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bus no ...', 'readonly': True }),
#            'full_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Source...', 'required': True}),
#            'From': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Destination...', 'readonly': True}),
#            'To': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Destination...', 'readonly': True}),
#            'Date1': forms.DateInput(attrs={'class': 'input', 'placeholder': 'Starting date...', 'required': True}),
#            'Date2': forms.DateInput(attrs={'class': 'input', 'placeholder': 'Final date...', 'required': True}),
#            'amount': forms.NumberInput(attrs={'class': 'input', 'readonly': True}),
#            'profile_pic': forms.ImageField(),
#            'cc_number': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Destination...', 'required': True}),
#            'cvv': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Destination...', 'required': True}),
#            'expiry': forms.ChoiceField(choices=GEEKS_CHOICES),
#            'month': forms.ChoiceField(),


#        }

class DateInput(forms.DateInput):
    input_type = 'date'

class renewpassform(forms.ModelForm):
    class Meta:
        model = createpass
        fields = '__all__'

        GEEKS_CHOICES = (
                            ("01", "January"),
                            ("02", "February"),
                            ("03", "March"),
                            ("04", "April"),
                            ("05", "May"),
                            ("06", "June"),
                            ("07", "July"),
                            ("08", "August"),
                            ("09", "September"),
                            ("10", "October"),
                            ("11", "November"),
                            ("12", "December")
                           )

        GEEKS_CHOICES2 = (
            ("16", "2016"),
            ("17", "2017"),
            ("18", "2018"),
            ("19", "2019"),
            ("20", "2020"),
            ("21", "2021")
        )

        widgets = {
            'user_id': forms.TextInput(attrs={'class': 'input', 'readonly': True}),
            'Busno': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bus no ...', 'readonly': True}),
            'full_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Source...', 'required': True}),
            'From': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Destination...', 'readonly': True}),
            'To': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Destination...', 'readonly': True}),
            #'Date1': forms.DateInput(attrs={'class': 'input', 'placeholder': 'Starting date...', 'required': True, 'id': 'txtDate'}),
            #'Date2': forms.DateInput(attrs={'class': 'input', 'placeholder': 'Final date...', 'id': 'follow_Date', 'required': True}),
            'Date1': DateInput(attrs={'class': 'input', 'placeholder': 'Starting date...', 'required': True, 'id': 'txtDate'}),
            'Date2': DateInput(attrs={'class': 'input', 'placeholder': 'end date...', 'readonly': True, 'id': 'follow_Date'}),
            'amount': forms.NumberInput(attrs={'class': 'input', 'readonly': True}),
            'cc_number': forms.NumberInput(attrs={'class': 'input', 'required': True, }),
            'expiry': forms.Select(choices=GEEKS_CHOICES),
            'month' : forms.Select(choices=GEEKS_CHOICES2)
        }




3
