# setTargetDeviceStatus (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## setTargetDeviceStatus

```TypeScript
function setTargetDeviceStatus(deviceType: string, status: number): Promise<void>
```

Sets the status of a device after it is successfully connected. Device status determines the notification mode of the current device when a notification is published.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setTargetDeviceStatus(deviceType: string, status: long): Promise<void>--><!--Device-notificationManager-function setTargetDeviceStatus(deviceType: string, status: long): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceType | string | Yes |
| status | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.setTargetDeviceStatus("current", 1).then(() => {
  console.info(`Succeeded in setting target device status.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set target device status. Code is ${err.code}, message is ${err.message}`);
});
```
