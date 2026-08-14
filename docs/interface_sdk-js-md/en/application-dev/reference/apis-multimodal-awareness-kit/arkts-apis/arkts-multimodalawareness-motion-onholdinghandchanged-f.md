# onHoldingHandChanged

## Modules to Import

```TypeScript
import { motion } from 'motion';
```

## onHoldingHandChanged

```TypeScript
function onHoldingHandChanged(callback: Callback<HoldingHandStatus>): void
```

Subscribe to detect the holding hand changed event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.DETECT_GESTURE

<!--Device-motion-function onHoldingHandChanged(callback: Callback<HoldingHandStatus>): void--><!--Device-motion-function onHoldingHandChanged(callback: Callback<HoldingHandStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HoldingHandStatus](arkts-multimodalawareness-motion-holdinghandstatus-e.md)&gt; | Yes | Indicates the callback for getting the event data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function can not work correctly due to limited <br> device capabilities. |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) | Service exception. |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-subscription-failed) | Subscribe Failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. An attempt was made to subscribe holdingHandChanged <br> event forbidden by permission: ohos.permission.DETECT_GESTURE. |

