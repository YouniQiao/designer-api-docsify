# subscribe

## 导入模块

```TypeScript
```

## subscribe

```TypeScript
function subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void
```

以回调形式订阅公共事件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [subscribe](arkts-basicservices-commoneventmanager-subscribe-f.md)

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscriber | [CommonEventSubscriber](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[CommonEventData](arkts-basicservices-commoneventdata-commoneventdata-i.md)&gt; | 是 |
