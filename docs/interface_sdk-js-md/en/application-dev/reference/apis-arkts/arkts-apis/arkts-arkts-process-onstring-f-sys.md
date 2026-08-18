# on_string (System API)

## Modules to Import

```TypeScript
import { process } from '@kit.ArkTS';
```

## on_string

```TypeScript
function on(type: string, listener: EventListener): void
```

Register for an event

**Since:** 7

<!--Device-process-function on(type: string, listener: EventListener): void--><!--Device-process-function on(type: string, listener: EventListener): void-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Indicates the type of event registered. |
| listener | EventListener | Yes | Represents the registered event function |

