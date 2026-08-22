# BadgeEnabledChangedCallback

Defines a callback function to listen for the enabling state changes of the application badge. type BadgeEnabledChangedCallback = (data: EnabledNotificationCallbackData) =&gt; void

**Since:** 12

<!--Device-unnamed-export interface BadgeEnabledChangedCallback--><!--Device-unnamed-export interface BadgeEnabledChangedCallback-End-->

**System capability:** SystemCapability.Notification.Notification

## constructor

```TypeScript
(data: EnabledNotificationCallbackData): void
```

Callback used to return the listened badge enabling state.

**Since:** 12

<!--Device-BadgeEnabledChangedCallback-(data: EnabledNotificationCallbackData): void--><!--Device-BadgeEnabledChangedCallback-(data: EnabledNotificationCallbackData): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [EnabledNotificationCallbackData](arkts-notification-notificationsubscriber-enablednotificationcallbackdata-i-sys.md) | Yes | Callback used to return the listened badge enabling state. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subscribeCallback = (err: BusinessError) => {
  if (err) {
    console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('subscribeCallback');
  }
};

let BadgeEnabledChangedCallback = (data: notificationSubscribe.EnabledNotificationCallbackData) => {
  console.info(`onBadgeEnabledChanged, badge enabled state change to: ${JSON.stringify(data)}`);
};
let subscriber: notificationSubscribe.NotificationSubscriber = {
  onBadgeEnabledChanged: BadgeEnabledChangedCallback
};

notificationSubscribe.subscribe(subscriber, subscribeCallback);
```

