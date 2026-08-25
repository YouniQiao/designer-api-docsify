# unsubscribe

## 导入模块

```TypeScript
```

## unsubscribe

```TypeScript
function unsubscribe(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>): void
```

以回调形式取消订阅公共事件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [unsubscribe](arkts-basicservices-commoneventmanager-unsubscribe-f.md)

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscriber | [CommonEventSubscriber](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |
