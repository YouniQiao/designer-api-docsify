# getActiveNotificationCount

## getActiveNotificationCount

```TypeScript
function getActiveNotificationCount(callback: AsyncCallback<number>): void
```

Obtains the number of active notifications of this application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#getActiveNotificationCount

<!--Device-notification-function getActiveNotificationCount(callback: AsyncCallback<number>): void--><!--Device-notification-function getActiveNotificationCount(callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |


## getActiveNotificationCount

```TypeScript
function getActiveNotificationCount(): Promise<number>
```

Obtains the number of active notifications of this application. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#getActiveNotificationCount

<!--Device-notification-function getActiveNotificationCount(): Promise<number>--><!--Device-notification-function getActiveNotificationCount(): Promise<number>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |
