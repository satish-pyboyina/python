def list_manipulation(lst,cmd,loc,value = 0):
    if lst == False or type(lst).__name__ != 'list' or (cmd != 'remove' and cmd != 'add') or (loc != 'end' and loc != 'beginning'):
        return None
    elif cmd == 'add' and value == False:
        return None
    elif cmd == 'remove' and loc == 'beginning':
        return lst[0]
    elif cmd == 'remove' and loc == 'end':
        return lst[-1]
    elif cmd == 'add' and loc == 'beginning':
        lst.insert(0,value)
        return lst
    elif cmd == 'add' and loc == 'end':
        lst.append(value)
        return lst
    else:
        return None

print(list_manipulation([1,2,3], "remove", "end")) # 3
print(list_manipulation([1,2,3], "remove", "beginning")) #  1
print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
print(list_manipulation([1,2,3], "add", "end", 30)) #  [1,2,3,30]