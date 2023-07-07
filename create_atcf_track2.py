x = 0
y = '0.0'
with open(F"STORM_DATA_TRACK.txt", "r") as f:
        data = f.read()
        data = data.split('\n')
        print("EP072014,          GENEVIEVE,     87,")
        for i in range(len(data)-1):
            if i % 2:
                row = data[i].split(',')
                row[5] = row[5].replace('-', ' ')
                if row[2].strip() != y:
                    y = row[2].strip()
                    print("EP072014,          GENEVIEVE,     87,")
                if (360-(float(row[6])) > 180):
                    x = str(round(360-(360-(float(row[6]))), 1)) + "E"
                else:
                    x = str(round((360-(float(row[6]))), 1)) + "W"
                #print(F"20000101, 0000, , HU,{row[5]}S, {x}, {round(float(row[8]) * 2.25)}, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999,")
                print(F"20000101, 0000, , HU,{row[5]}N, {round(360-(float(row[6])), 1)}W, {round(float(row[8]) * 2.25)}, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999,")

print("EP072014,          GENEVIEVE,     87,")