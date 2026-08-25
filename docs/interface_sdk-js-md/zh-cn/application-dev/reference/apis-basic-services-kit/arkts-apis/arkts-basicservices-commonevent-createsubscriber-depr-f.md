# createSubscriber

## 导入模块

```TypeScript
```

## createSubscriber

```TypeScript
function createSubscriber(
    subscribeInfo: CommonEventSubscribeInfo,
    callback: AsyncCallback<CommonEventSubscriber>
  ): void
```

以回调形式创建订阅者。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createSubscriber](arkts-basicservices-commoneventmanager-createsubscriber-f.md)( subscribeInfo: CommonEventSubscribeInfo, callback: AsyncCallback&lt;CommonEventSubscriber&gt; )

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](arkts-basicservices-commoneventsubscribeinfo-commoneventsubscribeinfo-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[CommonEventSubscriber](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md)&gt; | 是 |


## createSubscriber

```TypeScript
function createSubscriber(subscribeInfo: CommonEventSubscribeInfo): Promise<CommonEventSubscriber>
```

以Promise形式创建订阅者。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createSubscriber](arkts-basicservices-commoneventmanager-createsubscriber-f.md)(subscribeInfo: CommonEventSubscribeInfo)

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](arkts-basicservices-commoneventsubscribeinfo-commoneventsubscribeinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CommonEventSubscriber](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md)&gt; |
