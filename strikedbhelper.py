from datetime import datetime

def uuidAndNameToString(uuidAndname):
    return str(uuidAndname).split(":")[1]


def timestampToString(timestamp):
    ts = int(timestamp)
    # ts = int("1284101485")

    # if you encounter a "year is out of range" error the timestamp
    # may be in milliseconds, try `ts /= 1000` in that case
    return datetime.utcfromtimestamp(ts/1000).strftime('%Y-%m-%d %H:%M:%S')
    # s = datetime.utcfromtimestamp(ts/1000)
    # s = s.strftime('%Y-%m-%d %H:%M:%S')
    # s = str(s)
    # print(s)
    # return s

def kitinfoToLines(kitinfo):
    lines=str(kitinfo).split(":")
    html=""
    for line in lines:
        html+=line+"</br>"
    return html

def stripMinecraftColorCode(s):
    line=str(s)
    line=line.replace("§e","")
    line=line.replace("§l","")
    return line
