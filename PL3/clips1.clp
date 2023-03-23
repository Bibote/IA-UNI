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