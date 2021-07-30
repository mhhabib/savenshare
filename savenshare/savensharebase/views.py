from django.contrib.auth import forms
from django.shortcuts import render
from django.contrib.auth import authenticate, login as dj_login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from .forms import SignUpForm
from django.core.mail import send_mail, BadHeaderError
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import LinkPost, LinkFile, LinkWritePost
from .forms import LinkPostForm, LinkFileForm, LinkWritePostForm
from django.contrib.auth.models import User


class home(LoginRequiredMixin, ListView):
    #model = LinkWritePost
    context_object_name = 'posts'
    template_name = 'savensharebase/index.html'
    queryset = LinkWritePost.objects.all()

    def get_context_data(self, **kwargs):

        context = super(home, self).get_context_data(**kwargs)
        context['linkfiles'] = LinkFile.objects.all().filter(
            author=self.request.user)
        context['linkposts'] = LinkPost.objects.all().filter(
            author=self.request.user)
        context['posts'] = context['posts'].filter(
            author=self.request.user)
        return context


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = LinkPost
    form_class = LinkPostForm
    success_url = reverse_lazy('home')
    template_name = 'savensharebase/createlink.html'

    def form_valid(self, form):
        # form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


class LinkPostCreateView(LoginRequiredMixin, CreateView):
    model = LinkWritePost
    form_class = LinkWritePostForm
    success_url = reverse_lazy('home')
    template_name = 'savensharebase/createpostlink.html'

    def form_valid(self, form):
        # form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


class FileCreateView(LoginRequiredMixin, CreateView):
    model = LinkFile
    form_class = LinkFileForm
    success_url = reverse_lazy('home')
    template_name = 'savensharebase/createfilelink.html'

    def form_valid(self, form):
        # form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = LinkWritePost

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            author__username=self.kwargs['author']
        )


class SelectToShare(ListView):
    context_object_name = 'sharelinks'
    template_name = 'savensharebase/selectoshare.html'
    queryset = LinkWritePost.objects.all()

    def get_context_data(self, **kwargs):

        context = super(SelectToShare, self).get_context_data(**kwargs)
        context['linkfiles'] = LinkFile.objects.all().filter(
            author=self.request.user)
        context['linkposts'] = LinkPost.objects.all().filter(
            author=self.request.user)
        context['sharelinks'] = context['sharelinks'].filter(
            author=self.request.user)
        return context


def register(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            dj_login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = SignUpForm()
    return render(request, 'savensharebase/register.html', {'form': form})


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            dj_login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(
                request, f'Invalid user or password for {username}!')

    return render(request, "savensharebase/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
