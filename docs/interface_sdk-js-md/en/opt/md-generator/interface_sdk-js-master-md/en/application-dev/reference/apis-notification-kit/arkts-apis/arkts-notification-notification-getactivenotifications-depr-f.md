# getActiveNotifications

## getActiveNotifications

```TypeScript
function getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void
```

Obtains active notifications of this application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md#getActiveNotifications)

<!--Device-notification-function getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void--><!--Device-notification-function getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md)&gt;&gt; | Yes |


## getActiveNotifications

```TypeScript
function getActiveNotifications(): Promise<Array<NotificationRequest>>
```

Obtains active notifications of this application. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md#getActiveNotifications)

<!--Device-notification-function getActiveNotifications(): Promise<Array<NotificationRequest>>--><!--Device-notification-function getActiveNotifications(): Promise<Array<NotificationRequest>>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md)&gt;&gt; |
