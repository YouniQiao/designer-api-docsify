# onHoverHandChange (System API)

## Modules to Import

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## onHoverHandChange

```TypeScript
function onHoverHandChange(detectionArea: HoverHandDetectionArea, callback: Callback<HoverHandAction>): void
```

Subscribes to hover hand events and immediately starts detection for five seconds.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-motion-function onHoverHandChange(detectionArea: HoverHandDetectionArea, callback: Callback<HoverHandAction>): void--><!--Device-motion-function onHoverHandChange(detectionArea: HoverHandDetectionArea, callback: Callback<HoverHandAction>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| detectionArea | [HoverHandDetectionArea](arkts-multimodalawareness-motion-hoverhanddetectionarea-i-sys.md) | Yes |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;HoverHandAction&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-subscription-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## onHoverHandChange

```TypeScript
function onHoverHandChange(
    detectionArea: HoverHandDetectionArea, duration: number, callback: Callback<HoverHandAction>): void
```

Subscribes to hover hand events and immediately starts detection.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-motion-function onHoverHandChange(    detectionArea: HoverHandDetectionArea, duration: int, callback: Callback<HoverHandAction>): void--><!--Device-motion-function onHoverHandChange(    detectionArea: HoverHandDetectionArea, duration: int, callback: Callback<HoverHandAction>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| detectionArea | [HoverHandDetectionArea](arkts-multimodalawareness-motion-hoverhanddetectionarea-i-sys.md) | Yes |
| duration | number | Yes |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;HoverHandAction&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-subscription-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
