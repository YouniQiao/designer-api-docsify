# offOperatingHandChanged

## Modules to Import

```TypeScript
import { motion } from '@kit.MultimodalAwarenessKit';
```

## offOperatingHandChanged

```TypeScript
function offOperatingHandChanged(callback?: Callback<OperatingHandStatus>): void
```

Unsubscribe from the operating hand changed event.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE

<!--Device-motion-function offOperatingHandChanged(callback?: Callback<OperatingHandStatus>): void--><!--Device-motion-function offOperatingHandChanged(callback?: Callback<OperatingHandStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OperatingHandStatus](arkts-multimodalawareness-motion-operatinghandstatus-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) |
| [31500003](../../apis-multimodalawareness-kit/errorcode-motion.md#31500003-unsubscription-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
