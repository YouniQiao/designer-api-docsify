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

**Model restriction:** This API can be used only in the stage model.

<!--Device-motion-function offHoverHandChange(callback?: Callback<HoverHandAction>): void--><!--Device-motion-function offHoverHandChange(callback?: Callback<HoverHandAction>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;HoverHandAction&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) |
| [31500003](../../apis-multimodalawareness-kit/errorcode-motion.md#31500003-unsubscription-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
