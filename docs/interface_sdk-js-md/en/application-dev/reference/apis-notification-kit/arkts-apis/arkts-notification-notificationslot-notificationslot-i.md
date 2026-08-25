# NotificationSlot

The **NotificationSlot** module provides APIs for defining the notification slots. The notification reminder modes vary according to notification slots.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## badgeFlag

```TypeScript
badgeFlag?: boolean
```

Whether to display the badge. The default value is **true**.  
- **true**: Display the badge. - **false**: Do not display the badge.

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## bypassDnd

```TypeScript
bypassDnd?: boolean
```

Whether to bypass Do Not Disturb mode in the system. The default value is **false**.  
- **true**: Bypass Do Not Disturb mode, and notifications will still be alerted in Do Not Disturb mode. - **false**: Do not bypass Do Not Disturb mode, and notifications will not be alerted in Do Not Disturb mode.

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## desc

```TypeScript
desc?: string
```

Description of the notification channel. The size cannot exceed 243 bytes, and the excess part will be truncated.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## enabled

```TypeScript
readonly enabled?: boolean
```

Whether to allow notifications of this slot type to be published.  
- **true**: yes. - **false**: no.

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## level

```TypeScript
level?: notification.SlotLevel
```

Notification level.

**Type:** notification.SlotLevel

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 20

**Substitutes:** [notificationLevel](#notificationlevel)

**System capability:** SystemCapability.Notification.Notification

## lightColor

```TypeScript
lightColor?: int
```

Indicator color of the notification. This is a reserved capability and is not supported currently.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## lightEnabled

```TypeScript
lightEnabled?: boolean
```

Whether to enable the light. The default value is **false**.  
- **true**: yes. - **false**: no.

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## lockscreenVisibility

```TypeScript
lockscreenVisibility?: int
```

Mode for displaying the notification on the lock screen. This is a reserved capability and is not supported currently.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## notificationLevel

```TypeScript
notificationLevel?: notificationManager.SlotLevel
```

Notification level, which is used to describe the display priority and alert intensity of notifications of this channel type.

**Type:** notificationManager.SlotLevel

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## notificationType

```TypeScript
notificationType?: notificationManager.SlotType
```

Slot type. Different slot types have different notification reminder types.

**Type:** notificationManager.SlotType

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## sound

```TypeScript
sound?: string
```

File name of the custom ringtone for notifications from this channel. The file is placed in the **resources/rawfile** directory, and formats such as M4A, AAC, MP3, OGG, WAV, FLAC, and AMR are supported. The size cannot exceed 243 bytes, and the excess part will be truncated.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## type

```TypeScript
type?: notification.SlotType
```

Channel type.

**Type:** notification.SlotType

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 11

**Substitutes:** [notificationType](#notificationtype)

**System capability:** SystemCapability.Notification.Notification

## vibrationEnabled

```TypeScript
vibrationEnabled?: boolean
```

Whether to enable vibration. The default value is **false**.  
- **true**: yes. - **false**: no.

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## vibrationValues

```TypeScript
vibrationValues?: Array<long>
```

Vibration mode of the notification. This is a reserved capability and is not supported currently.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;long&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification
