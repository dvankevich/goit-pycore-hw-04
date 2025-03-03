from pathlib import Path

# ToDo rewrite this function with csv module https://docs.python.org/3/library/csv.html
def get_cats_info(path):
    '''
    Returns a list of dictionaries with information about each cat.
    Args:
        path (string): path to file
    Returns:
        {"id", "name", "age"} dictionary list or None if error
    Examples:
        Input file format example:
        60b90c1c13067a15887e1ae1,Tayson,3
        60b90c2413067a15887e1ae2,Vika,1

        List of dictionaries example:
        [
            {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
            {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
        ]

    '''
    f_path = Path(path)
    if not f_path.exists() or f_path.is_dir():
        return None
    elif f_path.stat().st_size == 0:
        return None
      
    cats_info = list()
    
    with open(f_path, "r") as fh:
        li = {}
        for line in fh.readlines():
            li["id"], li["name"], li["age"] = line.strip().split(",")
            cats_info.append(li)
            
    return cats_info



def main():
    assert get_cats_info("empty_file.txt") == None
    assert get_cats_info("nofile.txt") == None
    assert get_cats_info("salary.dir") == None

    #print(get_cats_info("cats_info.csv"))

if __name__ == "__main__":
    main()