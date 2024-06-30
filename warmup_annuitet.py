def annual_return(start, percent, years):
    n = 0
    while n < years:
        result = start + start * percent/100
        yield result
        start = result
        n += 1


for value in annual_return(70000, 8, 10):
    print(round(value))
