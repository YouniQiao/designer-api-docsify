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

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SUBSCRIBE_NOTIFICATION

<!--Device-notificationExtensionSubscription-function getUserGrantedEnabledBundles(): Promise<GrantedBundleInfo[]>--><!--Device-notificationExtensionSubscription-function getUserGrantedEnabledBundles(): Promise<GrantedBundleInfo[]>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;GrantedBundleInfo[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
notificationExtensionSubscription.getUserGrantedEnabledBundles().then((data: notificationExtensionSubscription.GrantedBundleInfo[]) => {
  console.info(`getUserGrantedEnabledBundles successfully. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`getUserGrantedEnabledBundles fail, code is ${err.code}, message is ${err.message}`);
});
```
