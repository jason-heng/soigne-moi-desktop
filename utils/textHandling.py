
def get_formated_text(text : str, max_len: int):
    splited_text = text.split(" ")
    list_of_lines = [[]]
    for word in splited_text:
        if len(" ".join(list_of_lines[-1])) + len(word) + 1 > max_len:
            list_of_lines.append([word])
        else:
            list_of_lines[-1].append(word)
    
    return "\n".join([" ".join(line) for line in list_of_lines])