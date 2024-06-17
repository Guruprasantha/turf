from django.shortcuts import render,redirect,HttpResponse
from .models import *
from datetime import datetime,timedelta
from django.contrib import messages


from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
          turfdetail=Turf.objects.all()
          context={'turfd':turfdetail}
          return render (request,'index.html',context)

def turfpage(request,id):
          data=Turf.objects.all().get(id=id)
          request.session['turf_name']=data.turfname
          print(data)
          x=datetime.now()
          d1=x + timedelta(days=1)
          d2=x + timedelta(days=2)
          d3=x + timedelta(days=3)
          d4=x + timedelta(days=4)
          d5=x + timedelta(days=5)
          d6=x + timedelta(days=6)
          d11=str(d1)
          d21=str(d2)
          d31=str(d3)
          d41=str(d4)
          d51=str(d5)
          d61=str(d6)
          d=[d11,d21,d31,d41,d51,d61]
          days=[]
          for i in d:
                    date = datetime(int(i[0:4]), int(i[5:7]),int(i[8:10]))
                    day = date.strftime('%A')
                    days.append(day)
          print(days)
          context={'data':data,
                   'd1':d11[0:10],
                   'd2':d21[0:10],
                   'd3':d31[0:10],
                   'd4':d41[0:10],
                   'd5':d51[0:10],
                   'd6':d61[0:10],
                   'days':days,
                   }
          return render(request,'turfpage.html',context)

def turf_book(request,id):
          print(id)
          turf_name=request.session['turf_name']
          request.session['date']=id
          data=Turf.objects.all().get(turfname=turf_name)
          bookdata=booking.objects.all().filter(date=id,turfname=turf_name)
          l=[]
          for i in bookdata:
                    print(i.timings)
                    l.append(i.timings)
          print(l)
                    
          context={'data':data,
                   'date':id,
                   'l':l,
                   }
          return render(request,'turf_date.html',context)

def turf_book_add(request,id):
          print(id)
          request.session['time']=id
          print(request.session['date'])
          print(request.session['turf_name'])
          return redirect('turfslot')

def turfslot(request):
          if request.method=='POST':
                    tb=booking()
                    tb.register_name=request.POST.get('username')
                    tb.register_id=request.POST.get('pan')
                    tb.register_mobile=request.POST.get('number')
                    tb.register_address=request.POST.get('email')
                    tb.register_mobile2=request.POST.get('number1')
                    tb.turfname=request.session['turf_name']
                    tb.date=request.session['date']
                    tb.timings=request.session['time']
                    tb.status='BOOKED'
                    tb.save()
                    subject = 'Your TURF booked successfully'
                    message = str(f'Hi {tb.register_name}, thank you for registering in The Turf, \n ' 
                    f' Turf name: {tb.turfname}, \n '
                    f' Turf Date : {tb.date}, \n ' 
                    f' Turf Timing :{tb.timings} ,\n ' )
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.POST.get('email') ]
                    send_mail( subject, message, email_from, recipient_list )
                    messages.success(request,'turf saved successfully..')
                    return redirect('index')
          
          t_time=request.session['time']
          t_date=request.session['date']
          t_name=request.session['turf_name']
          print(t_name)
          context={'tt':t_time,
                   'td':t_date,
                   't_n':t_name,
                   }
          return render(request,'turf_booking.html',context)