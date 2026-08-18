# onGenericEventData

## 导入模块

```TypeScript
```

## onGenericEventData

```TypeScript
function onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

持续订阅指定的事件，并在接收到该事件时，使用callback异步回调。

**起始版本：** 23

<!--Device-emitter-function onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | 是 |
