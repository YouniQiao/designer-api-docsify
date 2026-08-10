# SystemLiveViewSubscriber (System API)

系统实况窗订阅者。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-notificationManager-export interface SystemLiveViewSubscriber--><!--Device-notificationManager-export interface SystemLiveViewSubscriber-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## onResponse

ArkTS-Dyn:
```TypeScript
onResponse?: (notificationId: number, buttonOptions: ButtonOptions) => void
```

ArkTS-Sta:
```TypeScript
onResponse?: (notificationId: int, buttonOptions: ButtonOptions) => void
```

点击按钮的回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SystemLiveViewSubscriber-onResponse?: (notificationId: int, buttonOptions: ButtonOptions) => void--><!--Device-SystemLiveViewSubscriber-onResponse?: (notificationId: int, buttonOptions: ButtonOptions) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| notificationId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes |  |
| buttonOptions | [ButtonOptions](../../apis-arkui/arkts-apis/arkts-arkui-button-buttonoptions-i.md) | Yes |  |

