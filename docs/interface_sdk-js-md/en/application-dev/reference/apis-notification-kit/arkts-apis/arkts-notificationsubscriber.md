# notificationSubscriber(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)

The **NotificationSubscriber** module serves as the input parameter of subscribeNotification and provides
 callbacks for receiving or removing notifications.


## Summary

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [BadgeEnabledChangedCallback(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationsubscriber-badgeenabledchangedcallback-i-sys.md) | Defines a callback function to listen for the enabling state changes of the application badge. type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) = & gt; void |
| [BadgeNumberCallbackData(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationsubscriber-badgenumbercallbackdata-i-sys.md) | Returns the changes of the application badge number. |
| [EnabledNotificationCallbackData(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationsubscriber-enablednotificationcallbackdata-i-sys.md) | Returns the changes of the application enabling state. |
| [EnabledPriorityNotificationByBundleCallbackData(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationsubscriber-enabledprioritynotificationbybundlecallbackdata-i-sys.md) | Returns the notification priority switch state. |
| [EnabledPriorityNotificationCallbackData(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationsubscriber-enabledprioritynotificationcallbackdata-i-sys.md) | Returns the notification priority master switch state. |
| [EnabledSilentReminderCallbackData(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationsubscriber-enabledsilentremindercallbackdata-i-sys.md) | Returns the application notification silent reminder switch state. |
| [NotificationClassification(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationsubscriber-notificationclassification-i-sys.md) | Returns the notification classification information. |
| [NotificationSubscriber(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | Provides callback methods for subscribers to receive and cancel notifications. |
| [NotificationSwitchChangedCallbackData(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationsubscriber-notificationswitchchangedcallbackdata-i-sys.md) | Returns the changes of the notification switch state. |
| [SubscribeCallbackData(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationsubscriber-subscribecallbackdata-i-sys.md) | Returns notification information carrying system property values. |
| [VoiceContent(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationsubscriber-voicecontent-i-sys.md) | Returns the notification voice broadcast content. |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [EnabledSilentReminderChangedCallback(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-enabledsilentreminderchangedcallback-t-sys.md) | Defines a callback function to listen for the enabling state changes of the application's silent reminder. type EnabledSilentReminderChangedCallback = (callbackData: EnabledSilentReminderCallbackData) = & gt; void |
| [NotificationSwitchChangedCallback(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-notificationswitchchangedcallback-t-sys.md) | Registers the callback for notification switch state changes set by [notificationManager.setNotificationSwitch] [setNotificationSwitch](arkts-notification-notificationmanager-setnotificationswitch-f-sys.md) API. |
| [SystemUpdateCallback(Provides methods that will be called back when the subscriber receives a new notification or a notification is canceled)](arkts-notification-systemupdatecallback-t-sys.md) | Returns the notification information carrying system property values. type SystemUpdateCallback = (data: SubscribeCallbackData) = & gt; void |
<!--DelEnd-->
