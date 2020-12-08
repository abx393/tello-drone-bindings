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
| :---:   | :----:    | :----: |
|  `Enter` | take off | take off |
| `space` | land    |  land |
|  `w` | increase throttle | ascend |
| `s` | decrease throttle | descend |
| `a` | yaw left | rotate counter-clockwise |
| `d` | yaw right | rotate clockwise |
| `<left>` | roll left | move left |
| `<right>` | roll right | move right |
| `<up>` | pitch forward | move forward |
| `<down>` | pitch backward | move backward |
| `f` | flip | 360&deg; flip |

## References
* [https://github.com/dji-sdk/Tello-Python](https://github.com/dji-sdk/Tello-Python)
