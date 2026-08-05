# getListenerCount

## getListenerCount

```TypeScript
function getListenerCount(eventId: long | string): long
```

Obtains the number of subscriptions to a specified event.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function getListenerCount(eventId: long | string): long--><!--Device-emitter-function getListenerCount(eventId: long | string): long-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | ArkTS-Dyn: number \| string  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long \| string | Yes | Event ID. The value is a string, which cannot be empty or exceed 10,240bytes. Excess content will be truncated. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Number of subscriptions to a specified event. |

**Example**

ArkTS-Dyn example:

```TypeScript
let count: number = emitter.getListenerCount("eventId");
```

ArkTS-Sta example:

```TypeScript
let count: long = emitter.getListenerCount("eventId");
```

