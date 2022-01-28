from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from usuario.forms import Autor, AutorForm



def home(request):
    autores = Autor.objects.all()

    context = {
        'autores':autores
    } 

    return render(request, 'home.html', context)  


def autor(request):  
    
    form = AutorForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/auth/home/') 

    context = {
        'form':form
    }
    return render(request,'autor.html',context) 



def editar(request,id):
    autor = Autor.objects.get(id=id)

    form = AutorForm(request.POST or None, instance=autor) #pegue o formulario # se não colocar esse none ele não consegue pegar os valores já existentes, se não colocar vem zazio

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/auth/home/')  
            
    context ={
        'form':form
    }


    return render(request,'altera.html',context) 


def delete(request,id):
    autor = Autor.objects.get(id=id)
    autor.delete() 
    return redirect('/auth/home/')  

