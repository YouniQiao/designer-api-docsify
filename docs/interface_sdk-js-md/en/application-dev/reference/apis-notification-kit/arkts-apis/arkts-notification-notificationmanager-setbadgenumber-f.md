# setBadgeNumber

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## setBadgeNumber

```TypeScript
function setBadgeNumber(badgeNumber: int, callback: AsyncCallback<void>): void
```

Sets the notification badge number. This API uses an asynchronous callback to return the result.

A badge is a numeric identifier displayed in the upper right corner of an application's desktop icon, used to prompt the user about the number of unprocessed notifications. After setting, the desktop icon will display the corresponding badge number. This is suitable for scenarios where the number of pending messages needs to be prompted on the desktop icon, such as the number of unread messages and to-do items.

This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-notificationManager-function setBadgeNumber(badgeNumber: int, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function setBadgeNumber(badgeNumber: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

[getActiveNotificationCount](notificationManager.getActiveNotificationCount(callback: AsyncCallback<long>): void) obtains the number of

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| badgeNumber | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Notification badge number to set. If **badgeNumber** is set to a value less than or equal to **0**, badges are cleared; if the value is greater than **99**, **99+** is displayed on the badge. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.<br>**Applicable version:** 18 and later |
| [1600012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-insufficient-memory-space) | No memory space. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [1600002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let setBadgeNumberCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in setting badge number.`);
  }
}
let badgeNumber: number = 10;
notificationManager.setBadgeNumber(badgeNumber, setBadgeNumberCallback);
```


## setBadgeNumber

```TypeScript
function setBadgeNumber(badgeNumber: int): Promise<void>
```

Sets the notification badge number. This API uses a promise to return the result.

A badge is a numeric identifier displayed in the upper right corner of an application's desktop icon, used to prompt the user about the number of unprocessed notifications. After setting, the desktop icon will display the corresponding badge number. This is suitable for scenarios where the number of pending messages needs to be prompted on the desktop icon, such as the number of unread messages and to-do items.

This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-notificationManager-function setBadgeNumber(badgeNumber: int): Promise<void>--><!--Device-notificationManager-function setBadgeNumber(badgeNumber: int): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

[getActiveNotificationCount](notificationManager.getActiveNotificationCount(): Promise<number>) obtains the number of

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| badgeNumber | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Notification badge number to set. If **badgeNumber** is set to a value less than or equal to **0**, badges are cleared; if the value is greater than **99**, **99+** is displayed on the badge. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.<br>**Applicable version:** 18 and later |
| [1600012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-insufficient-memory-space) | No memory space. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [1600002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let badgeNumber: number = 10;
notificationManager.setBadgeNumber(badgeNumber).then(() => {
  console.info(`Succeeded in setting badge number.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
});
```

