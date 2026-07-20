# Message Pub Sub Example

### Test 1 with 2 windows
```bash
$ ros2 run pub_sub_pkg sub_node_exe
$ ros2 run pub_sub_pkg pub_node_exe
``` 


### Test 2: outputs from 2 nodes are interleaved in the same window
```bash
$ ros2 launch pub_sub_pkg pub_sub.launch.py
``` 

### Test 3 with 2 xterm windows
```bash
$ ros2 launch pub_sub_pkg pub_sub_xterm.launch.py
``` 