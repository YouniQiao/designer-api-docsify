# @ohos.distributedHardware.mechanicManager

提供与本设备连接的机械设备的控制和交互能力。 包括连接管理、控制和监控功能@namespace mechanicManager

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Mechanic.Core

## 导入模块

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getAttachedMechDevices](arkts-mechanic-mechanicmanager-getattachedmechdevices-f.md) |
| [getCameraTrackingEnabled](arkts-mechanic-mechanicmanager-getcameratrackingenabled-f.md) |
| [getCameraTrackingLayout](arkts-mechanic-mechanicmanager-getcameratrackinglayout-f.md) |
| [isControlSupported](arkts-mechanic-mechanicmanager-iscontrolsupported-f.md) |
| [off](arkts-mechanic-mechanicmanager-off-f.md#offattachstatechange) |
| [off](arkts-mechanic-mechanicmanager-off-f.md#offtrackingstatechange) |
| [offAttachStateChange](arkts-mechanic-mechanicmanager-offattachstatechange-f.md) |
| [offTrackingStateChange](arkts-mechanic-mechanicmanager-offtrackingstatechange-f.md) |
| [on](arkts-mechanic-mechanicmanager-on-f.md#onattachstatechange) |
| [on](arkts-mechanic-mechanicmanager-on-f.md#ontrackingstatechange) |
| [onAttachStateChange](arkts-mechanic-mechanicmanager-onattachstatechange-f.md) |
| [onTrackingStateChange](arkts-mechanic-mechanicmanager-ontrackingstatechange-f.md) |
| [setCameraTrackingEnabled](arkts-mechanic-mechanicmanager-setcameratrackingenabled-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [connectDevice](arkts-mechanic-mechanicmanager-connectdevice-f-sys.md) |
| [disconnectDevice](arkts-mechanic-mechanicmanager-disconnectdevice-f-sys.md) |
| [doAction](arkts-mechanic-mechanicmanager-doaction-f-sys.md) |
| [getCurrentAngles](arkts-mechanic-mechanicmanager-getcurrentangles-f-sys.md) |
| [getMaxRotationSpeed](arkts-mechanic-mechanicmanager-getmaxrotationspeed-f-sys.md) |
| [getMaxRotationTime](arkts-mechanic-mechanicmanager-getmaxrotationtime-f-sys.md) |
| [getRotationAxesStatus](arkts-mechanic-mechanicmanager-getrotationaxesstatus-f-sys.md) |
| [getRotationLimits](arkts-mechanic-mechanicmanager-getrotationlimits-f-sys.md) |
| [isSupportAction](arkts-mechanic-mechanicmanager-issupportaction-f-sys.md) |
| [move](arkts-mechanic-mechanicmanager-move-f-sys.md) |
| [moveBySpeed](arkts-mechanic-mechanicmanager-movebyspeed-f-sys.md) |
| [off](arkts-mechanic-mechanicmanager-off-f-sys.md#offrotationaxesstatuschange) |
| [offRotationAxesStatusChange](arkts-mechanic-mechanicmanager-offrotationaxesstatuschange-f-sys.md) |
| [on](arkts-mechanic-mechanicmanager-on-f-sys.md#onrotationaxesstatuschange) |
| [onRotationAxesStatusChange](arkts-mechanic-mechanicmanager-onrotationaxesstatuschange-f-sys.md) |
| [rotate](arkts-mechanic-mechanicmanager-rotate-f-sys.md) |
| [rotateBySpeed](arkts-mechanic-mechanicmanager-rotatebyspeed-f-sys.md) |
| [rotateToEulerAngles](arkts-mechanic-mechanicmanager-rotatetoeulerangles-f-sys.md) |
| [searchTarget](arkts-mechanic-mechanicmanager-searchtarget-f-sys.md) |
| [setCameraTrackingLayout](arkts-mechanic-mechanicmanager-setcameratrackinglayout-f-sys.md) |
| [setUserOperation](arkts-mechanic-mechanicmanager-setuseroperation-f-sys.md) |
| [stopMoving](arkts-mechanic-mechanicmanager-stopmoving-f-sys.md) |
| [subscribe](arkts-mechanic-mechanicmanager-subscribe-f-sys.md) |
| [turnBySpeed](arkts-mechanic-mechanicmanager-turnbyspeed-f-sys.md) |
| [unSubscribe](arkts-mechanic-mechanicmanager-unsubscribe-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AttachStateChangeInfo](arkts-mechanic-mechanicmanager-attachstatechangeinfo-i.md) |
| [MechInfo](arkts-mechanic-mechanicmanager-mechinfo-i.md) |
| [TrackingEventInfo](arkts-mechanic-mechanicmanager-trackingeventinfo-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AddressInfo](arkts-mechanic-mechanicmanager-addressinfo-i-sys.md) |
| [ConnectParam](arkts-mechanic-mechanicmanager-connectparam-i-sys.md) |
| [EulerAngles](arkts-mechanic-mechanicmanager-eulerangles-i-sys.md) |
| [MechEvent](arkts-mechanic-mechanicmanager-mechevent-i-sys.md) |
| [MoveParams](arkts-mechanic-mechanicmanager-moveparams-i-sys.md) |
| [RotationAngles](arkts-mechanic-mechanicmanager-rotationangles-i-sys.md) |
| [RotationAxesStateChangeInfo](arkts-mechanic-mechanicmanager-rotationaxesstatechangeinfo-i-sys.md) |
| [RotationAxesStatus](arkts-mechanic-mechanicmanager-rotationaxesstatus-i-sys.md) |
| [RotationLimits](arkts-mechanic-mechanicmanager-rotationlimits-i-sys.md) |
| [RotationSpeed](arkts-mechanic-mechanicmanager-rotationspeed-i-sys.md) |
| [SearchParams](arkts-mechanic-mechanicmanager-searchparams-i-sys.md) |
| [SearchResult](arkts-mechanic-mechanicmanager-searchresult-i-sys.md) |
| [SpeedParams](arkts-mechanic-mechanicmanager-speedparams-i-sys.md) |
| [TargetInfo](arkts-mechanic-mechanicmanager-targetinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AttachState](arkts-mechanic-mechanicmanager-attachstate-e.md) |
| [CameraTrackingLayout](arkts-mechanic-mechanicmanager-cameratrackinglayout-e.md) |
| [MechDeviceType](arkts-mechanic-mechanicmanager-mechdevicetype-e.md) |
| [TrackingEvent](arkts-mechanic-mechanicmanager-trackingevent-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ActionType](arkts-mechanic-mechanicmanager-actiontype-e-sys.md) |
| [AddressType](arkts-mechanic-mechanicmanager-addresstype-e-sys.md) |
| [MarchingMode](arkts-mechanic-mechanicmanager-marchingmode-e-sys.md) |
| [MechDeviceType](arkts-mechanic-mechanicmanager-mechdevicetype-e-sys.md) |
| [MechEventType](arkts-mechanic-mechanicmanager-mecheventtype-e-sys.md) |
| [Operation](arkts-mechanic-mechanicmanager-operation-e-sys.md) |
| [Result](arkts-mechanic-mechanicmanager-result-e-sys.md) |
| [RotationAxisLimited](arkts-mechanic-mechanicmanager-rotationaxislimited-e-sys.md) |
| [SearchDirection](arkts-mechanic-mechanicmanager-searchdirection-e-sys.md) |
| [SpeedGear](arkts-mechanic-mechanicmanager-speedgear-e-sys.md) |
| [TargetType](arkts-mechanic-mechanicmanager-targettype-e-sys.md) |
<!--DelEnd-->
