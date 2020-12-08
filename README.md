# tello-drone-controls
Python bindings to interact with the DJI Ryze Tello Drone.

## Dependencies
* Python 3.x.x
* opencv-python
* Python h264decoder

## Features
* Pilot drone with PC using customizable keyboard shortcuts (no joystick or controller necessary)
* View drone video stream from PC in realtime

### Current Key Bindings
| Key Binding | Control | Action |
| :---:   | :----:      | :----: |
|  `Enter` |take off | take off |
| `space` | land    |  land |
|  `w` | increase throttle | ascend |
| `s` | decrease throttle | descend |
| `a` | yaw left | rotate counter-clockwise |
| `d` | yaw right | rotate clockwise |
| `right arrow` | roll left | move left |
| `left arrow` | roll right | move right |

## References
* [https://github.com/dji-sdk/Tello-Python](https://github.com/dji-sdk/Tello-Python)
