# subscribe

## Modules to Import

```TypeScript
import { notificationExtensionSubscription } from 'kits/@kit.NotificationKit';
```

## subscribe

```TypeScript
function subscribe(info: NotificationExtensionSubscriptionInfo[]): Promise<void>
```

Subscribes to the notification extension. You can subscribe to the notification extension only after obtaining the unique address of the Bluetooth device by calling the APIs related to the   
[Bluetooth modules](../../../connectivity/connectivity-kit-intro.md#bluetooth). This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.SUBSCRIBE_NOTIFICATION

<!--Device-notificationExtensionSubscription-function subscribe(info: NotificationExtensionSubscriptionInfo[]): Promise<void>--><!--Device-notificationExtensionSubscription-function subscribe(info: NotificationExtensionSubscriptionInfo[]): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [NotificationExtensionSubscriptionInfo](arkts-notification-notificationextensionsubscriptioninfo-i.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600023](../errorcode-notification.md#1600023-notificationsubscriberextensionability-not-implemented) |

## Examples

```TypeScript
let infos: notificationExtensionSubscription.NotificationExtensionSubscriptionInfo[] = [
  {
    addr: '01:23:45:67:89:AB', // Use the dynamically obtained Bluetooth address.
    type: notificationExtensionSubscription.SubscribeType.BLUETOOTH
  }
];
notificationExtensionSubscription.subscribe(infos).then(() => {
  console.info(`subscribe success`);
}).catch((err: BusinessError) => {
  console.error(`subscribe fail, code is ${err.code}, message is ${err.message}`);
});
```
