from django.urls import path

from .views import HomePageView, ChecklistPageView, DpaPageView, FaqPageView, ResultsPageView

# Article views
from . import views


app_name = 'checklist'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('checklist/', ChecklistPageView.as_view(), name='checklist'),
    path('checklist/', views.checklist_view, name='checklist'),
    path('results/', ResultsPageView.as_view(), name='results'),
    path('faq/', FaqPageView.as_view(), name='faq'),
    path('dpa/', views.dpa_view, name='dpa'),
    path('regulations/', views.dpa_regulations_view, name='dpa_regulations'),
    path('icomply/', views.icomply_checklist_view, name='icomply'),
    path('dpia/', views.dpia_view, name='dpia'),
    path('checklist_submitted/', views.ChecklistSubmitView.as_view(), name='checklist_submitted'),
    path('user-results/', views.user_results_view, name='user-results'),

    # path('user-results/', views.ResultsListView.as_view(), name='user-results'),
    path('<int:pk>', views.ResultDetailView.as_view(), name='result-details'),
    path('uploads/', views.upload_documents, name='policies-upload'),
    path('certificate/', views.generate_certificate, name='gen_cert'),

    path('impact-assessment/', views.ImpactAssessmentView.as_view(), name='impact-assessment'),
    path('ilearn/', views.IlearnDpaView.as_view(), name='ilearndpa'),
    path('ienforce/', views.IEnforceView.as_view(), name='ienforce'),
    path('icomplymanager/', views.IComplyManagerView.as_view(), name='icomplymanager'),

]
