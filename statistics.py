def calculateStats(numbers):
    compStats = {'avg': 0 , 'min': 0,'max': 0 }
    if not numbers:
        for key in compStats.keys:
            if key == 'avg':
                compStats[key] = float('nan')
            elif key == 'min':
                compStats[key] = float('nan')
            elif key == 'max':
                compStats[key] = float('nan')
    else:
        for num in numbers:
            compStats['avg'] += num
            compStats['min'] = min(numbers)
            compStats['max'] = max(numbers)                
        compStats['avg'] /= len(numbers)
    return compStats
