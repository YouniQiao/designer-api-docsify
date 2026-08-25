# getRecentOperatingHandStatus

## Modules to Import

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## getRecentOperatingHandStatus

```TypeScript
function getRecentOperatingHandStatus(): OperatingHandStatus
```

Obtains the latest operating hand status.

**Since:** 15

**Required permissions:** 
- API version 20+: ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE
- API version 15 - 19: ohos.permission.ACTIVITY_MOTION

**System capability:** SystemCapability.MultimodalAwareness.Motion

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OperatingHandStatus](arkts-multimodalawareness-motion-operatinghandstatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [31500001](../errorcode-motion.md#31500001-service-exception) |
