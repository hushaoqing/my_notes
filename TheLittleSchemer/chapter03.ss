; rember 删除lat中的第一个和参数a相同的原子
(define remebr
  (lamada (a lat)
          (cond
            ((null? lat) '())
            (else (cond
                    ((eq? a (car lat)) (cdr lat))
                    (else (remebr a (cdr lat))))))))
; cons
(define remebr
  (lamada (a lat)
          (cond
            ((null? lat) '())
            (else (cond
                    ((eq? a (car lat)) (cdr lat))
                    (else (cons (car lat) (remebr a (cdr lat)))))))))
; rember simplify
(define remebr
  (lamada (a lat)
          (cond
            ((null? lat) '())
            ((eq? a (car lat)) (cdr lat))
            (else (cons (car lat) (remebr a (cdr lat)))))))
; firsts 函数输入一个lists表参数，null空表，或者只包含非空表。它抽取list表中每一个成员的第一个 S-expression表达式构建新的list表。
(define firsts
  (lamada (l)
          (cond
            ((null? l) ...)
            (else (cons (car (car l)) (firsts (cdr l)))))))
; insertR 它有三个参数：atom原子new和old，还有一个列表lat。函数insertR把new插入到第一个old后边创建一个lat。
(define insertR
  (lamada (new old lat)
          (cond
            ((null? lat) ...)
            (else (cond
                    ((eq? old (car lat))
                     (cons old (cons new (cdr lat))))
                    (else (cons (car lat) (insertR new old (cdr lat)))))))))
; insertL 把new原子插入到lat中的第一个old的左边
(define insertL
  (lamada (new old lat)
          (cond
            ((null? lat) ...)
            (else (cond
                    ((eq? old (car lat))
                     (cons new lat)
                    (else (cons (car lat) (insertL new old (cdr lat))))))))))
; subst (subst new old lat)用new替换lat中的第一个old
(define subst
  (lamada (new old lat)
          (cond
            ((null? lat) ...)
            (else (cond
                    ((eq? old (car lat))
                     (cons new (cdr lat))
                    (else (cons (car lat) (subst new old (cdr lat))))))))))
; subst2 把lat中第一个出现的o1或者第一个出现的o2替换为new
(define subst2
  (lamada (new o1 o2 lat)
          (cond
            ((null? lat) ...)
            (else (cond
                    ((or (eq? o1 (car lat))
                         (eq? o2 (car lat)))
                     (cons new (cdr lat))
                    (else (cons (car lat) (subst2 new old (cdr lat))))))))))
; multirember 把lat中所有的a都删除
(define multirember
  (lamada (a lat)
          (cond
            ((null? lat) '())
            ((eq? a (car lat))
             (multirember a (cdr lat)))
            (else (cons (car lat) (multirember a (cdr lat)))))))
; multiinsertR
(define multiinsertR
  (lamada (new old lat)
          (cond
            ((null? lat) ...)
            (else (cond
                    ((eq? old (car lat))
                     (cons (car lat) (cons new (multiinsertR new old (cdr lat))))
                    (else (cons (car lat) (multiinsertR new old (cdr lat))))))))))
; multiinsertL
(define multiinsertL
  (lamada (new old lat)
          (cond
            ((null? lat) ...)
            (else (cond
                    ((eq? old (car lat))
                     (cons new (cons old (multiinsertL new old (cdr lat))))
                    (else (cons (car lat) (multiinsertL new old (cdr lat))))))))))
; multisubst
(define multisubst
  (lamada (new old lat)
          (cond
            ((null? lat) ...)
            (else (cond
                    ((eq? old (car lat))
                     (cons new (multisubst new old (cdr lat)))
                    (else (cons (car lat) (multisubst new old (cdr lat))))))))))
