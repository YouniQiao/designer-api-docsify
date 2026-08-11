# getSubscribeInfo

## Modules to Import

```TypeScript
import { notificationExtensionSubscription } from 'kits/@kit.NotificationKit';
```

## getSubscribeInfo

```TypeScript
function getSubscribeInfo(): Promise<NotificationExtensionSubscriptionInfo[]>
```

Obtains the subscription information about the notification extension of this application. This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.SUBSCRIBE_NOTIFICATION

<!--Device-notificationExtensionSubscription-function getSubscribeInfo(): Promise<NotificationExtensionSubscriptionInfo[]>--><!--Device-notificationExtensionSubscription-function getSubscribeInfo(): Promise<NotificationExtensionSubscriptionInfo[]>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;NotificationExtensionSubscriptionInfo[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
notificationExtensionSubscription.getSubscribeInfo().then((data: notificationExtensionSubscription.NotificationExtensionSubscriptionInfo[]) => {
  console.info(`getSubscribeInfo successfully. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`getSubscribeInfo fail, code is ${err.code}, message is ${err.message}`);
});
```
