;; Compute pi to any number of digits
;; Author: Snorri Agnarsson

;; Notkun: (pow x n)
;; Fyrir:  x er tala
;; Gildi:  x^n
(define (pow x n)
  (if (= (modulo n 2) 0)
     (if (= n 0)
       1
       (pow (* x x) (quotient n 2))
     )
     (* x (pow (* x x) (quotient n 2)))
  )
)

;; Athugið að aðferðin byggist á því að Taylor-röðin fyrir atan er:
;; atan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...

;; Notkun: (atanr h x)
;; Fyrir:  h og x eru heiltölur
;; Gildi:  Góð nálgun á h*atan(1/x), fengin með því að leggja saman 
;; alla heiltöluhluta liðanna í Taylor-röðinni fyrir h*atan(1/x)
(define (atanr h x)
  (define x^2 (* x x))
  
  ;; Notkun: (hjalp1 summa hdxi i)
  ;; Fyrir:  i er einhver heiltalnanna 1,5,9,13,...
  ;;         summa, hdxi eru heiltölur, þannig að
  ;;         a) hdxi er heiltöluhlutinn af h*(1/x)^i,
  ;;         b) summa er summa heiltöluhlutanna af
  ;;            h*(1/x) - h*(1/x)^3/3 + ... - h*(1/x)^(i-2)/(i-2) + h*(1/x)^i/i
  ;; Gildi:  summa allra heiltöluhluta óendanlegu Taylor-raðarinnar
  ;;         h*(1/x) - h*(1/x)^3/3 + ... 
  (define (hjalp1 summa h i)
    (if (= h 0)
       summa
       (hjalp2 (- summa (quotient (quotient h x^2) (+ i 2))) (quotient h x^2) (+ i 2))
    )
  )
  ;; Notkun: (hjalp2 summa hdxi i)
  ;; Fyrir:  i er einhver heiltalnanna 3,7,11,15,...
  ;;         summa, hdxi eru heiltölur þannig að
  ;;         a) hdxi er heiltöluhlutinn af h*(1/x)^i
  ;;         b) summa er summa heiltöluhlutanna af
  ;;            h*(1/x) - h*(1/x)^3/3 + ... + h*(1/x)^(i-2)/(i-2) - h*(1/x)^i/i
  ;; Gildi:  summa allra heiltöluhluta óendanlegu Taylor-raðarinnar
  ;;         h*(1/x) - h*(1/x)^3/3 + ... 
  (define (hjalp2 summa h i)
    (hjalp1 (+ summa (quotient (quotient h x^2) (+ i 2))) (quotient h x^2) (+ i 2))
  )
  (hjalp1 (quotient h x) (quotient h x) 1)
)

(define (mypi n)
  (define h (pow 10 (+ n 6)))
  (quotient (* 4 (- (* 4 (atanr h 5)) (atanr h 239))) 1000000)
)
