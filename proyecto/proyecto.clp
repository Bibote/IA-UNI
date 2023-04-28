(deffacts init "
    turno
    fichas negativas en casa
    estado del tablero
    fichas positivas en casa
    fichas positivas comidas
    fichas negativas comidas
    dados
    "
    (tablero 
        (random 0 1)
        0
        2 0 0 0 0 -5     0 -3 0 0 0 5
        -5 0 0 0 3 0     5 0 0 0 0 -2
        0
        0
        0
        (random 1 6) (random 1 6)
    )
)
