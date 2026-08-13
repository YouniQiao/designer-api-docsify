# removeSlot

## removeSlot

```TypeScript
function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void
```

Removes a notification slot of a specified type. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeSlot](arkts-notification-notificationmanager-removeslot-f.md#removeSlot)

<!--Device-notification-function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void--><!--Device-notification-function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## removeSlot

```TypeScript
function removeSlot(slotType: SlotType): Promise<void>
```

Removes a notification slot of a specified type. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeSlot](arkts-notification-notificationmanager-removeslot-f.md#removeSlot)

<!--Device-notification-function removeSlot(slotType: SlotType): Promise<void>--><!--Device-notification-function removeSlot(slotType: SlotType): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
