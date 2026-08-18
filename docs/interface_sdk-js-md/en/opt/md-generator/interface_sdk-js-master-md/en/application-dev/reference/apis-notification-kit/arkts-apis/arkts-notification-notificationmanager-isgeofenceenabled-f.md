# isGeofenceEnabled

## Modules to Import

```TypeScript
```

## isGeofenceEnabled

```TypeScript
function isGeofenceEnabled(): Promise<boolean>
```

Checks whether geofencing is enabled. This API uses a promise to return the result.

**Since:** 23

<!--Device-notificationManager-function isGeofenceEnabled(): Promise<boolean>--><!--Device-notificationManager-function isGeofenceEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

**Examples**

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.isGeofenceEnabled().then((data: boolean) => {
  hilog.info(0x0000, 'testTag', '%{public}s', `isGeofenceEnabled success, enabled:  ${JSON.stringify(data)}.`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', '%{public}s',`isGeofenceEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```
