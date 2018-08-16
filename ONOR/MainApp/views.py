from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users
import smtplib
from MainApp.models import Carousel,Users



def send(request):
   gmail_user = 'bhanuchander008@gmail.com'
   gmail_pwd = 'abhi1015'
   FROM = gmail_user
   address = Users.objects.all().last()
   recipient = address.Email
   print("address:",address.Email)
   TO = recipient if type(recipient) is list else [recipient]
   SUBJECT = 'email test'
   TEXT = 'succesfully registered as a user in our app'
   message = """From: %s\nTo: %s\nSubject: %s\n\n%s
   """% (FROM, ", ".join(TO), SUBJECT, TEXT)
   try:
       server = smtplib.SMTP("smtp.gmail.com", 587)
       server.ehlo()
       server.starttls()
       server.login(gmail_user, gmail_pwd)
       server.sendmail(FROM, TO, message)
       server.close()
       return HttpResponse("success")
   except Exception as ex:
       return HttpResponse(ex)


def users(request):
    act= Users.objects.all()
    if act:
        context = {
            'act': act
        }
        return render(request, 'basic.html', context)
    else:
        return HttpResponseNotFound("no orders found")
