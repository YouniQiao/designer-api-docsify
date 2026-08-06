# SystemLiveViewSubscriber (System API)

Subscriber of the system live view notification.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-notificationManager-export interface SystemLiveViewSubscriber--><!--Device-notificationManager-export interface SystemLiveViewSubscriber-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onResponse

ArkTS-Dyn:
```TypeScript
onResponse?: (notificationId: number, buttonOptions: ButtonOptions) => void
```

ArkTS-Sta:
```TypeScript
onResponse?: (notificationId: int, buttonOptions: ButtonOptions) => void
```

Callback when the button is touched.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SystemLiveViewSubscriber-onResponse?: (notificationId: int, buttonOptions: ButtonOptions) => void--><!--Device-SystemLiveViewSubscriber-onResponse?: (notificationId: int, buttonOptions: ButtonOptions) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| notificationId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes |  |
| buttonOptions | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

