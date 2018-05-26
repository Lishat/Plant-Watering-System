from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensors, moto1, moto2, decide
def index(request):
    return HttpResponse("Hello! We are TASK JS")
def Display(request,temperature=None,humidity=None,pressure=None,altitude=None,seaPressure=None,soilMoisture=None,soilMoisture2=None,waterLevel=None,rainDrop=None,ultrasonic=None,time=None):
    all_sensors = Sensors()
    all_sensors.temperature=float(temperature)
    all_sensors.humidity=float(humidity)
    all_sensors.pressure=float(pressure)
    all_sensors.altitude=float(altitude)
    all_sensors.seaPressure=float(seaPressure)
    all_sensors.soilMoisture=float(soilMoisture)
    all_sensors.soilMoisture2=float(soilMoisture2)
    all_sensors.waterLevel=float(waterLevel)
    all_sensors.rainDrop=float(rainDrop)
    all_sensors.ultrasonic=float(ultrasonic)
    all_sensors.time = str(time)
    print(temperature)
    print(humidity)
    print(pressure)
    print(altitude)
    print(seaPressure)
    print(soilMoisture)
    print(soilMoisture2)
    print(waterLevel)
    print(rainDrop)
    print(ultrasonic)
    print(time)
    all_sensors.save()
    p = Sensors.objects.all()
    return render(request ,'temp/sensors.html',{'all_sensors':p})
def new_disp(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-1::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    print(all_sensors)
    return render(request,'temp/dashboard.html',{'all_sensors':all_sensors})
    #return render(request ,'temp/sensors.html',{'all_sensors':all_sensors})
def tempgraph(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    print(all_sensors)
    count = 0
    for i in all_sensors:
        i.serialId = str(count)
        count += 1
    return render(request ,'temp/tempgraph.html',{'all_sensors':all_sensors})
def gmap(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    count = 0
    for i in all_sensors:
        i.serialId = str(count)
        count += 1
    print(all_sensors)
    return render(request ,'temp/gmap.html',{'all_sensors':all_sensors})
def humigraph(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    count=0
    for i in all_sensors:
        i.serialId=str(count)
        count+=1
    print(all_sensors)
    return render(request ,'temp/humidity.html',{'all_sensors':all_sensors})
def presgraph(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    count=0
    for i in all_sensors:
        i.serialId=str(count)
        count+=1
    print(all_sensors)
    return render(request ,'temp/pressure.html',{'all_sensors':all_sensors})
def altigraph(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    count=0
    for i in all_sensors:
        i.serialId=str(count)
        count+=1
    print(all_sensors)
    return render(request ,'temp/altitude.html',{'all_sensors':all_sensors})
def seprgraph(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    count=0
    for i in all_sensors:
        i.serialId=str(count)
        count+=1
    print(all_sensors)
    return render(request ,'temp/seapressure.html',{'all_sensors':all_sensors})
def soimgraph(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    count=0
    for i in all_sensors:
        i.serialId=str(count)
        count+=1
    print(all_sensors)
    return render(request ,'temp/soilmoisture.html',{'all_sensors':all_sensors})
def soim2graph(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    count=0
    for i in all_sensors:
        i.serialId=str(count)
        count+=1
    print(all_sensors)
    return render(request ,'temp/soilMoisture2.html',{'all_sensors':all_sensors})
def walvgraph(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    count=0
    for i in all_sensors:
        i.serialId=str(count)
        count+=1
    print(all_sensors)
    return render(request ,'temp/waterlevel.html',{'all_sensors':all_sensors})
def rdrpgraph(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    count=0
    for i in all_sensors:
        i.serialId=str(count)
        count+=1
    print(all_sensors)
    return render(request ,'temp/raindrop.html',{'all_sensors':all_sensors})
def sobsgraph(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    count=0
    for i in all_sensors:
        i.serialId=str(count)
        count+=1
    print(all_sensors)
    return render(request ,'temp/sensorobstacle.html',{'all_sensors':all_sensors})
def sensortable(request):
    try:
        all_sensors = Sensors.objects.all()[len(Sensors.objects.all())-10::1][::-1]
    except:
        all_sensors = Sensors.objects.all()[::-1]
    print(all_sensors)
    return render(request ,'temp/sensortable.html',{'all_sensors':all_sensors})
def auto(request, value = 0):
    tempo = decide()
    tempo.value = int(value)
    tempo.save()
    return render(request, 'temp/auto.html', {'setA':value})
def motor1(request, value = 0):
    tempo = moto1()
    tempo.value = int(value)
    tempo.save()
    return render(request, 'temp/motor1.html', {'setA':value})
def motor2(request, value = 0):
    tempo = moto2()
    tempo.value = int(value)
    tempo.save()
    return render(request, 'temp/motor2.html', {'setA':value})
def autodef(request):
    if(decide.objects.count() >= 1):
        return render(request, 'temp/auto.html', {'setA': decide.objects.get(pk=decide.objects.count()).value})
    else:
        return render(request, 'temp/auto.html', {'setA': 0})
def motor1def(request):
    if(moto1.objects.count() >= 1):
        return render(request, 'temp/motor1.html', {'setA': moto1.objects.get(pk=moto1.objects.count()).value})
    else:
        return render(request, 'temp/motor1.html', {'setA': 0})
def motor2def(request):
    if(moto2.objects.count() >= 1):
        return render(request, 'temp/motor2.html', {'setA': moto2.objects.get(pk=moto2.objects.count()).value})
    else:
        return render(request, 'temp/motor2.html', {'setA': 0})
def control(request):
    return render(request, 'temp/control.html')