from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario


def index(request):
    return render(request, 'index.html')


def login(request):

    mensaje = ""

    if request.method == 'POST':

        correo = request.POST['correo']
        password = request.POST['password']

        try:

            usuario = Usuario.objects.get(
                correo=correo,
                password=password
            )

            return render(
                request,
                'inicio.html',
                {
                    'usuario': usuario
                }
            )

        except Usuario.DoesNotExist:

            mensaje = "Usuario o contraseña incorrectos"

    return render(
        request,
        'login.html',
        {
            'mensaje': mensaje
        }
    )


def registro(request):

    if request.method == 'POST':

        correo = request.POST['correo']

        if Usuario.objects.filter(correo=correo).exists():

            return render(
                request,
                'registro.html',
                {
                    'formulario': UsuarioForm(),
                    'mensaje': 'El correo ya se encuentra registrado'
                }
            )

        formulario = UsuarioForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            return redirect('login')

    formulario = UsuarioForm()

    return render(
        request,
        'registro.html',
        {
            'formulario': formulario
        }
    )