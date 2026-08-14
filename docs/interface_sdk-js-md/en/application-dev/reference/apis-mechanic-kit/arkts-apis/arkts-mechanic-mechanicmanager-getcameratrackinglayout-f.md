# getCameraTrackingLayout

## Modules to Import

```TypeScript
import { mechanicManager } from 'mechanicManager';
```

## getCameraTrackingLayout

```TypeScript
function getCameraTrackingLayout(): CameraTrackingLayout
```

Obtains the camera tracking layout of this mechanical device.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-mechanicManager-function getCameraTrackingLayout(): CameraTrackingLayout--><!--Device-mechanicManager-function getCameraTrackingLayout(): CameraTrackingLayout-End-->

**System capability:** SystemCapability.Mechanic.Core

**Return value:**

| Type | Description |
| --- | --- |
| [CameraTrackingLayout](arkts-mechanic-mechanicmanager-cameratrackinglayout-e.md) | Camera tracking layout obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) | Device not connected. |

## Examples

```TypeScript
console.info('Query layout');
let layout = mechanicManager.getCameraTrackingLayout();
console.info(`'Query layout successful, current layout:' ${layout}`);
```

