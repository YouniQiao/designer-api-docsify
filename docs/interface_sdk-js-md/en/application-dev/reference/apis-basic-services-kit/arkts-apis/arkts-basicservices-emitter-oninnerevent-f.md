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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function on(event: InnerEvent, callback: Callback<EventData>): void--><!--Device-emitter-function on(event: InnerEvent, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [InnerEvent](arkts-basicservices-emitter-innerevent-i.md) | Yes | Event to subscribe to in persistent manner. The [EventPriority](arkts-basicservices-emitter-eventpriority-e.md) parameter is not required and does not take effect. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes | Callback to be invoked when the event is received. |

**Examples**

ArkTS-Dyn example:

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let innerEvent: emitter.InnerEvent = {
  eventId: 1
};

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

// Execute the callback after receiving the event whose ID is 1.
emitter.on(innerEvent, callback);
```

ArkTS-Sta example:

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let innerEvent: emitter.InnerEvent = {
  eventId: 1
};

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
}

// Execute the callback after receiving the event whose eventId is 1.
emitter.on(innerEvent, callback);
```

