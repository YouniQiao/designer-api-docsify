# off

## 导入模块

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## off

```TypeScript
function off(eventId: number): void
```

取消事件ID为eventId的所有订阅。使用该接口取消某个事件订阅后，已通过emit接口发布但尚未被执行的事件将被取消。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | number | 是 |


## off

```TypeScript
function off(eventId: string): void
```

取消事件ID为eventId的所有订阅。使用该接口取消某个事件订阅后，已通过emit接口发布但尚未被执行的事件将被取消。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |


## off

```TypeScript
function off(eventId: number, callback: Callback<EventData>): void
```

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用on或 once接口订阅callback时，该接口才生效。使用该接口取消某个事件订阅后，已通过emit接口发布但尚未被执行的事件将被取消。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | number | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | 是 |


## off

```TypeScript
function off(eventId: string, callback: Callback<EventData>): void
```

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用on或 once接口订阅callback时，该接口才生效。使用该接口取消某个事件订阅后，已通过emit接口发布但尚未被执行的事件将被取消。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | 是 |


## off

```TypeScript
function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用 on或 once接口订阅callback时，该接口才生效。使用该接口取消某个事件订阅后，已通过emit接口发布但尚未被执行的事件将被取消。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | 是 |
