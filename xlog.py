
#I tried to create my own programming language
#This is kind of final version
#I'll maybe work on it on future

#I'll add a tutorial kind of thing when I finnaly finish this project

import sys
from functools import reduce
is_if_True = False
is_if_active = False
is_func_active = False
is_for_active = False
is_send_by_for = False

variables = dict()
functions = dict()
def add(line = str()):
    list1 = line.split(':')
    if list1[0] == 'add':
        if list1[1] == 'int':
            try:
                variables[list1[2]] = int(list1[3])
            except:
                sys.stderr.write('Please enter integer')
        elif list1[1] == 'str':
            variables[list1[2]] = list1[3]
        elif list1[1] == 'list':
            listA = list()
            if list1[3] == 'none':
                variables[list1[2]] = list()
            else:
                listB = list1[3].split(',')
                for i in listB:
                    if '-' in i:
                        listC = i.split('-')
                        if listC[0] == 'int':
                            listA.append(int(listC[1]))
                        elif listC[0] == 'str':
                            listA.append(listC[1])
                        continue
                    listA.append(i)
                variables[list1[2]] = listA
        else:
            sys.stderr.write('No object type avaible')
def show(line = str()):
    list1 = line.split(':')
    if list1[0] == 'show':
        if len(list1) != 2:
            sys.stderr.write('Unknown command')
        else:
            try:
                if '+' in list1[1]:
                    list2 = list1[1].split('+')
                    for i in list2:
                        if i in variables:
                            list2[list2.index(i)] = variables[i]
                        elif '-' in i:
                            list3 = i.split('-')
                            if list3[0] == 'str':
                                list2[list2.index(i)] = str(list3[1])
                            elif list3[0] == 'int':
                                list2[list2.index(i)] = int(list3[1])
                            else:
                                sys.stderr.write('No object type avaible')
                    print(reduce((lambda x, y: x + y), list2))
                else:
                    if list1[1] in variables or '~' in list1[1]:
                        if '~' in list1[1]:
                            listA = list1[1].split('~')
                            print(list(variables[listA[0]])[int(listA[1])])
                        else:
                            print(variables[list1[1]])
                    else:
                        print(list1[1])
            except:
                sys.stderr.write('Value Error')
def do_times(line, line_index, lines):
    list1 = line.split(':')
    try:
        if list1[0] == 'do':
            if list1[2] == 'codes':
                if list1[4] == 'times':
                    lines_to_read = list()
                    for i in range(1, int(list1[1]) + 1):
                        lines_to_read.append(lines[line_index + i])
                    for i in range(1, int(list1[3])):
                        for j in lines_to_read:
                            read_codes(j, j)
    except:
        sys.stderr.write('A problem showed about do loop')
def if_control(line):
    try:
        if '\n' in line:
            line = line[:-1]
        list1 = line.split(';')
        list2 = list1[1].split(':')
        if list2[0] in variables:
            list2[0] = variables[list2[0]]
        else:
            if '-' in list2[0]:
                list3 = list2[0].split('-')
                if list3[0] == 'str':
                    list2[0] = str(list3[1])
                elif list3[0] == 'int':
                    list2[0] = int(list3[1])
                else:
                    sys.stderr.write('No object type avaible')
        if list2[2] in variables:
            list2[2] = variables[list2[2]]
        else:
            if '-' in list2[2]:
                list3 = list2[2].split('-')
                if list3[0] == 'str':
                    list2[2] = str(list3[1])
                elif list3[0] == 'int':
                    list2[2] = int(list3[1])
                else:
                    sys.stderr.write('No object type avaible')
        if list2[1] == '==':
            return list2[0] == list2[2]
        elif list2[1] == '<=':
            return list2[0] <= list2[2]
        elif list2[1] == '<':
            return list2[0] < list2[2]
        elif list2[1] == '>':
            return list2[0] > list2[2]
        elif list2[1] == '>=':
            return list2[0] >= list2[2]
        elif list2[1] == '!=':
            return list2[0] != list2[2]
    except:
        sys.stderr.write('There is a problem with if line')
def get(line = str()):
    try:
        list1 = line.split(':')
        if list1[0] == 'get':
            if list1[2] == 'as':
                input_value = input()
                if list1[3] == 'int':
                    variables[list1[1]] = int(input_value)
                elif list1[3] == 'str':
                    variables[list1[1]] = input_value
                else:
                    sys.stderr.write('No object type avaible')
    except:
        sys.stderr.write('There is a problem with get line')
