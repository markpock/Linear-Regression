from Utility import Point

def find_values(plist):
    intercept = 0
    xcent = 0
    for p in plist:
        intercept += p.y
        xcent += p.x
    return intercept / len(plist), xcent / len(plist)


def alter_list(plist, intercept, xcent):
    newlist = []
    for p in plist:
        newlist.append(Point(p.x - xcent, p.y - intercept))
    return newlist


def find_slope(altlist):
    slope, maxpt, minpt = 1, altlist[0], altlist[0]
    maesn = [maes(slope, altlist)]
    for p in altlist:
        if p.y > maxpt.y:
            maxpt = p
        if p.y < minpt.y:
            minpt = p
    range = maxpt.y - minpt.y
    avg = roll10avg(maesn)
    while maesn[-1] >= avg + avg / 100:
        betaval = (maesn[-1] * slope) / range
        lslope, gslope = slope - betaval, slope + betaval
        lmaes = maes(lslope, altlist)
        gmaes = maes(gslope, altlist)
        while (lmaes > maesn[-1] and gmaes > maesn[-1]):
            betaval = betaval / 2
            lslope, gslope = slope - betaval, slope + betaval
            lmaes = maes(lslope, altlist)
            gmaes = maes(gslope, altlist)
        if lmaes > gmaes:
            slope = gslope
        else:
            slope = lslope
        maesn.append(maes(slope, altlist))
        avg = roll10avg(maesn)
    return slope


def roll10avg(maesn):
    sum, bound = 0, 11
    if len(maesn) < bound:
        bound = len(maesn)
    for i in range(1, bound):
        sum += maesn[-1 * i]
    return sum / (bound)


def maes(slope, altlist):
    aes = 0
    for p in altlist:
        aes += (p.y - (slope * p.x)) ** 2
    return aes / len(altlist)


def exec_regression(plist):
    intercept, xcent = find_values(plist)
    slope = find_slope(alter_list(plist, intercept, xcent))
    return slope, intercept, xcent