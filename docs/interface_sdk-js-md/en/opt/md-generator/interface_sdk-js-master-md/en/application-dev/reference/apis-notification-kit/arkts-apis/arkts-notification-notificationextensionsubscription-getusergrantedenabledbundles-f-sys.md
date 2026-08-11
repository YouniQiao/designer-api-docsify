# getUserGrantedEnabledBundles (System API)

## Modules to Import

```TypeScript
import { notificationExtensionSubscription } from 'kits/@kit.NotificationKit';
```

## getUserGrantedEnabledBundles

```TypeScript
function getUserGrantedEnabledBundles(targetBundle: BundleOption): Promise<BundleOption[]>
```

Obtains the applications that are allowed to access device notifications.This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationExtensionSubscription-function getUserGrantedEnabledBundles(targetBundle: BundleOption): Promise<BundleOption[]>--><!--Device-notificationExtensionSubscription-function getUserGrantedEnabledBundles(targetBundle: BundleOption): Promise<BundleOption[]>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| targetBundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;BundleOption[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600022](../errorcode-notification.md#1600022-invalid-bundle-information) |

## Examples

```TypeScript
let targetBundle: notificationExtensionSubscription.BundleOption =
{
  // Use the actual target application information.
  bundle: 'com.example.testnotification',
};
notificationExtensionSubscription.getUserGrantedEnabledBundles(targetBundle).then((data: notificationExtensionSubscription.BundleOption[]) => {
  console.info(`getUserGrantedEnabledBundles successfully. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`getUserGrantedEnabledBundles fail, code is ${err.code}, message is ${err.message}`);
});
```
