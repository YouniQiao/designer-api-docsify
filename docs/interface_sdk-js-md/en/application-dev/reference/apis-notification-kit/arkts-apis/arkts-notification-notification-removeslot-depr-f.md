# removeSlot

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
import { notificationManager } from '@kit.NotificationKit';
import { notificationSubscribe } from '@kit.NotificationKit';
import { notificationSubscribe } from '@kit.NotificationKit';
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## removeSlot

```TypeScript
function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void
```

Removes a notification slot of a specified type. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeSlot](arkts-notification-notificationmanager-removeslot-f.md#removeslot)

<!--Device-notification-function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void--><!--Device-notification-function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotType | SlotType | Yes | Type of the notification slot, which can be used for social communication, service information, content consultation, and other purposes. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |


## removeSlot

```TypeScript
function removeSlot(slotType: SlotType): Promise<void>
```

Removes a notification slot of a specified type. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeSlot](arkts-notification-notificationmanager-removeslot-f.md#removeslot)

<!--Device-notification-function removeSlot(slotType: SlotType): Promise<void>--><!--Device-notification-function removeSlot(slotType: SlotType): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotType | SlotType | Yes | Type of the notification slot, which can be used for social communication, service information, content consultation, and other purposes. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

