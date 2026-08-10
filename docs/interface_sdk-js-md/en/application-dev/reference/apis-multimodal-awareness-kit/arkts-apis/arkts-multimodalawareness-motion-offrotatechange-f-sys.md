# offRotateChange (System API)

## Modules to Import

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## offRotateChange

```TypeScript
function offRotateChange(callback?: Callback<RotateEvent>): void
```

Unsubscribe to rotate sensor event.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-motion-function offRotateChange(callback?: Callback<RotateEvent>): void--><!--Device-motion-function offRotateChange(callback?: Callback<RotateEvent>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;RotateEvent&gt; | No | Callback used for rotate event unsubscription. &lt;br&gt; If this parameter is not specified, all callbacks of the rotate event are unsubscribed from. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, &lt;br&gt; container-related exception; 2. N-API invocation exception, invalid N-API status. |
| 202 | Permission verification failed. A non-system application calls a system API. |

