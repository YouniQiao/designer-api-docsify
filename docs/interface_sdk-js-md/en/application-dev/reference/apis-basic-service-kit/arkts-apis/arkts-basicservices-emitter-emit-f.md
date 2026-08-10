# emit

## Modules to Import

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## emit

```TypeScript
function emit(event: InnerEvent, data?: EventData): void
```

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../../../arkts-utils/serializable-overview.md)。目前不支持使用  
[@State装饰器](../../../ui/state-management/arkts-state.md)、  
[@Observed装饰器](../../../ui/state-management/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function emit(event: InnerEvent, data?: EventData): void--><!--Device-emitter-function emit(event: InnerEvent, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [InnerEvent](arkts-basicservices-emitter-innerevent-i.md) | Yes | 发送的事件，其中[EventPriority](arkts-basicservices-emitter-eventpriority-e.md)用于指定事件被发送的优先级。 |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No | 事件携带的数据，默认为空。 |

## Examples

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


## emit

```TypeScript
function emit(eventId: string, data?: EventData): void
```

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../../../arkts-utils/serializable-overview.md)。目前不支持使用  
[@State装饰器](../../../ui/state-management/arkts-state.md)、  
[@Observed装饰器](../../../ui/state-management/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function emit(eventId: string, data?: EventData): void--><!--Device-emitter-function emit(eventId: string, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 发送的事件ID。 不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No | 事件携带的数据，默认为空。 |

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


## emit

```TypeScript
function emit(eventId: string): void
```

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[ArkTS-Sta并发迁移规则](../../quick-start/arkts-dyn-to-sta-concurrency-rules.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit(eventId: string): void--><!--Device-emitter-function emit(eventId: string): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |


## emit

```TypeScript
function emit(eventId: string, data: EventData): void
```

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[ArkTS-Sta并发迁移规则](../../quick-start/arkts-dyn-to-sta-concurrency-rules.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit(eventId: string, data: EventData): void--><!--Device-emitter-function emit(eventId: string, data: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | Yes | 事件携带的数据。 |


## emit

```TypeScript
function emit<T>(eventId: string, data?: GenericEventData<T>): void
```

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../../../arkts-utils/serializable-overview.md)。目前不支持使用  
[@State装饰器](../../../ui/state-management/arkts-state.md)、  
[@Observed装饰器](../../../ui/state-management/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function emit<T>(eventId: string, data?: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 发送的事件ID。 不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No | 事件携带的数据，默认为空。 |

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


## emit

```TypeScript
function emit<T>(eventId: string, data: GenericEventData<T>): void
```

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[ArkTS-Sta并发迁移规则](../../quick-start/arkts-dyn-to-sta-concurrency-rules.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit<T>(eventId: string, data: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, data: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | Yes | 事件携带的数据，默认为空。 |


## emit

```TypeScript
function emit(eventId: string, options: Options, data?: EventData): void
```

发送指定优先级事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../../../arkts-utils/serializable-overview.md)。目前不支持使用  
[@State装饰器](../../../ui/state-management/arkts-state.md)、  
[@Observed装饰器](../../../ui/state-management/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function emit(eventId: string, options: Options, data?: EventData): void--><!--Device-emitter-function emit(eventId: string, options: Options, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 发送的事件ID。 不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes | 事件优先级。 |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No | 事件携带的数据，默认为空。 |

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


## emit

```TypeScript
function emit(eventId: string, options: Options): void
```

发送指定优先级事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[ArkTS-Sta并发迁移规则](../../quick-start/arkts-dyn-to-sta-concurrency-rules.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit(eventId: string, options: Options): void--><!--Device-emitter-function emit(eventId: string, options: Options): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes | 事件优先级。 |


## emit

```TypeScript
function emit(eventId: string, options: Options, data: EventData): void
```

发送指定优先级事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[ArkTS-Sta并发迁移规则](../../quick-start/arkts-dyn-to-sta-concurrency-rules.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit(eventId: string, options: Options, data: EventData): void--><!--Device-emitter-function emit(eventId: string, options: Options, data: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes | 事件优先级。 |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | Yes | 事件携带的数据，默认为空。 |


## emit

```TypeScript
function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void
```

发送指定优先级事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../../../arkts-utils/serializable-overview.md)。目前不支持使用  
[@State装饰器](../../../ui/state-management/arkts-state.md)、  
[@Observed装饰器](../../../ui/state-management/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 发送的事件ID。 不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes | 事件优先级。 |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No | 事件携带的数据，默认为空。 |

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


## emit

```TypeScript
function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void
```

发送指定优先级事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[ArkTS-Sta并发迁移规则](../../quick-start/arkts-dyn-to-sta-concurrency-rules.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes | 事件优先级。 |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | Yes | 事件携带的数据，默认为空。 |

