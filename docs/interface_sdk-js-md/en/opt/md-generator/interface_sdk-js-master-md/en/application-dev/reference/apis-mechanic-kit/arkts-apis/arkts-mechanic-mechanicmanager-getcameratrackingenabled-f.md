# getCameraTrackingEnabled

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## getCameraTrackingEnabled

```TypeScript
function getCameraTrackingEnabled(): boolean
```

Checks whether camera tracking is enabled for this mechanical device.

**Since:** 20

<!--Device-mechanicManager-function getCameraTrackingEnabled(): boolean--><!--Device-mechanicManager-function getCameraTrackingEnabled(): boolean-End-->

**System capability:** SystemCapability.Mechanic.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [33300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-system-error) |
| [33300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300002-device-not-connected) |

## Examples

```TypeScript
console.info('Get tracking status');
// Call getCameraTrackingEnabled to obtain whether camera tracking is currently enabled.
let enabled = mechanicManager.getCameraTrackingEnabled();
console.info(`'current tracking status:' ${enabled}`);
```
