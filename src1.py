import tgod

def get_bus():
    df = tgod.taipei_transport.bus()
    entries = []
    for i in range(len(df)):
        a = df.iloc[i]
        x = a['Longitude']
        y = a['Latitude']
        p = a['BusID']
        s = a['Speed']
        pt = dict(x=x, y=y, p=p,s=s)
        entries.append(pt)
    return entries

def get_ubike():
    df = tgod.taipei_transport.bikeshare()
    entries = []
    for i in range(len(df)):
        a = df.iloc[i]
        x = a['lng']
        y = a['lat']
        n = a['sna']
        b = a['bemp']
        c = a['sbi']
        pt = dict(x=x, y=y, n=n, b=b, c=c)
        entries.append(pt)
    return entries
