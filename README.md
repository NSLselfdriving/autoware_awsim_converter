# autoware_awsim_converter

## 概要
autowareとAWSIMのROS2のトピックの互換性を保つための変換パッケージ

## 使い方
以下のノードを実行します
- control_mode_subscribe_node
- control_publish_node
- engage_publish_node
- gear_publish_node
- gear_subscribe_node
- steering_subscribe_node
- velocity_subscribe_node

```bash
colcon build --symlink-install
source install/setup.bash
ros2 run autoware_awsim_connect <node名>
```


また、以下の手順で、上記のノードをまとめて起動することができます


1. setup.py内の該当するコメントアウトを解除します
```bash
import os
from glob import glob
```

```bash
 (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
```
2. ワークスペースで以下のようにlaunchファイルを実行します
```bash
ros2 launch autoware_awsim_connect connect_launch.py
ros2 launch <パッケージ名> <launchファイル名>
```
