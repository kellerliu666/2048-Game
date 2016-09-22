"""
This code writen by Keller is for part of 2048 game project.

Go coding!
"""   
def merge(line):  
    """
    Merge function for 2048 game.
    """                 
    new_lst = []          # Create a new_lst where we can move all numbers to the left
    for raw_iter in range(len(line)):
        new_lst.append(0)
    new_pos = 0
    for raw_tile in line:
        if raw_tile != 0:
            new_lst[new_pos] = raw_tile
            new_pos += 1
        if raw_tile == 0:
            continue           
    merge_lst = []        # Create a merge_lst for merge function below to use
    for raw_iter in range(len(line)):
        merge_lst.append(0)        
    mer_lst_pos = 0       # Merge start
    mem = None
    if new_lst[0] == 0:
        return merge_lst
    if mem is None:
        mem = new_lst[0]
    for tile in new_lst[1:]:
        if mem is None:
            mem = tile
            merge_lst[mer_lst_pos] = mem
            continue
        if tile != mem:
            merge_lst[mer_lst_pos] = mem
            mem = tile
            mer_lst_pos += 1
            merge_lst[mer_lst_pos] = mem
            continue
        if tile == mem:
            merge_lst[mer_lst_pos] = mem + tile
            mer_lst_pos += 1
            mem = None
    if mem is None:
        return merge_lst
    merge_lst[mer_lst_pos] = mem
    return merge_lst      # Merge completed
