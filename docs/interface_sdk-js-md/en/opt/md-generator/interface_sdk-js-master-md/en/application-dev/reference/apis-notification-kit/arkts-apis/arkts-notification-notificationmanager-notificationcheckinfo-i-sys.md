# NotificationCheckInfo (System API)

Describes the parameters of check notifications.

**Since:** 23

<!--Device-notificationManager-export interface NotificationCheckInfo--><!--Device-notificationManager-export interface NotificationCheckInfo-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## bundleName

```TypeScript
bundleName: string
```

Bundle name.

**Type:** string

**Since:** 23

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-NotificationCheckInfo-bundleName: string--><!--Device-NotificationCheckInfo-bundleName: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## contentType

```TypeScript
contentType: ContentType
```

Notification type.

**Type:** ContentType

**Since:** 23

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-NotificationCheckInfo-contentType: ContentType--><!--Device-NotificationCheckInfo-contentType: ContentType-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## creatorUserId

```TypeScript
creatorUserId: number
```

User ID of the notification.

**Type:** number

**Since:** 23

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-NotificationCheckInfo-creatorUserId: int--><!--Device-NotificationCheckInfo-creatorUserId: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## extraInfos

```TypeScript
extraInfos?: Record<string, RecordData>
```

Extra information about the live view.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;

**Since:** 23

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-NotificationCheckInfo-extraInfos?: Record<string, RecordData>--><!--Device-NotificationCheckInfo-extraInfos?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## label

```TypeScript
label?: string
```

Notification label.

**Type:** string

**Since:** 23

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-NotificationCheckInfo-label?: string--><!--Device-NotificationCheckInfo-label?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## notificationId

```TypeScript
notificationId: number
```

Notification ID.

**Type:** number

**Since:** 23

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-NotificationCheckInfo-notificationId: int--><!--Device-NotificationCheckInfo-notificationId: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## slotType

```TypeScript
slotType: SlotType
```

Notification slot type.

**Type:** SlotType

**Since:** 23

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-NotificationCheckInfo-slotType: SlotType--><!--Device-NotificationCheckInfo-slotType: SlotType-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.
