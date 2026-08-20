# off_string

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## off_string

```TypeScript
function off(eventId: string): void
```

Unsubscribes from all events with the specified event ID.

After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-emitter-function off(eventId: string): void--><!--Device-emitter-function off(eventId: string): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |

**Examples**

```TypeScript
// Unregister the callbacks of all events whose ID is eventId1.
emitter.off('eventId1');
```


## off_string

```TypeScript
function off(eventId: string, callback: Callback<EventData>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\&lt;EventData&gt;** has been registered through the on or once API. Otherwise, no processing is performed.

After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function off(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes | Callback to unregister, which must be the same as the callback used during registration. |

**Examples**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}
// Unregister the callbacks for events whose ID is eventId1. The callback object must be the object used during registration.
// If the callback has not been registered, no processing is performed.
emitter.off('eventId1', callback);
```


## off_string

```TypeScript
function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\&lt;EventData&gt;** has been registered through the [on](arkts-basicservices-emitter-emitter-c.md#on_string) or once API. Otherwise, no processing is performed.

After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes | Callback to unregister, which must be the same as the callback used during registration. |

**Examples**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
}
// Unregister the callbacks for events whose ID is eventId1. The callback object must be the object used during registration.
// If the callback has not been registered, no processing is performed.
emitter.off('eventId1', callback);
```

