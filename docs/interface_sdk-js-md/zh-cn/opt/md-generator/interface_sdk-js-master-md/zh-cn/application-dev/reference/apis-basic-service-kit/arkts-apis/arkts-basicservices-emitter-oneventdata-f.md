# onEventData

## 导入模块

```TypeScript
```

## onEventData

```TypeScript
function onEventData(eventId: string, callback: Callback<EventData>): void
```

持续订阅指定的事件，并在接收到该事件时，使用callback异步回调。

**起始版本：** 23

<!--Device-emitter-function onEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function onEventData(eventId: string, callback: Callback<EventData>): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | 是 |
