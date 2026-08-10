# NotificationSlot

描述通知渠道，不同通知渠道对应的通知提醒方式不同。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationSlot--><!--Device-unnamed-export interface NotificationSlot-End-->

**System capability:** SystemCapability.Notification.Notification

## badgeFlag

```TypeScript
badgeFlag?: boolean
```

是否显示角标。默认值为true。

- true：显示角标。  
- false：不显示角标。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-badgeFlag?: boolean--><!--Device-NotificationSlot-badgeFlag?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

## bypassDnd

```TypeScript
bypassDnd?: boolean
```

是否在系统中绕过免打扰模式。默认值为false。

- true：绕过免打扰模式，免打扰模式下仍会提醒。  
- false：不绕过免打扰模式，免打扰模式下不提醒。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-bypassDnd?: boolean--><!--Device-NotificationSlot-bypassDnd?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

## desc

```TypeScript
desc?: string
```

通知渠道描述信息。大小不超过243字节，超出部分会被截断。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-desc?: string--><!--Device-NotificationSlot-desc?: string-End-->

**System capability:** SystemCapability.Notification.Notification

## enabled

```TypeScript
readonly enabled?: boolean
```

是否允许发布此通知渠道类型的通知。

- true：允许发布通知。  
- false：禁止发布通知。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-readonly enabled?: boolean--><!--Device-NotificationSlot-readonly enabled?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

## level

```TypeScript
level?: notification.SlotLevel
```

通知级别。

**Type:** notification.SlotLevel

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 20

**Substitutes:** [NotificationSlot#notificationLevel](arkts-notification-notificationslot-notificationslot-i.md#notificationlevel)

<!--Device-NotificationSlot-level?: notification.SlotLevel--><!--Device-NotificationSlot-level?: notification.SlotLevel-End-->

**System capability:** SystemCapability.Notification.Notification

## lightColor

```TypeScript
lightColor?: int
```

通知灯颜色。预留能力，暂不支持。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-lightColor?: int--><!--Device-NotificationSlot-lightColor?: int-End-->

**System capability:** SystemCapability.Notification.Notification

## lightEnabled

```TypeScript
lightEnabled?: boolean
```

是否闪灯。默认值为false。

- true：闪灯。  
- false：不闪灯。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-lightEnabled?: boolean--><!--Device-NotificationSlot-lightEnabled?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

## lockscreenVisibility

```TypeScript
lockscreenVisibility?: int
```

在锁定屏幕上显示通知的模式。预留能力，暂不支持。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-lockscreenVisibility?: int--><!--Device-NotificationSlot-lockscreenVisibility?: int-End-->

**System capability:** SystemCapability.Notification.Notification

## notificationLevel

```TypeScript
notificationLevel?: notificationManager.SlotLevel
```

通知级别，用于描述该渠道类型通知的显示优先级和提醒强度。

**Type:** notificationManager.SlotLevel

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-notificationLevel?: notificationManager.SlotLevel--><!--Device-NotificationSlot-notificationLevel?: notificationManager.SlotLevel-End-->

**System capability:** SystemCapability.Notification.Notification

## notificationType

```TypeScript
notificationType?: notificationManager.SlotType
```

渠道类型。不同渠道类型的通知提醒方式不同。

**Type:** notificationManager.SlotType

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-notificationType?: notificationManager.SlotType--><!--Device-NotificationSlot-notificationType?: notificationManager.SlotType-End-->

**System capability:** SystemCapability.Notification.Notification

## sound

```TypeScript
sound?: string
```

该渠道的通知的自定义铃声文件名。该文件放在resources/rawfile目录下，支持m4a、aac、mp3、ogg、wav、flac、amr等格式。大小不超过243字节，超出部分会被截断。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-sound?: string--><!--Device-NotificationSlot-sound?: string-End-->

**System capability:** SystemCapability.Notification.Notification

## type

```TypeScript
type?: notification.SlotType
```

渠道类型。

**Type:** notification.SlotType

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

**Substitutes:** [NotificationSlot#notificationType](arkts-notification-notificationslot-notificationslot-i.md#notificationtype)

<!--Device-NotificationSlot-type?: notification.SlotType--><!--Device-NotificationSlot-type?: notification.SlotType-End-->

**System capability:** SystemCapability.Notification.Notification

## vibrationEnabled

```TypeScript
vibrationEnabled?: boolean
```

是否可振动。默认值为false。

- true：可振动。  
- false：不可振动。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-vibrationEnabled?: boolean--><!--Device-NotificationSlot-vibrationEnabled?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

## vibrationValues

```TypeScript
vibrationValues?: Array<long>
```

通知振动样式。预留能力，暂不支持。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;long&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-vibrationValues?: Array<long>--><!--Device-NotificationSlot-vibrationValues?: Array<long>-End-->

**System capability:** SystemCapability.Notification.Notification

