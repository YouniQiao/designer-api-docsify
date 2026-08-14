# NotificationReminderInfo (System API)

Describes the information about the application reminder.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-notificationManager-export interface NotificationReminderInfo--><!--Device-notificationManager-export interface NotificationReminderInfo-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { notificationManager } from 'notificationManager';
```

## bundle

```TypeScript
bundle: BundleOption
```

Bundle information of the application.

**Type:** BundleOption

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationReminderInfo-bundle: BundleOption--><!--Device-NotificationReminderInfo-bundle: BundleOption-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## reminderFlags

```TypeScript
reminderFlags: long
```

Notification reminder mode flags.<br>- bit0: sound prompt. The value **0** indicates disabled, and **1** indicates enabled. <br>- bit1: lock screen. The value **0** indicates disabled, and **1** indicates enabled. <br>- bit2: banner. The value **0** indicates disabled, and **1** indicates enabled. <br>- bit3: screen on. The value **0** indicates disabled, and **1** indicates enabled. <br>- bit4: vibration. The value **0** indicates disabled, and **1** indicates enabled. <br>- bit5: status bar notification icon. The value **0** indicates disabled, and **1** indicates enabled.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationReminderInfo-reminderFlags: long--><!--Device-NotificationReminderInfo-reminderFlags: long-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## silentReminderEnabled

```TypeScript
silentReminderEnabled: boolean
```

Whether the silent reminder is enabled. The value **true** indicates that the silent reminder is enabled, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationReminderInfo-silentReminderEnabled: boolean--><!--Device-NotificationReminderInfo-silentReminderEnabled: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

