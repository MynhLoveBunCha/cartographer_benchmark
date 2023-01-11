#!/bin/bash

mate-terminal --title="localization" -e "bash -c 'cd /home/$USER/catkin_ws && source install_isolated/setup.bash && roslaunch cartographer_ros demo_backpack_2d_localization.launch \
   load_state_filename:=${HOME}/Downloads/b2-2016-04-05-14-44-52.bag.pbstream \
   bag_filename:=${HOME}/Downloads/b2-2016-04-27-12-31-41.bag'"
