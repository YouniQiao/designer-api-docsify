# @ohos.distributedHardware.mechanicManager

Provides capabilities for controlling and interacting with mechanical devices connected to this device.The capabilities cover connection management, control, and monitoring.

**Since:** 20

<!--Device-unnamed-declare namespace mechanicManager--><!--Device-unnamed-declare namespace mechanicManager-End-->

**System capability:** SystemCapability.Mechanic.Core

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAttachedMechDevices](arkts-mechanic-mechanicmanager-getattachedmechdevices-f.md#getattachedmechdevices) |
| [getCameraTrackingEnabled](arkts-mechanic-mechanicmanager-getcameratrackingenabled-f.md#getcameratrackingenabled) |
| [getCameraTrackingLayout](arkts-mechanic-mechanicmanager-getcameratrackinglayout-f.md#getcameratrackinglayout) |
| [isControlSupported](arkts-mechanic-mechanicmanager-iscontrolsupported-f.md#iscontrolsupported) |
| [off](arkts-mechanic-mechanicmanager-off-f.md#off) |
| [off](arkts-mechanic-mechanicmanager-off-f.md#off-1) |
| [on](arkts-mechanic-mechanicmanager-on-f.md#on) |
| [on](arkts-mechanic-mechanicmanager-on-f.md#on-1) |
| [setCameraTrackingEnabled](arkts-mechanic-mechanicmanager-setcameratrackingenabled-f.md#setcameratrackingenabled) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [connectDevice](arkts-mechanic-mechanicmanager-connectdevice-f-sys.md#connectdevice) |
| [disconnectDevice](arkts-mechanic-mechanicmanager-disconnectdevice-f-sys.md#disconnectdevice) |
| [doAction](arkts-mechanic-mechanicmanager-doaction-f-sys.md#doaction) |
| [getCurrentAngles](arkts-mechanic-mechanicmanager-getcurrentangles-f-sys.md#getcurrentangles) |
| [getMaxRotationSpeed](arkts-mechanic-mechanicmanager-getmaxrotationspeed-f-sys.md#getmaxrotationspeed) |
| [getMaxRotationTime](arkts-mechanic-mechanicmanager-getmaxrotationtime-f-sys.md#getmaxrotationtime) |
| [getRotationAxesStatus](arkts-mechanic-mechanicmanager-getrotationaxesstatus-f-sys.md#getrotationaxesstatus) |
| [getRotationLimits](arkts-mechanic-mechanicmanager-getrotationlimits-f-sys.md#getrotationlimits) |
| [isSupportAction](arkts-mechanic-mechanicmanager-issupportaction-f-sys.md#issupportaction) |
| [move](arkts-mechanic-mechanicmanager-move-f-sys.md#move) |
| [moveBySpeed](arkts-mechanic-mechanicmanager-movebyspeed-f-sys.md#movebyspeed) |
| [off](arkts-mechanic-mechanicmanager-off-f-sys.md#off-2) |
| [on](arkts-mechanic-mechanicmanager-on-f-sys.md#on-2) |
| [rotate](arkts-mechanic-mechanicmanager-rotate-f-sys.md#rotate) |
| [rotateBySpeed](arkts-mechanic-mechanicmanager-rotatebyspeed-f-sys.md#rotatebyspeed) |
| [rotateToEulerAngles](arkts-mechanic-mechanicmanager-rotatetoeulerangles-f-sys.md#rotatetoeulerangles) |
| [searchTarget](arkts-mechanic-mechanicmanager-searchtarget-f-sys.md#searchtarget) |
| [setCameraTrackingLayout](arkts-mechanic-mechanicmanager-setcameratrackinglayout-f-sys.md#setcameratrackinglayout) |
| [setUserOperation](arkts-mechanic-mechanicmanager-setuseroperation-f-sys.md#setuseroperation) |
| [stopMoving](arkts-mechanic-mechanicmanager-stopmoving-f-sys.md#stopmoving) |
| [subscribe](arkts-mechanic-mechanicmanager-subscribe-f-sys.md#subscribe) |
| [turnBySpeed](arkts-mechanic-mechanicmanager-turnbyspeed-f-sys.md#turnbyspeed) |
| [unSubscribe](arkts-mechanic-mechanicmanager-unsubscribe-f-sys.md#unsubscribe) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AttachStateChangeInfo](arkts-mechanic-mechanicmanager-attachstatechangeinfo-i.md) |
| [MechInfo](arkts-mechanic-mechanicmanager-mechinfo-i.md) |
| [TrackingEventInfo](arkts-mechanic-mechanicmanager-trackingeventinfo-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AttachState](arkts-mechanic-mechanicmanager-attachstate-e.md) |
| [CameraTrackingLayout](arkts-mechanic-mechanicmanager-cameratrackinglayout-e.md) |
| [MechDeviceType](arkts-mechanic-mechanicmanager-mechdevicetype-e.md) |
| [TrackingEvent](arkts-mechanic-mechanicmanager-trackingevent-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
