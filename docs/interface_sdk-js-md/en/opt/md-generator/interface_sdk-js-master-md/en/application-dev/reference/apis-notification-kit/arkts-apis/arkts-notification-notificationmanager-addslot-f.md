# addSlot

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## addSlot

```TypeScript
function addSlot(type: SlotType, callback: AsyncCallback<void>): void
```

Adds a notification slot of a specified type. This API uses an asynchronous callback to return the result.

The notification slot NotificationSlot defines the reminder type (such as alert sound, vibration, and banner) and level of a notification. Before publishing a notification, the application needs to create a corresponding type of notification slot first, or the system will automatically create a corresponding type of notification slot when the notification is published. Only one notification slot of the same type can be created.

**Since:** 9

<!--Device-notificationManager-function addSlot(type: SlotType, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function addSlot(type: SlotType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// addSlot callback
let addSlotCallBack = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to add slot. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in adding slot.`);
  }
}
notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION, addSlotCallBack);
```


## addSlot

```TypeScript
function addSlot(type: SlotType): Promise<void>
```

Adds a notification slot of a specified type. This API uses a promise to return the result.

The notification slot NotificationSlot defines the reminder type (such as alert sound, vibration, and banner) and level of a notification. Before publishing a notification, the application needs to create a corresponding type of notification slot first, or the system will automatically create a corresponding type of notification slot when the notification is published. Only one notification slot of the same type can be created.

**Since:** 9

<!--Device-notificationManager-function addSlot(type: SlotType): Promise<void>--><!--Device-notificationManager-function addSlot(type: SlotType): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION).then(() => {
  console.info(`Succeeded in adding slot.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to add slot. Code is ${err.code}, message is ${err.message}`);
});
```
