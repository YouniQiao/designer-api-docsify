# EnabledSilentReminderChangedCallback (System API)

```TypeScript
export type EnabledSilentReminderChangedCallback = (callbackData: EnabledSilentReminderCallbackData) => void
```

Defines a callback function to listen for the enabling state changes of the application's silent reminder. type EnabledSilentReminderChangedCallback = (callbackData: EnabledSilentReminderCallbackData) =&gt; void

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackData | [EnabledSilentReminderCallbackData](arkts-notification-notificationsubscriber-enabledsilentremindercallbackdata-i-sys.md) | Yes | Callback used to return the listened silent reminder enabling state. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let onEnabledSilentReminderChangedCallback: notificationSubscribe.EnabledSilentReminderChangedCallback = (callbackData: notificationSubscribe.EnabledSilentReminderCallbackData) => {
  console.info("bundle: ", callbackData.bundle);
  console.info("uid: ", callbackData.uid);
  console.info("enable: ", callbackData.enableStatus);
};

let subscriber: notificationSubscribe.NotificationSubscriber = {
  onEnabledSilentReminderChanged: onEnabledSilentReminderChangedCallback
};

notificationSubscribe.subscribeNotification(subscriber).then(() => {
  console.info("subscribeNotification success");
}).catch((err: BusinessError) => {
  console.error(`subscribeNotification failed, code is ${err.code}, message is ${err.message}`);
});
```
