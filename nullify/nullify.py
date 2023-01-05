# import os
# import pandas as pd

# fname, folderpath, timeCol, sep, n = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5])

# os.system("mkdir -p "+str(folderpath))

# graph_df = pd.read_csv(fname, sep=sep, header=None)
# no_events = len(graph_df)

# time = graph_df[[timeCol]]

# for i in range(n):
#     # shuffle the time column
#     time = time.sample(n=no_events)
#     time.reset_index(inplace=True,drop=True)

#     # reinsert column and sort
#     graph_df[[timeCol]] = time
#     graph_df.sort_values(by=graph_df.columns[timeCol],inplace=True)

#     graph_df.to_csv(folderpath+"/shuffled-"+str(i)+".csv",sep=sep,index=False, header=False)

# def shuffle_column(graph_df:pd.DataFrame, col_number=None, col_name=None, inplace=False):
#     """
#     returns a dataframe with a given column shuffled
#     """
#     assert col_number is not None or col_name is not None, f"No column number or name provided."
#     assert not (col_name is not None and col_number is not None), f"Cannot have both a column number and a column name."

#     if inplace:
#         df = graph_df
#     else:
#         df = graph_df.copy()

#     no_events = len(df)

#     if col_number is not None:
#         col = df[[col_number]].sample(n=no_events)
#         col.reset_index(inplace=True,drop=True)
#         df[[col_number]] = col
#     if col_name is not None:
#         col = df[col_name].sample(n=no_events)
#         col.reset_index(inplace=True,drop=True)
    
#     if inplace:
#         return
#     else:
#         return df

# # def shuffle_multiple_columns(graph_df:pd.DataFrame, col_numbers:list=[], col_names=None, inplace=False):
# #     assert col_numbers is not None or col_name is not None, f"No column number or name provided."
# #     assert not (col_names is not None and col_number is not None), f"Cannot have both a column number and a column name."