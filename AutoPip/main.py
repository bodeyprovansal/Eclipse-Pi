import json

from EclipseInterface import EclipseInterface 
from TestMeasurement import SingleTestMeasurement
from TestScript import TestScript

newScript = TestScript('script.JSON')
print("---- Start -----")
#newScript.showCommands()
newScript.runCommands()
print("---- End -----")

