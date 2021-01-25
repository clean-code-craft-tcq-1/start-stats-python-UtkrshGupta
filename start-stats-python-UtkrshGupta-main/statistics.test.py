import unittest
import statistics
import numpy as np

class EmailAlert():
    def __init__(self, threshold=0):
        self.threshold = threshold
    def emailSent():
        return False 
    
class LEDAlert():
    def ledGlows():
        return True
    
class StatsAlerter(): 
    def __init__(self, maxThreshold, object_li):
        self.maxThreshold = maxThreshold
        self.object_li = object_li
    def checkAndAlert(self, threshold_li):
        for threshold in threshold_li:
            if threshold < self.maxThreshold:
                self.object_li[0].__init__(threshold =threshold)

class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], np.nan, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], np.nan, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], np.nan, delta=epsilon)    
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Design the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html

  def test_raise_alerts_when_max_above_threshold(self):
    emailAlert = EmailAlert()
    ledAlert = LEDAlert()
    maxThreshold = 10.5
    statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
    statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent)
    self.assertTrue(ledAlert.ledGlows)

if __name__ == "__main__":
  unittest.main()
