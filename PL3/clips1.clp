(deffunction dentroDelRango (?a ?b)
    (bind ?c (read))
    (while (not(and(< ?a ?c)(< ?c ?b)))
        (printout t "No está en el rango" crlf)
        (bind ?c (read))
    )
    (printout t "Está en el rango" crlf)
)
(deffunction mcd (?a ?b)
    (if (eq ?a ?b) then
        (printout t ?a crlf)
        (return ?a)
    else (if (< ?a ?b) then
        (return (mcd ?a (- ?b ?a))))
    else (if (< ?b ?a) then
        (return (mcd (- ?a ?b) ?b)))
    )
)
(deffunction mcm (?a ?b)
    (printout t (/ (* ?a ?b) (mcd ?a ?b)) crlf)
)
(deffunction ascendente ($?list)
    (bind ?out (create$))
    (bind ?size (length$ ?list))
    (foreach ?i $?list
        (if (eq ?size 0) then
            (bind ?out (insert$ ?out (+ ?size 1) ?i))
        else
            (bind ?int 0)
            (foreach ?j $?out
                (if (> ?j ?i) then
                    (break)
                )
                (bind ?int (+ ?int 1))
            )
            (bind ?out (insert$ ?out (+ ?int 1) ?i))
        )
    )
)
(deffunction ascendentePar ($?list)
    (bind ?out (create$))
    (bind ?size (length$ ?list))
    (foreach ?i $?list
        (if (= (mod ?i 2) 0) then
            (if (eq ?size 0) then
                (bind ?out (insert$ ?out (+ ?size 1) ?i))
            else
                (bind ?int 0)
                (foreach ?j $?out
                    (if (> ?j ?i) then
                        (break)
                    )
                    (bind ?int (+ ?int 1))
                )
                (bind ?out (insert$ ?out (+ ?int 1) ?i))
            )
        )
    )
)
(deffunction diferencia (?in $?in2)
    (bind ?index 1)
    (foreach ?i ?in
        (bind ?found 0)
        (foreach ?j $?in2
            (if (eq ?i ?j) then
                (bind ?found 1)
                (break)
            )
        )
        (if (= ?found 1) then
            (bind ?in (delete$ ?in ?index ?index))
            (bind ?index (- ?index 1))
        )
        (bind ?index (+ ?index 1))
    )
    (return ?in)
)
(deffunction concatenacion (?in $?in2)
    (insert$ ?in (+ (length$ ?in) 1) $?in2)
)
(deffunction cartesiano (?in $?in2)
    (bind ?out (create$))
    (foreach ?i ?in
        (foreach ?j $?in2
            (bind ?out (insert$ ?out (+ (length$ ?out) 1) ?i ?j))
        )
    )
    (return $?out)
)

(deffunction esPrimo(?n)
    (bind ?i 2)
    (while (and (< ?i ?n)(not(= (mod ?n ?i) 0)))
        (bind ?i (+ ?i 1))
    )
    (if (eq ?i ?n) then
        (return TRUE)
    else
        (return FALSE)
    )
)

(deffunction esCapicua(?n)
    (bind ?n2 ?n)
    (bind ?n3 0)
    (while (> ?n2 0)
        (bind ?n3 (+ (* ?n3 10) (mod ?n2 10)))
        (bind ?n2 (div ?n2 10))
    )
    (if (eq ?n ?n3) then
        (return TRUE)
    else
        (return FALSE)
    )
)

(deffunction num_primos_y_capicua()
    (bind ?n (read))
    (bind ?i 1)

    (while (< ?i ?n)
        (if (and (esPrimo ?i)(esCapicua ?i)) then
            (printout t ?i crlf)
        )
        (bind ?i (+ ?i 1))
    )
)

(deffunction esMedio(?n)
    (bind ?sumInferiores 0)
    (bind ?i 1)
    (while (< ?i ?n)
        (bind ?sumInferiores (+ ?sumInferiores ?i))
        (bind ?i (+ ?i 1))
    )
    (bind ?sumSuperiores 0)
    (bind ?i (+ ?n 1))
    (while (< ?sumSuperiores ?sumInferiores)
        (bind ?sumSuperiores (+ ?sumSuperiores ?i))
        (bind ?i (+ ?i 1))
    )
    (if (eq ?sumSuperiores ?sumInferiores) then
        (return TRUE)
    else
        (return FALSE)
    )
)