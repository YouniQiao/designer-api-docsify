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

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function emit(eventId: string, data?: EventData): void--><!--Device-emitter-function emit(eventId: string, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No | Data carried by the event. This parameter is left empty by default. |

## Examples

```TypeScript
let eventData: emitter.EventData = {
  data: {
  "content": "content",
  "id": 1,
  }
};

emitter.emit("eventId", eventData);
```


## emit_string

```TypeScript
function emit(eventId: string): void
```

Emits the specified event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-emitter-function emit(eventId: string): void--><!--Device-emitter-function emit(eventId: string): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |

## Examples

```TypeScript
emitter.emit("eventId");
```


## emit_string

```TypeScript
function emit(eventId: string, data: EventData): void
```

Emits the specified event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-emitter-function emit(eventId: string, data: EventData): void--><!--Device-emitter-function emit(eventId: string, data: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | Yes | Data passed in the event. |

## Examples

```TypeScript
import { RecordData } from '@ohos.base';

let record: Record<string, RecordData> = {
  "content": "content",
  "id": 1,
};

let eventData: emitter.EventData = {
  data: record // The types are now compatible.
};

emitter.emit("eventId", eventData);
```


## emit_string

```TypeScript
function emit<T>(eventId: string, data?: GenericEventData<T>): void
```

Emits a specified event. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function emit<T>(eventId: string, data?: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No | Data carried by the event. This parameter is left empty by default. |

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
emitter.emit("eventId", eventData);
```


## emit_string

```TypeScript
function emit<T>(eventId: string, data: GenericEventData<T>): void
```

Emits the specified event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-emitter-function emit<T>(eventId: string, data: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, data: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | Yes | Data passed in the event. |


## emit_string

```TypeScript
function emit(eventId: string, options: Options, data?: EventData): void
```

Emits an event of a specified priority. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function emit(eventId: string, options: Options, data?: EventData): void--><!--Device-emitter-function emit(eventId: string, options: Options, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| options | Options | Yes | Event emit priority. |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No | Data carried by the event. This parameter is left empty by default. |

## Examples

ArkTS-Dyn example:

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

emitter.emit("eventId", options, eventData);
```


## emit_string

```TypeScript
function emit(eventId: string, options: Options): void
```

Emits an event of a specified priority.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-emitter-function emit(eventId: string, options: Options): void--><!--Device-emitter-function emit(eventId: string, options: Options): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |
| options | Options | Yes | Event emit priority. |

## Examples

```TypeScript
let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};

emitter.emit("eventId", options);
```


## emit_string

```TypeScript
function emit(eventId: string, options: Options, data: EventData): void
```

Emits an event of a specified priority.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-emitter-function emit(eventId: string, options: Options, data: EventData): void--><!--Device-emitter-function emit(eventId: string, options: Options, data: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |
| options | Options | Yes | Event emit priority. |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | Yes | Data passed in the event. |

## Examples

```TypeScript
let record: Record<string, RecordData> = {
  "content": "content",
  "id": 1,
};

let eventData: emitter.EventData = {
  data: record // The types are now compatible.
};

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};

emitter.emit("eventId", options, eventData);
```


## emit_string

```TypeScript
function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void
```

Emits an event of a specified priority. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| options | Options | Yes | Event emit priority. |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No | Data carried by the event. This parameter is left empty by default. |

## Examples

ArkTS-Dyn example:

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

emitter.emit("eventId", options, eventData);
```

ArkTS-Sta example:

```TypeScript
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

emitter.emit("eventId", options, eventData);
```


## emit_string

```TypeScript
function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void
```

Emits an event of a specified priority.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-emitter-function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |
| options | Options | Yes | Event emit priority. |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | Yes | Data passed in the event. |

