from file_analysis import file_analysis, search_file



def main():
    p = "/Users/aliyusani/workspace/github.com/file-system/sj"
    analysis = file_analysis(p)
    # print(analysis["duplicates"])
    print(search_file(p))

    
     
main()