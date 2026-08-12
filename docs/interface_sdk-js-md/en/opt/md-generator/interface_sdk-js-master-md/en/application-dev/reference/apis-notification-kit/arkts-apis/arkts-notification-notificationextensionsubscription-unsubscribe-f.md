# unsubscribe

## Modules to Import

```TypeScript
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## unsubscribe

```TypeScript
function unsubscribe(): Promise<void>
```

Unsubscribes from the notification extension. This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.SUBSCRIBE_NOTIFICATION

<!--Device-notificationExtensionSubscription-function unsubscribe(): Promise<void>--><!--Device-notificationExtensionSubscription-function unsubscribe(): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

[subscribe](notificationExtensionSubscription.subscribe(info: _NotificationExtensionSubscriptionInfo[]): Promise<void>) subscribes to the

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
notificationExtensionSubscription.unsubscribe().then(() => {
  console.info(`unsubscribe success`);
}).catch((err: BusinessError) => {
  console.error(`unsubscribe fail, code is ${err.code}, message is ${err.message}`);
});
```
