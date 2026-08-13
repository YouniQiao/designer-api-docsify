# once_InnerEvent

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## once_InnerEvent

```TypeScript
function once(event: InnerEvent, callback: Callback<EventData>): void
```

Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function once(event: InnerEvent, callback: Callback<EventData>): void--><!--Device-emitter-function once(event: InnerEvent, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [InnerEvent](arkts-basicservices-emitter-innerevent-i.md) | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let innerEvent: emitter.InnerEvent = {
  eventId: 1
};

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};
// Execute the callback after receiving the event whose ID is 1.
emitter.once(innerEvent, callback);
```
