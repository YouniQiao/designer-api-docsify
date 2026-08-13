# removeSlot

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## removeSlot

```TypeScript
function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void
```

Removes a notification slot of a specified type for this application. This API uses an asynchronous callback to return the result. After deletion, the corresponding type of notification slot and its configuration will be permanently removed. When a notification of this type is published subsequently, the system will automatically create a default slot. Notifications already published through this slot are not affected and can still be viewed in the notification center. This is suitable for scenarios where a slot needs to be deleted and then recreated for reconfiguration.

**Since:** 23

**Deprecated since:** -1

<!--Device-notificationManager-function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

addSlot adds a notification slot of

getSlot obtains a

removeAllSlots removes all notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// removeSlot callback
let removeSlotCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to remove slot. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in removing slot.`);
  }
}
let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.removeSlot(slotType, removeSlotCallback);
```


## removeSlot

```TypeScript
function removeSlot(slotType: SlotType): Promise<void>
```

Removes a notification slot of a specified type for this application. This API uses a promise to return the result. After deletion, the corresponding notification slot and its configuration will be permanently removed. When a notification of this type is published subsequently, the system will automatically create a default slot. Notifications already published through this slot are not affected and can still be viewed in the notification center. This is suitable for scenarios where a slot needs to be deleted and then recreated for reconfiguration.

**Since:** 23

**Deprecated since:** -1

<!--Device-notificationManager-function removeSlot(slotType: SlotType): Promise<void>--><!--Device-notificationManager-function removeSlot(slotType: SlotType): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

addSlot adds a notification slot of

getSlot obtains a notification slot of a

removeAllSlots removes all notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.removeSlot(slotType).then(() => {
  console.info(`Succeeded in removing slot.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to remove slot. Code is ${err.code}, message is ${err.message}`);
});
```
