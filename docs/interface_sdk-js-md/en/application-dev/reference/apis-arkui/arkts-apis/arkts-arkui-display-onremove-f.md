# onRemove

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## onRemove

```TypeScript
function onRemove(callback: Callback<long>): void
```

Register the callback for display remove events.

**Since:** 23

<!--Device-display-function onRemove(callback: Callback<long>): void--><!--Device-display-function onRemove(callback: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | the display id of changed |

