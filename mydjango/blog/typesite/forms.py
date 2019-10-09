#!/usr/bin/python3
# -*- coding:utf-8 -*-
from django import forms
from .models import User

class UserFrom(forms.ModelForm):

    class Meta:
        model = User
        fields = {
            "user_full_name",
            "user_name",
            "user_password",
            "user_email",
            "user_sex",
            "user_age",
            "user_phone_number",
            "user_card",
            "createby",
            # 'img_url',
            'is_active',
            }