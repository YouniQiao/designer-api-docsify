# SystemLiveViewSubscriber (System API)

Subscriber of the system live view notification.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
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

Callback when the button is touched.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| notificationId | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |
| buttonOptions | [ButtonOptions](../../apis-arkui/arkts-apis/arkts-arkui-button-buttonoptions-i.md) | Yes |
