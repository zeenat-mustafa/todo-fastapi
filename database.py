todos = []
users = []
todo_id_counter = 1

def get_next_id():
    global todo_id_counter
    current = todo_id_counter
    todo_id_counter += 1
    return current