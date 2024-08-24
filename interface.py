import argparse
from file_analysis import generate_scan_result, generate_duplicate_report, search_file

parser = argparse.ArgumentParser(
    prog="File Analyzer V1.0",
    description="analyze directory",
    epilog=""
)

parser.add_argument("--scan", help="Perform a full directory scan")
parser.add_argument("--duplicates", help="Find duplicate files")

search_group = parser.add_argument_group('search options')
search_group.add_argument("directory", type=str, help="Directory to search in")
search_group.add_argument("--search", type=str, help="File search pattern (e.g., '.pdf')")
search_group.add_argument("--size-gt", type=int, help="Filter files greater than this size in bytes")
search_group.add_argument("--size-lt", type=int, help="Filter files less than this size in bytes")
# search_group.add_argument("--date-after", type=str, help="Filter files modified after this date (YYYY-MM-DD)")
# search_group.add_argument("--date-before", type=str, help="Filter files modified before this date (YYYY-MM-DD)")

args = parser.parse_args()

if args.scan:
    print(generate_scan_result(args.scan))

if args.duplicates:
    print(generate_duplicate_report(dir=args.duplicates))

if (args.size_gt is not None or args.size_lt is not None) and args.search is None:
    parser.error("--size-gt, --size-lt can only be used with --search")

if args.directory:
    print(search_file(args.directory, args.search, args.size_lt, args.size_gt))