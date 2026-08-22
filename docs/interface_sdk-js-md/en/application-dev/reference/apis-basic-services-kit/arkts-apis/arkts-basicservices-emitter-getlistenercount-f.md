# getListenerCount

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## getListenerCount

```TypeScript
function getListenerCount(eventId: long | string): long
```

Obtains the number of subscriptions to a specified event.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-emitter-function getListenerCount(eventId: long | string): long--><!--Device-emitter-function getListenerCount(eventId: long | string): long-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | long \| string | Yes | Event ID. The value is a string, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Number of subscriptions to a specified event. |

**Examples**

ArkTS-Dyn example:

```TypeScript
let count: number = emitter.getListenerCount("eventId");
```

ArkTS-Sta example:

```TypeScript
let count: long = emitter.getListenerCount("eventId");
```

```TypeScript
let emitter1: emitter.Emitter = new emitter.Emitter();
let count = emitter1.getListenerCount("eventId");
```

