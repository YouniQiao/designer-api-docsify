# NotificationCheckResult (System API)

Describes the result of check notifications.

**Since:** 23

<!--Device-notificationManager-export interface NotificationCheckResult--><!--Device-notificationManager-export interface NotificationCheckResult-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## code

```TypeScript
code: int
```

Result code.  
**0**: display.  
**1**: no display.

**Type:** int

**Since:** 23

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-NotificationCheckResult-code: int--><!--Device-NotificationCheckResult-code: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## message

```TypeScript
message: string
```

Result.

**Type:** string

**Since:** 23

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-NotificationCheckResult-message: string--><!--Device-NotificationCheckResult-message: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

