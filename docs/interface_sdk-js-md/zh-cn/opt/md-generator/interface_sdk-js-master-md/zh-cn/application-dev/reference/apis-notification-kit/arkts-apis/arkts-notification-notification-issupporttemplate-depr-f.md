# isSupportTemplate

## isSupportTemplate

```TypeScript
function isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void
```

在使用[通知模板](arkts-notification-notificationtemplate-notificationtemplate-i.md#NotificationTemplate)发布通知前，可以通过该接口查询是否支持对应的通知模板。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isSupportTemplate](ohos.notificationManager/notificationManager#isSupportTemplate)

<!--Device-notification-function isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void--><!--Device-notification-function isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| templateName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isSupportTemplate

```TypeScript
function isSupportTemplate(templateName: string): Promise<boolean>
```

在使用[通知模板](arkts-notification-notificationtemplate-notificationtemplate-i.md#NotificationTemplate)发布通知前，可以通过该接口查询是否支持对应的通知模板。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isSupportTemplate](ohos.notificationManager/notificationManager#isSupportTemplate)

<!--Device-notification-function isSupportTemplate(templateName: string): Promise<boolean>--><!--Device-notification-function isSupportTemplate(templateName: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| templateName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
