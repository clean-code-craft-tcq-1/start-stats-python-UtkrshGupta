import statistics 
import numpy as np

def calculateStats(numbers):
    compStats = {'avg': 0 , 'min': 0,'max': 0 }
    if not numbers:
        for key in compStats.keys:
            if key == 'avg':
                compStats[key] = np.nan
            elif key == 'min':
                compStats[key] = np.nan
            elif key == 'max':
                compStats[key] = np.nan       
    else:
        for key in compStats.keys:
            if key == 'avg':
                compStats[key] = statistics.mean(numbers)
            elif key == 'min':
                compStats[key] = np.min(numbers)
            elif key == 'max':
                compStats[key] = np.max(numbers)                
    
    return compStats
