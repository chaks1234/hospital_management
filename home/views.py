from  django.views import  generic
from .models import Doctor
from .models import Patient
from  django.views.generic.edit import CreateView,UpdateView,DeleteView
from  django.core.urlresolvers import reverse_lazy
from  django.shortcuts import redirect,render
from  django.contrib.auth import authenticate,login
from  django.views.generic import View
from  .forms import UserForm

class IndexView(generic.ListView):
	template_name = 'home/doctor.html'
	context_object_name = 'all_doctor'

	def get_queryset(self):
		return Doctor.objects.all()

class Patient_view(generic.ListView):
	template_name = 'home/patient_list.html'
	context_object_name = 'all_patient'

	def get_queryset(self):
		return Patient.objects.all()

class PatientView(generic.DetailView):
	model = Doctor
	template_name = 'home/patient.html'



class DoctorCreate(CreateView):
	model = Patient
	fields = ['Teacher', 'name', 'adhar']

class PatientCreate(CreateView):
	model = Doctor
	fields = ['name']

class PatientDelete(DeleteView):
	model = Doctor
	fields = ['name']
	success_url = reverse_lazy('home:index')

class DoctorUpdate(UpdateView):
	model = Patient
	fields = ['Teacher','name','adhar']
	#template_name_suffix = 'patient_update_form'

class DoctorDelete(DeleteView):
	model = Patient
	success_url = reverse_lazy('home:patient')

class UserFormView(View):
	form_class = UserForm
	template_name = 'home/registration_form.html'
	def get(self,request):
		form =self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

		#cleaned (normalised ) data

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()


			# retruns User objects if credentials are write

			user = authenticate(username = username,password = password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('home:index')

		return render(request, self.template_name, {'form': form})
