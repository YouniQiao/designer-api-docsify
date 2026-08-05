# NotificationRequestProxy

Notification request proxy.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-reminderAgentManager-interface NotificationRequestProxy--><!--Device-reminderAgentManager-interface NotificationRequestProxy-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## appMessageId

```TypeScript
appMessageId?: string
```

Unique ID carried in a notification sent by an application, which is used for notification deduplication. This parameter is left empty by default. For details, see [NotificationRequest.appMessageId]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationRequestProxy-appMessageId?: string--><!--Device-NotificationRequestProxy-appMessageId?: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## isAlertOnce

```TypeScript
isAlertOnce?: boolean
```

Whether to send a notification alert only once when a notification is published or updated. The default value is **false**. For details, see [NotificationRequest.isAlertOnce]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. - **true**: An alert is sent only when the notification is published for the first time. For subsequent update, the alert mode is changed to [LEVEL\_LOW]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. - **false**: The alert is sent in the configured alert mode.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationRequestProxy-isAlertOnce?: boolean--><!--Device-NotificationRequestProxy-isAlertOnce?: boolean-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

