# @ohos.multimodalAwareness.deviceStatus

The **deviceStatus** module provides the device status awareness functionality.

**Since:** 18

**System capability:** SystemCapability.MultimodalAwareness.DeviceStatus

## Modules to Import

```TypeScript
import deviceStatus from '@kit.MultimodalAwarenessKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [off](arkts-multimodalawareness-devicestatus-off-f.md#offsteadystandingdetect) | Unsubscribes from steady standing state events. |
| [on](arkts-multimodalawareness-devicestatus-on-f.md#onsteadystandingdetect) | Subscribes to steady standing state events. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getDeviceRotationRadian](arkts-multimodalawareness-devicestatus-getdevicerotationradian-f-sys.md) | Obtains the device posture data.The posture data contains the rotation angles of the x, y, and z axes, that is, the Euler angles of the three axes. The definitions of the three axes are the same as those of the device sensor, and the right-handed coordinate system is used. Posture rotation angles are calculated under the z-x-y intrinsic rotation order, and derived by converting quaternions obtained via sensor fusion. |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [DeviceRotationRadian](arkts-multimodalawareness-devicestatus-devicerotationradian-i-sys.md) | Interface for device rotation radian |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [SteadyStandingStatus](arkts-multimodalawareness-devicestatus-steadystandingstatus-e.md) | Defines the steady standing state (that is, stand mode).A device enters stand mode when it is stationary, and its screen is at an angle between 45 and 135 degrees relative to the horizontal plane. For foldable smartphones, the device must be in a folded state or fully unfolded state. |
