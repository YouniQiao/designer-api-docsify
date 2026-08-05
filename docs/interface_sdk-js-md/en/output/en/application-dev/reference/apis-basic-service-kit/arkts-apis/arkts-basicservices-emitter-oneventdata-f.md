# onEventData

## onEventData

```TypeScript
function onEventData(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function onEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function onEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event to subscribe to in persistent manner. The value cannot be an empty string and exceed 10240 bytes. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;EventData&gt; | Yes | Callback to be executed when the event is received. |

**Example**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

// Execute the callback after receiving the event whose ID is eventId.
emitter.onEventData(`eventId`, callback);
```

