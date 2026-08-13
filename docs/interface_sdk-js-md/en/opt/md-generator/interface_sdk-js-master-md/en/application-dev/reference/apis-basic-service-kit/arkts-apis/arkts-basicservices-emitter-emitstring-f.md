# emit_string

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## emit_string

```TypeScript
function emit(eventId: string, data?: EventData): void
```

Emits a specified event. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function emit(eventId: string, data?: EventData): void--><!--Device-emitter-function emit(eventId: string, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No |

## Examples

```TypeScript
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

emitter.emit('eventId', eventData);
```


## emit_string

```TypeScript
function emit(eventId: string): void
```

Emits the specified event.

**Since:** 23

**Deprecated since:** -1

<!--Device-emitter-function emit(eventId: string): void--><!--Device-emitter-function emit(eventId: string): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |


## emit_string

```TypeScript
function emit(eventId: string, data: EventData): void
```

Emits the specified event.

**Since:** 23

**Deprecated since:** -1

<!--Device-emitter-function emit(eventId: string, data: EventData): void--><!--Device-emitter-function emit(eventId: string, data: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | Yes |


## emit_string

```TypeScript
function emit<T>(eventId: string, data?: GenericEventData<T>): void
```

Emits a specified event. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function emit<T>(eventId: string, data?: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No |

## Examples

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

let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};
emitter.emit('eventId', eventData);
```


## emit_string

```TypeScript
function emit<T>(eventId: string, data: GenericEventData<T>): void
```

Emits the specified event.

**Since:** 23

**Deprecated since:** -1

<!--Device-emitter-function emit<T>(eventId: string, data: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, data: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | Yes |


## emit_string

```TypeScript
function emit(eventId: string, options: Options, data?: EventData): void
```

Emits an event of a specified priority. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function emit(eventId: string, options: Options, data?: EventData): void--><!--Device-emitter-function emit(eventId: string, options: Options, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No |

## Examples

```TypeScript
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};

emitter.emit('eventId', options, eventData);
```


## emit_string

```TypeScript
function emit(eventId: string, options: Options): void
```

Emits an event of a specified priority.

**Since:** 23

**Deprecated since:** -1

<!--Device-emitter-function emit(eventId: string, options: Options): void--><!--Device-emitter-function emit(eventId: string, options: Options): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |


## emit_string

```TypeScript
function emit(eventId: string, options: Options, data: EventData): void
```

Emits an event of a specified priority.

**Since:** 23

**Deprecated since:** -1

<!--Device-emitter-function emit(eventId: string, options: Options, data: EventData): void--><!--Device-emitter-function emit(eventId: string, options: Options, data: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | Yes |


## emit_string

```TypeScript
function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void
```

Emits an event of a specified priority. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No |

## Examples

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

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter.emit('eventId', options, eventData);
```


## emit_string

```TypeScript
function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void
```

Emits an event of a specified priority.

**Since:** 23

**Deprecated since:** -1

<!--Device-emitter-function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | Yes |
