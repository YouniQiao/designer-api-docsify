# offEventData

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## offEventData

```TypeScript
function offEventData(eventId: string, callback: Callback<EventData>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback.This API takes effect only when Callback&lt;EventData&gt; has been registered through the on or once API.Otherwise, no processing is performed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function offEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function offEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID. The value cannot be an empty string and exceed 10240 bytes. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes | Callback to unregister. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData | undefined | null) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

// Unregister the callbacks for events whose ID is eventId. The callback object must be the object used during registration.
// If the callback handler has not been subscribed, no processing is performed.
emitter.offEventData("eventId", callback);
```