def func(line, line_index, lines):
    if '\n' in line:
        line = line[:-1]
    list1 = line.split(':')
    list2 = list()
    start = False
    if list1[0] == 'func' and len(list1) == 2:
            for i in lines:
                if i == lines[line_index]:
                    start = True
                    continue
                if '\n' in i:
                    i = i[:-1]
                if i == 'end:lines':
                    break
                if start:
                    list2.append(i)
            variables[list1[1]] = list2
def call_func(line = str()):
    list1 = line.split(':')
    if list1[0] == 'call' and len(list1) == 2:
        for i in variables[list1[1]]:
            read_codes(i, i)
def for_every(line, line_index, lines):
    list1 = line.split(':')
    global is_send_by_for
    if list1[0] == 'forevery' and list1[2] == 'on':
        if list1[3] in variables:
            for i in variables[list1[3]]:
                variables[list1[1]] = i
                start = False
                list2 = list()
                for i in lines:
                    if i == lines[line_index]:
                        start = True
                        continue
                    if '\n' in i:
                        i = i[:-1]
                    if i == 'end:for':
                        break
                    if start:
                        list2.append(i)
                is_send_by_for = True
                for i in list2:
                    read_codes(i, i)
                is_send_by_for = False
            del variables[list1[1]]
        else:
            listA = list()
            listB = list1[3].split(',')
            for i in listB:
                if '-' in i:
                    listC = i.split('-')
                    if listC[0] == 'int':
                        listA.append(int(listC[1]))
                    elif listC[0] == 'str':
                        listA.append(listC[1])
                    continue
                listA.append(i)
            for i in listA:
                variables[list1[1]] = i
                start = False
                list2 = list()
                for i in lines:
                    if i == lines[line_index]:
                        start = True
                        continue
                    if '\n' in i:
                        i = i[:-1]
                    if i == 'end:for':
                        break
                    if start:
                        list2.append(i)
                is_send_by_for = True
                for i in list2:
                    read_codes(i, i)
                is_send_by_for = False
            del variables[list1[1]]
def update(line = str()):
    list1 = line.split(':')
    if list1[0] == 'update' and list1[1] in variables and list1[2] == 'as':

        if type(variables[list1[1]]) == int or type(variables[list1[1]]) == str:
            if list1[3] in variables:
                try:
                    variables[list1[1]] += variables[list1[3]]
                except:
                    sys.stderr.write('Value Error')
            else:
                if '-' in list1[3]:
                    listA = list1[3].split('-')
                    if listA[0] == 'int':
                        variables[list1[1]] += int(listA[1])
                    elif listA[0] == 'str':
                        try:
                            variables[list1[1]] += listA[1]
                        except:
                            sys.stderr.write('Value Error')
                    else:
                        sys.stderr.write('No Value Found')
                else:
                    try:
                        variables[list1[1]] += list1[3]
                    except:
                        sys.stderr.write('Value Error')
        elif type(variables[list1[1]]) == list:
            if list1[3] in variables:
                variables[list1[1]].append(variables[list1[3]])
            else:
                if '-' in list1[3]:
                    listA = list1[3].split('-')
                    if listA[0] == 'int':
                        variables[list1[1]].append(int(listA[1]))
                    elif listA[0] == 'str':
                        try:
                            variables[list1[1]].append(listA[1])
                        except:
                            sys.stderr.write('Value Error')
                    else:
                        sys.stderr.write('No Value Found')
                else:
                    try:
                        variables[list1[1]].append(list1[3])
                    except:
                        sys.stderr.write('Value Error')
def read_codes(i, original_line):
    global is_if_True
    global is_if_active
    global is_func_active
    global is_for_active
    global is_send_by_for
    if '\n' in i:
        i = i[:-1]
    if (is_if_active and is_if_True) or not(is_if_active or is_func_active or is_for_active) or (is_send_by_for):
        if '\n' in i:
            i = i[:-1]
        if 'add' in i:
            add(i)
        elif 'show' in i:
            show(i)
        elif 'do' in i:
            do_times(i, lines.index(original_line), lines)
        elif 'if' in i:
            is_if_active = True
            is_if_True = if_control(i)
        elif 'func' in i:
            is_func_active = True
            func(i, lines.index(original_line), lines)
        elif 'get' in i:
            get(i)
        elif 'forevery' in i:
            is_for_active = True
            for_every(i, lines.index(original_line), lines)
        elif 'call' in i:
            call_func(i)
        elif 'update' in i:
            update(i)
    elif i == 'end':
        is_if_active = False
    elif i == 'end:lines':
        is_func_active = False
    elif i == 'end:for':
        is_for_active = False


with open('your_files_name.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        read_codes(i, i)
