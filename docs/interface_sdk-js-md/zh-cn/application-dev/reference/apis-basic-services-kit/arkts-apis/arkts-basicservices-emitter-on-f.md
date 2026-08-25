# on

## 导入模块

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## on

```TypeScript
function on(event: InnerEvent, callback: Callback<EventData>): void
```

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [InnerEvent](arkts-basicservices-emitter-innerevent-i.md) | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | 是 |


## on

```TypeScript
function on(eventId: string, callback: Callback<EventData>): void
```

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | 是 |


## on

```TypeScript
function on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | 是 |
