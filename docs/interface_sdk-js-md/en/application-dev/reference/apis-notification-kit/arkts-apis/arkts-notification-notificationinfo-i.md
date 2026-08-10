# NotificationInfo

通知订阅扩展能力中  
[onReceiveMessage](arkts-notification-application-notificationsubscriberextensionability-notificationsubscriberextensionability-c.md#onreceivemessage)回调的通知信息。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationInfo--><!--Device-unnamed-export interface NotificationInfo-End-->

**System capability:** SystemCapability.Notification.Notification

## appIndex

```TypeScript
readonly appIndex: int
```

创建通知的应用的分身索引标识，仅在分身应用中生效。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationInfo-readonly appIndex: int--><!--Device-NotificationInfo-readonly appIndex: int-End-->

**System capability:** SystemCapability.Notification.Notification

## appName

```TypeScript
readonly appName?: string
```

创建通知的应用名称。

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationInfo-readonly appName?: string--><!--Device-NotificationInfo-readonly appName?: string-End-->

**System capability:** SystemCapability.Notification.Notification

## bundleName

```TypeScript
readonly bundleName: string
```

创建通知的应用包名。

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationInfo-readonly bundleName: string--><!--Device-NotificationInfo-readonly bundleName: string-End-->

**System capability:** SystemCapability.Notification.Notification

## content

```TypeScript
readonly content: NotificationExtensionContent
```

通知内容。包含通知的标题和正文。

**Type:** [NotificationExtensionContent](arkts-notification-notificationextensioncontent-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationInfo-readonly content: NotificationExtensionContent--><!--Device-NotificationInfo-readonly content: NotificationExtensionContent-End-->

**System capability:** SystemCapability.Notification.Notification

## deliveryTime

```TypeScript
readonly deliveryTime?: long
```

通知发布的时间戳。数据格式：时间戳。单位：毫秒。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationInfo-readonly deliveryTime?: long--><!--Device-NotificationInfo-readonly deliveryTime?: long-End-->

**System capability:** SystemCapability.Notification.Notification

## groupName

```TypeScript
readonly groupName?: string
```

通知组名称。

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationInfo-readonly groupName?: string--><!--Device-NotificationInfo-readonly groupName?: string-End-->

**System capability:** SystemCapability.Notification.Notification

## hashCode

```TypeScript
readonly hashCode: string
```

通知的唯一标识符。

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationInfo-readonly hashCode: string--><!--Device-NotificationInfo-readonly hashCode: string-End-->

**System capability:** SystemCapability.Notification.Notification

## notificationSlotType

```TypeScript
readonly notificationSlotType: notificationManager.SlotType
```

通知渠道类型，标识通知所属的渠道分类（如社交通讯、服务提醒等）。不同渠道类型对应不同的提醒方式。

**Type:** notificationManager.SlotType

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationInfo-readonly notificationSlotType: notificationManager.SlotType--><!--Device-NotificationInfo-readonly notificationSlotType: notificationManager.SlotType-End-->

**System capability:** SystemCapability.Notification.Notification

