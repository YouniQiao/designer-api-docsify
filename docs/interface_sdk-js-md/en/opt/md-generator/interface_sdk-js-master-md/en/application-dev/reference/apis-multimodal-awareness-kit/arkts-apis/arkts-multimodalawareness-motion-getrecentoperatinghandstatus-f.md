# getRecentOperatingHandStatus

## Modules to Import

```TypeScript
```

## getRecentOperatingHandStatus

```TypeScript
function getRecentOperatingHandStatus(): OperatingHandStatus
```

Obtains the latest operating hand status.

**Since:** 23

**Required permissions:** 
- API version 20+: ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE
- API version 15 - 19: ohos.permission.ACTIVITY_MOTION

<!--Device-motion-function getRecentOperatingHandStatus(): OperatingHandStatus--><!--Device-motion-function getRecentOperatingHandStatus(): OperatingHandStatus-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OperatingHandStatus](arkts-multimodalawareness-motion-operatinghandstatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let data:motion.OperatingHandStatus = motion.getRecentOperatingHandStatus();
    console.info('get succeeded' + data);
} catch (err) {
    let error = err as BusinessError;
    console.error("Failed get and err code is " + error.code);
}
```
