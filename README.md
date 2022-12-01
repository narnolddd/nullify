# nullify (WIP)

Generate randomised reference networks from temporal network data. 

## Usage

### Event shuffling

This is currently the only feature implemented. Randomly shuffles the timestamps at which the edge events occurred.

```bash
python3 nullify fname folderpath timeCol sep n
```

The parameters are:
* `fname` : the name of the datafile. It is assumed that the file is a csv format where each row contains a source, target and time column and potentially others. The time doesn't need to be any particular format.
* `folderpath` : folder where the generated datafiles should go to
* `timeCol` : expected column for the timestamp
* `sep` : separator for the file
* `n` number of networks to generate
