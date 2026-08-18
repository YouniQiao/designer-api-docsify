# enableNotification (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
import { notificationSubscribe } from '@kit.NotificationKit';
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## enableNotification

```TypeScript
function enableNotification(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void
```

Sets whether to enable notification for a specified application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function enableNotification(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void--><!--Device-notification-function enableNotification(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | BundleOption | Yes | Bundle information of the application. |
| enable | boolean | Yes | Whether to enable notification. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |


## enableNotification

```TypeScript
function enableNotification(bundle: BundleOption, enable: boolean): Promise<void>
```

Sets whether to enable notification for a specified application. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function enableNotification(bundle: BundleOption, enable: boolean): Promise<void>--><!--Device-notification-function enableNotification(bundle: BundleOption, enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | BundleOption | Yes | Bundle information of the application. |
| enable | boolean | Yes | Whether to enable notification. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

