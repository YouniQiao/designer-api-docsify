# isUserGranted

## Modules to Import

```TypeScript
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## isUserGranted

```TypeScript
function isUserGranted(): Promise<boolean>
```

Checks whether the **Allow access to notifications on this device** switch is toggled on. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SUBSCRIBE_NOTIFICATION

<!--Device-notificationExtensionSubscription-function isUserGranted(): Promise<boolean>--><!--Device-notificationExtensionSubscription-function isUserGranted(): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
notificationExtensionSubscription.isUserGranted().then((isOpen: boolean) => {
  if (isOpen) {
    console.info('isUserGranted true');
  } else {
    console.info('isUserGranted false');
  }
}).catch((err: BusinessError) => {
  console.error(`isUserGranted fail, code is ${err.code}, message is ${err.message}`);
});
```
