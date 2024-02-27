
#V1 of the grade scale print
print('Grade ranges:' '\n' + str(round(points_var, ndigits = 2)) + ' - ' + str(round(points_var - result[0], ndigits = 2)) + ' points:  1' '\n' + 
        str(round(points_var - result[0] - 1, ndigits = 2)) + ' - ' + str(round(points_var - (result[0] + result[1]), ndigits = 2)) + ' points:  2' '\n' + 
        str(round(points_var - (result[0] + result[1]) - 1, ndigits = 2)) + ' - ' + str(round(points_var - (result[0] + result[1] + result[2]), ndigits = 2)) + ' points:  3' '\n' + 
        str(round(points_var - (result[0] + result[1] + result[2]) - 1, ndigits = 2)) + ' - ' + str(round(points_var - (result[0] + result[1] + result[2] + result[3]), ndigits = 2)) + ' points:  4' '\n' + 
        str(round(points_var - (result[0] + result[1] + result[2] + result[3]) - 1, ndigits = 2)) + ' - ' + str(round(points_var - (result[0] + result[1] + result[2] + result[3] + result[4]), ndigits = 2)) + ' points:  5')

#extra line in front of V2 grade scale print that uses a loop, needed to ensure proper function while using the loop for the rest of
#the grades except the first one, which uses a slightly different formula
print('Grade ranges:' '\n' + str(round(points_var)) + ' - ' + str(round(points_var - result[0])) + ': 1')