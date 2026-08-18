# Emitter

This module provides the capabilities of sending and processing inter- or intra-thread events in a process of the same **Emitter** instance. You can use the following APIs to subscribe to an event in persistent or one-shot manner, cancel the subscription, or emit an event to the event queue. This module is applicable when inter-thread communication and event management are required based on independent instances. Different **Emitter** instances are isolated from each other.

**Since:** 23

<!--Device-emitter-export class Emitter--><!--Device-emitter-export class Emitter-End-->

**System capability:** SystemCapability.Notification.Emitter

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Defines a constructor.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Emitter-constructor()--><!--Device-Emitter-constructor()-End-->

**System capability:** SystemCapability.Notification.Emitter

**Examples**

```TypeScript
let emitter1: emitter.Emitter = new emitter.Emitter();
```

## emit_string

```TypeScript
emit(eventId: string, data?: EventData): void
```

Emits a specified event to the Emitter class instance. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Emitter-emit(eventId: string, data?: EventData): void--><!--Device-Emitter-emit(eventId: string, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No |

**Examples**

```TypeScript
let emitter1: emitter.Emitter = new emitter.Emitter();
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

emitter1.emit('eventId', eventData);
```

## emit_string

```TypeScript
emit<T>(eventId: string, data?: GenericEventData<T>): void
```

Emits a specified event to the Emitter class instance. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Emitter-emit<T>(eventId: string, data?: GenericEventData<T>): void--><!--Device-Emitter-emit<T>(eventId: string, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No |

**Examples**

```TypeScript
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

let emitter1: emitter.Emitter = new emitter.Emitter();

let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter1.emit('eventId', eventData);
```

## emit_string

```TypeScript
emit(eventId: string, options: Options, data?: EventData): void
```

Emits an event of a specified priority to the Emitter instance. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Emitter-emit(eventId: string, options: Options, data?: EventData): void--><!--Device-Emitter-emit(eventId: string, options: Options, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No |

**Examples**

```TypeScript
let emitter1: emitter.Emitter = new emitter.Emitter();

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

emitter1.emit('eventId', options, eventData);
```

## emit_string

```TypeScript
emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void
```

Emits an event of a specified priority to the Emitter instance. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Emitter-emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void--><!--Device-Emitter-emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No |

**Examples**

```TypeScript
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

let emitter1: emitter.Emitter = new emitter.Emitter();

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter1.emit('eventId', options, eventData);
```

## getListenerCount

```TypeScript
getListenerCount(eventId: string): number
```

Obtains the number of subscriptions to a specified event of the Emitter instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Emitter-getListenerCount(eventId: string): long--><!--Device-Emitter-getListenerCount(eventId: string): long-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
let emitter1: emitter.Emitter = new emitter.Emitter();
let count: number = emitter1.getListenerCount('eventId');
```

## offEventData

```TypeScript
offEventData(eventId: string, callback: Callback<EventData>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback.

**Since:** 23

<!--Device-Emitter-offEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-offEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |

## offGenericEventData

```TypeScript
offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback.

**Since:** 23

<!--Device-Emitter-offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes |

## off_string

```TypeScript
off(eventId: string): void
```

Unsubscribes from all events with the specified event ID of the Emitter instance. After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Emitter-off(eventId: string): void--><!--Device-Emitter-off(eventId: string): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |

**Examples**

```TypeScript
let emitter1: emitter.Emitter = new emitter.Emitter();

emitter1.off('eventId');
```

## off_string

```TypeScript
off(eventId: string, callback: Callback<EventData>): void
```

Unsubscribes from an event of the Emitter instance. This API takes effect only when the [on](#onstring) or once API is used to subscribe to the event with specified event ID and a callback is used to process the event. After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-off(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-off(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |

**Examples**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};

emitter1.off('eventId', callback);
```

## off_string

```TypeScript
off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Unsubscribes from an event of the Emitter instance. This API takes effect only when the on or once API is used to subscribe to the event with specified event ID and a callback is used to process the event. After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes |

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

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
};

emitter1.off('eventId', callback);
```

## onEventData

```TypeScript
onEventData(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Since:** 23

<!--Device-Emitter-onEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-onEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |

## onGenericEventData

```TypeScript
onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Since:** 23

<!--Device-Emitter-onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes |

## on_string

```TypeScript
on(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event specified by the Emitter instance in persistent manner and executes a callback after the event is received.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-on(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-on(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |

**Examples**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};

emitter1.on('eventId', callback);
```

## on_string

```TypeScript
on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event specified by the Emitter instance in persistent manner and executes a callback after the event is received.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes |

**Examples**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

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

emitter1.on('eventId', callback);
```

## onceEventData

```TypeScript
onceEventData(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed.

**Since:** 23

<!--Device-Emitter-onceEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-onceEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |

## onceGenericEventData

```TypeScript
onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed.

**Since:** 23

<!--Device-Emitter-onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes |

## once_string

```TypeScript
once(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event specified by the Emitter instance in one-shot manner and unsubscribes from it after the event callback is executed. This API uses an asynchronous callback to return the result.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-once(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-once(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |

**Examples**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};

emitter1.once('eventId', callback);
```

## once_string

```TypeScript
once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event specified by the Emitter instance in one-shot manner and unsubscribes from it after the event callback is executed. This API uses an asynchronous callback to return the result.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes |

**Examples**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

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

emitter1.once('eventId', callback);
```
