(define (-1+ n) (- n 1))
(define (1+ n) (+ n 1))

(define stream-car car)
(define (stream-cdr x) (force(cdr x)))

(define-syntax cons-stream
  (syntax-rules ()
    ((cons-stream head tail)
     (cons head (delay tail))
    )
   )
)
(define einn
  (letrec  ((einn (cons-stream 1 einn)))
    einn
    )
  )

(define (stream-map f s)
  (cons-stream (f (stream-car s))
               (stream-map f (stream-cdr s))
               )
  )
(define (XX x)
  (* x x)
  )
(define (stream-binop + x y)
  (cons-stream
   (+ (stream-car x) (stream-car y))
   (stream-binop + (stream-cdr x) (stream-cdr y))
   )
  )

(define heil
  (letrec ((temp (cons-stream
                  1
                  (stream-map 1+ temp)
                  )
                 )
           )
    temp
    )
  )

(define (stream-list x n)
  (if (= n 0)
      '()
      (cons (stream-car x)
            (stream-list (stream-cdr x)(-1+ n))
            )
      )
  )
(define factorial
  (lambda (n)
    (let iter ((product 1)
               (counter 1))
      (if (> counter n)
          product
          (iter (* counter product) (+ counter 1))))))

(define fact2
  (lambda (n)
    (letrec ((iter
              (lambda (product counter)
                (if (> counter n)
                    product
                    (iter (* counter product)
                          (+ counter 1))))))
      (iter 1 1)))
  )
(define fibo
  (cons-stream 1
               (cons-stream 1
                            (stream-binop + fibo (stream-cdr fibo))
                            )
               )
  )

(define fact
  (cons-stream 1 (stream-binop * fact heil))
  )


;; Taylor series

(define taylor-zero
  (letrec ((temp (cons-stream 0 temp))) temp)
  )
;; Integration of taylor series
;; �essi �tg�fa er fyrir DrScheme:
(define-syntax taylor-integrate
  (syntax-rules ()
    ((taylor-integrate c s)
     (cons-stream c (stream-binop / s heil))
    )
   )
)
;taylor sin
(define taylor-sin
  (taylor-integrate 0 taylor-cos)
  )
;taylor-cos
(define taylor-cos
  (taylor-integrate 1 taylor-msin)
  )
;taylor minus sin
(define taylor-msin
  (taylor-integrate 0 taylor-mcos)
  )
;taylor minus cos
(define taylor-mcos
  (taylor-integrate -1 taylor-sin)
  )
;; N�stu fj�rar eru svipa�ar, en stu�larnir eru alltaf fleytit�lur

(define taylor-sinf (taylor-integrate 0.0 taylor-cosf))
(define taylor-cosf (taylor-integrate 1.0 taylor-msinf))
(define taylor-msinf (taylor-integrate 0.0 taylor-mcosf))
(define taylor-mcosf (taylor-integrate -1.0 taylor-sinf))
;; Notkun: (taylor-diff s)
;; Fyrir:  s er Taylor r��
;; Gildi:  Taylor r��in fyrir diffurkv�ta s
(define (taylor-diff s)
    (stream-binop * (stream-cdr s) heil)
)
;; Notkun: (taylor+ a b)
;; Fyrir:  a og b eru Taylor ra�ir e�a t�lur
;; Gildi:  Taylor r��in fyrir a+b, e�a talan a+b ef b��ar eru t�lur
(define (taylor+ x y) 
    (if (number? x)
        (if (number? y)
            (+ x y)
            (cons-stream (+ x (stream-car y)) (stream-cdr y))
        )
        (if (number? y)
            (cons-stream (+ (stream-car x) y) (stream-cdr x))
            (stream-binop + x y)
        )
    )
)

;; Notkun: (taylor- a b)
;; Fyrir:  a og b eru Taylor ra�ir e�a t�lur
;; Gildi:  Taylor r��in fyrir a-b, e�a talan a-b ef b��ar eru t�lur
(define (taylor- x y)
    (if (number? x)
        (if (number? y)
            (- x y)
            (taylor- (cons-stream x taylor-zero) y)
        )
        (if (number? y)
            (cons-stream (- (stream-car x) y) (stream-cdr x))
            (stream-binop - x y)
        )
    )
)
;tayllor-eval
(define (taylor-eval f x n)
  (if (= n 0)
      0
      (+ (stream-car f)
         (* x (taylor-eval (stream-cdr f)
                           x
                           (-1+ n)
                           )
            )
         )
      )
  )
;; Notkun: (taylor* a b)
;; Fyrir:  a og b eru Taylor ra�ir e�a t�lur
;; Gildi:  Taylor r��in fyrir a*b, e�a talan a*b ef b��ar eru t�lur
(define (taylor* x y)
    ;; Notkun: (taylor* a b)
    ;; Fyrir:  a og b eru Taylor ra�ir
    ;; Gildi:  Taylor r��in fyrir a*b
    (define (help x y)
        (taylor+
            (taylor* (stream-car x) y)
            (cons-stream 0 (taylor* (stream-cdr x) y))
        )
    )
    (if (number? x)
        (if (number? y)
            (* x y)
            (stream-map (lambda (y) (* x y)) y)
        )
        (if (number? y)
            (stream-map (lambda (x) (* x y)) x)
            (help x y)
        )
    )
)

