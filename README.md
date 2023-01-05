# nullify (WIP)

Generate randomised reference networks from temporal network data. 

## Usage

### Event shuffling

This is currently the only feature implemented. Randomly shuffles a column (e.g. timestamp, source node, destination node)

Create randomised version of a temporal network datafile.

positional arguments:
  filename
  output_path

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
  -s SEP, --separator SEP
                        Datafile line separator
  --header              Does datafile contain header

subcommands:
  valid null models

  {col_shuffle}
    col_shuffle         Null model based on shuffling contents of a column

    optional arguments:
  -h, --help            show this help message and exit
  -cname--column-name [COL_NAME ...]
                        Name of column to be shuffled
  -cnum [COL_NUM ...], --column-number [COL_NUM ...]
                        Number of column to be shuffled
  --sortby-name SORT_NAME
                        Column name to sort by
  --sortby-number SORT_NUM
                        Column number to sort by