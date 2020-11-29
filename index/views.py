from django.shortcuts import render
from . models import Musico, Mensaje
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    

    num_Musicos = Musico.objects.all().count()
    num_Mensajes = Mensaje.objects.all().count()
    mensajes_enviados = Mensaje.objects.filter(usuario="seba_123").values()
    mensajes_recibidos = Mensaje.objects.all().values_list()

    return render(
        request,
        'index.html',
        context={'num_musicos': num_Musicos, 'num_mensajes': num_Mensajes, 'men_enviados': mensajes_enviados, 'men_recibidos': mensajes_recibidos, 
        },

        
    )

def perfil(request):
    

    num_Musicos = Musico.objects.all().count()
    num_Mensajes = Mensaje.objects.all().count()


    return render(
        request,
        'perfil.html',
        context={'num_musicos': num_Musicos, 'num_mensajes': num_Mensajes, 
        },

        
    )  

def buscar(request):
    

    num_Musicos = Musico.objects.all().count()
    num_Mensajes = Mensaje.objects.all().count()


    return render(
        request,
        'buscar.html',
        context={'num_musicos': num_Musicos, 'num_mensajes': num_Mensajes, 
        },

        
    )            

def registro(request):
    

    num_Musicos = Musico.objects.all().count()
    num_Mensajes = Mensaje.objects.all().count()


    return render(
        request,
        'registro.html',
        context={'num_musicos': num_Musicos, 'num_mensajes': num_Mensajes, 
        },

        
    ) 


def mensajes(request):
    
    mensajes_enviados = Mensaje.objects.filter(usuario='seba_123').values_list()
    mensajes_recibidos = Mensaje.objects.all().values()


    return render(
        request,
        'mensajes.html',
        context={'men_enviados': mensajes_enviados, 'men_recibidos': mensajes_recibidos, 
        },

        
    )  
    
def admin(request):
    

    num_Musicos = Musico.objects.all().count()
    num_Mensajes = Mensaje.objects.all().count()


    return render(
        request,
        'admin.html',
        context={'num_musicos': num_Musicos, 'num_mensajes': num_Mensajes, 
        },

        
    )    

       

class CrearMusico(CreateView):
    model = Musico
    fields = '__all__'
    success_url = reverse_lazy('index')

class ActualizarMusico(UpdateView):
    model = Musico
    fields = '__all__'
    success_url = reverse_lazy('index')

class EliminarMusico(DeleteView):
    model = Musico
    success_url = reverse_lazy('index')

class ConsultarMusico(generic.DetailView):
    model=Musico   

 
class CrearMensaje(CreateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy('index')

class ActualizarMensaje(UpdateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy('index')

class EliminarMensaje(DeleteView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy('index')

class ConsultarMensaje(generic.DetailView):
    model=Mensaje     



