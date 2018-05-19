#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re, sys

        
'''GLOBAL VARIABLES'''
function_list = {}

'''REGEX DEFINITIONS'''
'''General Use'''
clear_comments = re.compile(r'(.*);.*')
#Repére ligne ou defun et sa parenthèse ne sont pas sur la même ligne du nom de la fonction.
dfun_on_sm_ln = re.compile(r'(?:.*\([\t ]*$)|(?:.*\([\t ]*defun[\t ]*$)')

'''Functions'''
#for user defined function definition
fdef = re.compile(r'[\t ]*\([\t ]*defun[\t ]*([-<>+=\w]+)[\t ]*\((.*?)\)', re.UNICODE)
#To divide up parameters
pdef = re.compile(r'&[^&]*|\w+', re.UNICODE)
#for any other
flan = re.compile('\([\t ]*([-<>+=\w]+).*?', re.UNICODE)
'''SUBROUTINES'''

'''Print name of file and path if needed'''
def print_file_path(aFile) :
    path_name = re.findall('([.\w]+)', aFile)
    print "\nFile name: " + path_name[len(path_name)-1]
    if len(path_name)>1 :
        print "Path:",
        for i in range(len(path_name)-1) :
            print path_name[i]+"/"
    print ''


'''Find all the functions'''
#Organise en nom et paramètres, note la redéfinition d'une fonction
def find_functions(matched, n) :
    fdef_n = matched[0]
    if fdef not in function_list : # Si première définition
        function_list[fdef_n] = {}
        function_list[fdef_n]['definition']=[]
        function_list[fdef_n]['usage'] = []
        function_list[fdef_n]['type'] = 'User Defined'
    function_list[fdef_n]['args']=[]
    params_n_types = pdef.findall(matched[1])# Divise les paramètres
    for i in params_n_types :
        function_list[fdef_n]['args'].append(i)
        
    function_list[fdef_n]['definition'].append(n)



'''Imprime en détail chaque fonction et avec formatage'''
def print_functions() :
    print 'All Functions: \n\nBelow functions as defined by user:\n'
    for i in function_list:
        if function_list[i]['type'] == 'User Defined' :
            print_us_defined(i)
    print 'Below functions defined by the language:\n'
    for i in function_list:
        if function_list[i]['type'] == 'Language Defined':
            print_lan_defined(i)

'''Spécifique pour les fonctions définies par l\'utilisateur'''
def print_us_defined(i) :
    print 'Name: %s\nType: %s\nParameters:' % (i.encode('UTF-8'), function_list[i]['type'])

    if 'args' in function_list[i] :
        c = 1
        for y in function_list[i]['args']:
            print '\tParameter %i\tName: %s' % (c, y.encode('UTF-8'))
            c = c+1
    else : print 'No Parameters'
                    
    print 'Definition: %04i\n' % function_list[i]['definition'][0],
    if len(function_list[i]['definition']) > 1 :
        for m in range(1, len(function_list[i]['definition'])) :
            print 'Fonction redéfinie: %04i\n' % function_list[i]['definition'][m]
    print 'Referencing:',

    if function_list[i]['usage'] :
        for y in range(len(function_list[i]['usage'])-1) : print '%04i,' % function_list[i]['usage'][y],
        print '%04i\n' % function_list[i]['usage'][len(function_list[i]['usage'])-1]
    else : print 'No referencing\n'

'''Spécifique pour les fonctions issues du langage'''
def print_lan_defined(i) :
    print 'Name: %s\nType: %s' % (i.encode('UTF-8'), function_list[i]['type'])
    print 'Referencing:',

    for y in range(len(function_list[i]['usage'])-1) :
        print '%04i,' % function_list[i]['usage'][y],

    print '%04i\n' % function_list[i]['usage'][len(function_list[i]['usage'])-1]


'''Procède en deux passes car une fonction peut être référencée avant d'être définie'''
def two_passes(file, firstIt) :
    file = open(file)
    par_open = 0 ; line_cont = None;n=0;m=0
    line = file.readline()
    while line : #Pour une deuxième passe
        line_read = line.decode('UTF-8')
        line = file.readline()
        n=n+1 #index commence à 1.
        line_tmp = clear_comments.match(line_read) #Get rid of semi-colon comments
        if line_tmp :
            line_read = line_tmp.group(1)

        if line_cont :   #si on continue une ligne préc
            #On nettoie la ligne en enlevant le  \n
            line_read = line_cont[:-1] + ' ' + line_read

        #Bring open parenthesis and defun on one single line for future regex if they were separated.
        if dfun_on_sm_ln.match(line_read):
            line_cont = line_read; m=m+1
            continue
                
        if firstIt: #Pour la 1ère boucle sur le fichier
            put_fun(line_read, n-m) #Inscrit les fonctions trouvées dans des dictionnaires
            if not line : #fin de fichier
                file.seek(0) #On remet à 0 pour une nouvelle passe
                firstIt = False;line = file.readline();n=0
        else :
            find_referencing(line_read, n-m)

        line_cont=None; m=0
               
                
def put_fun(line_read, n) :
    #If function
    matched = fdef.findall(line_read)
    if  matched:
        for i in matched :
            find_functions(i, n)
    

def find_referencing(line, n) :
    fname = flan.findall(line)# Pour toutes les occurences où un mot suit une parenthèse ouverte
    for j, i in enumerate(fname):
          #Get rid of parameters from defun function as they are not functions
        is_param=None
        if j<len(fname)-1:
            #Can't compile it since it changes every iteration
            is_param = re.match('.*defun[\t ]*[-<>+=\w]+[\t ]*\([\t ]*'+fname[j+1]+'.*',line, re.UNICODE)
        if i == 'defun' and is_param: #If match is a param
            fname.pop(j+1) #Get rid of it
        if i in function_list:
            function_list[i]['usage'].append(n)
        else:
            function_list[i]={}
            function_list[i]['usage']=[n]
            function_list[i]['type']='Language Defined'



'''MAIN FUNCTION'''         
def scan(file) :
    print_file_path(file) #print file name and path
    two_passes(file, True)
    print_functions()
    

    
if len(sys.argv) is 1 :
    exit('missing source-file name')
for f in sys.argv[1:] :
    scan(f)
