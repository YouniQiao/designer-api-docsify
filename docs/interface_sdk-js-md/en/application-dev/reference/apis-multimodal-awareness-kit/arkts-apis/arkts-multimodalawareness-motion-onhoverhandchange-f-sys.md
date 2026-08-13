# onHoverHandChange (System API)

## Modules to Import

```TypeScript
import { motion } from '@kit.MultimodalAwarenessKit';
```

## onHoverHandChange

```TypeScript
function onHoverHandChange(detectionArea: HoverHandDetectionArea, callback: Callback<HoverHandAction>): void
```

Subscribes to hover hand events and immediately starts detection for five seconds.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-motion-function onHoverHandChange(detectionArea: HoverHandDetectionArea, callback: Callback<HoverHandAction>): void--><!--Device-motion-function onHoverHandChange(detectionArea: HoverHandDetectionArea, callback: Callback<HoverHandAction>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| detectionArea | [HoverHandDetectionArea](arkts-multimodalawareness-motion-hoverhanddetectionarea-i-sys.md) | Yes | Rectangular detection area for hover hand. &lt;br&gt; Repeated calls will override the previously set detection area. &lt;br&gt; If the area exceeds the screen bounds, it defaults to detecting the overlap. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HoverHandAction](arkts-multimodalawareness-motion-hoverhandaction-e-sys.md)&gt; | Yes | Callback used to return hover hand action. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited &lt;br&gt; device capabilities. |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) | Service exception. Possible causes: 1. A system error, such as null pointer, &lt;br&gt; container-related exception; 2. N-API invocation exception, invalid N-API status. |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-subscription-failed) | Subscription failed. Possible causes: 1. Callback registration failure; &lt;br&gt; 2. Failed to bind native object to js wrapper; 3. N-API invocation exception, invalid N-API status; 4. IPC &lt;br&gt; request exception. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |


## onHoverHandChange

```TypeScript
function onHoverHandChange(
    detectionArea: HoverHandDetectionArea, duration: int, callback: Callback<HoverHandAction>): void
```

Subscribes to hover hand events and immediately starts detection.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-motion-function onHoverHandChange(    detectionArea: HoverHandDetectionArea, duration: int, callback: Callback<HoverHandAction>): void--><!--Device-motion-function onHoverHandChange(    detectionArea: HoverHandDetectionArea, duration: int, callback: Callback<HoverHandAction>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| detectionArea | [HoverHandDetectionArea](arkts-multimodalawareness-motion-hoverhanddetectionarea-i-sys.md) | Yes | Rectangular detection area for hover hand. &lt;br&gt; Repeated calls will override the previously set detection area. &lt;br&gt; If the area exceeds the screen bounds, it defaults to detecting the overlap. |
| duration | int | Yes | Detection duration. &lt;br&gt; Unit: Seconds. The value must be an integer within [1,10]. &lt;br&gt; Subscription ends automatically after duration expires. Call again to restart the detection. &lt;br&gt; Hover hand events are high power consumption events, developers are advised to set the duration as needed. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HoverHandAction](arkts-multimodalawareness-motion-hoverhandaction-e-sys.md)&gt; | Yes | Callback used to return hover hand action. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited &lt;br&gt; device capabilities. |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) | Service exception. Possible causes: 1. A system error, such as null pointer, &lt;br&gt; container-related exception; 2. N-API invocation exception, invalid N-API status. |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-subscription-failed) | Subscription failed. Possible causes: 1. Callback registration failure; &lt;br&gt; 2. Failed to bind native object to js wrapper; 3. N-API invocation exception, invalid N-API status; 4. IPC &lt;br&gt; request exception. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

