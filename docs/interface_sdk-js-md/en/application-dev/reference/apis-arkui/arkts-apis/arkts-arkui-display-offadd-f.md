# offAdd

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## offAdd

```TypeScript
function offAdd(callback?: Callback<long>): void
```

Unregister the callback for display add events.

**Since:** 23

<!--Device-display-function offAdd(callback?: Callback<long>): void--><!--Device-display-function offAdd(callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;long&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

