# EnabledSilentReminderChangedCallback (System API)

```TypeScript
export type EnabledSilentReminderChangedCallback = (callbackData: EnabledSilentReminderCallbackData) => void
```

Defines a callback function to listen for the enabling state changes of the application's silent reminder. type EnabledSilentReminderChangedCallback = (callbackData: EnabledSilentReminderCallbackData) => void

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type EnabledSilentReminderChangedCallback = (callbackData: EnabledSilentReminderCallbackData) => void--><!--Device-unnamed-export type EnabledSilentReminderChangedCallback = (callbackData: EnabledSilentReminderCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackData | [EnabledSilentReminderCallbackData](arkts-notification-notificationsubscriber-enabledsilentremindercallbackdata-i-sys.md) | Yes |
