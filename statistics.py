def calculateStats(numbers):
    compStats = {'avg': 0 , 'min': 0,'max': 0 }
    if not numbers:
        compStats['avg'] = float('nan')
        compStats['min'] = float('nan')
        compStats['max'] = float('nan')
    else:
        for num in numbers:
            compStats['avg'] += num
            compStats['min'] = min(numbers)
            compStats['max'] = max(numbers)                
        compStats['avg'] /= len(numbers)
    return compStats
