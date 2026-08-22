# off_long

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## off_long

```TypeScript
function off(eventId: long): void
```

Unsubscribes from all events with the specified event ID.

After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: long): void--><!--Device-emitter-function off(eventId: long): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | long | Yes | Event ID. |

**Examples**

```TypeScript
// Unregister the callbacks of all events whose ID is 1.
emitter.off(1);
```


## off_long

```TypeScript
function off(eventId: long, callback: Callback<EventData>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\&lt;EventData&gt;** has been registered through the on or once API. Otherwise, no processing is performed.

After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: long, callback: Callback<EventData>): void--><!--Device-emitter-function off(eventId: long, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | long | Yes | Event ID. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes | Callback to unregister, which must be the same as the callback used during registration. |

**Examples**

ArkTS-Dyn example:

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}
// Cancel the callback handler for the event with eventId 1. The callback object must be the same as the one used for subscription.
// If the callback has not been registered, no processing is performed.
emitter.off(1, callback);
```

ArkTS-Sta example:

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData | undefined | null) => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
}
// Unregister the callbacks for events whose ID is 1. The callback object must be the object used during registration.
// If the callback handler has not been subscribed, no processing is performed.
emitter.off(1, callback);
```

