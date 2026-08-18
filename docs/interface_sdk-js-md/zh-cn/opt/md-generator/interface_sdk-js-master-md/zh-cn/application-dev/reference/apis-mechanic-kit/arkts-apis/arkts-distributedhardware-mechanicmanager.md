# @ohos.distributedHardware.mechanicManager

提供与本设备连接的机械设备的控制和交互能力。 包括连接管理、控制和监控功能

**起始版本：** 23

<!--Device-unnamed-declare namespace mechanicManager--><!--Device-unnamed-declare namespace mechanicManager-End-->

**系统能力：** SystemCapability.Mechanic.Core

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [getAttachedMechDevices](arkts-mechanic-mechanicmanager-getattachedmechdevices-f.md#getattachedmechdevices) |
| [getCameraTrackingEnabled](arkts-mechanic-mechanicmanager-getcameratrackingenabled-f.md#getcameratrackingenabled) |
| [getCameraTrackingLayout](arkts-mechanic-mechanicmanager-getcameratrackinglayout-f.md#getcameratrackinglayout) |
| [isControlSupported](arkts-mechanic-mechanicmanager-iscontrolsupported-f.md#iscontrolsupported) |
| [offAttachStateChange](arkts-mechanic-mechanicmanager-offattachstatechange-f.md#offattachstatechange) |
| [offTrackingStateChange](arkts-mechanic-mechanicmanager-offtrackingstatechange-f.md#offtrackingstatechange) |
| [off_attachStateChange](arkts-mechanic-mechanicmanager-offattachstatechange-f.md#offattachstatechange) |
| [off_trackingStateChange](arkts-mechanic-mechanicmanager-offtrackingstatechange-f.md#offtrackingstatechange) |
| [onAttachStateChange](arkts-mechanic-mechanicmanager-onattachstatechange-f.md#onattachstatechange) |
| [onTrackingStateChange](arkts-mechanic-mechanicmanager-ontrackingstatechange-f.md#ontrackingstatechange) |
| [on_attachStateChange](arkts-mechanic-mechanicmanager-onattachstatechange-f.md#onattachstatechange) |
| [on_trackingStateChange](arkts-mechanic-mechanicmanager-ontrackingstatechange-f.md#ontrackingstatechange) |
| [setCameraTrackingEnabled](arkts-mechanic-mechanicmanager-setcameratrackingenabled-f.md#setcameratrackingenabled) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [connectDevice](arkts-mechanic-mechanicmanager-connectdevice-f-sys.md#connectdevice系统接口) |
| [disconnectDevice](arkts-mechanic-mechanicmanager-disconnectdevice-f-sys.md#disconnectdevice系统接口) |
| [doAction](arkts-mechanic-mechanicmanager-doaction-f-sys.md#doaction系统接口) |
| [getCurrentAngles](arkts-mechanic-mechanicmanager-getcurrentangles-f-sys.md#getcurrentangles系统接口) |
| [getMaxRotationSpeed](arkts-mechanic-mechanicmanager-getmaxrotationspeed-f-sys.md#getmaxrotationspeed系统接口) |
| [getMaxRotationTime](arkts-mechanic-mechanicmanager-getmaxrotationtime-f-sys.md#getmaxrotationtime系统接口) |
| [getRotationAxesStatus](arkts-mechanic-mechanicmanager-getrotationaxesstatus-f-sys.md#getrotationaxesstatus系统接口) |
| [getRotationLimits](arkts-mechanic-mechanicmanager-getrotationlimits-f-sys.md#getrotationlimits系统接口) |
| [isSupportAction](arkts-mechanic-mechanicmanager-issupportaction-f-sys.md#issupportaction系统接口) |
| [move](arkts-mechanic-mechanicmanager-move-f-sys.md#move系统接口) |
| [moveBySpeed](arkts-mechanic-mechanicmanager-movebyspeed-f-sys.md#movebyspeed系统接口) |
| [offRotationAxesStatusChange](arkts-mechanic-mechanicmanager-offrotationaxesstatuschange-f-sys.md#offrotationaxesstatuschange) |
| [off_rotationAxesStatusChange](arkts-mechanic-mechanicmanager-offrotationaxesstatuschange-f-sys.md#offrotationaxesstatuschange) |
| [onRotationAxesStatusChange](arkts-mechanic-mechanicmanager-onrotationaxesstatuschange-f-sys.md#onrotationaxesstatuschange) |
| [on_rotationAxesStatusChange](arkts-mechanic-mechanicmanager-onrotationaxesstatuschange-f-sys.md#onrotationaxesstatuschange) |
| [rotate](arkts-mechanic-mechanicmanager-rotate-f-sys.md#rotate系统接口) |
| [rotateBySpeed](arkts-mechanic-mechanicmanager-rotatebyspeed-f-sys.md#rotatebyspeed系统接口) |
| [rotateToEulerAngles](arkts-mechanic-mechanicmanager-rotatetoeulerangles-f-sys.md#rotatetoeulerangles系统接口) |
| [searchTarget](arkts-mechanic-mechanicmanager-searchtarget-f-sys.md#searchtarget系统接口) |
| [setCameraTrackingLayout](arkts-mechanic-mechanicmanager-setcameratrackinglayout-f-sys.md#setcameratrackinglayout系统接口) |
| [setUserOperation](arkts-mechanic-mechanicmanager-setuseroperation-f-sys.md#setuseroperation系统接口) |
| [stopMoving](arkts-mechanic-mechanicmanager-stopmoving-f-sys.md#stopmoving系统接口) |
| [subscribe](arkts-mechanic-mechanicmanager-subscribe-f-sys.md#subscribe系统接口) |
| [turnBySpeed](arkts-mechanic-mechanicmanager-turnbyspeed-f-sys.md#turnbyspeed系统接口) |
| [unSubscribe](arkts-mechanic-mechanicmanager-unsubscribe-f-sys.md#unsubscribe系统接口) |
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
