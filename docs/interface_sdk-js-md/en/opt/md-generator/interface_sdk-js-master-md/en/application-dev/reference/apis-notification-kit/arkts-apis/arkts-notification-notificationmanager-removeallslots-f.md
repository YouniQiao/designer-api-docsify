# removeAllSlots

## Modules to Import

```TypeScript
```

## removeAllSlots

```TypeScript
function removeAllSlots(callback: AsyncCallback<void>): void
```

Removes all notification slots for this application. This API uses an asynchronous callback to return the result. After deletion, all notification slots and their configurations of the current application will be permanently removed. When notifications are published subsequently, the system will automatically create slots of the corresponding types. Notifications already published through these slots are not affected and can still be viewed in the notification center. This is suitable for scenarios where all slot configurations need to be cleared at once.

**Since:** 23

<!--Device-notificationManager-function removeAllSlots(callback: AsyncCallback<void>): void--><!--Device-notificationManager-function removeAllSlots(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

addSlot adds a notification slot of

getSlot obtains a notification slot of

removeSlots removes all notification slots

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let removeAllSlotsCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to remove all slots. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in removing all slots.`);
  }
}
notificationManager.removeAllSlots(removeAllSlotsCallback);
```


## removeAllSlots

```TypeScript
function removeAllSlots(): Promise<void>
```

Removes all notification slots for this application. This API uses a promise to return the result. After deletion, all notification slots and their configurations of the current application will be permanently removed. When notifications are published subsequently, the system will automatically create slots of the corresponding types. Notifications already published through these slots are not affected and can still be viewed in the notification center. This is suitable for scenarios where all slot configurations need to be cleared at once.

**Since:** 23

<!--Device-notificationManager-function removeAllSlots(): Promise<void>--><!--Device-notificationManager-function removeAllSlots(): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

addSlot adds a notification slot of

getSlot obtains a notification slot of a

removeSlot removes a notification

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.removeAllSlots().then(() => {
  console.info(`Succeeded in removing all slots.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to remove all slots. Code is ${err.code}, message is ${err.message}`);
});
```
