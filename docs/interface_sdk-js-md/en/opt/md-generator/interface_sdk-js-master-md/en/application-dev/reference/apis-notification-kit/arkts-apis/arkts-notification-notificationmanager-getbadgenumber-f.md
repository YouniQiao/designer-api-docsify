# getBadgeNumber

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getBadgeNumber

```TypeScript
function getBadgeNumber(): Promise<number>
```

Obtains the badge number of this application. This API uses a promise to return the result.

This API is used to query the badge number displayed on the current application's desktop icon.

**Since:** 22

<!--Device-notificationManager-function getBadgeNumber(): Promise<long>--><!--Device-notificationManager-function getBadgeNumber(): Promise<long>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getBadgeNumber().then((badgeNumber: number) => {
  console.info(`Succeeded in getting badge number, badgeNumber is ${JSON.stringify(badgeNumber)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get badge number. Code is ${err.code}, message is ${err.message}`);
});
```
