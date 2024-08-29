import argparse
from file_analysis import generate_scan_result, generate_duplicate_report, search_file, traverse_dir

parser = argparse.ArgumentParser(
    prog="File Analyzer V1.0",
    description="analyze directory",
    epilog="Use the appropriate options to perform different analyses."
)

parser.add_argument("--scan", help="Perform a full directory scan")
parser.add_argument("--duplicates", help="Find duplicate files")
parser.add_argument("--tree", help="visualize the tree structure of the director")

search_group = parser.add_argument_group('search options')
search_group.add_argument("directory", nargs='?', type=str, help="Directory to search in")
search_group.add_argument("--search", type=str, help="File search pattern (e.g., '.pdf')")
search_group.add_argument("--size-gt", type=int, help="Filter files greater than this size in bytes")
search_group.add_argument("--size-lt", type=int, help="Filter files less than this size in bytes")

args = parser.parse_args()

if args.scan:
    print(generate_scan_result(args.scan))

if args.tree:
    _, tree = traverse_dir(args.tree)
    for i in tree:
        print(i)

if args.duplicates:
    print(generate_duplicate_report(dir=args.duplicates))

if (args.size_gt is not None or args.size_lt is not None) and args.search is None:
    parser.error("--size-gt, --size-lt can only be used with --search")

if args.directory:
    print(search_file(args.directory, args.search, args.size_lt, args.size_gt))

