from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentFM
from .models import Student
from django.views.generic.base import TemplateView, RedirectView
from django.views import View


# For Add and Show 
class UserAddShowView(TemplateView):
    template_name = 'enroll/addshow.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentFM()
        context = {'data':Student.objects.all(), 'form':fm}
        return context

    def post(self, request):
        if request.method == 'POST':
            fm = StudentFM(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/')
# For Delete Data
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, **kwargs):
        Student.objects.get(pk=kwargs['id']).delete()
        return super().get_redirect_url(**kwargs)

# for Update
class UserUpdateView(View):
    def get(self, request, id):
        pi = Student.objects.get(pk=id)
        fm = StudentFM(instance=pi)
        return render(request, 'enroll/update.html', {'form':fm})
    
    def post(self, request, id):
        pi = Student.objects.get(pk=id)
        fm = StudentFM(request.POST, instance=pi)
        fm.save()
        return HttpResponseRedirect('/')