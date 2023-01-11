#!/bin/bash

mate-terminal --title="Mapping" -e "bash -c 'cd /home/$USER/catkin_ws && source install_isolated/setup.bash && roslaunch cartographer_ros offline_backpack_2d.launch bag_filenames:=${HOME}/Downloads/b2-2016-04-05-14-44-52.bag'" 
