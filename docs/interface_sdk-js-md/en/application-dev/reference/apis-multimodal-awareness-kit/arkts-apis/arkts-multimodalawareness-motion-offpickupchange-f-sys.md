# offPickupChange (System API)

## Modules to Import

```TypeScript
import { motion } from '@kit.MultimodalAwarenessKit';
```

## offPickupChange

```TypeScript
function offPickupChange(callback?: Callback<PickupEvent>): void
```

Unsubscribe to pick up sensor event.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-motion-function offPickupChange(callback?: Callback<PickupEvent>): void--><!--Device-motion-function offPickupChange(callback?: Callback<PickupEvent>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[PickupEvent](arkts-multimodalawareness-motion-pickupevent-e-sys.md)&gt; | No | Callback used for pick up event unsubscription. &lt;br&gt; If this parameter is not specified, all callbacks of the pick up event are unsubscribed from. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [31500001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) | Service exception. Possible causes: 1. A system error, such as null pointer, &lt;br&gt; container-related exception; 2. N-API invocation exception, invalid N-API status. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

