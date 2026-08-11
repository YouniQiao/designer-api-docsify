# offHoldingHandChanged

## Modules to Import

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## offHoldingHandChanged

```TypeScript
function offHoldingHandChanged(callback?: Callback<HoldingHandStatus>): void
```

Unsubscribe from the holding hand changed event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.DETECT_GESTURE

<!--Device-motion-function offHoldingHandChanged(callback?: Callback<HoldingHandStatus>): void--><!--Device-motion-function offHoldingHandChanged(callback?: Callback<HoldingHandStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;HoldingHandStatus&gt; | No | Indicates the callback for getting the event data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) | Service exception. |
| [31500003](../../apis-multimodalawareness-kit/errorcode-motion.md#31500003-unsubscription-failed) | Unsubscribe Failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. An attempt was made to unsubscribe holdingHandChanged &lt;br&gt; event forbidden by permission: ohos.permission.DETECT_GESTURE. |

