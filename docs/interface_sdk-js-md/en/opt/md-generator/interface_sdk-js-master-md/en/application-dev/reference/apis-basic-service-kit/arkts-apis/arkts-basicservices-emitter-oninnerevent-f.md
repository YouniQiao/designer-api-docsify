# on_InnerEvent

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## on_InnerEvent

```TypeScript
function on(event: InnerEvent, callback: Callback<EventData>): void
```

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function on(event: InnerEvent, callback: Callback<EventData>): void--><!--Device-emitter-function on(event: InnerEvent, callback: Callback<EventData>): void-End-->

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
emitter.on(innerEvent, callback);
```
