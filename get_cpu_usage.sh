top -p $(pidof cartographer_offline_node) -b > carto_mapping.txt
top -p $(pidof cartographer_node) -b > carto_localization.txt
