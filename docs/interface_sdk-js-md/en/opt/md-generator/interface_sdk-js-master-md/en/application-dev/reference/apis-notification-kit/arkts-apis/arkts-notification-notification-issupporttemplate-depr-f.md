# isSupportTemplate

## isSupportTemplate

```TypeScript
function isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void
```

Checks whether a specified template is supported before using  
[NotificationTemplate](@link ./notification/notificationTemplate:NotificationTemplate) to publish a notification.This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isSupportTemplate](ohos.notificationManager/notificationManager#isSupportTemplate)

<!--Device-notification-function isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void--><!--Device-notification-function isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| templateName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## isSupportTemplate

```TypeScript
function isSupportTemplate(templateName: string): Promise<boolean>
```

Checks whether a specified template is supported before using  
[NotificationTemplate](@link ./notification/notificationTemplate:NotificationTemplate) to publish a notification.This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isSupportTemplate](ohos.notificationManager/notificationManager#isSupportTemplate)

<!--Device-notification-function isSupportTemplate(templateName: string): Promise<boolean>--><!--Device-notification-function isSupportTemplate(templateName: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| templateName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
