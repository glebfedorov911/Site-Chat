import datetime
import time
import string
import random

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, DetailView
from django.db.models import Q

from .forms import *
from .models import *
from .models import generate_string
from .context_processors import *

class MainPage(CreateView):
    template_name = "guide/main.html"
    form_class = MessageForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Основная страница"
        context["msg"] = Message.objects.filter(Q(from_user=self.request.user.id) | Q(to_user=self.request.user.id)).order_by("date_create")
        context["msg1"] = Message.objects.filter(Q(key=self.request.session.get("id")) | Q(to_user=self.request.user.id)).order_by("date_create")
        context["key_id"] = self.request.session.get("id")
        context["adminEdit"] = adminEdit(self.request)["adminEdit"]
        check_data()
        return context

    def post(self, request, *args, **kwargs):
        try:
            if not self.request.FILES.get("audio") is None:
                user = UserCustomModel.objects.filter(id=request.user.id)
                chat = UserCustomModel.objects.get(username="CHAT-BOT")

                path = default_storage.save('audio/file' + '.wav', ContentFile(self.request.FILES.get("audio").read()))
                msg_obj = Message.objects.create(from_user=user[0], to_user=chat, audio=path)
                msg_obj.save()

                chat_answer("Голосовое сообщение", user[0], chat)

            elif self.request.user.username == "":
                chat = UserCustomModel.objects.get(username="CHAT-BOT")

                if "msg" not in self.request.session:
                    self.request.session['msg'] = 3
                    self.request.session['id'] = randomword()

                if not self.request.session.get("msg") == 0:
                    self.request.session['msg'] -= 1

                    msg = Message.objects.create(key=self.request.session["id"], to_user=chat,
                                                 msg=self.request.POST.get("msg"))
                    msg.save()

                    chat_answer(self.request.POST.get("msg"), self.request.session["id"], chat, True)
                else:
                    chat_answer("Зарегистрируйтесь или авторизуйтесь чтобы продолжить!", self.request.session["id"], chat,
                                True)

            # if not is_ajax(self.request):
            #     user = UserCustomModel.objects.filter(id=request.user.id)
            #     user.update(msg=user[0].msg-1)
            #     chat = UserCustomModel.objects.get(username="CHAT-BOT")
            #     msg = request.POST.get("msg")
            #
            #     msg_obj = Message.objects.create(from_user=user[0], to_user=chat, msg=msg)
            #     msg_obj.save()
            #
            #     chat_answer(msg, user[0], chat)

            elif is_ajax(self.request):
                user = UserCustomModel.objects.filter(id=request.user.id)
                user.update(msg=user[0].msg - 1)
                chat = UserCustomModel.objects.get(username="CHAT-BOT")
                msg = request.POST.get("msg")

                msg_obj = Message.objects.create(from_user=user[0], to_user=chat, msg=msg)
                msg_obj.save()

                chat_answer(msg, user[0], chat)
        except:
            return redirect("error")

        return redirect("home")

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip

def randomword():
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(10))

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def check_data():
    users = UserCustomModel.objects.all()

    for user in users:
        if datetime.now().month - user.date_of_reg_ref.month:
            try:
                UserCustomModel.objects.filter(username=user.username).update(ref_code="")
            except:
                pass
def chat_answer(msg, user_id, chat, flag=False):
    # req = msg запрос тут
    if flag:
        msg_obj_chat = Message.objects.create(from_user=chat, key=user_id, to_user=chat, msg=msg)
    else:
        msg_obj_chat = Message.objects.create(from_user=chat, to_user=user_id, msg=msg + " ответ")
    msg_obj_chat.save()

def logout_user(request):
    logout(request)
    request.session['id'] = randomword()
    request.session['msg'] = 0
    return redirect("home")

class SignUpPage(CreateView):
    form_class = RegistrationForm
    template_name = 'guide/signup.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")

class RefPage(TemplateView):
    template_name = "guide/ref.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Реф"
        context["form"] = RefForm
        return context

    def post(self, request, *args, **kwargs):
        refcode = self.request.POST.get("refcode")
        try:

            if not ( self.request.user.id == UserCustomModel.objects.filter(ref_code=refcode)[0].id ):

                UserCustomModel.objects.filter(ref_code=refcode).update(ref=True, discount=20, ref_code="")
                user = UserCustomModel.objects.filter(username=self.request.user.username)
                user.update(ref_signUp=True)
                user.update(msg=int(user[0].msg+5))

        except:
            redirect("error")

        return redirect("home")


def error(request):
    return HttpResponse("Ошибка!")

class PesonalAccount(DetailView):
    model = UserCustomModel
    template_name = "guide/user.html"
    context_object_name = "user"
    pk_url_kwarg = "id"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Личный кабинет"
        return context

class RatePage(ListView):
    model = Rate
    template_name = "guide/rate.html"
    context_object_name = "rate"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Тарифы"
        return context

    def post(self, request, *args, **kwargs):
        if is_ajax(self.request):

            id = self.request.POST.get("id")

        return redirect("home")

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'guide/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Авторизация"
        return context

    def get_success_url(self):
        return reverse_lazy('home')

class GenerateCode(TemplateView):
    template_name = "guide/generate.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Реферальный код"
        context["code"] = self.code
        return context

    def post(self, request, *args, **kwargs):

        UserCustomModel.objects.filter(username=self.request.user.username).update(ref_code=generate_string(8))

        return redirect("user", self.request.user.id)

    def get(self, request, *args, **kwargs):

        try:
            UserCustomModel.objects.filter(id=self.request.user.id).update(ref_code=self.code, date_of_reg_ref=datetime.now())
        except:
            redirect("error")

        return redirect("user", self.request.user.id)

class EditAdmin(CreateView):
    template_name = "guide/editadmin.html"
    form_class = EditAdminForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Админка"
        context["workpiece"] = WorkPiece.objects.all()
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect("home")

def price():
    pass