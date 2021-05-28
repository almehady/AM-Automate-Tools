import pandas as pd
import numpy as np

chunksize = 20000
i=0
df = pd.read_excel("file_name.xlsx")
for chunk in np.array_split(df, len(df) // chunksize):
    chunk.to_excel('your_dir/file_{:02d}.xlsx'.format(i), index=False)
    print('now working on', i)
    i += 1
