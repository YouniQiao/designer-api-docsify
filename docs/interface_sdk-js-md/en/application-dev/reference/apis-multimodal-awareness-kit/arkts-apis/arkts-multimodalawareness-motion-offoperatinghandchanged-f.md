# offOperatingHandChanged

## Modules to Import

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## offOperatingHandChanged

```TypeScript
function offOperatingHandChanged(callback?: Callback<OperatingHandStatus>): void
```

Unsubscribe from the operating hand changed event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE

<!--Device-motion-function offOperatingHandChanged(callback?: Callback<OperatingHandStatus>): void--><!--Device-motion-function offOperatingHandChanged(callback?: Callback<OperatingHandStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;OperatingHandStatus&gt; | No | Indicates the callback for getting the event data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) | Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; &lt;br&gt; 2. N-API invocation exception, invalid N-API status. |
| [31500003](../../apis-multimodalawareness-kit/errorcode-motion.md#31500003-unsubscription-failed) | Unsubscription failed. Possible causes: 1. Callback failure; &lt;br&gt; 2. N-API invocation exception, invalid N-API status; 3. IPC request exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. An attempt was made to unsubscribe operatingHandChanged &lt;br&gt; event forbidden by permission: ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE. |

