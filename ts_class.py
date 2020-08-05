import json
import glob
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


ts_list = []
accx_list = []
accy_list = []
accz_list = []

for name in glob.glob('./data/*'):
    print(name)
    f = open(name)
    lines = f.readlines()

    for line in lines:
        line_json = json.loads(line)
        # print(line_json['timeStamp'])
        ts = line_json['timeStamp']
        accx = line_json['accx']
        accy = line_json['accy']
        accz = line_json['accz']
        # datetimeObj = datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S.%fZ')
        # print(datetimeObj)
        # print(line_json['accx'])
        ts_list.append(ts)
        accx_list.append(accx)
        accy_list.append(accy)
        accz_list.append(accz)

    # data = json.load(f)
    # data = f
    # print(type(lines[0]))
    print(lines[0])

    f.close()

# construct pandas data frame
ts_pd = pd.to_datetime(pd.Series(ts_list), format='%Y-%m-%dT%H:%M:%S.%fZ')
accx_pd = pd.Series(accx_list)
accy_pd = pd.Series(accy_list)
accz_pd = pd.Series(accz_list)

data_df = pd.DataFrame({'time':ts_pd,'accx':accx_pd,'accy':accy_pd,'accz':accz_pd})

plt.figure()

data_df.plot()
