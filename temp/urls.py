from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.new_disp, name='new_disp'),
    url(r'^display/$', views.new_disp, name="new_disp"),
    url(r'^display/sensortable/$', views.sensortable, name="sensortable"),
    url(r'^display/tempgraph/$',views.tempgraph, name="tempgraph"),
    url(r'^display/humigraph/$',views.humigraph, name="humigraph"),
    url(r'^display/presgraph/$',views.presgraph, name="presgraph"),
    url(r'^display/altigraph/$',views.altigraph, name="altigraph"),
    url(r'^display/seprgraph/$',views.seprgraph, name="seprgraph"),
    url(r'^display/soimgraph/$',views.soimgraph, name="soimgraph"),
    url(r'^display/soim2graph/$',views.soim2graph, name="soim2graph"),
	url(r'^display/walvgraph/$',views.walvgraph, name="walvgraph"),
	url(r'^display/rdrpgraph/$',views.rdrpgraph, name="rdrpgraph"),
	url(r'^display/sobsgraph/$',views.sobsgraph, name="sobsgraph"),
	url(r'^display/gmap/$',views.gmap, name="gmap"),
	url(r'^auto/(?P<value>[01]+)/$', views.auto, name="auto"),
	url(r'^motor1/(?P<value>[01]+)/$', views.motor1, name="motor1"),
	url(r'^motor2/(?P<value>[01]+)/$', views.motor2, name="motor2"),
	url(r'^auto/$', views.autodef, name="autodef"),
	url(r'^motor1/$', views.motor1def, name="motor1def"),
	url(r'^motor2/$', views.motor2def, name="motor2def"),
	url(r'^control/$', views.control, name="control"),
    url(r'^display/(?P<temperature>[0-9]+.[0-9]+)/(?P<humidity>[0-9]+.?[0-9]*)/(?P<pressure>[0-9]+.?[0-9]*)/(?P<altitude>[0-9]+.?[0-9]*)/(?P<seaPressure>[0-9]+.?[0-9]*)/(?P<soilMoisture>[0-9]+.?[0-9]*)/(?P<soilMoisture2>[0-9]+.?[0-9]*)/(?P<waterLevel>[0-9]+.?[0-9]*)/(?P<rainDrop>[0-9]+.?[0-9]*)/(?P<ultrasonic>[0-9]+.?[0-9]*)/(?P<time>[A-Za-z][A-Za-z][A-Za-z] [A-Za-z][A-Za-z][A-Za-z] [012]?[0-9] [012]?[0-9]:[0-5][0-9]:[0-5][0-9] [0-9][0-9][0-9][0-9])/$',views.Display,name="Display"),
]