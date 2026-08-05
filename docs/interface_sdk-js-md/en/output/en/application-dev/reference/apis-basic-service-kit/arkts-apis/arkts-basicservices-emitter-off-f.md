# off

## off

```TypeScript
function off(eventId: long): void
```

Unsubscribes from all events with the specified event ID. After this API is used to unsubscribe from an event, the event that has been published through the [emit]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API but has not been executed will be unsubscribed.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: long): void--><!--Device-emitter-function off(eventId: long): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | Event ID. |

**Example**

```TypeScript
// Unregister the callbacks of all events whose ID is 1.
emitter.off(1);
```


## off

```TypeScript
function off(eventId: string): void
```

Unsubscribes from all events with the specified event ID. After this API is used to unsubscribe from an event, the event that has been published through the [emit]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API but has not been executed will be unsubscribed.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: string): void--><!--Device-emitter-function off(eventId: string): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |

**Example**

```TypeScript
// Unregister the callbacks of all events whose ID is eventId1.
emitter.off('eventId1');
```


## off

```TypeScript
function off(eventId: long, callback: Callback<EventData>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\_\_\_ESCAPED\_UNDERSCORE\_DESC\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_** has been registered through the [on]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [once]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API. Otherwise, no processing is performed. After this API is used to unsubscribe from an event, the event that has been published through the [emit]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ API but has not been executed will be unsubscribed.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: long, callback: Callback<EventData>): void--><!--Device-emitter-function off(eventId: long, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | Event ID. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;EventData&gt; | Yes | Callback to unregister, which must be the same as the callback used during registration. |

**Example**

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


## off

```TypeScript
function off(eventId: string, callback: Callback<EventData>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\_\_\_ESCAPED\_UNDERSCORE\_DESC\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_** has been registered through the [on]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [once]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API. Otherwise, no processing is performed. After this API is used to unsubscribe from an event, the event that has been published through the [emit]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ API but has not been executed will be unsubscribed.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function off(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;EventData&gt; | Yes | Callback to unregister, which must be the same as the callback used during registration. |

**Example**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}
// Unregister the callbacks for events whose ID is eventId1. The callback object must be the object used during registration.
// If the callback has not been registered, no processing is performed.
emitter.off('eventId1', callback);
```


## off

```TypeScript
function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\_\_\_ESCAPED\_UNDERSCORE\_DESC\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_** has been registered through the [on]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [once]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API. Otherwise, no processing is performed. After this API is used to unsubscribe from an event, the event that has been published through the [emit]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ API but has not been executed will be unsubscribed.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;GenericEventData&lt;T&gt;&gt; | Yes | Callback to unregister, which must be the same as the callback used during registration. |

**Example**

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

