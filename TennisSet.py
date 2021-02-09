def tennisSet(score1, score2):
    if not (0 <= score1 < 8 and 0 <= score2 < 8):
        return False
    elif score1 < 6 and score2 < 6:
        return False
    elif (score1 == 6 and score2 == 5) or (score1 == 5 and score2 == 6) or (score1 == 6 and score2 == 6):
        return False
    elif (score1 == 6 or score2 == 6) or (score1 == 5 and score2 == 7) or (score1 == 7 and score2 == 5):
        return True
    else:
        return False
