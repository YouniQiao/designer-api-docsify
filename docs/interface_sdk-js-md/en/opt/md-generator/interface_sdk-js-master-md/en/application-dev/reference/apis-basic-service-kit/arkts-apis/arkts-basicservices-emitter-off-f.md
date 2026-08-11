# off

## Modules to Import

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## off

```TypeScript
function off(eventId: number): void
```

Unsubscribes from all events with the specified event ID.

After this API is used to unsubscribe from an event, the event that has been published through the   
[emit](emitter.emit(eventId: string)) API but has not been executed will be unsubscribed.

**Since:** 7

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


## off

```TypeScript
function off(eventId: string): void
```

Unsubscribes from all events with the specified event ID.

After this API is used to unsubscribe from an event, the event that has been published through the   
[emit](emitter.emit(eventId: string)) API but has not been executed will be unsubscribed.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: string): void--><!--Device-emitter-function off(eventId: string): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |

## Examples

```TypeScript
// Unregister all callbacks for events whose event ID is eventId1.
emitter.off('eventId1');
```


## off

```TypeScript
function off(eventId: number, callback: Callback<EventData>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\&lt;EventData&gt;** has been registered through the   
[on](emitter.on(event: InnerEvent, callback: Callback&lt;EventData&gt;)) or   
[once](emitter.once(event: InnerEvent, callback: Callback&lt;EventData&gt;)) API. Otherwise, no processing is performed.

After this API is used to unsubscribe from an event, the event that has been published through the   
[emit](emitter.emit(eventId: string)) API but has not been executed will be unsubscribed.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: long, callback: Callback<EventData>): void--><!--Device-emitter-function off(eventId: long, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | number | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes |

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


## off

```TypeScript
function off(eventId: string, callback: Callback<EventData>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\&lt;EventData&gt;** has been registered through the   
[on](emitter.on(eventId: string, callback: Callback&lt;EventData&gt;)) or   
[once](emitter.once(eventId: string, callback: Callback&lt;EventData&gt;)) API. Otherwise, no processing is performed.

After this API is used to unsubscribe from an event, the event that has been published through the   
[emit](emitter.emit(eventId: string)) API but has not been executed will be unsubscribed.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function off(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};
// Unregister all callbacks for events whose event ID is eventId1. The callback object must be the object used during registration.
// If the callback has not been registered, no processing is performed.
emitter.off('eventId1', callback);
```


## off

```TypeScript
function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\&lt;EventData&gt;** has been registered through the   
[on](emitter.on&lt;T&gt;(eventId: string, callback: Callback&lt;GenericEventData<T>&gt;&lt;T&gt;>)) or   
[once](emitter.once&lt;T&gt;(eventId: string, callback: Callback&lt;GenericEventData<T>&gt;&lt;T&gt;>)) API. Otherwise, no processing is performed.

After this API is used to unsubscribe from an event, the event that has been published through the   
[emit](emitter.emit(eventId: string)) API but has not been executed will be unsubscribed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;GenericEventData&lt;T&gt;&gt; | Yes |

## Examples

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
};
// Unregister all callbacks for events whose event ID is eventId1. The callback object must be the object used during registration.
// If the callback has not been registered, no processing is performed.
emitter.off('eventId1', callback);
```
