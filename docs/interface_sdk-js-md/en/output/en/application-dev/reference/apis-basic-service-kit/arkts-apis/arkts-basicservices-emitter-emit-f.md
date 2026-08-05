# emit

## emit

```TypeScript
function emit(event: InnerEvent, data?: EventData): void
```

Emits a specified event. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. Currently, complex data decorated by decorators such as \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ and \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function emit(event: InnerEvent, data?: EventData): void--><!--Device-emitter-function emit(event: InnerEvent, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Event to emit, where [EventPriority]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ specifies the emit priority of the event. |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Data carried by the event. This parameter is left empty by default. |

**Example**

ArkTS-Dyn example:

```TypeScript
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

let innerEvent: emitter.InnerEvent = {
  eventId: 1,
  priority: emitter.EventPriority.HIGH
};

emitter.emit(innerEvent, eventData);
```

ArkTS-Sta example:

```TypeScript
import { RecordData } from '@ohos.base';

let record: Record<string, RecordData> = {
  "content": "content",
  "id": 1,
};

let eventData: emitter.EventData = {
  data: record // The types are now compatible.
};

let innerEvent: emitter.InnerEvent = {
  eventId: 1,
  priority: emitter.EventPriority.HIGH
};

emitter.emit(innerEvent, eventData);
```


## emit

```TypeScript
function emit(eventId: string, data?: EventData): void
```

Emits a specified event. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. Currently, complex data decorated by decorators such as \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ and \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function emit(eventId: string, data?: EventData): void--><!--Device-emitter-function emit(eventId: string, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Data carried by the event. This parameter is left empty by default. |

**Example**

```TypeScript
let eventData: emitter.EventData = {
  data: {
  "content": "content",
  "id": 1,
  }
};

emitter.emit("eventId", eventData);
```


## emit

```TypeScript
function emit(eventId: string): void
```

Emits the specified event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit(eventId: string): void--><!--Device-emitter-function emit(eventId: string): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |

**Example**

```TypeScript
emitter.emit("eventId");
```


## emit

```TypeScript
function emit(eventId: string, data: EventData): void
```

Emits the specified event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit(eventId: string, data: EventData): void--><!--Device-emitter-function emit(eventId: string, data: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Data passed in the event. |

**Example**

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


## emit

```TypeScript
function emit<T>(eventId: string, data?: GenericEventData<T>): void
```

Emits a specified event. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. Currently, complex data decorated by decorators such as \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ and \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function emit<T>(eventId: string, data?: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | No | Data carried by the event. This parameter is left empty by default. |

**Example**

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


## emit

```TypeScript
function emit<T>(eventId: string, data: GenericEventData<T>): void
```

Emits the specified event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit<T>(eventId: string, data: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, data: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes | Data passed in the event. |


## emit

```TypeScript
function emit(eventId: string, options: Options, data?: EventData): void
```

Emits an event of a specified priority. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. Currently, complex data decorated by decorators such as \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ and \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function emit(eventId: string, options: Options, data?: EventData): void--><!--Device-emitter-function emit(eventId: string, options: Options, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Event emit priority. |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Data carried by the event. This parameter is left empty by default. |

**Example**

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


## emit

```TypeScript
function emit(eventId: string, options: Options): void
```

Emits an event of a specified priority.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit(eventId: string, options: Options): void--><!--Device-emitter-function emit(eventId: string, options: Options): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Event emit priority. |

**Example**

```TypeScript
let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};

emitter.emit("eventId", options);
```


## emit

```TypeScript
function emit(eventId: string, options: Options, data: EventData): void
```

Emits an event of a specified priority.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit(eventId: string, options: Options, data: EventData): void--><!--Device-emitter-function emit(eventId: string, options: Options, data: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Event emit priority. |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Data passed in the event. |

**Example**

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


## emit

```TypeScript
function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void
```

Emits an event of a specified priority. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. Currently, complex data decorated by decorators such as \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ and \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Event emit priority. |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | No | Data carried by the event. This parameter is left empty by default. |

**Example**

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


## emit

```TypeScript
function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void
```

Emits an event of a specified priority.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | ID of the event to emit. The value cannot be an empty string and exceed 10240 bytes. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Event emit priority. |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes | Data passed in the event. |

