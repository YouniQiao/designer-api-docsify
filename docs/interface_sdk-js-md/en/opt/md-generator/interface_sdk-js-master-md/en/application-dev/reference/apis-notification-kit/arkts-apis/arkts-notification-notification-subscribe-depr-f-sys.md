# subscribe (System API)

## Modules to Import

```TypeScript
```

## subscribe

```TypeScript
function subscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void
```

Subscribes to notifications of all applications under this user. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [subscribe](arkts-notification-notificationsubscribe-subscribe-f-sys.md#subscribe-system-api)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function subscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void--><!--Device-notification-function subscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscriber | [NotificationSubscriber](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## subscribe

```TypeScript
function subscribe(
    subscriber: NotificationSubscriber,
    info: NotificationSubscribeInfo,
    callback: AsyncCallback<void>
  ): void
```

Subscribes to a notification with the subscription information specified. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [subscribe](arkts-notification-notificationsubscribe-subscribe-f-sys.md#subscribe-system-api)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function subscribe(    subscriber: NotificationSubscriber,    info: NotificationSubscribeInfo,    callback: AsyncCallback<void>  ): void--><!--Device-notification-function subscribe(    subscriber: NotificationSubscriber,    info: NotificationSubscribeInfo,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscriber | [NotificationSubscriber](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | Yes |
| info | [NotificationSubscribeInfo](arkts-notification-notificationsubscribeinfo-notificationsubscribeinfo-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## subscribe

```TypeScript
function subscribe(subscriber: NotificationSubscriber, info?: NotificationSubscribeInfo): Promise<void>
```

Subscribes to a notification with the subscription information specified. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [subscribe](arkts-notification-notificationsubscribe-subscribe-f-sys.md#subscribe-system-api)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function subscribe(subscriber: NotificationSubscriber, info?: NotificationSubscribeInfo): Promise<void>--><!--Device-notification-function subscribe(subscriber: NotificationSubscriber, info?: NotificationSubscribeInfo): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscriber | [NotificationSubscriber](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | Yes |
| info | [NotificationSubscribeInfo](arkts-notification-notificationsubscribeinfo-notificationsubscribeinfo-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
