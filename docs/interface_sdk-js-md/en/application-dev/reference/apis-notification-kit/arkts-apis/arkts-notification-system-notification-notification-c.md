# Notification

提供通知管理的能力。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 7

**Substitutes:** ohos.notification/notification

<!--Device-unnamed-declare class Notification--><!--Device-unnamed-declare class Notification-End-->

**System capability:** SystemCapability.Notification.Notification

## Modules to Import

```TypeScript
import { ActionResult, ShowNotificationOptions } from 'kits/@kit.NotificationKit';
```

## show

```TypeScript
static show(options?: ShowNotificationOptions): void
```

显示通知。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 7

**Substitutes:** ohos.notification/notification

<!--Device-Notification-static show(options?: ShowNotificationOptions): void--><!--Device-Notification-static show(options?: ShowNotificationOptions): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ShowNotificationOptions](arkts-notification-system-notification-shownotificationoptions-i.md) | No | 通知标题。 |

