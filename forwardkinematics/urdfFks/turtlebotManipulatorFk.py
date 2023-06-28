import numpy as np
import casadi as ca
from forwardkinematics.urdfFks.urdfFk import URDFForwardKinematics


class TurtlebotManipulatorFk(URDFForwardKinematics):
    def __init__(self):
        fileName = "turtlebot_manipulator_model.urdf"
        relevantLinks = ["base_footprint", "base_link","link1","link2","link3", "link4", "link5"] 
        # + [
            # "panda_link" + str(i) for i in [0, 3, 4, 5, 6, 7, 8, 9]
        # ]
        super().__init__(fileName, relevantLinks, "base_footprint", "link5", 6)