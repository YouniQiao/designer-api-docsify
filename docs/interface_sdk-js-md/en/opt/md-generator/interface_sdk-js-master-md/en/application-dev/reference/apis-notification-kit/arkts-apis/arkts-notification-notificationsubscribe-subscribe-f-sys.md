# subscribe (System API)

## Modules to Import

```TypeScript
import { notificationSubscribe } from '@kit.NotificationKit';
```

## subscribe

```TypeScript
function subscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void
```

Subscribes to notifications of all applications under this user. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 26.0.0

**Substitutes:** [subscribeNotification](arkts-notification-notificationsubscribe-subscribenotification-f-sys.md#subscribeNotification-(System-API))

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function subscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void--><!--Device-notificationSubscribe-function subscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscriber | [NotificationSubscriber](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subscribeCallback = (err: BusinessError) => {
  if (err) {
    console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info("subscribe success");
  }
}
let onConsumeCallback = (data: notificationSubscribe.SubscribeCallbackData) => {
  console.info(`Consume callback: ${JSON.stringify(data)}`);
}
let subscriber: notificationSubscribe.NotificationSubscriber = {
  onConsume: onConsumeCallback
};
notificationSubscribe.subscribe(subscriber, subscribeCallback);
```


## subscribe

```TypeScript
function subscribe(
    subscriber: NotificationSubscriber,
    info: NotificationSubscribeInfo,
    callback: AsyncCallback<void>
  ): void
```

Subscribes to a notification with the subscription information specified. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 26.0.0

**Substitutes:** [subscribeNotification](arkts-notification-notificationsubscribe-subscribenotification-f-sys.md#subscribeNotification-(System-API))

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function subscribe(    subscriber: NotificationSubscriber,    info: NotificationSubscribeInfo,    callback: AsyncCallback<void>  ): void--><!--Device-notificationSubscribe-function subscribe(    subscriber: NotificationSubscriber,    info: NotificationSubscribeInfo,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscriber | [NotificationSubscriber](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | Yes |
| info | [NotificationSubscribeInfo](arkts-notification-notificationsubscribe-notificationsubscribeinfo-t-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// subscribe callback
let subscribeCallback = (err: BusinessError) => {
  if (err) {
    console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info("subscribe success");
  }
}
let onConsumeCallback = (data: notificationSubscribe.SubscribeCallbackData) => {
  console.info(`Consume callback: ${JSON.stringify(data)}`);
}
let subscriber: notificationSubscribe.NotificationSubscriber = {
  onConsume: onConsumeCallback
};
// Bundle names are not verified. You need to determine the target bundle names.
let info: notificationSubscribe.NotificationSubscribeInfo = {
  bundleNames: ["bundleName1","bundleName2"]
};
notificationSubscribe.subscribe(subscriber, info, subscribeCallback);
```


## subscribe

```TypeScript
function subscribe(subscriber: NotificationSubscriber, info?: NotificationSubscribeInfo): Promise<void>
```

Subscribes to a notification with the subscription information specified. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 26.0.0

**Substitutes:** [subscribeNotification](arkts-notification-notificationsubscribe-subscribenotification-f-sys.md#subscribeNotification-(System-API))

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function subscribe(subscriber: NotificationSubscriber, info?: NotificationSubscribeInfo): Promise<void>--><!--Device-notificationSubscribe-function subscribe(subscriber: NotificationSubscriber, info?: NotificationSubscribeInfo): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscriber | [NotificationSubscriber](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | Yes |
| info | [NotificationSubscribeInfo](arkts-notification-notificationsubscribe-notificationsubscribeinfo-t-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let onConsumeCallback = (data: notificationSubscribe.SubscribeCallbackData) => {
  console.info(`Consume callback: ${JSON.stringify(data)}`);
}
let subscriber: notificationSubscribe.NotificationSubscriber = {
  onConsume: onConsumeCallback
};
notificationSubscribe.subscribe(subscriber).then(() => {
  console.info("subscribe success");
}).catch((err: BusinessError) => {
  console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
});
```
