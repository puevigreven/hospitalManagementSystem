from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from appointments.models import Appointment
from practitioner.models import Practitioner
from django.http import HttpResponse
from forms import AppointmentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def appointments(request):
	args = {}
	args.update(csrf(request))

	args['appointments'] = Appointment.objects.all()
	return render_to_response('appointments.html',
		args )

def appointment(request, appointment_id=1):
	return render_to_response('appointment.html', 
		{'appointment': Appointment.objects.get(id = appointment_id)})

def create(request):
	if request.POST:
		form = AppointmentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/appointments/all')

	else:
		form = AppointmentForm()

	args = {}
	args.update(csrf(request))
	args['practitioner'] = Practitioner.objects.all()
	args['form'] = form
	return render_to_response('create_appointment.html', args)	
