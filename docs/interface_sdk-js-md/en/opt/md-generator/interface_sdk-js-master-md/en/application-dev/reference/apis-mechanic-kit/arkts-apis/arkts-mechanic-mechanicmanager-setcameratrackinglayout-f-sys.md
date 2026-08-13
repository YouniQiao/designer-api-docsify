# setCameraTrackingLayout (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## setCameraTrackingLayout

```TypeScript
function setCameraTrackingLayout(trackingLayout: CameraTrackingLayout): void
```

Sets the camera tracking layout for this mechanical device.

**Since:** 23

**Deprecated since:** -1

<!--Device-mechanicManager-function setCameraTrackingLayout(trackingLayout: CameraTrackingLayout): void--><!--Device-mechanicManager-function setCameraTrackingLayout(trackingLayout: CameraTrackingLayout): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| trackingLayout | [CameraTrackingLayout](arkts-mechanic-mechanicmanager-cameratrackinglayout-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) |
| [33300003](../errorcode-mechanic.md#33300003-function-not-supported) |

## Examples

```TypeScript
console.info('Set layout');
mechanicManager.setCameraTrackingLayout(mechanicManager.CameraTrackingLayout.LEFT);
console.info('Set layout successful');
```
