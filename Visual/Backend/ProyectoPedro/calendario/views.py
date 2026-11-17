from datetime import datetime

from django.shortcuts import redirect, render


MESES = (
    'enero',
    'febrero',
    'marzo',
    'abril',
    'mayo',
    'junio',
    'julio',
    'agosto',
    'septiembre',
    'octubre',
    'noviembre',
    'diciembre',
)


def inicio(request):
    if request.method == 'GET' and 'fecha' in request.GET:
        fecha = request.GET['fecha']
        if fecha:
            return redirect('calendario:fecha', fecha=fecha)
        return render(
            request,
            'calendario/inicio.html',
            {'error': 'Escribe una fecha para continuar.'},
            status=400,
        )

    return render(request, 'calendario/inicio.html')


def calendario(request, fecha):
    try:
        fecha_parseada = datetime.strptime(fecha, '%d-%m-%Y')
    except ValueError:
        fecha_parseada = None

    if fecha_parseada is None or fecha_parseada.strftime('%d-%m-%Y') != fecha:
        return render(
            request,
            'calendario/error.html',
            {'fecha': fecha},
            status=400,
        )

    mes = MESES[fecha_parseada.month - 1]
    return render(
        request,
        'calendario/fecha.html',
        {
            'dia': fecha_parseada.day,
            'mes': mes,
            'ano': fecha_parseada.year,
            'mensaje': 'La fecha se ha interpretado correctamente.',
        },
    )
