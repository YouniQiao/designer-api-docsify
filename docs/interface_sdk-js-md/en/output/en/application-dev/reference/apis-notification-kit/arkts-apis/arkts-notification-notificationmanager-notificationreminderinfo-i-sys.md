# NotificationReminderInfo (System API)

Describes the information about the application reminder.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-notificationManager-export interface NotificationReminderInfo--><!--Device-notificationManager-export interface NotificationReminderInfo-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## bundle

```TypeScript
bundle: BundleOption
```

Bundle information of the application.

**Type:** BundleOption

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-NotificationReminderInfo-bundle: BundleOption--><!--Device-NotificationReminderInfo-bundle: BundleOption-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## reminderFlags

```TypeScript
reminderFlags: long
```

Notification reminder mode flags.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_- bit0: sound prompt. The value **0** indicates disabled, and **1** indicates enabled. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- bit1: lock screen. The value **0** indicates disabled, and **1** indicates enabled. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- bit2: banner. The value **0** indicates disabled, and **1** indicates enabled. \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_- bit3: screen on. The value **0** indicates disabled, and **1** indicates enabled. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_- bit4: vibration. The value **0** indicates disabled, and **1** indicates enabled. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_- bit5: status bar notification icon. The value **0** indicates disabled, and **1** indicates enabled.

**Type:** long

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-NotificationReminderInfo-reminderFlags: long--><!--Device-NotificationReminderInfo-reminderFlags: long-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## silentReminderEnabled

```TypeScript
silentReminderEnabled: boolean
```

Whether the silent reminder is enabled. The value **true** indicates that the silent reminder is enabled, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-NotificationReminderInfo-silentReminderEnabled: boolean--><!--Device-NotificationReminderInfo-silentReminderEnabled: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

