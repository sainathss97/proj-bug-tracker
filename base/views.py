from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Task,Bug
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class Register(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    def form_valid(self,form):
        #If the form is valid, redirect to the supplied URL.
        user = form.save()
        if user is not None:
            login(self.request,user)
            
        return super(Register,self).form_valid(form)

    def get(self,*args, **kwargs):
       #Handle GET requests: instantiate a blank version of the form.
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(Register,self).get(*args, **kwargs)
    
class TaskLogin(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('home')
        # don't forget to introduce LOGIN_URL in settings.py

class TaskLogout(LoginRequiredMixin,LogoutView):
    next_page = 'index'	
    
#--------------------------------------------------------------------------------------------------------------------------------#
class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = "base/home.html"
    context_object_name = 'task'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = context['task'].filter(user = self.request.user)
        #context['count'] = context['task'].filter(complete = False).count()
        context['count'] = context['task'].filter(complete = False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['task'] = context['task'].filter(title__startswith = search_input)
        context['search_input'] = search_input
        
        return context

class TaskListView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = "base/task-list.html"
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
   # template_name = "base/task-create.html"
    fields = ['title','content','complete']	
    success_url = reverse_lazy('home')
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)


class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','content','complete']	
    success_url = reverse_lazy('home')


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    #template_name = "TEMPLATE_NAME"
    success_url = reverse_lazy('home')
#---------------------------------------------------------------------------------------------------------------------------------------#
def bug(request):
    return render(request, 'base/index.html')



class BugView(LoginRequiredMixin,DetailView):
    model = Bug
    template_name = "base/bug-list.html"
    context_object_name = 'bug'



class BugCreate(LoginRequiredMixin,CreateView):
    model = Bug
   # template_name = "base/task-create.html"
    fields = ['ticket','description','status','task','image','attachment']	
    success_url = reverse_lazy('bug-home')
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(BugCreate,self).form_valid(form)


class BugUpdate(LoginRequiredMixin,UpdateView):
    model = Bug
    fields = ['ticket','description','status','task','image','attachment']	
    success_url = reverse_lazy('bug-home')

class BugDelete(LoginRequiredMixin,DeleteView):
    model = Bug
    #template_name = "TEMPLATE_NAME"
    success_url = reverse_lazy('bug-home')

class BugList(LoginRequiredMixin,ListView):
    model = Bug
    template_name = "base/bug-home.html"
    context_object_name = 'bug'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bug"] = context['bug'].filter(user = self.request.user)
        context['count'] = context['bug'].filter(status = False).count()
        #context['task'] = context['bug'].filter(task = self.request.task)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['bug'] = context['bug'].filter(ticket__startswith = search_input)
        context['search_input'] = search_input
       
        return context