# getUserGrantedState (System API)

## Modules to Import

```TypeScript
import { notificationExtensionSubscription } from 'kits/@kit.NotificationKit';
```

## getUserGrantedState

```TypeScript
function getUserGrantedState(targetBundle: BundleOption): Promise<boolean>
```

Obtains the enabling state of the **Allow access to notifications on this device** switch of a specified application. This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationExtensionSubscription-function getUserGrantedState(targetBundle: BundleOption): Promise<boolean>--><!--Device-notificationExtensionSubscription-function getUserGrantedState(targetBundle: BundleOption): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| targetBundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

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
notificationExtensionSubscription.getUserGrantedState(targetBundle).then((isOpen: boolean) => {
  if (isOpen) {
    console.info('GrantedState true');
  } else {
    console.info('GrantedState false');
  }
}).catch((err: BusinessError) => {
  console.error(`getUserGrantedState fail, code is ${err.code}, message is ${err.message}`);
});
```
