# unsubscribe (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
import { notificationSubscribe } from '@kit.NotificationKit';
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## unsubscribe

```TypeScript
function unsubscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void
```

Unsubscribes from a notification. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [unsubscribe](arkts-notification-notificationsubscribe-unsubscribe-f-sys.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function unsubscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void--><!--Device-notification-function unsubscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subscriber | [NotificationSubscriber](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | Yes | Notification subscriber. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import Base from '@ohos.base';
import NotificationSubscribe from '@ohos.notificationSubscribe';

let unsubscribeCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("unsubscribe failed " + JSON.stringify(err));
  } else {
    console.info("unsubscribe success");
  }
}
let onDisconnectCallback = () => {
  console.info("subscribe disconnect");
}
let subscriber: NotificationSubscribe.NotificationSubscriber = {
  onDisconnect: onDisconnectCallback
};
Notification.unsubscribe(subscriber, unsubscribeCallback);
```

```TypeScript
import Base from '@ohos.base';
import NotificationSubscribe from '@ohos.notificationSubscribe';

function onDisconnectCallback() {
  console.info("subscribe disconnect");
}
let subscriber: NotificationSubscribe.NotificationSubscriber = {
  onDisconnect: onDisconnectCallback
};
Notification.unsubscribe(subscriber).then(() => {
  console.info("unsubscribe success");
}).catch((err: Base.BusinessError) => {
  console.error(`unsubscribe failed, code is ${err}`);
});
```


## unsubscribe

```TypeScript
function unsubscribe(subscriber: NotificationSubscriber): Promise<void>
```

Unsubscribes from a notification. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [unsubscribe](arkts-notification-notificationsubscribe-unsubscribe-f-sys.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function unsubscribe(subscriber: NotificationSubscriber): Promise<void>--><!--Device-notification-function unsubscribe(subscriber: NotificationSubscriber): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subscriber | [NotificationSubscriber](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | Yes | Notification subscriber. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [unsubscribe](#unsubscribe)

