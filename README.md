# TAFRC

TAFRC is a physics library intended for use in the FIRST Robotics Competition (hence the name tool-assisted FRC).

It consists of a few modules written to simulate the trajectory of field elements on the competition field.

The trajectory simulation is done through the modules that will eventually end up on the software for our robot in the upcoming season.

## Usage
Download the folder `tafrc_ui` which contains the the module `tafrc_ui/trajectory.py` and the GUI `tafrc_ui/tafrc_UI.py`.

To run the simulation GUI, run

```python3 tafrc_UI.py```
## Calculations

Most of the trajectory calculations comprise of kinematics that are easily computable:

The calculator takes in an input vector **R** which is the 3-dimensional distance between the robot shooter and the target location.

![image](https://user-images.githubusercontent.com/62197882/145667121-eadbc798-622b-4cde-bd27-a77fcf90f717.png)

The orientation of the shooter from the goal is input as spherical coordinates - with `theta_vertical` being Φ and `theta_horizontal` being Θ.
The library uses spherical coordinates that are split into rectangular form during the calculation.

![image](https://user-images.githubusercontent.com/62197882/145667288-ced49828-b0bd-4fec-826d-a44a87c1acf8.png)

With the vector **R** and the height of the shooter given, the calculations split **R** into component vectors and evaluate the kinematics for each dimension, 
after splitting the initial velocity into component vectors. 

![image](https://user-images.githubusercontent.com/62197882/145667353-ca23dbb5-0087-4da0-a105-804cd8904ce5.png)

![image](https://user-images.githubusercontent.com/62197882/145667357-30d90b11-f91c-49b5-b1fd-909a31aa4e7b.png)

![image](https://user-images.githubusercontent.com/62197882/145667390-bcdd3d9d-292e-45a4-bafe-59f0bbd2fef7.png)

The UI takes these values and displays them accordingly, along with the position of the target to assist with aiming.

## Competition and Previous Experience

This module was made due to my experiences in FRC in the 2019-2020 season. Our robot previously had difficulties taking advantage of our sensors that could detect the reflective tape located on the target goal:

![image](https://user-images.githubusercontent.com/62197882/145667535-ce412c69-6019-4634-b12f-7e3e41c27106.png)

Our sensors were imprecise, and our autonomous phase during the competition was sloppy. However, this year, our team has purchased a new sensor with much stronger and precise measurement capabilities, that send data on the distance of the reflective tape from the sensor, as well as the angle of the target from the sensor.

This library was made to assist our team, as well as any other FRC teams looking to improve the aiming on their robots, which ended up being extremely inaccurate during the competition for most robots. 
