def calculateStats(numbers):
    compStats = {'avg': 0 , 'min': 0,'max': 0 }
    if not numbers:
        compStats['avg'] = 'nan'
        compStats['min'] = 'nan'
        compStats['max'] = 'nan'
    else:
        for num in numbers:
            compStats['avg'] += num
            compStats['min'] = min(numbers)
            compStats['max'] = max(numbers)                
        compStats['avg'] /= len(numbers)
    return compStats
