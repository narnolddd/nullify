import argparse
import pandas as pd
import os

parser = argparse.ArgumentParser(
    prog="nullify",
    description="Create randomised version of a temporal network datafile."
)

subparser = parser.add_subparsers(dest="model", description="valid null models")

column_shuffle = subparser.add_parser("col_shuffle", help="Null model based on shuffling contents of a column")
group1 = column_shuffle.add_mutually_exclusive_group(required=True)
group1.add_argument('-cname' '--column-name', help="Name of column to be shuffled", dest='col_name', type=str, nargs='*')
group1.add_argument('-cnum','--column-number', help="Number of column to be shuffled", dest='col_num', type=int, nargs='*')

group2 = column_shuffle.add_mutually_exclusive_group(required=False)
group2.add_argument("--sortby-name", help="Column name to sort by", dest="sort_name", type=str)
group2.add_argument("--sortby-number", help="Column number to sort by", dest="sort_num", type=int)

parser.add_argument("filename", type=str)
parser.add_argument("output_path", type=str, default=None)
parser.add_argument("-n", "--number", type=int, default=1)
parser.add_argument("-s", "--separator", help="Datafile line separator", dest="sep", default=" ", type=str)
parser.add_argument("--header", help="Does datafile contain header", dest="header", action="store_true", default=False)

args = parser.parse_args()

os.system("mkdir -p "+str(args.output_path))
df = pd.read_csv(args.filename, sep=args.sep, header=(0 if args.header else None))
n = len(df)

for i in range(args.number):
    if args.col_name:
        for name in args.col_name:
            new_col = df[name].sample(n=n)
            new_col.reset_index(inplace=True,drop=True)
            df[name] = new_col
    if args.col_num:
        for ind in args.col_num:
            new_col = df[[ind]].sample(n=n)
            new_col.reset_index(inplace=True,drop=True)
            df[[ind]] = new_col
    if args.sort_name:
        df.sort_values(by=args.sort_name, inplace=True)
    if args.sort_num:
        df.sort_values(by=df.columns[args.sort_num], inplace=True)
    df.to_csv(args.output_path+"/shuffled-"+str(i)+".csv",sep=args.sep, header = args.header, index=False)