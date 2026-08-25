# addSlot (System API)

## Modules to Import

```TypeScript
```

## addSlot

```TypeScript
function addSlot(slot: NotificationSlot, callback: AsyncCallback<void>): void
```

Adds a notification slot. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addSlot](arkts-notification-notificationmanager-addslot-f.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [slot](arkts-notification-notificationsorting-notificationsorting-i-sys.md) | [NotificationSlot](arkts-notification-notificationslot-notificationslot-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## addSlot

```TypeScript
function addSlot(slot: NotificationSlot): Promise<void>
```

Adds a notification slot. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addSlot](arkts-notification-notificationmanager-addslot-f.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [slot](arkts-notification-notificationsorting-notificationsorting-i-sys.md) | [NotificationSlot](arkts-notification-notificationslot-notificationslot-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
