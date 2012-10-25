;; hópverkefni
;; búum til lista til að vinna með
(define l (list 1 2 3 4 5 6 7 8 9 10))
;; og svo fall sem hefur upp viðfang sitt í annað veldi
(define (xx x)
  (* x x)
)
;; Notum svo map fallið sem er innbyggt til að hefja allt í
;; listanum l upp í annað veldi
>(map xx l)
(1 4 9 16 25 36 49 64 81 100)
;; 3. Skrifi[ Scheme fall sem tekut tolu sem vidfang og skilar falli sem 
;; tekur lista (x1 . .... xN)  sem vidfang og skilar listanum
;;  (y + x1 ... ... . y + xN)
;; Skilgr fyrst hjalparfall addy sem skilar falli sem baetir vid y
(define (addy y)
  (lambda(x) (+ y x))
)
;; notum thad sidan i adalfallinu addLy
(define (addLy y)
  (lambda (s) (map (addy y) s))
)
;; ath map tekur fall sem fyrsta vidfang, th.a. addLy
;; tekur y sem vidfang og skilar falli sem tekur lista
;; sem vidfang
>((addLy 3) l)
(4 5 6 7 8 9 10 11 12 13)
;; hópverkefni
;; 4. Fall sem tekur tvö viðföng x o z og skilar falli sem 
;; tekur gildi z sem viðfang og og skilar x ef z er #t og y
;; ef z er #f
;; eftirfarandi fall swt tekur 2 vidfong og skilar falli
(define (swt x y)
  (lambda (z) (if (< 1 2) x y))
)
;;notkun
>((swt 7 6)#t)
7
;; Einstaklingsverkefni
;; sumfun2 tekur 2 vidfong fall f og talnalista l, og
;; framkvaemir fallid a ollum stokunum og sumerar sidan
;; up og kemur med eina tolu 
(define (sumfun2 f l)
  (define (hjlp f l s)
    (if (null? l)
        s
        (hjlp f (cdr l) (+ s (f (car l))))
        )
    
    )
  (hjlp f l 0)
  )
;; Notkunardaemi
> (sumfun2 (lambda (x) (* x x)) '(1 2 3))
14

