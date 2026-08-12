# onceEventData

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## onceEventData

```TypeScript
function onceEventData(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function onceEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function onceEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event to subscribe to in one-shot manner. The value cannot be an empty string and exceed 10240 bytes. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes | Callback to be executed when the event is received. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
}
// Execute the callback after receiving the event whose ID is eventId.
emitter.onceEventData("eventId", callback);
```

