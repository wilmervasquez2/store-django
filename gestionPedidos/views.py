import json 
from django.conf import settings
from gestionPedidos.models import Articles
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def search_products(request):
  return render(request,"search.html", {})

def search(request):

  mensaje = "" % request.GET['product']
  return HttpResponse(mensaje)

def result_products(request):
  if request.method == 'GET':

    product_query = request.GET['q']
    articles = Articles.objects.filter(name__icontains = product_query) # LIKE
    articles_list = list(articles.values("name","section","price"))
    
    result = { 'query': product_query, 'articles': articles_list} 
    return JsonResponse(result, safe=False)
  
def contact(request):
  if request.method == 'POST':
    issue = request.POST['issue']
    email = request.POST['email']
    message = "<b>" + request.POST['message'] + " </b>" + email
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["wilmerluisvasquezlino@outlook.es"]

    send_mail(issue, message,email_from,recipient_list,fail_silently=False)

    return HttpResponse("Gracias por enviar la informacion <a href=\"/contact/\">Regresar</a>")
  return render(request, "contact.html", {})