# Message Pub Sub Example

### Test 1 with 2 windows
```bash
$ ros2 run pub_sub_pkg pub_sub_node
$ ros2 run pub_sub_pkg pub_sub_node
``` 


### Test 2: outputs from 2 nodes are interleaved in the same window
```bash
$ ros2 launch pub_sub_pkg pub_sub_pkg.launch.py
``` 

### Test 3 with 2 xterm windows
```bash
$ ros2 launch pub_sub_pkg pub_sub_pkg.xlaunch.py
``` 