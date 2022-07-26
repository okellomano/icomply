import io
import os

from reportlab.pdfgen import canvas

from django.conf import settings
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

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
def user_results_view(request, entries=None):
    # entries = UserChecklistEntries.objects.filter(user=request.user)[0]
    try:
        entries = get_object_or_404(UserChecklistEntries.objects.filter(user=request.user))
    except MultipleObjectsReturned:
        entries = UserChecklistEntries.objects.filter(user=request.user).first()

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


def generate_report(request, id):
    buffer = io.BytesIO()
    x = canvas.Canvas(buffer)
    x.drawString(100, 100, 'Testing pdf generator')
    x.showPage()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='pdf_test.pdf')

