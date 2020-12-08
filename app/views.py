# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from .forms import GrievanceForm
from .models import Grievance, Plate
from django.utils.translation import gettext as _


class GrievanceView(FormView):
    template_name = 'home.html'
    form_class = GrievanceForm
    model = Grievance
    success_url = reverse_lazy('home')

    def setup(self, request, *args, **kwargs):
        # ToDo: add restriction to 5 times per day
        super().setup(request, *args, **kwargs)

    def form_valid(self, form):
        Grievance.objects.create(
            plate=form.cleaned_data['plate'],
            level=form.cleaned_data.get('level', 3),
            description=form.cleaned_data['description'])
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Your grievance created'))
        return redirect(self.success_url)
