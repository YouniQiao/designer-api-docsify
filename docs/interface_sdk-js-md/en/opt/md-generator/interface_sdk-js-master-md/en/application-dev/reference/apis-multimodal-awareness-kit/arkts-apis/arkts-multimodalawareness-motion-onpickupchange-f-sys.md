# onPickupChange (System API)

## Modules to Import

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## onPickupChange

```TypeScript
function onPickupChange(callback: Callback<PickupEvent>): void
```

Subscribe to pick up sensor event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-motion-function onPickupChange(callback: Callback<PickupEvent>): void--><!--Device-motion-function onPickupChange(callback: Callback<PickupEvent>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;PickupEvent&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
