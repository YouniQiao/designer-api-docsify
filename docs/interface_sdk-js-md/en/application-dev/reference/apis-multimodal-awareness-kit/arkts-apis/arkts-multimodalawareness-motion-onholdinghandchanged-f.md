# onHoldingHandChanged

## Modules to Import

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## onHoldingHandChanged

```TypeScript
function onHoldingHandChanged(callback: Callback<HoldingHandStatus>): void
```

Subscribe to detect the holding hand changed event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.DETECT_GESTURE

<!--Device-motion-function onHoldingHandChanged(callback: Callback<HoldingHandStatus>): void--><!--Device-motion-function onHoldingHandChanged(callback: Callback<HoldingHandStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;HoldingHandStatus&gt; | Yes | Indicates the callback for getting the event data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) | Service exception. |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-subscription-failed) | Subscribe Failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. An attempt was made to subscribe holdingHandChanged &lt;br&gt; event forbidden by permission: ohos.permission.DETECT_GESTURE. |

