import json

from TestScript import TestScript

newScript = TestScript('script.JSON')
print("---- Start -----")
#newScript.showCommands()
newScript.runCommands()
print("---- End -----")

