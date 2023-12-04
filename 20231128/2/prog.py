import math
import sys


mark_d = {}
marks = []
var_d = {}
cmd_list = []
while s := sys.stdin.readline():
    s = s.split()
    if s == []:
        continue
    if ':' in s[0]:
        mark_d[s[0][:-1]] = len(cmd_list)
        s = s[1:]
    match s:
        case ['stop']:
            break
        case ['store', var, addr]:
            try:
                s[1] = float(var)
            except:
                s[1] = 0
            cmd_list.append(s)
        case ['add' | 'sub' | 'div' | 'mul', sender, oper, addr]:
            cmd_list.append(s)
        case ['ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle', sender, oper, mark]:
            marks.append(mark)
            cmd_list.append(s)
        case ['out', sender]:
            cmd_list.append(s)

for mark in mark_d:
    if mark not in marks:
        exit()


i = 0
while i < len(cmd_list):
    match cmd_list[i]:
        case ['stop']:
            break
        case ['store', var, addr]:
            var_d[addr] = var
        case [OP, sender, oper, addr]:
            if sender not in var_d:
                var_d[sender] = 0
            if oper not in var_d:
                var_d[oper] = 0
            match OP:
                case 'add':
                    var_d[addr] = var_d[sender] + var_d[oper]
                case 'sub':
                    var_d[addr] = var_d[sender] - var_d[oper]
                case 'div':
                    try:
                        var_d[addr] = var_d[sender] / var_d[oper]
                    except:
                        var_d[addr] = math.inf
                case 'mul':
                    var_d[addr] = var_d[sender] * var_d[oper]
                case 'ifeq':
                    if var_d[sender] == var_d[oper]:
                        i = mark_d[addr]
                        continue
                case 'ifne':
                    if var_d[sender] != var_d[oper]:
                        i = mark_d[addr]
                        continue
                case 'ifgt':
                    if var_d[sender] > var_d[oper]:
                        i = mark_d[addr]
                        continue
                case 'ifge':
                    if var_d[sender] >= var_d[oper]:
                        i = mark_d[addr]
                        continue
                case 'iflt':
                    if var_d[sender] < var_d[oper]:
                        i = mark_d[addr]
                        continue
                case 'ifle':
                    if var_d[sender] <= var_d[oper]:
                        i = mark_d[addr]
                        continue
        case ['out', sender]:
            if sender not in var_d:
                var_d[sender] = 0
            print(var_d[sender])
    i += 1


