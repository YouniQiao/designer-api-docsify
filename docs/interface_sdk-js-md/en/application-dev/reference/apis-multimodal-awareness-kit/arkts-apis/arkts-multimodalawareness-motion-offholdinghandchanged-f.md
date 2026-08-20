# offHoldingHandChanged

## Modules to Import

```TypeScript
import { motion } from '@kit.MultimodalAwarenessKit';
```

## offHoldingHandChanged

```TypeScript
function offHoldingHandChanged(callback?: Callback<HoldingHandStatus>): void
```

Unsubscribe from the holding hand changed event.

**Since:** 23

**Required permissions:** ohos.permission.DETECT_GESTURE

<!--Device-motion-function offHoldingHandChanged(callback?: Callback<HoldingHandStatus>): void--><!--Device-motion-function offHoldingHandChanged(callback?: Callback<HoldingHandStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[HoldingHandStatus](arkts-multimodalawareness-motion-holdinghandstatus-e.md)&gt; | No | Indicates the callback for getting the event data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. An attempt was made to unsubscribe holdingHandChanged <br> event forbidden by permission: ohos.permission.DETECT_GESTURE. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function can not work correctly due to limited <br> device capabilities. |
| [31500001](../errorcode-motion.md#31500001-service-exception) | Service exception. |
| [31500003](../errorcode-motion.md#31500003-unsubscription-failed) | Unsubscribe Failed. |

