# NotificationReminderInfo (System API)

Describes the information about the application reminder.

**Since:** 21

<!--Device-notificationManager-export interface NotificationReminderInfo--><!--Device-notificationManager-export interface NotificationReminderInfo-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## bundle

```TypeScript
bundle: BundleOption
```

Bundle information of the application.

**Type:** [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md)

**Since:** 21

<!--Device-NotificationReminderInfo-bundle: BundleOption--><!--Device-NotificationReminderInfo-bundle: BundleOption-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## reminderFlags

```TypeScript
reminderFlags: number
```

Notification reminder mode flags.&lt;br&gt;- bit0: sound prompt. The value **0** indicates disabled, and **1**indicates enabled. &lt;br&gt;- bit1: lock screen. The value **0** indicates disabled, and **1** indicates enabled. &lt;br&gt;- bit2: banner. The value **0** indicates disabled, and **1** indicates enabled. &lt;br&gt;- bit3:screen on. The value **0** indicates disabled, and **1** indicates enabled. &lt;br&gt;- bit4: vibration. The value **0** indicates disabled, and **1** indicates enabled. &lt;br&gt;- bit5: status bar notification icon. The value **0** indicates disabled, and **1** indicates enabled.

**Type:** number

**Since:** 21

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

<!--Device-NotificationReminderInfo-silentReminderEnabled: boolean--><!--Device-NotificationReminderInfo-silentReminderEnabled: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.
