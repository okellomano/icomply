import pandas as pd
import weasyprint
import os

from PIL import Image, ImageFont, ImageDraw

from reportlab.pdfgen import canvas

from django.conf import settings
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .models import Checklist, Category, UserChecklistEntries, PoliciesDocuments
from .forms import UploadForm, PoliciesUploadForm
from .operations import calculate_scores, get_compliance_tier, get_user_scores_for_specific_checklist, save_user_entries


class HomePageView(TemplateView):
    template_name = 'home.html'


class ResultsPageView(TemplateView):
    template_name = 'result.html'


class ChecklistPageView(LoginRequiredMixin, ListView):
    pass


@login_required(login_url='account_login')
def checklist_view(request):
    '''Processing the checklist form view. '''

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
        # return render(request, 'result.html', context)
        return redirect('/uploads/')
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'checklist_quiz.html', context)


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
def user_results_view(request, entries=None):
    try:
        entries = get_object_or_404(UserChecklistEntries.objects.filter(user=request.user))
    except MultipleObjectsReturned:
        entries = UserChecklistEntries.objects.filter(user=request.user).order_by('-date_filled').first()

    return render(request, 'result.html', {'entries': entries})


class ResultsListView(ListView):
    model = UserChecklistEntries
    template_name = 'user_result.html'
    context_object_name = 'results'


class ResultDetailView(DetailView):
    model = UserChecklistEntries
    template_name = 'user_result_detail.html'
    context_object_name = 'result'


class UploadView(FormView):
    template_name = 'policies_upload.html'
    form_class = UploadForm
    success_url = '/checklist_submitted/'

    def form_valid(self, form):
        for each in form.cleaned_data['policies']:
            PoliciesDocuments.objects.create(document=each)
        return super(UploadView, self).form_valid(form)


def upload_documents(request):
    '''Handles uploading of the supportive documents. '''
    if request.method == 'POST':
        form = PoliciesUploadForm(request.POST, request.FILES)
        # documents = request.FILES.getlist('document')
        if form.is_valid():
            policiesdocuments = form.save(commit=False)
            policiesdocuments.organization = request.user
            policiesdocuments.save()

            return HttpResponseRedirect('/checklist_submitted/')
    else:
        form = PoliciesUploadForm()

    return render(request, 'policies_upload.html', {'form': form})


def generate_certificate(request):
    '''A function for generating user certificates. '''

    try:
        data = get_object_or_404(UserChecklistEntries.objects.filter(user=request.user))
    except MultipleObjectsReturned:
        data = UserChecklistEntries.objects.filter(user=request.user).order_by('-date_filled').first()

    data_list = {'user': data.user, 'percent': data.percent_s, 'score': data.user_score,
                 'tier': data.tier, 'date': data.date_filled}

    cert = Image.open('static/images/cert.png')
    cert_draw = ImageDraw.Draw(cert)

    tier_location = (1047, 274)
    user_location = (635, 461)
    date_location = (660, 698)
    font = ImageFont.truetype('arial.ttf', 150)

    cert_draw.text(user_location, data_list['user'], font=font)
    cert_draw.text(tier_location, data_list['tier'], font=font)
    cert_draw.text(date_location, data_list['date'], font=font)

    cert.save(f'{data_list["user"]} Compliance cert.pdf')
    return FileResponse(open(f'{data_list["user"]} Compliance cert.pdf', 'rb'), as_attachment=True, content_type='application/pdf')


class ImpactAssessmentView(LoginRequiredMixin, TemplateView):
    template_name = 'dpia.html'


class IlearnDpaView(TemplateView):
    template_name = 'ilearn.html'


class IEnforceView(TemplateView):
    template_name = 'enforce.html'


class IComplyManagerView(TemplateView):
    template_name = 'icomply_manager.html'


@login_required(login_url='account_login')
def result_pdf_reports(request):
    try:
        entries = get_object_or_404(UserChecklistEntries.objects.filter(user=request.user))
    except MultipleObjectsReturned:
        entries = UserChecklistEntries.objects.filter(user=request.user).order_by('-date_filled').first()

    html = render_to_string('pdf.html', {'entries': entries})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=compliance_{request.user}.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
        settings.STATIC_ROOT + '/css/style.css')])

    return response


@login_required(login_url='account_login')
def cert_pdf(request):
    try:
        entries = get_object_or_404(UserChecklistEntries.objects.filter(user=request.user))
    except MultipleObjectsReturned:
        entries = UserChecklistEntries.objects.filter(user=request.user).order_by('-date_filled').first()

    html = render_to_string('cert.html', {'entries': entries})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=compliance_{request.user}.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
        settings.STATIC_ROOT + '/css/style.css')])

    if entries.percent_s > 70:
        return response
    else:
        return redirect('checklist:nocert')

        # return HttpResponse('Please increase your compliance level to get a certificate')
        # return f'Please increase your compliance level to get a certificate'

    # return response


class ChecklistDemoView(LoginRequiredMixin, TemplateView):
    template_name = 'checklist_demo.html'


class NoCertView(TemplateView):
    template_name = 'nocert.html'


