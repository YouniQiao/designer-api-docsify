# ReminderRequest

Defines the request for publishing a reminder.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-reminderAgentManager-interface ReminderRequest--><!--Device-reminderAgentManager-interface ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## forceDistributed

```TypeScript
forceDistributed?: boolean
```

Whether notifications are forcibly displayed in all scenarios across devices. The default value is **false**. For details, see  
[NotificationRequest.forceDistributed]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_  
- **true**: Notifications are displayed on all collaboration devices.  
- **false**: Notifications are displayed on the applications that are on the collaborative management list.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ReminderRequest-forceDistributed?: boolean--><!--Device-ReminderRequest-forceDistributed?: boolean-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**System API:** This is a system API.

## notDistributed

```TypeScript
notDistributed?: boolean
```

Whether notifications are not displayed in all scenarios across devices. The default value is **false**. For details, see  
[NotificationRequest.notDistributed]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_  
- **true**: Notifications are displayed only on the local device.  
- **false**: Notifications are displayed on all collaborative devices.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ReminderRequest-notDistributed?: boolean--><!--Device-ReminderRequest-notDistributed?: boolean-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**System API:** This is a system API.

