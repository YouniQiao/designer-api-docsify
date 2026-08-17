# NotificationSorting (System API)

The **NotificationSorting** module provides APIs for defining the sorting information of active notifications.

**Since:** 23

<!--Device-unnamed-export interface NotificationSorting--><!--Device-unnamed-export interface NotificationSorting-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## hashCode

```TypeScript
readonly hashCode: string
```

Unique ID of the notification.

**Type:** string

**Since:** 23

<!--Device-NotificationSorting-readonly hashCode: string--><!--Device-NotificationSorting-readonly hashCode: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## ranking

```TypeScript
readonly ranking: long
```

Notification level. If this parameter is not set, the default value is used based on the notification slot type.

**Type:** long

**Since:** 23

<!--Device-NotificationSorting-readonly ranking: long--><!--Device-NotificationSorting-readonly ranking: long-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## slot

```TypeScript
readonly slot: NotificationSlot
```

Notification slot type.

**Type:** [NotificationSlot](arkts-notification-notificationslot-notificationslot-i.md)

**Since:** 23

<!--Device-NotificationSorting-readonly slot: NotificationSlot--><!--Device-NotificationSorting-readonly slot: NotificationSlot-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

