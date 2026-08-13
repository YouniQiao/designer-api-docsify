# onceGenericEventData

## onceGenericEventData

```TypeScript
function onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

单次订阅当前Emitter类实例指定的事件，在接收到该事件且执行完相应的回调函数后，自动取消订阅。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-emitter-function onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | 是 |
