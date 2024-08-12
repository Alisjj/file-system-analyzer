from utils import traverse_dir, categorize_file_type, find_duplicates

def most_common_type(categories):
    common = []
    cat = ""
    for key, val in categories.items():
        if len(val) > len(common):
            common = val
            cat = key
    return {common[0]['extension']: len(categories[cat])}

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
    print(most_common_file_type)
    
    file_system = {
        "root_path": dir,
        "total_size": total_file_size,  # in bytes
        "total_files": total_files,
        "file_types": categories,
        "files": file_list,
        "duplicates": duplicates
    }

    return file_system
     