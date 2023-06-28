import casadi as ca
import numpy as np
from forwardkinematics.urdfFks.turtlebotManipulatorFk import TurtlebotManipulatorFk

import autograd.numpy as gnp

def main():
    q_ca = ca.SX.sym("q", 5)
    fk_panda = TurtlebotManipulatorFk()
    # q_np = np.random.random(5)
    # fk_casadi = fk_panda.fk(q_ca, 2, positionOnly=False)
    # fk_numpy = fk_panda.fk(q_np, 2, positionOnly=False)
    # print(fk_numpy)
    print("_________________________________________________ ")
    fk_casadi = fk_panda.fk(q_ca, 1, positionOnly=False)
    print(fk_casadi)
    print("_________________________________________________ ")
    fk_casadi = fk_panda.fk(q_ca, 2, positionOnly=False)
    print(fk_casadi)
    print("_________________________________________________ ")
    fk_casadi = fk_panda.fk(q_ca, 3, positionOnly=False)
    print(fk_casadi)
    print("_________________________________________________ ")


    fk_casadi = fk_panda.fk(q_ca, 4, positionOnly=False)
    print(fk_casadi)
    print("_________________________________________________ ")
    fk_casadi = fk_panda.fk(q_ca, 5, positionOnly=False)
    print(fk_casadi)
    print("_________________________________________________ ")
    print(type(fk_casadi))
    print(fk_casadi.elements())

    # fk_casadi_by_name = fk_panda.fk_by_name(
    #     q_ca, "panda_rightfinger", positionOnly=True
    # )
    # print(fk_casadi_by_name)


if __name__ == "__main__":
    main()

[SX(@1=cos(q_0), (((@1*cos(q_1))*cos(q_2))-((@1*sin(q_1))*sin(q_2)))), 
 SX(@1=sin(q_0), (((@1*cos(q_1))*cos(q_2))-((@1*sin(q_1))*sin(q_2)))), 
 SX((-((sin(q_1)*cos(q_2))+(cos(q_1)*sin(q_2))))), 
 SX(0), 
 SX((-sin(q_0))), 
 SX(cos(q_0)), 
 SX(0), 
 SX(0), 
 SX(@1=cos(q_0), (((@1*cos(q_1))*sin(q_2))+((@1*sin(q_1))*cos(q_2)))), 
 SX(@1=sin(q_0), (((@1*cos(q_1))*sin(q_2))+((@1*sin(q_1))*cos(q_2)))), 
 SX(((cos(q_1)*cos(q_2))-(sin(q_1)*sin(q_2)))), 
 SX(0), 
 SX(@1=cos(q_0), (((0.024*(@1*cos(q_1)))+(0.128*(@1*sin(q_1))))+-0.08)), 
 SX(@1=sin(q_0), ((0.024*(@1*cos(q_1)))+(0.128*(@1*sin(q_1))))), 
 SX((((0.128*cos(q_1))-(0.024*sin(q_1)))+0.176)), 
 SX(1)]