# cancelAll

## cancelAll

```TypeScript
function cancelAll(callback: AsyncCallback<void>): void
```

取消所有已发布的通知（callback形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.notificationManager/notificationManager#cancelAll

<!--Device-notification-function cancelAll(callback: AsyncCallback<void>): void--><!--Device-notification-function cancelAll(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## cancelAll

```TypeScript
function cancelAll(): Promise<void>
```

取消所有已发布的通知（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.notificationManager/notificationManager#cancelAll

<!--Device-notification-function cancelAll(): Promise<void>--><!--Device-notification-function cancelAll(): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |
