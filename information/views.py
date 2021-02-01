
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import AboutUs, Contact, ContactModel, Benefits
from django.views.generic.edit import FormView 
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def about_us(request):
    about = AboutUs.objects.all()
    benefits = Benefits.objects.all()

    return render(request, 'information/about.html', {
        'about': about,
        'benefits': benefits
    })



class ContactFormView(FormMixin, TemplateView ):
    template_name = 'information/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('info:contact')


    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['form'] = ContactForm()
        context['contact'] = Contact.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'Сообщение успешно отправлено.')
            return self.form_valid(form)
        else:
            messages.error(request, 'Сообщение не отправлено. Проверьте введенные данные')
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()        
        return super(ContactFormView, self).form_valid(form)


