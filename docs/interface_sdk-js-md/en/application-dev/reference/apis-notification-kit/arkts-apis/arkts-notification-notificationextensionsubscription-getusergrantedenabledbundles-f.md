# getUserGrantedEnabledBundles

## Modules to Import

```TypeScript
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## getUserGrantedEnabledBundles

```TypeScript
function getUserGrantedEnabledBundles(): Promise<GrantedBundleInfo[]>
```

Obtains the applications that are allowed to access device notifications for the current application. This API uses a promise to return the result.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SUBSCRIBE_NOTIFICATION

<!--Device-notificationExtensionSubscription-function getUserGrantedEnabledBundles(): Promise<GrantedBundleInfo[]>--><!--Device-notificationExtensionSubscription-function getUserGrantedEnabledBundles(): Promise<GrantedBundleInfo[]>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;GrantedBundleInfo[]&gt; | Promise used to return the list of applications that are allowed to access device notifications for the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied or current device not supported. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

## Examples

```TypeScript
notificationExtensionSubscription.getUserGrantedEnabledBundles().then((data: notificationExtensionSubscription.GrantedBundleInfo[]) => {
  console.info(`getUserGrantedEnabledBundles successfully. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`getUserGrantedEnabledBundles fail: ${JSON.stringify(err)}`);
});
```

