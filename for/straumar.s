;; A�ger�ir � �endanlega strauma og taylor ra�ir

;; H�fundur: Snorri Agnarsson

;; Fyrir PC-Scheme ver�um vi� a� gefa stream-car og stream-cdr gildi
;; (sleppum n�stu tveimur l�num � MIT-Scheme og DrScheme):
;(define stream-car head)
;(define stream-cdr tail)

;; Fyrir DrScheme:
(define (-1+ n) (- n 1))
(define (1+ n) (+ n 1))
(define-syntax cons-stream
  (syntax-rules ()
    ((cons-stream head tail)
     (cons head (delay tail))
    )
   )
)
(define stream-car car)
(define (stream-cdr s) (force (cdr s)))
;; Lok kafla fyrir DrScheme

;; Notkun: einn
;; Gildi:  straumurinn [1 1 ...]
(define einn
    (letrec ((einn (cons-stream 1 einn)))
        einn
    )
)

;; Notkun: (stream-map f s)
;; Fyrir:  f er einundara�ger�, s=[s1 s2 ...] er �endanlegur
;;         straumur vi�fanga � f
;; Gildi:  �endanlegi straumurinn [(f s1) (f s2) ...]
(define (stream-map f s)
    (cons-stream (f (stream-car s)) (stream-map f (stream-cdr s)))
)

;; Notkun: (stream-binop f x y)
;; Fyrir:  f er tv�undara�ger�, x=[x1 x2 ...] og y=[y1 y2 ...]
;;         eru �endanlegir straumar fyrri og seinni vi�fanga � f
;; Gildi:  �endanlegi straumurinn [(f x1 y1) (f x2 y2) ...]
(define (stream-binop + x y)
    (cons-stream 
        (+ (stream-car x) (stream-car y))
        (stream-binop + (stream-cdr x) (stream-cdr y))
    )
)

;; Notkun: heil
;; Gildi:  �endanlegi straumurinn [1 2 3 ...]
(define heil
    (letrec ((temp (cons-stream 1 (stream-map 1+ temp))))
        temp
    )
)

;; Notkun: (stream-list x n)
;; Fyrir:  x=[x1 x2 ...] er straumur af lengd a.m.k. n, n er heiltala >=0
;; Gildi:  listinn (x1 x2 ... xn)
(define (stream-list x n)
	(if (= n 0)
		'()
		(cons (stream-car x) (stream-list (stream-cdr x) (-1+ n)))
	)
)

;; Notkun: fibo
;; Gildi:  �endanlegur straumur Fibonacci talna: [1 1 2 3 5 8 ...]
(define fibo
	(cons-stream 1
	    (cons-stream 1
            (stream-binop + fibo (stream-cdr fibo))
        )
    )
)

;; Notkun: fact
;; Gildi:  �endanlegur straumur hr�pmerktra talna: [0! 1! 2! ...]
(define fact
    (cons-stream 1 (stream-binop * fact heil))
)

;; Eftirfarandi kafli �tf�rir �endanlegar Taylor ra�ir.
;; Taylor r��in a_0+a_1*x+a_2*x^2+... er t�knu� me� straumnum
;; [a_0 a_1 ...]

;; Notkun: taylor-zero
;; Gildi:  Taylor r��in fyrir n�ll falli�: 0+0x+0x^2+...
(define taylor-zero
    (letrec ((temp (cons-stream 0 temp))) temp)
)

;; N� viljum vi� f� fall sem tegrar Taylor ra�ir, me� eftirfarandi
;; l�singu:

;; Notkun: (taylor-integrate c s)
;; Fyrir:  c er tala, s er Taylor r��
;; Gildi:  Taylor r��in fyrir c + tegri� af s fr� 0 til x

;; Eftirfarandi er e.t.v. fyrsta �tf�rslan � sl�ku falli, sem okkur
;; dettur � hug, en �essi �tf�rsla hefur �ann galla a� ekki er h�gt
;; a� tegra fall fyrr en b�i� er a� skilgreina �a� (e�a a.m.k. fyrsta
;; li�inn � �v�.
;(define (taylor-integrate c s)
;    (cons-stream c (stream-binop / s heil))
;)
;; �a� sem vi� viljum er �tf�rsla �.a. seg�in (taylor-integrate c s)
;; s� jafngilt seg�inni (cons-stream c (stream-binop / s heil)),
;; fyrir hva�a Taylor seg� s og t�lu s sem er.
;; Vandam�li� er a� �etta er �� ekki h�gt a� �tf�ra sem venjulegt
;; fall, �v� venjulegt fall myndi gilda seg�ina s ��ur en kalla�
;; er � taylor-integrate.
;; Vi� getum leyst m�li� me� �v� a� skilgreina fj�lva:

;; Notkun: (taylor-integrate x s)
;; Fyrir:  c er tala, s er seg�, sem skilar Taylor r��
;; Gildi:  Taylor r��in fyrir c + tegri� af s fr� 0 til x
;; Aths.:  s �arf ekki a� skila gildi fyrr en reikna�ur
;;         er halinn � �tkomunni


;; �essi �tg�fa er fyrir DrScheme:
(define-syntax taylor-integrate
  (syntax-rules ()
    ((taylor-integrate c s)
     (cons-stream c (stream-binop / s heil))
    )
   )
)

;; �essi �tg�fa er fyrir MIT-Scheme:
;(define-syntax taylor-integrate 
;    (lambda (c s)
;        `(cons-stream ,c (stream-binop / ,s heil))
;    )
;)

;; �essi �tg�fa er fyrir PC-Scheme:
;(macro taylor-integrate
;    (lambda (form)
;        (let ((c (cadr form)) (s (caddr form)))
;            `(cons-stream ,c (stream-binop / ,s heil))
;        )
;    )
;)

;; Vi� skilgreinum n� nokkrar Taylor ra�ir me� gagnkv�mri tegrun.
;; Fyrstu fj�rar eru me� brotastu�lum � �eim afbrig�um af Scheme,
;; sem bj��a upp � �a� (t.d. MIT-Scheme), en me� fleytit�lustu�lum
;; � ��rum (t.d. PC-Scheme).

;; Notkun: taylor-sin
;; Gildi:  Taylor r��in fyrir sin
(define taylor-sin (taylor-integrate 0 taylor-cos))

;; Notkun: taylor-cos
;; Gildi:  Taylor r��in fyrir cos
(define taylor-cos (taylor-integrate 1 taylor-msin))

;; Notkun: taylor-msin
;; Gildi:  Taylor r��in fyrir -sin
(define taylor-msin (taylor-integrate 0 taylor-mcos))

;; Notkun: taylor-mcos
;; Gildi:  Taylor r��in fyrir -cos
(define taylor-mcos (taylor-integrate -1 taylor-sin))

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

;; Notkun: (taylor-eval f x n)
;; Fyrir:  f er Taylor r��, x er tala, n er heiltala >=0
;; Gildi:  Summa fyrstu n li�a Taylor ra�arinnar me� gefnu gildi x
(define (taylor-eval f x n)
    (if (= n 0)
        0
        (+ (stream-car f) (* x (taylor-eval (stream-cdr f) x (-1+ n))))
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
