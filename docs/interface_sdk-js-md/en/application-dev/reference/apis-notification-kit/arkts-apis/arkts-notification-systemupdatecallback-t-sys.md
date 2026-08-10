# SystemUpdateCallback (System API)

```TypeScript
export type SystemUpdateCallback = (data: SubscribeCallbackData) => void
```

type SystemUpdateCallback = (data: SubscribeCallbackData) => void返回携带系统属性值通知信息的回调函数类型。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type SystemUpdateCallback = (data: SubscribeCallbackData) => void--><!--Device-unnamed-export type SystemUpdateCallback = (data: SubscribeCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [SubscribeCallbackData](arkts-notification-notificationsubscribe-subscribecallbackdata-t-sys.md) | Yes | 返回携带系统属性值的通知信息。 |

