# getActiveNotificationByFilter (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getActiveNotificationByFilter

```TypeScript
function getActiveNotificationByFilter(filter: NotificationFilter, callback: AsyncCallback<NotificationRequest>): void
```

Obtains information about the common live view that matches the specified filter criteria. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getActiveNotificationByFilter(filter: NotificationFilter, callback: AsyncCallback<NotificationRequest>): void--><!--Device-notificationManager-function getActiveNotificationByFilter(filter: NotificationFilter, callback: AsyncCallback<NotificationRequest>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [NotificationFilter](arkts-notification-notificationmanager-notificationfilter-t-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NotificationRequest&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { notificationSubscribe } from '@kit.NotificationKit';

let bundleOption: notificationManager.BundleOption = {
  bundle: "bundleName1",
};
let notificationKey: notificationSubscribe.NotificationKey = {
    id: 11,
    label: ""
};
let filter: notificationManager.NotificationFilter = {
    bundle: bundleOption,
    notificationKey: notificationKey,
    extraInfoKeys: ['event']
}
let getActiveNotificationByFilterCallback = (err: BusinessError, data: notificationManager.NotificationRequest): void => {
    if (err) {
        console.error(`getActiveNotificationByFilter failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("getActiveNotificationByFilter success");
    }
}
notificationManager.getActiveNotificationByFilter(filter, getActiveNotificationByFilterCallback);
```


## getActiveNotificationByFilter

```TypeScript
function getActiveNotificationByFilter(filter: NotificationFilter, callback: AsyncCallback<NotificationRequest|null>): void
```

Obtains information about the common live view that matches the specified filter criteria. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getActiveNotificationByFilter(filter: NotificationFilter, callback: AsyncCallback<NotificationRequest|null>): void--><!--Device-notificationManager-function getActiveNotificationByFilter(filter: NotificationFilter, callback: AsyncCallback<NotificationRequest|null>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [NotificationFilter](arkts-notification-notificationmanager-notificationfilter-t-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NotificationRequest \| null & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) |


## getActiveNotificationByFilter

```TypeScript
function getActiveNotificationByFilter(filter: NotificationFilter): Promise<NotificationRequest>
```

Obtains information about the common live view that matches the specified filter criteria. This API uses a promise to return the result.

**Since:** 11

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getActiveNotificationByFilter(filter: NotificationFilter): Promise<NotificationRequest>--><!--Device-notificationManager-function getActiveNotificationByFilter(filter: NotificationFilter): Promise<NotificationRequest>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [NotificationFilter](arkts-notification-notificationmanager-notificationfilter-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;NotificationRequest & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { notificationSubscribe } from '@kit.NotificationKit';

let bundleOption: notificationManager.BundleOption = {
  bundle: "bundleName1",
};
let notificationKey: notificationSubscribe.NotificationKey = {
    id: 11,
    label: ""
};
let filter: notificationManager.NotificationFilter = {
    bundle: bundleOption,
    notificationKey: notificationKey,
    extraInfoKeys: ['event']
}
notificationManager.getActiveNotificationByFilter(filter).then((data: notificationManager.NotificationRequest) => {
    console.info(`getActiveNotificationByFilter success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getActiveNotificationByFilter failed, code is ${err.code}, message is ${err.message}`);
});
```


## getActiveNotificationByFilter

```TypeScript
function getActiveNotificationByFilter(filter: NotificationFilter): Promise<NotificationRequest|null>
```

Obtains information about the common live view that matches the specified filter criteria. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getActiveNotificationByFilter(filter: NotificationFilter): Promise<NotificationRequest|null>--><!--Device-notificationManager-function getActiveNotificationByFilter(filter: NotificationFilter): Promise<NotificationRequest|null>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [NotificationFilter](arkts-notification-notificationmanager-notificationfilter-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;NotificationRequest \ | null & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
