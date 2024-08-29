import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.shortcuts import get_object_or_404
from .models import FormAssur, Contact, MutuelleCatalog


@require_GET
def formassur_list(request):
    formassurs = FormAssur.objects.all()
    formassur_data = [
        {
            'id': formassur.id,
            'nom': formassur.nom,
            'prenom': formassur.prenom,
            'tel': formassur.tel,
            'email': formassur.email,
            'montant': formassur.montant,
            'situation': formassur.situation,
            'banque': formassur.banque,
            'accepter': formassur.accepter
        } for formassur in formassurs
    ]
    return JsonResponse({'formassurs': formassur_data})

@require_GET
def formassur_detail(request, id):
    formassur = get_object_or_404(FormAssur, pk=id)
    formassur_data = {
        'id': formassur.id,
        'nom': formassur.nom,
        'prenom': formassur.prenom,
        'tel': formassur.tel,
        'email': formassur.email,
        'montant': formassur.montant,
        'situation': formassur.situation,
        'banque': formassur.banque,
        'accepter': formassur.accepter
    }
    return JsonResponse({'formassur': formassur_data})

@require_POST
@csrf_exempt
def create_formassur(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        formassur = FormAssur.objects.create(
            nom=data.get('nom'),
            prenom=data.get('prenom'),
            tel=data.get('tel'),
            email=data.get('email'),
            montant=data.get('montant'),
            situation=data.get('situation'),
            banque=data.get('banque'),
            accepter=data.get('accepter')
        )
        return JsonResponse({'message': 'FormAssur created successfully', 'formassur_id': formassur.id})
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON data')

@require_http_methods(['PUT', 'PATCH'])
@csrf_exempt
def update_formassur(request, id):
    try:
        formassur = get_object_or_404(FormAssur, pk=id)
        data = json.loads(request.body.decode('utf-8'))

        formassur.nom = data.get('nom', formassur.nom)
        formassur.prenom = data.get('prenom', formassur.prenom)
        formassur.tel = data.get('tel', formassur.tel)
        formassur.email = data.get('email', formassur.email)
        formassur.montant = data.get('montant', formassur.montant)
        formassur.situation = data.get('situation', formassur.situation)
        formassur.banque = data.get('banque', formassur.banque)
        formassur.accepter = data.get('accepter', formassur.accepter)

        formassur.save()
        return JsonResponse({'message': 'FormAssur updated successfully'})
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON data')

@require_http_methods(['DELETE'])
@csrf_exempt
def delete_formassur(request, id):
    formassur = get_object_or_404(FormAssur, pk=id)
    formassur.delete()
    return JsonResponse({'message': 'FormAssur deleted successfully'})

@require_GET
def mutuellecatalog_list(request):
    mutuellecatalogs = MutuelleCatalog.objects.all()
    mutuellecatalog_data = [
        {
            'id': mutuellecatalog.id,
            'nom': mutuellecatalog.nom,
            'prenom': mutuellecatalog.prenom,
            'tel': mutuellecatalog.tel,
            'email': mutuellecatalog.email,
            'accepter': mutuellecatalog.accepter
        } for mutuellecatalog in mutuellecatalogs
    ]
    return JsonResponse({'mutuellecatalogs': mutuellecatalog_data})

@require_GET
def mutuellecatalog_detail(request, id):
    mutuellecatalog = get_object_or_404(MutuelleCatalog, pk=id)
    mutuellecatalog_data = {
        'id': mutuellecatalog.id,
        'nom': mutuellecatalog.nom,
        'prenom': mutuellecatalog.prenom,
        'tel': mutuellecatalog.tel,
        'email': mutuellecatalog.email,
        'accepter': mutuellecatalog.accepter
    }
    return JsonResponse({'mutuellecatalog': mutuellecatalog_data})

@require_POST
@csrf_exempt
def create_mutuellecatalog(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        mutuellecatalog = MutuelleCatalog.objects.create(
            nom=data.get('nom'),
            prenom=data.get('prenom'),
            tel=data.get('tel'),
            email=data.get('email'),
            accepter=data.get('accepter')
        )
        return JsonResponse({'message': 'MutuelleCatalog created successfully', 'mutuellecatalog_id': mutuellecatalog.id})
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON data')

@require_http_methods(['PUT', 'PATCH'])
@csrf_exempt
def update_mutuellecatalog(request, id):
    try:
        mutuellecatalog = get_object_or_404(MutuelleCatalog, pk=id)
        data = json.loads(request.body.decode('utf-8'))

        mutuellecatalog.nom = data.get('nom', mutuellecatalog.nom)
        mutuellecatalog.prenom = data.get('prenom', mutuellecatalog.prenom)
        mutuellecatalog.tel = data.get('tel', mutuellecatalog.tel)
        mutuellecatalog.email = data.get('email', mutuellecatalog.email)
        mutuellecatalog.accepter = data.get('accepter', mutuellecatalog.accepter)

        mutuellecatalog.save()
        return JsonResponse({'message': 'MutuelleCatalog updated successfully'})
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON data')

@require_http_methods(['DELETE'])
@csrf_exempt
def delete_mutuellecatalog(request, id):
    mutuellecatalog = get_object_or_404(MutuelleCatalog, pk=id)
    mutuellecatalog.delete()
    return JsonResponse({'message': 'MutuelleCatalog deleted successfully'})




@require_GET
def contact_list(request):
    contacts = Contact.objects.all()
    contact_data = [
        {
            'id': contact.id,
            'surname': contact.surname,
            'name': contact.name,
            'phone': contact.phone,
            'email': contact.email,
            'postal_code': contact.postal_code,
            'montant': contact.montant,
            'data_usage': contact.data_usage
        } for contact in contacts
    ]
    return JsonResponse({'contacts': contact_data})

@require_GET
def contact_detail(request, id):
    contact = get_object_or_404(Contact, pk=id)
    contact_data = {
        'id': contact.id,
        'surname': contact.surname,
        'name': contact.name,
        'phone': contact.phone,
        'email': contact.email,
        'postal_code': contact.postal_code,
        'montant': contact.montant,
        'data_usage': contact.data_usage
    }
    return JsonResponse({'contact': contact_data})

@require_POST
@csrf_exempt
def create_contact(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        contact = Contact.objects.create(
            surname=data.get('surname'),
            name=data.get('name'),
            phone=data.get('phone'),
            email=data.get('email'),
            postal_code=data.get('postal_code'),
            montant=data.get('montant'),
            data_usage=data.get('data_usage')
        )
        return JsonResponse({'message': 'Contact created successfully', 'contact_id': contact.id})
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON data')

@require_http_methods(['PUT', 'PATCH'])
@csrf_exempt
def update_contact(request, id):
    try:
        contact = get_object_or_404(Contact, pk=id)
        data = json.loads(request.body.decode('utf-8'))

        contact.surname = data.get('surname', contact.surname)
        contact.name = data.get('name', contact.name)
        contact.phone = data.get('phone', contact.phone)
        contact.email = data.get('email', contact.email)
        contact.postal_code = data.get('postal_code', contact.postal_code)
        contact.montant = data.get('montant', contact.montant)
        contact.data_usage = data.get('data_usage', contact.data_usage)

        contact.save()
        return JsonResponse({'message': 'Contact updated successfully'})
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON data')

@require_http_methods(['DELETE'])
@csrf_exempt
def delete_contact(request, id):
    contact = get_object_or_404(Contact, pk=id)
    contact.delete()
    return JsonResponse({'message': 'Contact deleted successfully'})