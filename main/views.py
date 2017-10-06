# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.
@login_required
def index(request):
    current_user = request.user
    #user=UserEmployee.objects.all()
    # return HttpResponse(user)
    return render(request, 'index.html')