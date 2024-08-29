from django.urls import path
from . import views

urlpatterns = [
    # FormAssur URLs
    path('formassur/', views.formassur_list, name='formassur-list'),
    path('formassur/<int:id>/', views.formassur_detail, name='formassur-detail'),
    path('formassur/create/', views.create_formassur, name='create-formassur'),
    path('formassur/update/<int:id>/', views.update_formassur, name='update-formassur'),
    path('formassur/delete/<int:id>/', views.delete_formassur, name='delete-formassur'),

    # MutuelleCatalog URLs
    path('mutuellecatalog/', views.mutuellecatalog_list, name='mutuellecatalog-list'),
    path('mutuellecatalog/<int:id>/', views.mutuellecatalog_detail, name='mutuellecatalog-detail'),
    path('mutuellecatalog/create/', views.create_mutuellecatalog, name='create-mutuellecatalog'),
    path('mutuellecatalog/update/<int:id>/', views.update_mutuellecatalog, name='update-mutuellecatalog'),
    path('mutuellecatalog/delete/<int:id>/', views.delete_mutuellecatalog, name='delete-mutuellecatalog'),

    # Contact URLs
    path('contact/', views.contact_list, name='contact-list'),
    path('contact/<int:id>/', views.contact_detail, name='contact-detail'),
    path('contact/create/', views.create_contact, name='create-contact'),
    path('contact/update/<int:id>/', views.update_contact, name='update-contact'),
    path('contact/delete/<int:id>/', views.delete_contact, name='delete-contact'),
]
