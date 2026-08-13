# off_long

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## off_long

```TypeScript
function off(eventId: number): void
```

Unsubscribes from all events with the specified event ID. After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: long): void--><!--Device-emitter-function off(eventId: long): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | number | Yes |

## Examples

```TypeScript
// Unregister all callbacks for events whose event ID is 1.
emitter.off(1);
```


## off_long

```TypeScript
function off(eventId: number, callback: Callback<EventData>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\&lt;EventData&gt;** has been registered through the [on](arkts-basicservices-emitter-oninnerevent-f.md#on_InnerEvent) or once API. Otherwise, no processing is performed. After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: long, callback: Callback<EventData>): void--><!--Device-emitter-function off(eventId: long, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | number | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};
// Unregister all callbacks for events whose event ID is 1. The callback object must be the object used during registration.
// If the callback has not been registered, no processing is performed.
emitter.off(1, callback);
```
