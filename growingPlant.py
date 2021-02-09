def growingPlant(upSpeed, downSpeed, desiredHeight):
    a = desiredHeight - upSpeed
    if a >= 0:
        diff = upSpeed-downSpeed
        nDays = int(a/diff)
        if a%diff != 0:
            nDays = nDays + 1
    else:
        nDays = 0
    return nDays + 1