from django.shortcuts import render,get_object_or_404,redirect
from .models import Student
from django.views.generic import ListView , DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.'
"""
def home(request):
    context = {'students':Student.objects.all()}
    return render(request,'index.html',context)

def spage1(request,id):
    context = {'student':get_object_or_404(Student , pk = id)}
    return render(request,'spage1.html',context )"""
    
class HomePageView(ListView):
    template_name = 'index.html'
    model = Student
    context_object_name = 'students'
    def get_queryset(self):
        students = super().get_queryset()
        if not self.request.user.is_authenticated:
            return None
        return students.filter(manager = self.request.user)

class spage1View(LoginRequiredMixin,DetailView):
    template_name = 'spage1.html'
    model = Student
    context_object_name = 'student'

@login_required    
def search(request):
    print (request.GET)
    
    if request.GET:
        search_term = request.GET['search_term']
        #search_result = Student.objects.filter(firstname__icontains = search_term)
        # for complex query
        search_result = Student.objects.filter(
                Q(manager = request.user) &
                Q(firstname__icontains = search_term) |
                Q(lastname__icontains = search_term) 
                )
            
        context = {'search_term':search_term,
                   'students':search_result}
        return render(request ,'search.html',context)
    else:
        return redirect('home')
    
    

class CreateStudent(LoginRequiredMixin,CreateView):
    model = Student
    template_name = 'create.html'
    fields = ['firstname','lastname','email','gender','date_added']
    success_url = '/student/create/success'
    
    def form_valid(self,form):
        instance = form.save(commit = False)
        instance.manager = self.request.user
        instance.save()
        return redirect('home')
    
def success(request):
    context = {}
    return render(request,'success.html',context)

class UpdateStudent(LoginRequiredMixin,UpdateView):
    model = Student
    template_name = 'update.html'
    fields = ['firstname','lastname','email','gender','date_added']
    success_url = '/'
    
    def form_valid(self,form):
        instance = form.save()
        return redirect ('spage1',instance.pk)
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = "/"
    
class DeleteStudent(DeleteView):
    model = Student
    template_name = "delete.html"
    success_url = '/'
    

    
