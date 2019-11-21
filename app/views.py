from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.utils import timezone
from django.urls import reverse_lazy
from app import forms
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "base.html", {"posts": posts})

def make_post(requuest, id):
    if request.method == "GET":
        post = Post.objects.get(id=id)
    elif request.method == "POST":
        pass


class SignUpView(FormView):
    form_class = forms.SignUpForm
    template_name = "user_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.signup()
        login(self.request, user)
        return super().form_valid(form)

