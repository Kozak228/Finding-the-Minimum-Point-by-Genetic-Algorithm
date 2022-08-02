from os import path, mkdir

def proverka_brekets(text, brackets="()"):
    opening, closing = brackets[::2], brackets[1::2]
    stack = []
    for character in text:
        if character in opening:
            stack.append(opening.index(character))
        elif character in closing:
            if stack and stack[-1] == closing.index(character):
                stack.pop() 
            else:
                return False 
    return (not stack) 

def proverka_path(name_dir):
    path_file = path.abspath(__file__)

    path_file = path_file[:path_file.rindex("\\") + 1]

    path_file += name_dir

    if path.exists(path_file):
        path_file += "\\"
        return path_file
    else:
        mkdir(path_file)
        path_file += "\\"
        return path_file