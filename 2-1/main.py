with open('spreadsheet.txt') as f:
    spreadsheet = f.readlines()

checksum = 0
for row in spreadsheet:
    row = row.split()
    high = int(row[0])
    low = int(row[0])
    
    for cell in row:
        cell = int(cell)
        if cell > high:
            high = cell
        if cell < low:
            low = cell

    checksum = checksum + (high - low)

print(checksum)
