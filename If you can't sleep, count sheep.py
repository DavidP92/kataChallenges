def count_sheep(n):
    output = ""                        ##First we will make a variable output that will store our phrase each cycle and print
    for x in range(1, n+1):            ## Second we will start (x) from 1 and go to n+1
        output += str(x) + ' sheep...' ## Now we will store the phrase within output with the number variable
    return output                      ## Now print to screen the output
