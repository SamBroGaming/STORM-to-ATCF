x = 0
with open(F"STORM_DATA_TRACK.txt", "r") as f:
        data = f.read()
        data = data.split('\n')
        for i in range(len(data)-1):
            if i % 2:
                row = data[i].split(',')
                row[5] = row[5].replace('-', ' ')
                print(F"20000101, 0000, , HU,{row[5]}N, {round(360-(float(row[6])), 1)}W, {round(float(row[8]) * 2.25)}")