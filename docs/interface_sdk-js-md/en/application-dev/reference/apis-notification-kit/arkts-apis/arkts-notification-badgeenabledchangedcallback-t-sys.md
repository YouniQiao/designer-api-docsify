# BadgeEnabledChangedCallback (System API)

```TypeScript
export type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) => void
```

Defines a callback function to listen for the enabling state changes of the application badge. type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) => void

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) => void--><!--Device-unnamed-export type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [EnabledNotificationCallbackData](arkts-notification-notificationsubscriber-enablednotificationcallbackdata-i-sys.md) | Yes | Callback used to return the listened badge enabling state. |

