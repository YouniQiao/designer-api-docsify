# NotificationSlot

The **NotificationSlot** module provides APIs for defining the notification slots. The notification reminder modes vary according to notification slots.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## authorizedStatus

```TypeScript
readonly authorizedStatus?: int
```

Authorization status.  
- **0**: means the feature is authorized. - **1**: means the feature is to be authorized.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## reminderMode

```TypeScript
readonly reminderMode?: int
```

Reminder mode of the notification.  
- Bit 0: sound alert. The value **0** means to enable the feature, and **1** means the opposite. - Bit 1: locking the screen. The value **0** means to enable the feature, and **1** means the opposite. - Bit 2: banner. The value **0** means to enable the feature, and **1** means the opposite. - Bit 3: turning on the screen. The value **0** means to enable the feature, and **1** means the opposite. - Bit 4: vibration. The value **0** means to enable the feature, and **1** means the opposite. - Bit 5: notification icon in the status bar. The value **0** means to enable the feature, and **1** means the opposite.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.
