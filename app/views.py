import decimal
from django.urls import reverse_lazy

import pyrebase
from django import forms
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.utils import timezone
from datetime import timedelta



today = timezone.now().date()


from .models import Scale

config = {
    "apiKey": "AIzaSyDapKpMKn9ngK0aicwldlDY3fjML_tL3N0",
    "authDomain": "smart-scale-e9019.firebaseapp.com",
    "databaseURL": "https://smart-scale-e9019-default-rtdb.firebaseio.com",
    "projectId": "smart-scale-e9019",
    "storageBucket": "smart-scale-e9019.appspot.com",
    "messagingSenderId": "607200793665",
    "appId": "1:607200793665:web:74d9b6ab62e2c497a022c0",
    "measurementId": "G-VWTQT9XR68",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def scale(request):
    mass = database.child("Mass").get().val()
    print(mass, type(mass))
    s = None
    try:
        s = Scale.objects.get(pk=1)
    except Exception:
        s = Scale()
    s.mass = decimal.Decimal(round(mass, 10))
    s.save()
    
    upto_expiry = (s.expire_date.date() - today).days
    
    mass = mass/1000

    return render(request, "app/index.html", {"scale": s, "mass":mass, 'upto_expiry':upto_expiry})


class ScaleForm(forms.ModelForm):
    class Meta:
        model = Scale
        fields = ["name", "expire_date"]
        widgets = {
            "expire_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class EditScaleView(UpdateView):
    model = Scale
    form_class = ScaleForm
    template_name = "app/update_scale.html"

    success_url = reverse_lazy("scale")
