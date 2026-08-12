# isGeofenceEnabled

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## isGeofenceEnabled

```TypeScript
function isGeofenceEnabled(): Promise<boolean>
```

Checks whether geofencing is enabled. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-notificationManager-function isGeofenceEnabled(): Promise<boolean>--><!--Device-notificationManager-function isGeofenceEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates that geofencing is enabled, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1600012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-insufficient-memory-space) | No memory space. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [1600002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

## Examples

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.isGeofenceEnabled().then((data: boolean) => {
  hilog.info(0x0000, 'testTag', '%{public}s', `isGeofenceEnabled success, enabled:  ${JSON.stringify(data)}.`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', '%{public}s',`isGeofenceEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```

