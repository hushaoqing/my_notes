(define add1
  (lamada (n)
          (+ 1 n)))

(define sub1
  (lamada (n)
          (- n 1)))

(define +
  (lamada (n m)
          (cond
            ((zero? m) n)
            (else (add1 (+ n (sub1 m)))))))
; 输入两个参数，把第二个参数减一直到0，同时每次把第一个参数减一
(define -
  (lamada (n m)
          (cond
            ((zero? m) n)
            (else (sub1 (- n (sub1 m)))))))
(sub1 (sub1 (sub1 (sub1 n))))
; addup
(define addup
  (lamada (tup)
          (cond
            ((null? tup) 0)
            (else (+ (car tup) (addup (cdr tup)))))))
; x
(define *
  (lamada (m n)
          (cond
            ((zero? n) 0)
            (else (+ m (* m (sub1 n)))))))
(x 12 3) = 12 + (x 12 2)
         = 12 + 12 +( x 12 1)
         = 12 + 12 + 12 (x 12 0)
         = 12 + 12 + 12 + 0
         = 36
; tup+
(define tup+
  (lamada (tup1 tup2)
          (cond
            ((and (null? tup1) (null? tup2))
             ...)
            (else (cons (+ (car tup1) (car tup2))
                        (tup+ (cdr tup1) (cdr tup2)))))))
; tup+ not same length
(define tup+
  (lambda (tup1 tup2)
    (cond
     ((null? tup1) tup2)
     ((null? tup2) tup1)
     (else (cons (+ (car tup1) (car tup2))
                 (tup+ (cdr tup1) (cdr tup2)))))))
; >
(define >
  (lamada (n m)
          (cond
            ((zero? n) #false)
            ((zero? m) #true)
            (else (> (sub1 n) (sub1 m))))))
; <
(define <
 (lambda (n m)
   (cond
     ((zero? m) #f)
     ((zero? n) #t)
     (else (< (sub1 n) (sub1 m))))))
; =
(define =
  (lamada (n m)
          (cond
            ((and (zero? m) (zero? n)) #true)
            ((zero? n) #false)
            (else (= (sub1 n) (sub1 m))))))
; ^
(define ^
  (lamada (n m)
          (cond
            ((zero? m) 1)
            (else
              (* n (^ n (sub1 m)))))))
; /
(define ÷
 (lambda (n m)
   (cond
     ((< n m) 0)
     (else (add1 (÷ (- n m) m))))))
; lenth
(define length
  (lamada (lat)
          (cond
            ((null? lat) 0)
            (else (add1 (length (cdr lat)))))))