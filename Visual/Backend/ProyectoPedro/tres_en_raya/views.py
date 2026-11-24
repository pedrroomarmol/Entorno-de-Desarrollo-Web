from django.shortcuts import redirect, render


LINEAS_GANADORAS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def hay_ganador(tablero):
    return any(
        tablero[a] != '-' and tablero[a] == tablero[b] == tablero[c]
        for a, b, c in LINEAS_GANADORAS
    )


def tres_en_raya(request):
    if request.GET.get("reiniciar") == "1":
        request.session["tablero"] = "-" * 9
        request.session["turno"] = "X"
        request.session["mensaje"] = "Turno de X"
        request.session["terminado"] = False
        return redirect("tres_en_raya:juego")

    tablero = request.session.get("tablero", "-" * 9)
    turno = request.session.get("turno", "X")
    mensaje = request.session.get("mensaje", f"Turno de {turno}")
    terminado = request.session.get("terminado", False)
    
    if request.method == 'POST':
        tablero_enviado = tablero
        turno_enviado = turno

        if (
            len(tablero_enviado) == 9
            and set(tablero_enviado) <= {'-', 'X', 'O'}
            and turno_enviado in {'X', 'O'}
            and not hay_ganador(tablero_enviado)
            and '-' in tablero_enviado
        ):
            tablero = tablero_enviado
            turno = turno_enviado
            try:
                posicion = int(request.POST.get('posicion', '-1'))
            except (TypeError, ValueError):
                posicion = -1

            if 0 <= posicion < 9 and tablero[posicion] == '-':
                tablero = tablero[:posicion] + turno + tablero[posicion + 1:]

                if hay_ganador(tablero):
                    terminado = True
                    mensaje = f'¡Ha ganado {turno}!'
                elif '-' not in tablero:
                    terminado = True
                    mensaje = 'Empate'
                else:
                    turno = 'O' if turno == 'X' else 'X'
                    mensaje = f'Turno de {turno}'

                request.session["tablero"] = tablero
                request.session["turno"] = turno
                request.session["mensaje"] = mensaje
                request.session["terminado"] = terminado

    return render(
        request,
        'tres_en_raya/tres_en_raya.html',
        {
            'tablero': tablero,
            'turno': turno,
            'mensaje': mensaje,
            'terminado': terminado,
        },
    )
