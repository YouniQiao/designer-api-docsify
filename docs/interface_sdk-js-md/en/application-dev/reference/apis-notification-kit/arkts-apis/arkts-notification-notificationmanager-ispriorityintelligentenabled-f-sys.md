# isPriorityIntelligentEnabled (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## isPriorityIntelligentEnabled

```TypeScript
function isPriorityIntelligentEnabled(): Promise<boolean>
```

Obtains whether the intelligent priority notification service is enabled. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationManager-function isPriorityIntelligentEnabled(): Promise<boolean>--><!--Device-notificationManager-function isPriorityIntelligentEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise that contains the enabling status of the intelligent priority notification service. &lt;br&gt; - **true**: The intelligent priority notification service is enabled. &lt;br&gt; - **false**: The intelligent priority notification service is disabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1600012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-insufficient-memory-space) | No memory space. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

notificationManager.isPriorityIntelligentEnabled().then((result: boolean) => {
  hilog.info(0x0000, 'testTag', `isPriorityIntelligentEnabled result: ${result}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `isPriorityIntelligentEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```

