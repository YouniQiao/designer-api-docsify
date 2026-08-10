# setCameraTrackingEnabled

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## setCameraTrackingEnabled

```TypeScript
function setCameraTrackingEnabled(isEnabled: boolean): void
```

启用或禁用摄像机跟踪

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-mechanicManager-function setCameraTrackingEnabled(isEnabled: boolean): void--><!--Device-mechanicManager-function setCameraTrackingEnabled(isEnabled: boolean): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean | Yes | 是否启用摄像机跟踪 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |
| 33300003 | Feature not supported. |

## Examples

```TypeScript
console.info('Enable tracing');
// Call the setCameraTrackingEnabled method. The value true indicates enabling camera tracking.
mechanicManager.setCameraTrackingEnabled(true);
console.info('Succeeded in enabling tracking.');
```

