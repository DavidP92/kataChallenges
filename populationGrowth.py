def nb_year(p0, percent, aug, p):
    years = 0
    while p0 <= p:                                    ## While our population growth is lower than the given limit, we will run the formula
        p0 = p0 + p0 * (float((percent)/100)) + aug
        years = years + 1
    return years
