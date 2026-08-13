# @ohos.distributedHardware.mechanicManager

Provides capabilities for controlling and interacting with mechanical devices connected to this device. The capabilities cover connection management, control, and monitoring.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace mechanicManager--><!--Device-unnamed-declare namespace mechanicManager-End-->

**System capability:** SystemCapability.Mechanic.Core

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAttachedMechDevices](arkts-mechanic-mechanicmanager-getattachedmechdevices-f.md#getAttachedMechDevices) |
| [getCameraTrackingEnabled](arkts-mechanic-mechanicmanager-getcameratrackingenabled-f.md#getCameraTrackingEnabled) |
| [getCameraTrackingLayout](arkts-mechanic-mechanicmanager-getcameratrackinglayout-f.md#getCameraTrackingLayout) |
| [isControlSupported](arkts-mechanic-mechanicmanager-iscontrolsupported-f.md#isControlSupported) |
| [offAttachStateChange](arkts-mechanic-mechanicmanager-offattachstatechange-f.md#offAttachStateChange) |
| [offTrackingStateChange](arkts-mechanic-mechanicmanager-offtrackingstatechange-f.md#offTrackingStateChange) |
| [off_attachStateChange](arkts-mechanic-mechanicmanager-offattachstatechange-f.md) |
| [off_trackingStateChange](arkts-mechanic-mechanicmanager-offtrackingstatechange-f.md) |
| [onAttachStateChange](arkts-mechanic-mechanicmanager-onattachstatechange-f.md#onAttachStateChange) |
| [onTrackingStateChange](arkts-mechanic-mechanicmanager-ontrackingstatechange-f.md#onTrackingStateChange) |
| [on_attachStateChange](arkts-mechanic-mechanicmanager-onattachstatechange-f.md) |
| [on_trackingStateChange](arkts-mechanic-mechanicmanager-ontrackingstatechange-f.md) |
| [setCameraTrackingEnabled](arkts-mechanic-mechanicmanager-setcameratrackingenabled-f.md#setCameraTrackingEnabled) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [connectDevice](arkts-mechanic-mechanicmanager-connectdevice-f-sys.md#connectDevice-(System-API)) |
| [disconnectDevice](arkts-mechanic-mechanicmanager-disconnectdevice-f-sys.md#disconnectDevice-(System-API)) |
| [doAction](arkts-mechanic-mechanicmanager-doaction-f-sys.md#doAction-(System-API)) |
| [getCurrentAngles](arkts-mechanic-mechanicmanager-getcurrentangles-f-sys.md#getCurrentAngles-(System-API)) |
| [getMaxRotationSpeed](arkts-mechanic-mechanicmanager-getmaxrotationspeed-f-sys.md#getMaxRotationSpeed-(System-API)) |
| [getMaxRotationTime](arkts-mechanic-mechanicmanager-getmaxrotationtime-f-sys.md#getMaxRotationTime-(System-API)) |
| [getRotationAxesStatus](arkts-mechanic-mechanicmanager-getrotationaxesstatus-f-sys.md#getRotationAxesStatus-(System-API)) |
| [getRotationLimits](arkts-mechanic-mechanicmanager-getrotationlimits-f-sys.md#getRotationLimits-(System-API)) |
| [isSupportAction](arkts-mechanic-mechanicmanager-issupportaction-f-sys.md#isSupportAction-(System-API)) |
| [move](arkts-mechanic-mechanicmanager-move-f-sys.md#move-(System-API)) |
| [moveBySpeed](arkts-mechanic-mechanicmanager-movebyspeed-f-sys.md#moveBySpeed-(System-API)) |
| [offRotationAxesStatusChange](arkts-mechanic-mechanicmanager-offrotationaxesstatuschange-f-sys.md#offRotationAxesStatusChange-(System-API)) |
| [off_rotationAxesStatusChange](arkts-mechanic-mechanicmanager-offrotationaxesstatuschange-f-sys.md) |
| [onRotationAxesStatusChange](arkts-mechanic-mechanicmanager-onrotationaxesstatuschange-f-sys.md#onRotationAxesStatusChange-(System-API)) |
| [on_rotationAxesStatusChange](arkts-mechanic-mechanicmanager-onrotationaxesstatuschange-f-sys.md) |
| [rotate](arkts-mechanic-mechanicmanager-rotate-f-sys.md#rotate-(System-API)) |
| [rotateBySpeed](arkts-mechanic-mechanicmanager-rotatebyspeed-f-sys.md#rotateBySpeed-(System-API)) |
| [rotateToEulerAngles](arkts-mechanic-mechanicmanager-rotatetoeulerangles-f-sys.md#rotateToEulerAngles-(System-API)) |
| [searchTarget](arkts-mechanic-mechanicmanager-searchtarget-f-sys.md#searchTarget-(System-API)) |
| [setCameraTrackingLayout](arkts-mechanic-mechanicmanager-setcameratrackinglayout-f-sys.md#setCameraTrackingLayout-(System-API)) |
| [setUserOperation](arkts-mechanic-mechanicmanager-setuseroperation-f-sys.md#setUserOperation-(System-API)) |
| [stopMoving](arkts-mechanic-mechanicmanager-stopmoving-f-sys.md#stopMoving-(System-API)) |
| [subscribe](arkts-mechanic-mechanicmanager-subscribe-f-sys.md#subscribe-(System-API)) |
| [turnBySpeed](arkts-mechanic-mechanicmanager-turnbyspeed-f-sys.md#turnBySpeed-(System-API)) |
| [unSubscribe](arkts-mechanic-mechanicmanager-unsubscribe-f-sys.md#unSubscribe-(System-API)) |
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
