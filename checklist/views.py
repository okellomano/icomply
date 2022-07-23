import io
from ast import Pass
import os
from datetime import datetime

from reportlab.pdfgen import canvas

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect

from .models import Checklist, Category, UserChecklistEntries
from .operations import calculate_scores, get_compliance_tier, get_user_scores_for_specific_checklist, save_user_entries


class HomePageView(TemplateView):
    template_name = 'home.html'


class ResultsPageView(TemplateView):
    template_name = 'result.html'


class ChecklistPageView(LoginRequiredMixin, ListView):
    pass


@login_required(login_url='account_login')
def checklist_view(request):

    if request.method == 'POST':
        user = request.user
        score_entries = request.POST.getlist('boxes')

        scores_rslt = calculate_scores(score_entries=score_entries)

        user_score_total = scores_rslt['user_score_total']
        percent = scores_rslt['percent']
        total_available_score = scores_rslt['total_available_score']

        tier_level = get_compliance_tier(percent=percent)

        '''save the results. '''
        save_user_entries(user=user, entries=score_entries)
        get_user_scores_for_specific_checklist(user=user, checklist_id=1)

        context = {
            'total_score': user_score_total,
            'percent': percent,
            'total': total_available_score,
            'user': user,
            'tier_level': tier_level
        }
        return render(request, 'result.html', context)
    context = {
        'categories': Category.objects.all()
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


# user score view
def user_results_view(request):
    entries = UserChecklistEntries.objects.filter(user=request.user)

    # for entry in entries:
    #     context = {
    #         'user': entry.user,
    #         'percent': entry.percent_s,
    #         'tier': entry.tier,
    #         'date_filled': entry.date_filled
    #     }
    return render(request, 'user_result.html', {'entries': entries})


class ResultsListView(ListView):
    model = UserChecklistEntries
    template_name = 'user_result.html'
    context_object_name = 'results'


class ResultDetailView(DetailView):
    model = UserChecklistEntries
    template_name = 'user_result_detail.html'
    context_object_name = 'result'


def generate_report(request, id):
    buffer = io.BytesIO()
    x = canvas.Canvas(buffer)
    x.drawString(100, 100, 'Testing pdf generator')
    x.showPage()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='pdf_test.pdf')

