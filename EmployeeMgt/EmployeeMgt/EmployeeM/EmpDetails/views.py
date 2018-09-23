from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from EmpDetails.forms import EmpDetailsForm #PostForm, CommentForm
from django.urls import reverse_lazy
from EmpDetails.models import EmpDetailsModel #Post, Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                   DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class contactus(TemplateView):
    template_name = 'contactus.html'


class EmpDetailsListView(ListView):
    model = EmpDetailsModel

    def get_queryset(self):
        pass#return Post.objects.filter()


class EmpDetailsDetailView(DetailView):
    model = EmpDetailsModel

class CreateEmpDetailsView(CreateView):
    #login_url = '/login/'
    template_name = 'AddEmployee.html'
    redirect_field_name = 'Registraions/Allemployee.html'
    form_class = EmpDetailsForm
    model = EmpDetailsModel


class EmpDetailsUpdateView(UpdateView):
    #login_url = '/login/'
    #edirect_field_name = 'Registraions/post_detail.html'
    template_name = 'updateemp.html'
    redirect_field_name = 'Registraions/updateemp.html'
    form_class = EmpDetailsForm
    model = EmpDetailsModel


class DraftListView(ListView):
    #login_url = '/login/'
    redirect_field_name = 'Registraions/Allemployee.html'
    template_name = 'Registraions/Allemployee.html'
    #form_class = EmpDetailsForm
    model = EmpDetailsModel
    print('DraftListView called')
    context_object_name ='EmpDetailsModel_list'
    def get_queryset(self):
        queryset = EmpDetailsModel.objects.all()
        return queryset
############################################################################
##########################################################################
