# offHoverHandChange (System API)

## Modules to Import

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## offHoverHandChange

```TypeScript
function offHoverHandChange(callback?: Callback<HoverHandAction>): void
```

Unsubscribe to hover hand event.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-motion-function offHoverHandChange(callback?: Callback<HoverHandAction>): void--><!--Device-motion-function offHoverHandChange(callback?: Callback<HoverHandAction>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;HoverHandAction&gt; | No | Callback used to return hover hand action. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) | Service exception. Possible causes: 1. A system error, such as null pointer, &lt;br&gt; container-related exception; 2. N-API invocation exception, invalid N-API status. |
| [31500003](../../apis-multimodalawareness-kit/errorcode-motion.md#31500003-unsubscription-failed) | Unsubscription failed. Possible causes: 1. Callback failure; &lt;br&gt; 2. N-API invocation exception, invalid N-API status; 3. IPC request exception. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

