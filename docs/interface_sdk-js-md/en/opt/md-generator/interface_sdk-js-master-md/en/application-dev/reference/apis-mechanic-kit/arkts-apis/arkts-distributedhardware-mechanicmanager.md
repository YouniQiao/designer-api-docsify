# @ohos.distributedHardware.mechanicManager

Provides capabilities for controlling and interacting with mechanical devices connected to this device. The capabilities cover connection management, control, and monitoring.

**Since:** 23

<!--Device-unnamed-declare namespace mechanicManager--><!--Device-unnamed-declare namespace mechanicManager-End-->

**System capability:** SystemCapability.Mechanic.Core

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [connectDevice](arkts-mechanic-mechanicmanager-connectdevice-f-sys.md#connectdevice-system-api) |
| [disconnectDevice](arkts-mechanic-mechanicmanager-disconnectdevice-f-sys.md#disconnectdevice-system-api) |
| [doAction](arkts-mechanic-mechanicmanager-doaction-f-sys.md#doaction-system-api) |
| [getCurrentAngles](arkts-mechanic-mechanicmanager-getcurrentangles-f-sys.md#getcurrentangles-system-api) |
| [getMaxRotationSpeed](arkts-mechanic-mechanicmanager-getmaxrotationspeed-f-sys.md#getmaxrotationspeed-system-api) |
| [getMaxRotationTime](arkts-mechanic-mechanicmanager-getmaxrotationtime-f-sys.md#getmaxrotationtime-system-api) |
| [getRotationAxesStatus](arkts-mechanic-mechanicmanager-getrotationaxesstatus-f-sys.md#getrotationaxesstatus-system-api) |
| [getRotationLimits](arkts-mechanic-mechanicmanager-getrotationlimits-f-sys.md#getrotationlimits-system-api) |
| [isSupportAction](arkts-mechanic-mechanicmanager-issupportaction-f-sys.md#issupportaction-system-api) |
| [move](arkts-mechanic-mechanicmanager-move-f-sys.md#move-system-api) |
| [moveBySpeed](arkts-mechanic-mechanicmanager-movebyspeed-f-sys.md#movebyspeed-system-api) |
| [offRotationAxesStatusChange](arkts-mechanic-mechanicmanager-offrotationaxesstatuschange-f-sys.md#offrotationaxesstatuschange) |
| [off_rotationAxesStatusChange](arkts-mechanic-mechanicmanager-offrotationaxesstatuschange-f-sys.md#offrotationaxesstatuschange) |
| [onRotationAxesStatusChange](arkts-mechanic-mechanicmanager-onrotationaxesstatuschange-f-sys.md#onrotationaxesstatuschange) |
| [on_rotationAxesStatusChange](arkts-mechanic-mechanicmanager-onrotationaxesstatuschange-f-sys.md#onrotationaxesstatuschange) |
| [rotate](arkts-mechanic-mechanicmanager-rotate-f-sys.md#rotate-system-api) |
| [rotateBySpeed](arkts-mechanic-mechanicmanager-rotatebyspeed-f-sys.md#rotatebyspeed-system-api) |
| [rotateToEulerAngles](arkts-mechanic-mechanicmanager-rotatetoeulerangles-f-sys.md#rotatetoeulerangles-system-api) |
| [searchTarget](arkts-mechanic-mechanicmanager-searchtarget-f-sys.md#searchtarget-system-api) |
| [setCameraTrackingLayout](arkts-mechanic-mechanicmanager-setcameratrackinglayout-f-sys.md#setcameratrackinglayout-system-api) |
| [setUserOperation](arkts-mechanic-mechanicmanager-setuseroperation-f-sys.md#setuseroperation-system-api) |
| [stopMoving](arkts-mechanic-mechanicmanager-stopmoving-f-sys.md#stopmoving-system-api) |
| [subscribe](arkts-mechanic-mechanicmanager-subscribe-f-sys.md#subscribe-system-api) |
| [turnBySpeed](arkts-mechanic-mechanicmanager-turnbyspeed-f-sys.md#turnbyspeed-system-api) |
| [unSubscribe](arkts-mechanic-mechanicmanager-unsubscribe-f-sys.md#unsubscribe-system-api) |
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
