; FICHIER : listchar.lisp
; CONTENU : code pour comparer les caractères français entre eux
; AUTEUR : Solal Gaillard
; VERSION : 25 juillet 2015
; LICENCE : GNU

; NAME : lire-en-liste - crée une liste à partir d'un fichier de données où tous les éléments sont à la ligne
; ARGS : <un atome> <auxiliaire : une liste>
; USAGES : (lire-en-liste 'char) => liste de caractères, (lire-en-liste 'code) => liste de codes
; GLOBALS : <alphabet> <ligne>
; CALL : aucune
; USER : "toplevel"

(
defun 
lire-en-liste (codeOuChar &aux liste)
    (setq 
    
        ; NAME : alphabet - contient le fichier ouvert d'où seront lues les données
        ; USAGES : le fichier de données
        ; USER : <lire-en-liste>

        alphabet 
        (open (string-concat "alphabet_" (string codeOuChar) ".txt") 
            :direction :input 
            :if-does-not-exist :error ) )
    (loop
        (setq
        
            ; NAME : ligne - contient la ligne lue du fichier
            ; USAGES : chaîne de caractère contenant la donnée lue ou nil
            ; USER : <lire-en-liste>
        
            ligne 
            (read-line alphabet nil nil) )
        (cond
            ((not ligne) (close alphabet) (return liste))
            (t (push (read-from-string ligne) liste)) ) )
        (reverse liste) )
         
; NAME : ALPHABET - contient la liste des caractères
; USAGES : Liste de référence pour comparer les caractères
; USER : <member-listchar>        
        
(setq ALPHABET (lire-en-liste 'char))

; NAME : member-listchar - Regarde si le caractère fait partie de la liste et si oui en construit une nouvelle avec les éléments suivants
; ARGS : <un atome> <une liste>
; USAGES : member-listchar (caractère liste) => liste de caractères à partir de caractère
; GLOBALS : aucune
; CALL : <member-listchar>
; USER : <french-char>=>

(defun member-listchar (caractère liste)
    (cond
        ((atom liste) nil)
        ((equal caractère (car liste)) (cons (car liste) (cdr liste)))
        (t (member-listchar caractère (cdr liste))) ) )

; NAME : french-char>= - compare si le premier caractère suit le suivant
; ARGS : <un atome> <un atome>
; USAGES : french-char>= => t, french-char>= => nil
; GLOBALS : <listeCaractèreUn> <listeCaractèreDeux>
; CALL : <char>=>
; USER : <comparaisons>

(defun french-char>= (caractèreDeux caractèreUn)
    (setq 
    
        ; NAME : listeCaractèreUn - liste contenant tous les caractères après caractèreUn
        ; USAGES : Utilisée pour savoir le caractèreDeux suit le caractèreUn (s'il est contenu dans liste) ou pour savoir s'il est contenu dans l'alphabet
        ; USER : <french-char>=>
    
        listeCaractèreUn 
        (member-listchar caractèreUn ALPHABET) )
        
     (setq 
    
        ; NAME : listeCaractèreDeux - liste contenant tous les caractères après caractèreDeux
        ; USAGES : Utilisée pour savoir le caractèreDeux est contenu dans l'alphabet
        ; USER : <french-char>=>
    
        listeCaractèreDeux
        (member-listchar caractèreDeux ALPHABET) )
        
    (cond 
        ((and (not listeCaractèreUn) (not listeCaractèreDeux)) (char>= caractèreDeux caractèreUn))
        ((not listeCaractèreUn) nil)
        ((not listeCaractèreDeux) t)
        ((member-listchar caractèreDeux listeCaractèreUn) t)
        (nil) ) )

        
; NAME : load - charge le contenu de benchmark.lisp
; ARGS : <une chaîne de caractères>
; USAGES : load "benchmark.lisp" => charge le contenu de benchmark.lisp
; GLOBALS : aucune
; CALL : aucun
; USER : <load "listcode.lisp">
        
(load "benchmark.lisp")
