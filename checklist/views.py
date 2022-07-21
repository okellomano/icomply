import os
from datetime import datetime
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Checklist, UserChecklist, Category


class HomePageView(TemplateView):
    template_name = 'home.html'


class ResultsPageView(TemplateView):
    template_name = 'result.html'


class ChecklistPageView(LoginRequiredMixin, ListView):
    pass


@login_required(login_url='account_login')
def checklist_view(request):
    checklists = Checklist.objects.all()

    all_values = [score.value for score in checklists]
    total = 0
    for value in all_values:
        total = total + value
    user = request.user
    score_list = request.POST.getlist('boxes')
    total_score = sum([int(score) for score in score_list])

    percent = round((total_score / total) * 100)

    if percent > 90:
        tier_level = 'Tier 1'
    elif percent > 80:
        tier_level = 'Tier 2'
    elif percent > 70:
        tier_level = 'Tier 3'
    elif percent > 50:
        tier_level = 'Tier 4'
    else:
        tier_level = 'Non Compliant'

    context = {
        'total_score': total_score,
        'percent': percent,
        'total': total,
        'user': user,
        'tier_level': tier_level
    }

    if request.method == "POST":
        return render(request, 'result.html', context)

    context = {
        'categories': Category.objects.all(),
        # 'form': form,
    }
    return render(request, 'checklist_quiz.html', context)


def user_scores_view(request):
    pass


def user_filled_checklists(request):
    pass


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


def icomply_checklist_view(request):
    with open(os.path.join(settings.STATIC_ROOT, 'dpa/iComply - DPA [2019] checklist v1.0.pdf'), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=iComply - DPA [2019] checklist v1.0.pdf'
        return response
    pdf.closed


def dpia_view(request):
    with open(os.path.join(settings.STATIC_ROOT, 'dpa/dpia.pdf'), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=dpia.pdf'
        return response
    pdf.closed


class DpaPageView(TemplateView):
    template_name = 'dpa.html'


class FaqPageView(TemplateView):
    template_name = 'faq.html'


class ChecklistSubmitView(TemplateView):
    template_name = 'checklist_submit.html'

