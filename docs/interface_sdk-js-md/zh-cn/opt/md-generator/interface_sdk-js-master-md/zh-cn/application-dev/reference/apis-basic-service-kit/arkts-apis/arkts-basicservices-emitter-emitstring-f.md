# emit_string

## emit_string

```TypeScript
function emit(eventId: string, data?: EventData): void
```

发送指定事件。 该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../../../arkts-utils/serializable-overview.md)。目前不支持使用 [@State装饰器](../../../ui/state-management/arkts-state.md)、 [@Observed装饰器](../../../ui/state-management/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。 该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-emitter-function emit(eventId: string, data?: EventData): void--><!--Device-emitter-function emit(eventId: string, data?: EventData): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | 否 |

## 示例

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

发送指定事件。 该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见ArkTS-Sta并发迁移规则

**起始版本：** 23

**废弃版本：** -1

<!--Device-emitter-function emit(eventId: string): void--><!--Device-emitter-function emit(eventId: string): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |


## emit_string

```TypeScript
function emit(eventId: string, data: EventData): void
```

发送指定事件。 该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见ArkTS-Sta并发迁移规则

**起始版本：** 23

**废弃版本：** -1

<!--Device-emitter-function emit(eventId: string, data: EventData): void--><!--Device-emitter-function emit(eventId: string, data: EventData): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | 是 |


## emit_string

```TypeScript
function emit<T>(eventId: string, data?: GenericEventData<T>): void
```

发送指定事件。 该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../../../arkts-utils/serializable-overview.md)。目前不支持使用 [@State装饰器](../../../ui/state-management/arkts-state.md)、 [@Observed装饰器](../../../ui/state-management/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。 该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-emitter-function emit<T>(eventId: string, data?: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, data?: GenericEventData<T>): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | 否 |

## 示例

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

发送指定事件。 该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见ArkTS-Sta并发迁移规则

**起始版本：** 23

**废弃版本：** -1

<!--Device-emitter-function emit<T>(eventId: string, data: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, data: GenericEventData<T>): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | 是 |


## emit_string

```TypeScript
function emit(eventId: string, options: Options, data?: EventData): void
```

发送指定优先级事件。 该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../../../arkts-utils/serializable-overview.md)。目前不支持使用 [@State装饰器](../../../ui/state-management/arkts-state.md)、 [@Observed装饰器](../../../ui/state-management/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。 该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-emitter-function emit(eventId: string, options: Options, data?: EventData): void--><!--Device-emitter-function emit(eventId: string, options: Options, data?: EventData): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | 是 |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | 否 |

## 示例

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

发送指定优先级事件。 该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见ArkTS-Sta并发迁移规则

**起始版本：** 23

**废弃版本：** -1

<!--Device-emitter-function emit(eventId: string, options: Options): void--><!--Device-emitter-function emit(eventId: string, options: Options): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | 是 |


## emit_string

```TypeScript
function emit(eventId: string, options: Options, data: EventData): void
```

发送指定优先级事件。 该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见ArkTS-Sta并发迁移规则

**起始版本：** 23

**废弃版本：** -1

<!--Device-emitter-function emit(eventId: string, options: Options, data: EventData): void--><!--Device-emitter-function emit(eventId: string, options: Options, data: EventData): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | 是 |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | 是 |


## emit_string

```TypeScript
function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void
```

发送指定优先级事件。 该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../../../arkts-utils/serializable-overview.md)。目前不支持使用 [@State装饰器](../../../ui/state-management/arkts-state.md)、 [@Observed装饰器](../../../ui/state-management/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。 该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-emitter-function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | 是 |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | 否 |

## 示例

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

发送指定优先级事件。 该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见ArkTS-Sta并发迁移规则

**起始版本：** 23

**废弃版本：** -1

<!--Device-emitter-function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void--><!--Device-emitter-function emit<T>(eventId: string, options: Options, data: GenericEventData<T>): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| options | [Options](arkts-basicservices-zlib-options-i.md) | 是 |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | 是 |
