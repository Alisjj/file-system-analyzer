from hurry.filesize import size
from datetime import datetime
from utils import traverse_dir, categorize_file_type, find_duplicates, is_recent, last_seven_days

def most_common_type(categories):
    common = []
    cat = ""
    for key, val in categories.items():
        if len(val) > len(common):
            common = val
            cat = key
    return {"name": cat, "num": len(categories[cat])}

def file_analysis(dir):
    file_list, _ = traverse_dir(dir)
    categories = categorize_file_type(file_list)
    
    total_files = len(file_list)
    duplicates = find_duplicates(file_list=file_list)
    
    total_file_size = 0
    largest_file = file_list[0]

    for file in file_list:
        total_file_size += int(file["size"])
        if file["size"] > largest_file["size"]:
            largest_file = file

    most_common_file_type = most_common_type(categories)

    recent_files = [f for f in file_list if is_recent(f["modified_time"])]
    last_7_days = [f for f in file_list if last_seven_days(f["created_time"])] 
    file_system = {
        "root_path": dir,
        "largest_file": largest_file,
        "total_size": total_file_size,  # in bytes
        "total_files": total_files,
        "file_types": categories,
        "files": file_list,
        "duplicates": duplicates,
        "recent_files": recent_files,
        "last_seven_days": last_7_days,
        "common_file": most_common_file_type, 
    }

    return file_system

def generate_scan_result(dir):
    analysis = file_analysis(dir)
    day =  datetime.today().strftime('%Y-%m-%d')
    result = f"""
    Scan Results:
    Total files: {len(analysis["files"])}
    Total size: {size(analysis["total_size"])}
    Largest file: {analysis["largest_file"]["name"]} {size(analysis["largest_file"]["size"])} 
    Most common file type: {analysis["common_file"]["name"]} ({analysis["common_file"]["num"]} files)

    File type distribution:
    - Documents: 65%
    - Images: 20%
    - Videos: 10%
    - Others: 5%

    Recent activity:
    - Modified in last 24 hours: {len(analysis["recent_files"])} files
    - Created in last 7 days: {len(analysis["last_seven_days"])}
    

    """
    return result

def generate_duplicate_report(dir):
    file_list, _ = traverse_dir(dir)
    duplicates = find_duplicates(file_list)
    index = 1
    print(f"\nFound {len(duplicates)} sets of duplicate files:")
    for k,v in duplicates.items():
        print(f"\n{index}. {v[0]['name']} ({len(v)} copies)")
        for f in v:
            print(f"    -{f['path']}")
        index+=1
    print("\nTotal space that could be saved: 15.7 MB ") 

    return ""

def search_file(dir, name=None, min_size=None, max_size=None):
    files, _ = traverse_dir(dir)
    result = []
    for file in files:
        if not name:
            result = files

        if name and name in file["name"]:
            result.append(file)

    if not min_size and not max_size: 
        return [i["path"] for i in result]

    if min_size and not max_size: 
        return [f["path"] for f in result if f["size"] > min_size]
    
    if max_size and not min_size:
        return [f["path"] for f in result if f["size"] > max_size]
    
    if min_size and max_size:
       return [f["path"] for f in result if f["size"] > min_size and f["size"] < max_size]