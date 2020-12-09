# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView, View)
from .forms import GrievanceForm
from .models import Grievance, Plate
from django.utils.translation import gettext as _
from .utils import validate_plate, map_words, clean_p


class GrievanceView(FormView):
    template_name = 'home.html'
    form_class = GrievanceForm
    model = Grievance
    success_url = reverse_lazy('success')

    def setup(self, request, *args, **kwargs):
        # ToDo: add restriction to 5 times per day
        super().setup(request, *args, **kwargs)

    def form_valid(self, form):
        Grievance.objects.create(
            plate=form.cleaned_data['plate'],
            level=form.cleaned_data.get('level', 3),
            description=form.cleaned_data['description'])
        return redirect(self.success_url)


class SearchView(View):
    template_name = 'search.html'

    def get_context_data(self):
        search = self.request.POST.get('search')
        if not search or len(search) > 30:
            return {}
        plate = clean_p(search.lower())
        plate = map_words(plate)
        plate, country = validate_plate(plate)
        plate = Plate.objects.filter(name=plate, country=country).last()
        if not plate:
            return {}
        context = {'plate': plate}
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
