# getDeviceRemindType (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getDeviceRemindType

```TypeScript
function getDeviceRemindType(callback: AsyncCallback<DeviceRemindType>): void
```

Obtains the notification reminder type. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 26.0.0

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getDeviceRemindType(callback: AsyncCallback<DeviceRemindType>): void--><!--Device-notificationManager-function getDeviceRemindType(callback: AsyncCallback<DeviceRemindType>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DeviceRemindType&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let getDeviceRemindTypeCallback = (err: BusinessError, data: notificationManager.DeviceRemindType): void => {
    if (err) {
        console.error(`getDeviceRemindType failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info(`getDeviceRemindType success, data is ${JSON.stringify(data)}`);
    }
};
notificationManager.getDeviceRemindType(getDeviceRemindTypeCallback);
```


## getDeviceRemindType

```TypeScript
function getDeviceRemindType(): Promise<DeviceRemindType>
```

Obtains the notification reminder type. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 26.0.0

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getDeviceRemindType(): Promise<DeviceRemindType>--><!--Device-notificationManager-function getDeviceRemindType(): Promise<DeviceRemindType>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DeviceRemindType & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getDeviceRemindType().then((data: notificationManager.DeviceRemindType) => {
    console.info(`getDeviceRemindType success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDeviceRemindType failed, code is ${err.code}, message is ${err.message}`);
});
```
