from utils import traverse_dir, categorize_file_type, find_duplicates, is_recent, search_file

def most_common_type(categories):
    common = []
    cat = ""
    for key, val in categories.items():
        if len(val) > len(common):
            common = val
            cat = key
    return {cat: len(categories[cat])}

def file_analysis(dir):
    file_list = traverse_dir(dir)
    categories = categorize_file_type(file_list)
    
    total_files = len(file_list)
    duplicates = find_duplicates(file_list)
    
    total_file_size = 0
    largest_file = file_list[0]

    for file in file_list:
        total_file_size += int(file["size"])
        if file["size"] > largest_file["size"]:
            largest_file = file

    most_common_file_type = most_common_type(categories)

    recent_files = [f for f in file_list if is_recent(f["modified_time"])]
    
    file_system = {
        "root_path": dir,
        "total_size": total_file_size,  # in bytes
        "total_files": total_files,
        "file_types": categories,
        "files": file_list,
        "duplicates": duplicates,
        "recent_files": recent_files
    }

    return file_system


# def filter_file_by_min_size(size)

 
def search_file(dir, name=None, type=None, min_size=None, max_size=None):
    files = traverse_dir(dir)
    result = []
    for file in files:
        if not name and not type:
            result = files

        if name and name == file["name"]:
            result.append(file)

        if type and type == file["type"]:
            result.append(file)

    if not min_size and not max_size: 
        return [i["path"] for i in result]

    if min_size and not max_size: 
        return [f["path"] for f in result if f["size"] > min_size]
    
    if max_size and not min_size:
        return [f["path"] for f in result if f["size"] > max_size]
    
    if min_size and max_size:
       return [f["path"] for f in result if f["size"] > min_size and f["size"] < max_size]