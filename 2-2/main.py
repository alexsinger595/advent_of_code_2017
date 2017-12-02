with open('spreadsheet.txt') as f:
    spreadsheet = f.readlines()

checksum = 0
for row in spreadsheet:
    row = [int(i) for i in row.split()]

    high = row[0]
    low = row[0]
    
    for value in row:
        for cell in row:
            if value != cell and value / cell % 1 == 0:
                checksum = checksum + int(value / cell)


print(checksum)
