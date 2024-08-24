from file_analysis import file_analysis, search_file, generate_report



def main():
    p = "/Users/aliyusani/workspace/github.com/file-system/sj"
    analysis = file_analysis(p)
    # print(analysis["duplicates"])
    print(search_file(p, max_size=20))
    # print(generate_report(p))


    
     
main()