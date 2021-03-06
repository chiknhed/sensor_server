# -*- coding: utf-8 -*-

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label=u"사용자 : ")
    password = forms.CharField(label=u"암호 : ", widget=forms.PasswordInput())


class SettingForm(forms.Form):
    secure_key = forms.CharField(max_length=50, label=u"보안키 : ")
    mac_address = forms.CharField(max_length=20, label=u"MAC주소 : ")


class SensorSettingForm(forms.Form):
    secure_key = forms.CharField(max_length=50, label=u"보안키 : ")
    mac_address = forms.CharField(max_length=20, label=u"MAC주소 : ")
    type = forms.IntegerField(label=u"형식 : ")


class InputForm(forms.Form):
    secure_key = forms.CharField(max_length=50, label=u"보안키 : ")
    mac_address = forms.CharField(max_length=20, label=u"MAC주소 : ")
    type = forms.IntegerField(label=u"형식 : ")
    value = forms.CharField(max_length=100, label=u"측정값*10 : ")
    rssi = forms.CharField(max_length=10, label=u'RSSI : ')
    first = forms.IntegerField(label=u"reset_first")