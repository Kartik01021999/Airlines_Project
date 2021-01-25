from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import flights
from .models import Booking
from django.utils import timezone
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords did not match'})

    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return render(request,'accounts/booking.html',{'name':request.POST['username']})
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def searchflights(request):
        if request.method == 'POST':
            source=request.POST['source']
            Destination = request.POST['destination']
            if flights.objects.filter(Source=source,destination=Destination):
                no_of_flights=flights.objects.filter(Source=source,destination=Destination).count()
                return render(request,'accounts/flights.html',{'routes':flights.objects.filter(Source=source,destination=Destination),'source':source,'destination':Destination,'no_of_flights':range(no_of_flights),'date':request.POST['date']})

def BookTickets(request):
    if request.method == 'POST':
        fare=request.POST['price']
        source=request.POST['source']
        Destination=request.POST['destination']
        takeoff=request.POST['Start']
        land=request.POST['End']
        return render(request,'accounts/BookTickets.html',{'cost':fare,'source':source,'destination':Destination,'Takeoff':takeoff,'land':land,'date':request.POST['date']})

def payment(request):
    if request.method == 'POST':
        f_name=request.POST['firstname']
        l_name=request.POST['lastname']
        mob=request.POST['mobilenumber']
        date_of_flight = request.POST['date']
        amount = request.POST['price']
        takeoff = request.POST['takeoff']
        land = request.POST['land']
        source = request.POST['source']
        destination = request.POST['destination']
        mailid = request.POST['mailid']
        gender = request.POST['gender']
        return render(request,"accounts/payment.html",{'name':f_name,'surname':l_name,'mob':mob,'date':date_of_flight,'cost':amount,'takeoff':takeoff,'land':land,'source':source,'destination':destination,'mailid':mailid,'gender':gender})

def feedback(request):
    if request.method == 'POST':
        booking = Booking()
        booking.first_name = request.POST['firstname']
        booking.last_name = request.POST['lastname']
        booking.source = request.POST['source']
        booking.destination = request.POST['destination']
        booking.booking_date = timezone.datetime.now()
        booking.journey_date = request.POST['date']
        booking.mob = request.POST['mobile']
        booking.price = request.POST['price']
        booking.booked_by = request.user
        booking.save()
        customer=request.POST['mailid']
        firstname=request.POST['firstname']
        lastanme=request.POST['lastname']
        source= request.POST['source']
        destination= request.POST['destination']
        date= request.POST['date']
        contact= request.POST['mobile']
        amount=request.POST['price']
        start=request.POST['takeoff']
        finish=request.POST['land']
        message = MIMEMultipart("alternative")
        test = "This is for testing"
        message["Subject"] = "BOOKING CONFIRMATION"
        text = """\
        Hi,
        Please find the tickets below"""
        html = """\
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
          <meta name="description" content="">
          <meta name="author" content="">


          <title>My Airlines</title>

          <!-- Bootstrap core CSS -->
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

        </head>

        <body>

          <header>
            <nav class="navbar navbar-expand-lg navbar-light bg-info">
                <div class="container">
              <a class="navbar-brand" href="">
                <b style="font-size:200%">My Airlines</b>
              </a>
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav ml-auto">
                </div>
              </div>
                </div>
            </nav>
          </header>
          <div class="container" style="border:2px solid black">

              <h2>Ticket Details:</h2>
              <h4 style:"color:blue;">    Passenger    :  """+firstname+""" """+lastanme+"""</h4>
              <h4 style:"color:blue;">    Source       :  """+source+"""</h4>
              <h4 style:"color:blue;">    Destination  :  """+destination+"""</h4>
              <h4 style:"color:blue;">    Email-id     :  """+customer+"""</h4>
              <h4 style:"color:blue;">    Contact no   :  """+contact+"""</h4>
              <h4 style:"color:blue;">    Timing       :  """+start+""" -> """+finish+"""</h4>
              <h4 style:"color:blue;"> Date of journey :  """+date+"""</h4>
              <br><i style="color:red;">*Note:20KG Check-in,7KG handbag.</i>
          </div>

          <footer class="text-muted">
            <div class="container text-center">
              <p>Thanks for choosing MY Airlines,</p><p> Kartik Mishra </p>
              </div>
          </footer>

          <!-- Bootstrap core JavaScript
          ================================================== -->
          <!-- Placed at the end of the document so the pages load faster -->
          <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        </body>
        </html>
        """
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo()
        conn.starttls()
        conn.login('kartikmishra866@gmail.com', 'pijxwwecemufyzgw')
        conn.sendmail('kartikmishra866@gmail.com', customer, message.as_string())
        conn.quit()

        return render(request,"accounts/feedback.html")