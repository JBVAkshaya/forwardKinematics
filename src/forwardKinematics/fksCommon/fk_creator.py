import casadi as ca
from forwardKinematics.urdfFks.pandaFk import PandaFk
from forwardKinematics.urdfFks.mobilePandaFk import MobilePandaFk
from forwardKinematics.urdfFks.tiagoFk import TiagoFk
from forwardKinematics.planarFks.planarArmFk import PlanarArmFk
from forwardKinematics.planarFks.groundRobotFk import GroundRobotFk
from forwardKinematics.planarFks.pointFk import PointFk


class FkCreator(object):
    def __init__(self, robotType, n):
        if robotType == 'panda':
            self._fk = PandaFk(n)
        elif robotType == 'tiago':
            self._fk = TiagoFk(n-4)
        elif robotType == 'planarArm':
            self._fk = PlanarArmFk(n)
        elif robotType == 'mobilePanda':
            self._fk = MobilePandaFk(n)
        elif robotType == 'pointRobot' or robotType == 'pointMass':
            self._fk = PointFk(n)
        elif robotType == 'groundRobot':
            self._fk = GroundRobotFk(n)

    def fk(self):
        return self._fk


if __name__ == "__main__":
    fk = FkCreator('groundRobot', 2).fk()
    q_ca = ca.SX.sym('q', fk.n())
    fk = fk.fk(q_ca, fk.n(), positionOnly=True)
    print(fk)
