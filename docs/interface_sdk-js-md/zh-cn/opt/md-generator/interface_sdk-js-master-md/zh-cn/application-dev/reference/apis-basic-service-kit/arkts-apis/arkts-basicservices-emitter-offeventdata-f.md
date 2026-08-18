# offEventData

## 导入模块

```TypeScript
```

## offEventData

```TypeScript
function offEventData(eventId: string, callback: Callback<EventData>): void
```

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用 [onEventData](arkts-basicservices-emitter-oneventdata-f.md#oneventdata)或 [onceEventData](arkts-basicservices-emitter-onceeventdata-f.md#onceeventdata)接口订阅callback时，该接口才生效。 使用该接口取消某个事件订阅后，已通过emit接口发布但尚未被执行的事件将被取消。

**起始版本：** 23

<!--Device-emitter-function offEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function offEventData(eventId: string, callback: Callback<EventData>): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | 是 |
