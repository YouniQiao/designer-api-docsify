# getListenerCount

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## getListenerCount

```TypeScript
function getListenerCount(eventId: number | string): number
```

Obtains the number of subscriptions to a specified event.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function getListenerCount(eventId: long | string): long--><!--Device-emitter-function getListenerCount(eventId: long | string): long-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let count: number = emitter.getListenerCount('eventId');
```
