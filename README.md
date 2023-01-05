# nullify (WIP)

Generate randomised reference networks from temporal network data. 

## Usage

```
python3 nullify/commandline.py [args] filename outputpath
```
## Example

```
python3 nullify/commandline.py -n 10 col_shuffle -cnum 2 --sortby-num 2 ~/Data/CollegeMsg.txt output
```

produces 10 null networks by shuffling the time column (column 2) of the datafile, then sorting by time (column 2) and writing to a folder named `output`.

### Column shuffling

This is currently the only feature implemented. Randomly shuffles a column (e.g. timestamp, source node, destination node)

Create randomised version of a temporal network datafile.

positional arguments:
* `filename` datafile name
* `output_path` output location folder (generates it if not present)

optional arguments:
* `-h, --help` show this help message and exit
* `-n, --number` number of new datafiles to generate (default 1)
* `-s --separator` file line separator (default is `" "`)
* `--header` include if datafile contains header (false by default)

Subcommands:
* `col_shuffle` Null model based on shuffling contents of a column

Optional arguments:
*  `-h, --help` show this help message and exit
*  `-cname--column-name` name of column to be shuffled
*  `-cnum, --column-number` number of column to be shuffled
*  `--sortby-name` column name to sort by (default no sorting)
*  `--sortby-number` column number to sort by