;; Notkun: (taylor/ a b)
;; Fyrir:  a og b eru Taylor ra�ir e�a t�lur
;;         b m� ekki vera n�ll, og a ver�ur a� hafa a.m.k. jafn
;;         marga n�ll li�i fremst og b
;; Gildi:  Taylor r��in fyrir a/b, e�a talan a/b ef b��ar eru t�lur
(define (taylor/ x y)
    ;; Notkun: (help a b)
    ;; Fyrir:  a og b eru Taylor ra�ir
    ;;         a ver�ur a� hafa a.m.k. jafn marga n�ll li�i fremst og b
    ;; Gildi:  Taylor r��in fyrir a/b
    (define (help x y)
        (if (= (stream-car y) 0)
            (if (= (stream-car x) 0)
                (help (stream-cdr y) (stream-cdr x))
                (/ 0 (stream-car x))
            )
            (let
                (
                    (z0 (/ (stream-car x) (stream-car y)))
                )
                (cons-stream
                    z0
                    (help (taylor- (stream-cdr x) (taylor* z0 (stream-cdr y))) y)
                )
            )
        )
    )
    (if (number? y)
        (if (number? x)
            (/ x y)
            (stream-map (lambda (x) (/ x y)) x)
        )
        (if (number? x)
            (help (cons-stream x taylor-zero) y)
            (help x y)
        )
    )
)
;; Notkun: taylor-x
;; Gildi:  Taylor r��in fyrir falli� f(x)=x
(define taylor-x
    (cons-stream 0 (cons-stream 1 taylor-zero))
)

;; Notkun: taylor-ln_1+x
;; Gildi:  Taylor r��in fyrir falli� f(x)=ln(1+x)
(define taylor-ln_1+x
    (taylor-integrate 0 (taylor/ 1 (taylor+ 1 taylor-x)))
)

;; Notkun: taylor-exp
;; Gildi:  Taylor r��in fyrir falli� exp
(define taylor-exp (taylor-integrate 1 taylor-exp))


;; Notkun: taylor-tan
;; Gildi:  Taylor r��in fyrir falli� tan (brotastu�lar ef Scheme
;;         r��ur vi� �a�)
(define taylor-tan (taylor/ taylor-sin taylor-cos))

;; Notkun: taylor-tanf
;; Gildi:  Taylor r��in fyrir falli� tan (fleytit�lustu�lar)
(define taylor-tanf (taylor/ taylor-sinf taylor-cosf))

;; Notkun: (taylor-compose f g)
;; Fyrir:  f og g eru Taylor ra�ir, g(0)=0
;; Gildi:  Taylor r��in fyrir falli� f o g
(define (taylor-compose f g)
    (if (= (stream-car g) 0)
        (cons-stream
            (stream-car f)
            (taylor* (stream-cdr g) (taylor-compose (stream-cdr f) g))
        )
        (/ 1 0)
    )
)

;; Notkun: (taylor-general-inverse f g)
;; Fyrir:  f og g eru Taylor ra�ir, g(0)=0
;; Gildi:  Taylor r�� fyrir fall h �.a. h o g = f
(define (taylor-general-inverse f g)
    (if (= (stream-car g) 0)
        (cons-stream
            (stream-car f)
            (taylor-general-inverse
                (taylor/ (stream-cdr f) (stream-cdr g))
                g
            )
        )
        (/ 1 0)
    )
)

;; Notkun: (taylor-inverse f)
;; Fyrir:  f er Taylor r��, f(0)=0
;; Gildi:  Taylor r�� fyrir andhverfa falli� vi� f,
;;         �.e.fall h �.a. h o f = x = f o h
(define (taylor-inverse f)
    (taylor-general-inverse taylor-x f)
)

;; Notkun: taylor-asin
;; Gildi:  Taylor r��in fyrir andhverfa falli� vi� sin
;;         me� brotastu�lum ef Scheme r��ur vi� �a�,
;;         annars fleytit�lustu�lum
(define taylor-asin (taylor-inverse taylor-sin))

;; Notkun: taylor-asinf
;; Gildi:  Taylor r��in fyrir andhverfa falli� vi� sin
;;         me� fleytit�lustu�lum
(define taylor-asinf (taylor-inverse taylor-sinf))

;; Notkun: taylor-atan
;; Gildi:  Taylor r��in fyrir andhverfa falli� vi� tan
;;         me� brotastu�lum ef Scheme r��ur vi� �a�,
;;         annars fleytit�lustu�lum
(define taylor-atan (taylor-inverse taylor-tan))

;; Notkun: taylor-atanf
;; Gildi:  Taylor r��in fyrir andhverfa falli� vi� tan
;;         me� fleytit�lustu�lum
(define taylor-atanf (taylor-inverse taylor-tanf))

(define f (taylor-integrate 2 (taylor* 2 f)))



;; 1
(define (sumsum n)
  (define (h  s1 s2 i)
    (if (= i n)
        s2
        (h (+ s1 1 i)(+ s2 s1 i 1)(+ 1 i))
           )
        )
    (h 0 0 0)
    )
 

;; 2
;; f'(x)=-f
;; f(0)=1, f'(0) = -1


(define g
  (taylor-integrate 1(taylor- taylor-zero g))
  )



;; 3.
;; 2^i
(define (XX x)
            (* x x)
  )

            

(define g
  (cons-stream 2 (stream-map XX g))
)  

(define s
  (cons-stream 1 (stream-map (lambda (x) (* 2 x)) s))
  )

(define (heil+strm x)
  (stream-binop + heil x)
  )