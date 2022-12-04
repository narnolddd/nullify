import pandas as pd
import sys
import os

fname, folderpath, timeCol, sep, n = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5])

os.system("mkdir -p "+str(folderpath))

graph_df = pd.read_csv(fname, sep=sep, header=None)
no_events = len(graph_df)

time = graph_df[[timeCol]]

for i in range(n):
    # shuffle the time column
    time = time.sample(n=no_events)
    time.reset_index(inplace=True,drop=True)

    # reinsert column and sort
    graph_df[[timeCol]] = time
    graph_df.sort_values(by=graph_df.columns[timeCol],inplace=True)

    graph_df.to_csv(folderpath+"/shuffled-"+str(i)+".csv",sep=sep,index=False, header=False)
