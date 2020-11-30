import py_trees
from math import pi

class BaseBehavior(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(BaseBehavior, self).__init__(name)
        self.log("__init__")

    def setup(self, timeout=15):
        super(BaseBehavior, self).setup(timeout)
        self.log("setup")
        return True
    
    def mirror_radians(self, angle):
        if angle < pi:
            return angle
        else:
            return angle- 2*pi

    def log(self, str, vals = None):
        if (vals is  None):
            print(("%s:  " + str) % self.name)
        else:
            print(("%s:"+str+" %s") % (self.name, vals))


    
    
