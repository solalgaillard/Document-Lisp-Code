# Document-Lisp-Code
Python program to document lisp code

Documents both language defined functions and user defined functions. It tells the user where they are defined and where they are used as well the parameters they take

$ ./document_Lisp.py listchar.lisp 

File name: listchar.lisp

All Functions: 

Below functions as defined by user:

Name: member-listchar
Type: User Defined
Parameters:
	Parameter 1	Name: caractère
	Parameter 2	Name: liste
Definition: 0054
Referencing: 0058, 0075, 0084, 0090

Name: french-char>=
Type: User Defined
Parameters:
	Parameter 1	Name: caractèreDeux
	Parameter 2	Name: caractèreUn
Definition: 0067
Referencing: No referencing

Name: lire-en-liste
Type: User Defined
Parameters:
	Parameter 1	Name: codeOuChar
	Parameter 2	Name: &aux liste
Definition: 0014
Referencing: 0045

Below functions defined by the language:

Name: and
Type: Language Defined
Referencing: 0087

Name: load
Type: Language Defined
Referencing: 0101

Name: cons
Type: Language Defined
Referencing: 0057

Name: cond
Type: Language Defined
Referencing: 0036, 0055, 0086

Name: cdr
Type: Language Defined
Referencing: 0057, 0058

Name: close
Type: Language Defined
Referencing: 0037

Name: open
Type: Language Defined
Referencing: 0024

Name: defun
Type: Language Defined
Referencing: 0014, 0054, 0067

Name: t
Type: Language Defined
Referencing: 0038, 0058

Name: char>=
Type: Language Defined
Referencing: 0087

Name: setq
Type: Language Defined
Referencing: 0017, 0028, 0045, 0068, 0077

Name: return
Type: Language Defined
Referencing: 0037

Name: string
Type: Language Defined
Referencing: 0024

Name: nil
Type: Language Defined
Referencing: 0091

Name: atom
Type: Language Defined
Referencing: 0056

Name: not
Type: Language Defined
Referencing: 0037, 0087, 0087, 0088, 0089

Name: reverse
Type: Language Defined
Referencing: 0039

Name: car
Type: Language Defined
Referencing: 0057, 0057

Name: equal
Type: Language Defined
Referencing: 0057

Name: read-line
Type: Language Defined
Referencing: 0035

Name: read-from-string
Type: Language Defined
Referencing: 0038

Name: string-concat
Type: Language Defined
Referencing: 0024

Name: push
Type: Language Defined
Referencing: 0038

Name: loop
Type: Language Defined
Referencing: 0027
