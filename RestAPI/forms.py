from django import forms


class Coordinates(forms.Form):
    lat1 = forms.FloatField()
    long1 = forms.FloatField()
    lat2 = forms.FloatField()
    long2 = forms.FloatField()
