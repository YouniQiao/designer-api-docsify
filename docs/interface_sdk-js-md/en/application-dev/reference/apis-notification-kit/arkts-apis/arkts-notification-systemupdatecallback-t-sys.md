# SystemUpdateCallback (System API)

```TypeScript
export type SystemUpdateCallback = (data: SubscribeCallbackData) => void
```

Returns the notification information carrying system property values. type SystemUpdateCallback = (data: SubscribeCallbackData) =&gt; void

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type SystemUpdateCallback = (data: SubscribeCallbackData) => void--><!--Device-unnamed-export type SystemUpdateCallback = (data: SubscribeCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [SubscribeCallbackData](arkts-notification-notificationsubscriber-subscribecallbackdata-i-sys.md) | Yes | Notification information that carries the system property value. |

**Examples**

```TypeScript
let subscriber: notificationSubscribe.NotificationSubscriber = {
  onSystemUpdate: (data: notificationSubscribe.SubscribeCallbackData) => {
    let req = data.request;
    console.info(`onSystemUpdate callback req.priorityType: ${req.priorityNotificationType}`);
  }
};
try {
  notificationSubscribe.subscribe(subscriber);
} catch (error) {
  console.error("subscribe failed");
}
```

