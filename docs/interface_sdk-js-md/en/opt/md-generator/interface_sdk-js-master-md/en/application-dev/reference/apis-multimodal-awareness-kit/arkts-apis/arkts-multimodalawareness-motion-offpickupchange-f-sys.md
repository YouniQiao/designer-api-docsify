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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-motion-function offPickupChange(callback?: Callback<PickupEvent>): void--><!--Device-motion-function offPickupChange(callback?: Callback<PickupEvent>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PickupEvent](arkts-multimodalawareness-motion-pickupevent-e-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
