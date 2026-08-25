# SystemLiveViewSubscriber (System API)

Subscriber of the system live view notification.

**Since:** 11

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## onResponse

```TypeScript
onResponse?: (notificationId: number, buttonOptions: ButtonOptions) => void
```

Callback when the button is touched.

**Since:** 11

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| notificationId | number | Yes |
| buttonOptions | [ButtonOptions](../../apis-arkui/arkts-components/arkts-arkui-buttonoptions-i.md) | Yes |
