from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Flan, ContactForm
from .forms import Formulario_Contacto,ContactFormForm
# Create your views here.

def flanes_publicos(request):
    flanes = Flan.objects.filter(is_private = False)
    context = {"flanespublic": flanes}
    return render(request, 'flanespublicos.html', context)

@login_required
def flanes_privados(request):
    flanes = Flan.objects.filter(is_private = True)
    context = {"flanes": flanes}
    return render(request, 'flanescard.html', context)

def log_in(request):
    template = loader.get_template('login.html')
    context = {'form':AuthenticationForm}
    if request.method == "GET":
        return HttpResponse(template.render(context, request))
    else:
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate( request, username=usuario, password=clave)
        if user is None:
            context["error"] = "Usuario o contraseña incorrectos"
            return HttpResponse(template.render(context, request))
        else:
            login(request, user)
            return HttpResponseRedirect('/flanesprivados/')
        
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def exito(request):
    return render(request, 'exito.html',{})

def contacto(request):
    if request.method == "POST":
        try:
            form =ContactFormForm(request.POST)
            if form.is_valid():
                ## crea el nuevo formulario de contacto usando el formulario personalizado
                ## por eso se hace a través del método create 
                ## no nativamente como se hace con save() cuando el objeto proviene directamente del modelo
                nuevo_form = ContactForm.objects.create(**form.cleaned_data)
                ## se cargar el templato exito para evitar hacer el redirect 
                template = loader.get_template('exito.html')
                # el render carga la página exito pero sin cambiar la url
                # hacer redirect implica tener la URL registrada
                return HttpResponseRedirect('/exito/')
                return HttpResponse(template.render({}, request))
        except ValueError:
            template = loader.get_template('contactus.html')
            context = {'form':form, 'error':"Error al procesar el formulario"}
            return HttpResponse(template.render(context, request))
    else:
        form = ContactFormForm()
        return render(request, "contactus.html", {"form":form}) 