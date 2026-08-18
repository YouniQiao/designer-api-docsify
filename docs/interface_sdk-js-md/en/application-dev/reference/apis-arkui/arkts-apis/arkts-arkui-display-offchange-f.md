# offChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## offChange

```TypeScript
function offChange(callback?: Callback<long>): void
```

Unregister the callback for display changes.

**Since:** 23

<!--Device-display-function offChange(callback?: Callback<long>): void--><!--Device-display-function offChange(callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

