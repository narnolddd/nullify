import pandas as pd
import sys
import os

fname, folderpath, timeCol, sep, n = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5])

graph_df = pd.read_csv(fname, sep=sep, header=None)

os.system("mkdir -p "+str(folderpath))

for i in range(n):
    # shuffle the time column
    time = graph_df[[timeCol]]
    time = time.sample(n=len(time))
    time.reset_index(inplace=True,drop=True)

    # reinsert column and sort
    graph_df[[timeCol]] = time
    graph_df.sort_values(by=graph_df.columns[timeCol])

    graph_df.to_csv(folderpath+"/shuffled-"+str(i)+".csv",sep=sep,index=False, header=False)
