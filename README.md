# Added support for reading turtlebot manipulator urdf and generating associated homogenous transformation matrix. 

# Generating URDF from xacro for adding new robot support


```bash
rosrun xacro xacro -o <target-name.urdf> <path-to-xacro-file.xacro>
```

This generates urdf. Sometimes you might have to change the package:/ -> relative-path-for-meshes


# Installation

This package provides a forward kinematics for simple robots as symbolic functions using
casadi. This allows the usage in model predictive control schemes and other trajectory
optimization methods.

```bash
pip3 install forwardkinematics
```

## Install in editable mode

If you want to install as an editable without the usage of an virtual environment, you
must create a setup.py first.
This can be done using poetry2setup (`pip install poetry2setup`)
Then you can run 
```bash
poetry2setup > setup.py
mv pyproject.toml pyproject.toml_BACKUP
pip3 install -e .
```
