(define lst1 (list 'a 'b 'c "Easy as" 1 2 3))
(cdr lst1)
(car lst1)

(define (rev2 x)
  (define (snusk x y)
    (if (null? x)
        y
        (snusk (cdr x) (cons (car x) y))
        )
    )
  (snusk x '())
  )



;; Notkun: (fibo n)
;; Fyrir: n er heiltala . >=0
;; Gildi: n-ta Fibonacci talan
(define (fibo n)
  ;; Notkun: (hjalp f1 f2 i)
  ;; Fyrir: 0 <= i <= n,
  ;;        f1 er i-ta Fibonacci talan,
  ;;        f2 er (i+1)-ta Fibonacci talan,
  ;; Gildi: n-ta Fibonacci talan.
  (define (hjalp f1 f2 i)
    (if (= i n)
        f1
        (hjalp f2 (+ f1 f2) (+ i 1))
        )
    )
  ;; stofn fallsins fibo:
  (hjalp 1 1 0)
  )

(define (sum x)
  (if (= x 0)
      0
      (+ x (sum (- x 1)))
      )
  )
;; 2 hopverkefni, tekur lista (x1 ...xn) og skilar (x1^2 ..... x2^2) 
(define l (list 1 2 3 4 5 6 7 8 9 10))

(define (xx  x )
            (* x x)
            )
  

;;(define (sqr (x))
  ;;(lambda (x)(* x x))
  ;;)

(define (addy y)
  (lambda(x) (+ y x))
  )
(define (addx x)
  (lambda (j) (map (+ x j) j))
  )

(define (addLy y)
  (lambda (s) (map (addy y) s))
  )

(define (swt x y)
  (lambda (z) (if (< 1 2) x y))
  )
(define (sumfun f l)
  (map f l)
  )

(define (sumfun2 f l)
  (define (hjlp f l s)
    (if (null? l)
        s
        (hjlp f (cdr l) (+ s (f (car l))))
        )
    
    )
  (hjlp f l 0)
  )
