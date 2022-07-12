from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
import os
from django.conf import settings

from django.shortcuts import render, redirect
from .forms import ChecklistForm, DpaChecklistForm
from .models import Checklist, DpaChecklist


class HomePageView(TemplateView):
    template_name = 'home.html'


class ChecklistPageView(LoginRequiredMixin, ListView):
    model = Checklist
    context_object_name = 'checklists'
    template_name = 'checklist.html'
    login_url = 'account_login'


def dpa_view(request):
    with open(os.path.join(settings.STATIC_ROOT, 'dpa/TheDataProtectionAct__No24of2019.pdf'), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=TheDataProtectionAct__No24of2019.pdf'
        return response
    pdf.closed


def dpa_regulations_view(request):
    with open(os.path.join(settings.STATIC_ROOT, 'dpa/DataProtectionRegulations,2021.pdf'), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=DataProtectionRegulations.pdf'
        return response
    pdf.closed


class DpaPageView(TemplateView):
    template_name = 'dpa.html'


class FaqPageView(TemplateView):
    template_name = 'faq.html'


@login_required(login_url='account_login')
def ChecklistView(request):
    if request.method == 'POST':
        # form = DpaChecklistForm(request.POST)
        form = ChecklistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('checklist_submitted')
    else:
        form = ChecklistForm()
        # form = DpaChecklistForm()
        context = {'form': form}
    return render(request, 'checklist.html', context)


class ChecklistSubmitView(TemplateView):
    template_name = 'checklist_submit.html'




# Articles
class ArticleOneView(TemplateView):
    template_name = 'articles/art1.html'
class Article2View(TemplateView):
    template_name = 'articles/art2.html'
class Article3View(TemplateView):
    template_name = 'articles/art3.html'
class Article4View(TemplateView):
    template_name = 'articles/art4.html'
class Article5View(TemplateView):
    template_name = 'articles/art5.html'
class Article6View(TemplateView):
    template_name = 'articles/art6.html'
class Article7View(TemplateView):
    template_name = 'articles/art7.html'
class Article8View(TemplateView):
    template_name = 'articles/art8.html'
class Article9View(TemplateView):
    template_name = 'articles/art9.html'
class Article10View(TemplateView):
    template_name = 'articles/art10.html'
class Article11View(TemplateView):
    template_name = 'articles/art11.html'
class Article12View(TemplateView):
    template_name = 'articles/art12.html'
class Article13View(TemplateView):
    template_name = 'articles/art13.html'
class Article14View(TemplateView):
    template_name = 'articles/art14.html'
class Article15View(TemplateView):
    template_name = 'articles/art15.html'
class Article16View(TemplateView):
    template_name = 'articles/art16.html'
class Article17View(TemplateView):
    template_name = 'articles/art17.html'
class Article18View(TemplateView):
    template_name = 'articles/art18.html'
class Article19View(TemplateView):
    template_name = 'articles/art19.html'
class Article20View(TemplateView):
    template_name = 'articles/art20.html'
class Article21View(TemplateView):
    template_name = 'articles/art21.html'
class Article22View(TemplateView):
    template_name = 'articles/art22.html'
class Article23View(TemplateView):
    template_name = 'articles/art23.html'
class Article24View(TemplateView):
    template_name = 'articles/art24.html'
class Article25View(TemplateView):
    template_name = 'articles/art25.html'
class Article26View(TemplateView):
    template_name = 'articles/art26.html'
class Article27View(TemplateView):
    template_name = 'articles/art27.html'
class Article28View(TemplateView):
    template_name = 'articles/art28.html'
class Article29View(TemplateView):
    template_name = 'articles/art29.html'
class Article30View(TemplateView):
    template_name = 'articles/art30.html'
class Article31View(TemplateView):
    template_name = 'articles/art31.html'
class Article32View(TemplateView):
    template_name = 'articles/art32.html'
class Article33View(TemplateView):
    template_name = 'articles/art33.html'
class Article34View(TemplateView):
    template_name = 'articles/art34.html'
class Article35View(TemplateView):
    template_name = 'articles/art35.html'
class Article36View(TemplateView):
    template_name = 'articles/art36.html'
class Article37View(TemplateView):
    template_name = 'articles/art37.html'
class Article38View(TemplateView):
    template_name = 'articles/art38.html'
class Article39View(TemplateView):
    template_name = 'articles/art39.html'
class Article40View(TemplateView):
    template_name = 'articles/art40.html'
class Article41View(TemplateView):
    template_name = 'articles/art41.html'
class Article42View(TemplateView):
    template_name = 'articles/art42.html'
class Article43View(TemplateView):
    template_name = 'articles/art43.html'
class Article44View(TemplateView):
    template_name = 'articles/art44.html'
class Article45View(TemplateView):
    template_name = 'articles/art45.html'
class Article46View(TemplateView):
    template_name = 'articles/art46.html'
class Article47View(TemplateView):
    template_name = 'articles/art47.html'
class Article48View(TemplateView):
    template_name = 'articles/art48.html'
class Article49View(TemplateView):
    template_name = 'articles/art49.html'
class Article50View(TemplateView):
    template_name = 'articles/art50.html'
class Article51View(TemplateView):
    template_name = 'articles/art51.html'
class Article52View(TemplateView):
    template_name = 'articles/art52.html'
class Article53View(TemplateView):
    template_name = 'articles/art53.html'
class Article54View(TemplateView):
    template_name = 'articles/art54.html'
class Article55View(TemplateView):
    template_name = 'articles/art55.html'
class Article56View(TemplateView):
    template_name = 'articles/art56.html'
class Article57View(TemplateView):
    template_name = 'articles/art57.html'
class Article58View(TemplateView):
    template_name = 'articles/art58.html'
class Article59View(TemplateView):
    template_name = 'articles/art59.html'
class Article60View(TemplateView):
    template_name = 'articles/art60.html'
class Article61View(TemplateView):
    template_name = 'articles/art61.html'
class Article62View(TemplateView):
    template_name = 'articles/art62.html'
class Article63View(TemplateView):
    template_name = 'articles/art63.html'
class Article64View(TemplateView):
    template_name = 'articles/art64.html'
class Article65View(TemplateView):
    template_name = 'articles/art65.html'
class Article66View(TemplateView):
    template_name = 'articles/art66.html'
class Article67View(TemplateView):
    template_name = 'articles/art67.html'
class Article68View(TemplateView):
    template_name = 'articles/art68.html'
class Article69View(TemplateView):
    template_name = 'articles/art69.html'
class Article70View(TemplateView):
    template_name = 'articles/art70.html'
class Article71View(TemplateView):
    template_name = 'articles/art71.html'
class Article72View(TemplateView):
    template_name = 'articles/art72.html'
class Article73View(TemplateView):
    template_name = 'articles/art73.html'
class Article74View(TemplateView):
    template_name = 'articles/art74.html'
class Article75View(TemplateView):
    template_name = 'articles/art75.html'
