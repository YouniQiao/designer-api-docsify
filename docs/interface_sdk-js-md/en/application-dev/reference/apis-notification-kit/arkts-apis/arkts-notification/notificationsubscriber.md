# notification/notificationSubscriber(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)

The **NotificationSubscriber** module serves as the input parameter of subscribeNotification and provides
 callbacks for receiving or removing notifications.


## Summary

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [BadgeEnabledChangedCallback](notificationsubscriber-badgeenabledchangedcallback-i-sys.md) | Defines a callback function to listen for the enabling state changes of the application badge.type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) =   void |
| [BadgeNumberCallbackData](notificationsubscriber-badgenumbercallbackdata-i-sys.md) | Returns the changes of the application badge number. |
| [EnabledNotificationCallbackData](notificationsubscriber-enablednotificationcallbackdata-i-sys.md) | Returns the changes of the application enabling state. |
| [EnabledPriorityNotificationByBundleCallbackData](notificationsubscriber-enabledprioritynotificationbybundlecallbackdata-i-sys.md) | Returns the notification priority switch state. |
| [EnabledPriorityNotificationCallbackData](notificationsubscriber-enabledprioritynotificationcallbackdata-i-sys.md) | Returns the notification priority master switch state. |
| [EnabledSilentReminderCallbackData](notificationsubscriber-enabledsilentremindercallbackdata-i-sys.md) | Returns the application notification silent reminder switch state. |
| [NotificationClassification](notificationsubscriber-notificationclassification-i-sys.md) | Returns the notification classification information. |
| [NotificationSubscriber](notificationsubscriber-notificationsubscriber-i-sys.md) | Provides callback methods for subscribers to receive and cancel notifications. |
| [NotificationSwitchChangedCallbackData](notificationsubscriber-notificationswitchchangedcallbackdata-i-sys.md) | Returns the changes of the notification switch state. |
| [SubscribeCallbackData](notificationsubscriber-subscribecallbackdata-i-sys.md) | Returns notification information carrying system property values. |
| [VoiceContent](notificationsubscriber-voicecontent-i-sys.md) | Returns the notification voice broadcast content. |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [BadgeEnabledChangedCallback](arkts-notification-badgeenabledchangedcallback-t-sys.md) | Defines a callback function to listen for the enabling state changes of the application badge.type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) =   void |
| [EnabledSilentReminderChangedCallback](arkts-notification-enabledsilentreminderchangedcallback-t-sys.md) | Defines a callback function to listen for the enabling state changes of the application's silent reminder.type EnabledSilentReminderChangedCallback = (callbackData: EnabledSilentReminderCallbackData) =   void |
| [NotificationSwitchChangedCallback](arkts-notification-notificationswitchchangedcallback-t-sys.md) | Registers the callback for notification switch state changes set by  [notificationManager.setNotificationSwitch]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ API. |
| [SystemUpdateCallback](arkts-notification-systemupdatecallback-t-sys.md) | Returns the notification information carrying system property values.type SystemUpdateCallback = (data: SubscribeCallbackData) =   void |
<!--DelEnd-->

