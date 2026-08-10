# BadgeEnabledChangedCallback (System API)

```TypeScript
export type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) => void
```

type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) => void注册应用角标使能状态变化的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) => void--><!--Device-unnamed-export type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [EnabledNotificationCallbackData](arkts-notification-notificationsubscribe-enablednotificationcallbackdata-t-sys.md) | Yes | 回调返回监听到的角标使能状态信息。 |

