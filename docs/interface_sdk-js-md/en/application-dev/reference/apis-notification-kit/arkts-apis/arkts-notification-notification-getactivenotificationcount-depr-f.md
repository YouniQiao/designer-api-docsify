# getActiveNotificationCount

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
import { notificationSubscribe } from '@kit.NotificationKit';
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## getActiveNotificationCount

```TypeScript
function getActiveNotificationCount(callback: AsyncCallback<number>): void
```

Obtains the number of active notifications of this application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getActiveNotificationCount](arkts-notification-notificationmanager-getactivenotificationcount-f.md)

<!--Device-notification-function getActiveNotificationCount(callback: AsyncCallback<number>): void--><!--Device-notification-function getActiveNotificationCount(callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import Base from '@ohos.base';

let getActiveNotificationCountCallback = (err: Base.BusinessError, data: number) => {
  if (err) {
    console.info("getActiveNotificationCount failed " + JSON.stringify(err));
  } else {
    console.info("getActiveNotificationCount success");
  }
}

Notification.getActiveNotificationCount(getActiveNotificationCountCallback);
```

```TypeScript
import Base from '@ohos.base';

Notification.getActiveNotificationCount().then((data: number) => {
  console.info("getActiveNotificationCount success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`getAllActiveNotifications failed, code is ${err}`);
});
```


## getActiveNotificationCount

```TypeScript
function getActiveNotificationCount(): Promise<number>
```

Obtains the number of active notifications of this application. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getActiveNotificationCount](arkts-notification-notificationmanager-getactivenotificationcount-f.md)

<!--Device-notification-function getActiveNotificationCount(): Promise<number>--><!--Device-notification-function getActiveNotificationCount(): Promise<number>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the result. |

**Examples**

See [getActiveNotificationCount](#getactivenotificationcount)

